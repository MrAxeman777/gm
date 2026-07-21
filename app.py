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

    clubs = [
        club.name
        for club in game.available_clubs
    ]

    selected = st.selectbox(
        "Choose your club:",
        clubs
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
                "👥 Squad",
                len(club.players)
            )


        st.divider()


        st.subheader("⚽ Match")


        if st.button(
            "▶ Play Match",
            use_container_width=True
        ):

            result = game.play_match()

            st.session_state.last_match = result


        if "last_match" in st.session_state:

            match = st.session_state.last_match


            st.success(
                match["result"]
            )


            st.write(
                f"🏆 Winner: {match['winner']}"
            )


            st.write(
                "⚽ Goals:"
            )


            for scorer in match["home_scorers"]:

                st.write(
                    f"⚽ {scorer}"
                )


            for scorer in match["away_scorers"]:

                st.write(
                    f"⚽ {scorer}"
                )


            st.write(
                f"💰 Prize Money: ${match['money']:,}"
            )


    elif page == "👥 Squad":

        st.title("👥 Squad")


        for player in club.players:

            st.subheader(
                f"⚽ {player.name}"
            )

            st.write(
                f"{player.position} | ⭐ {player.overall}"
            )

            st.write(
                f"Goals: {player.goals}"
            )

            st.divider()



    elif page == "🔄 Transfers":

        st.title("🔄 Transfer Market")


        for player in game.available_players:

            if player not in club.players:

                st.subheader(
                    player.name
                )

                st.write(
                    f"{player.position} | ⭐ {player.overall}"
                )

                if st.button(
                    f"Buy {player.name}",
                    key=f"buy_{player.name}"
                ):

                    success, message = (
                        game.transfer.buy_player(
                            club,
                            player
                        )
                    )

                    if success:
                        st.success(message)
                        st.rerun()

                    else:
                        st.error(message)



    elif page == "🏆 League":

        st.title("🏆 League")
        st.info("Coming soon.")



    elif page == "💰 Finances":

        st.title("💰 Finances")

        st.write(
            f"Budget: ${club.budget:,}"
        )
