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

    selected_club = st.selectbox(
        "Choose your club:",
        club_names
    )

    if st.button(
        "Start Career",
        use_container_width=True
    ):

        game.choose_club(selected_club)
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

        st.title(f"🏟️ {club.name}")

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
                "👥 Squad Size",
                len(club.players)
            )


        st.divider()

        st.subheader("📅 Next Match")

        if st.button(
            "▶ Play Match",
            use_container_width=True
        ):

            result = game.play_match()

            st.success(result["result"])

            st.write(
                f"💰 Earned ${result['money']:,}"
            )

            st.write(
                f"📅 Week {result['week']}"
            )


    elif page == "👥 Squad":

        st.title("👥 Squad")

        if club.players:

            for player in club.players:

                st.subheader(
                    f"⚽ {player.name}"
                )

                st.write(
                    f"{player.position} | "
                    f"⭐ {player.overall} | "
                    f"💰 ${player.value:,}"
                )

                st.divider()

        else:

            st.info(
                "Your squad is empty."
            )


    elif page == "🔄 Transfers":

        st.title("🔄 Transfer Market")

        for player in game.available_players:

            if player not in club.players:

                st.subheader(
                    f"⚽ {player.name}"
                )

                st.write(
                    f"{player.position} | "
                    f"⭐ {player.overall}"
                )

                st.write(
                    f"💰 Value: ${player.value:,}"
                )


                if st.button(
                    f"Buy {player.name}",
                    key=player.name
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


                st.divider()


    elif page == "🏆 League":

        st.title("🏆 League")

        st.info(
            "League system coming soon."
        )


    elif page == "💰 Finances":

        st.title("💰 Finances")

        st.write(
            f"Transfer Budget: ${club.budget:,}"
        )

        st.write(
            f"Wage Budget: ${club.wage_budget:,}"
        )
