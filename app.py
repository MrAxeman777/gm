import streamlit as st

from game_engine import GameEngine
from services.save_service import SaveService


st.set_page_config(
    page_title="Soccer GM",
    page_icon="⚽",
    layout="wide"
)


if "game" not in st.session_state:
    st.session_state.game = GameEngine()


if "save" not in st.session_state:
    st.session_state.save = SaveService()


game = st.session_state.game
save = st.session_state.save


st.sidebar.title("⚽ Soccer GM")


# Save / Load buttons

st.sidebar.divider()

if st.sidebar.button("💾 Save Career"):

    save.save_game(game)

    st.sidebar.success(
        "Career saved!"
    )


if st.sidebar.button("📂 Load Career"):

    loaded = save.load_game(game)

    if loaded:
        st.sidebar.success(
            "Career loaded!"
        )

        st.rerun()

    else:
        st.sidebar.error(
            "No save found."
        )



if game.club is None:

    st.title("⚽ Soccer GM")

    st.write(
        "Start your manager career."
    )


    clubs = [
        club.name
        for club in game.available_clubs
    ]


    selected = st.selectbox(
        "Choose your club:",
        clubs
    )


    if st.button(
        "Start Career"
    ):

        game.choose_club(
            selected
        )

        st.rerun()



else:

    club = game.club


    st.sidebar.success(
        f"Managing {club.name}"
    )


    page = st.sidebar.radio(
        "Menu",
        [
            "🏠 Dashboard",
            "👥 Squad",
            "🔄 Transfers",
            "🏆 League",
            "💰 Finances"
        ]
    )


    if page == "🏠 Dashboard":

        st.title(
            f"🏟️ {club.name}"
        )


        col1, col2, col3 = st.columns(3)


        with col1:

            st.metric(
                "💰 Budget",
                f"${club.budget:,}"
            )


        with col2:

            st.metric(
                "🏆 Points",
                club.points
            )


        with col3:

            st.metric(
                "📅 Week",
                game.season.current_week
            )


        st.divider()


        fixture = (
            game.fixture_service
            .get_next_match(club)
        )


        if fixture:

            opponent = (
                fixture["away"]
                if fixture["home"] == club
                else fixture["home"]
            )


            st.info(
                f"Next Match: {club.name} vs {opponent.name}"
            )


            if st.button(
                "▶ Play Match"
            ):

                result = game.play_match()

                st.session_state.last_match = result

                st.rerun()



        if "last_match" in st.session_state:

            st.subheader(
                "📋 Last Match"
            )

            st.success(
                st.session_state.last_match["result"]
            )



    elif page == "👥 Squad":

        st.title("👥 Squad")


        for player in club.players:

            st.write(
                f"⚽ {player.name} | "
                f"{player.position} | "
                f"⭐ {player.overall}"
            )



    elif page == "🏆 League":

        st.title(
            "🏆 League Table"
        )


        table = sorted(
            game.available_clubs,
            key=lambda x:x.points,
            reverse=True
        )


        for i, team in enumerate(
            table,
            1
        ):

            st.write(
                f"{i}. {team.name} - {team.points} pts"
            )



    elif page == "🔄 Transfers":

        st.title(
            "🔄 Transfers"
        )

        st.info(
            "Transfer system active."
        )



    elif page == "💰 Finances":

        st.title(
            "💰 Finances"
        )

        st.write(
            f"Budget: ${club.budget:,}"
        )
