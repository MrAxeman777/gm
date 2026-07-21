import streamlit as st

from game_engine import GameEngine


st.set_page_config(
    page_title="Soccer GM",
    page_icon="⚽",
    layout="wide"
)


# Create game engine
if "game" not in st.session_state:
    st.session_state.game = GameEngine()


game = st.session_state.game


st.sidebar.title("⚽ Soccer GM")


# -------------------------
# New Career
# -------------------------

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


# -------------------------
# Main Game
# -------------------------

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


    # Dashboard
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

            st.success(
                result["result"]
            )

            st.write(
                f"💰 Earned: ${result['money']:,}"
            )

            st.write(
                f"📅 Week {result['week']}"
            )


    # Squad
    elif page == "👥 Squad":

        st.title("👥 Squad")


        if len(club.players) > 0:

            for player in club.players:

                st.subheader(
                    f"⚽ {player.name}"
                )


                col1, col2, col3 = st.columns(3)


                with col1:
                    st.write(
                        f"Position: {player.position}"
                    )

                    st.write(
                        f"Age: {player.age}"
                    )


                with col2:
                    st.write(
                        f"⭐ Overall: {player.overall}"
                    )

                    st.write(
                        f"🚀 Potential: {player.potential}"
                    )


                with col3:
                    st.write(
                        f"💰 Value: ${player.value:,}"
                    )

                    st.write(
                        f"💵 Wage: ${player.wage:,}"
                    )


                st.divider()


        else:

            st.info(
                "Your squad is empty."
            )


    # Transfers
    elif page == "🔄 Transfers":

        st.title("🔄 Transfer Market")

        st.info(
            "Transfer market coming next."
        )


    # League
    elif page == "🏆 League":

        st.title("🏆 League")

        st.info(
            "League system coming next."
        )


    # Finances
    elif page == "💰 Finances":

        st.title("💰 Finances")

        st.write(
            f"Transfer Budget: ${club.budget:,}"
        )

        st.write(
            f"Wage Budget: ${club.wage_budget:,}"
        )
