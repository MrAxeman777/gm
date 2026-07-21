import streamlit as st

from game_engine import GameEngine


st.set_page_config(
    page_title="Soccer GM",
    page_icon="⚽",
    layout="wide"
)


if "game" not in st.session_state:
    st.session_state.game = GameEngine()


game = st.session_state.game


st.sidebar.title("⚽ Soccer GM")


if game.club is None:

    st.title("⚽ Soccer GM")
    st.write("Start your manager career.")

    club_names = [
        club.name
        for club in game.available_clubs
    ]

    selected = st.selectbox(
        "Choose your club:",
        club_names
    )


    if st.button("Start Career"):

        game.choose_club(selected)
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


        st.subheader("⚽ Next Match")


        fixture = game.fixture_service.get_next_match(
            club
        )


        if fixture:

            opponent = (
                fixture["away"]
                if fixture["home"] == club
                else fixture["home"]
            )


            st.info(
                f"{club.name} vs {opponent.name}"
            )


            if st.button(
                "▶ Play Match",
                use_container_width=True
            ):

                result = game.play_match()

                st.session_state.last_match = result

                st.rerun()


        else:

            st.success(
                "Season finished!"
            )



        if "last_match" in st.session_state:

            st.divider()

            st.subheader(
                "📋 Last Match"
            )

            result = st.session_state.last_match

            st.success(
                result["result"]
            )

            st.write(
                f"Winner: {result['winner']}"
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

        st.title("🏆 League Table")


        table = sorted(
            game.available_clubs,
            key=lambda x: x.points,
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

        st.title("🔄 Transfers")
        st.info("Transfer market active.")



    elif page == "💰 Finances":

        st.title("💰 Finances")

        st.write(
            f"Budget: ${club.budget:,}"
        )
