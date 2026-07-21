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
                "⭐ Reputation",
                club.reputation
            )

        with col3:
            st.metric(
                "🏆 Points",
                club.points
            )


        st.divider()


        if st.button(
            "▶ Play Match"
        ):

            result = game.play_match()

            st.session_state.last_match = result


        if "last_match" in st.session_state:

            match = st.session_state.last_match

            st.success(
                match["result"]
            )

            st.write(
                f"Winner: {match['winner']}"
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


        for index, team in enumerate(
            table,
            start=1
        ):

            goal_difference = (
                team.goals_for
                -
                team.goals_against
            )


            st.write(
                f"""
{index}. **{team.name}**

Games: {team.matches}

Wins: {team.wins}

Draws: {team.draws}

Losses: {team.losses}

GD: {goal_difference}

Points: {team.points}
"""
            )

            st.divider()



    elif page == "🔄 Transfers":

        st.title("🔄 Transfers")

        st.info(
            "Transfer system active."
        )



    elif page == "💰 Finances":

        st.title("💰 Finances")

        st.write(
            f"Budget: ${club.budget:,}"
        )
