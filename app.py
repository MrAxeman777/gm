import streamlit as st

from game_engine import GameEngine


st.set_page_config(
    page_title="Soccer GM",
    page_icon="⚽",
    layout="wide"
)


# Create game
if "game" not in st.session_state:
    st.session_state.game = GameEngine()


game = st.session_state.game


st.sidebar.title("⚽ Soccer GM")


# --------------------
# NEW CAREER
# --------------------

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


    if st.button(
        "Start Career",
        use_container_width=True
    ):

        game.choose_club(selected)

        st.rerun()


# --------------------
# GAME DASHBOARD
# --------------------

else:

    club = game.club


    st.sidebar.success(
        f"Manager of {club.name}"
    )


    page = st.sidebar.radio(
        "Menu",
        [
            "🏠 Dashboard",
            "👥 Squad",
            "🔄 Transfers",
            "🏆 League"
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


        st.subheader(
            "📅 Next Match"
        )


        if st.button(
            "▶ Play Match",
            use_container_width=True
        ):

            result = game.play_match()

            st.success(
                result["result"]
            )

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
                st.write(player.name)

        else:

            st.info(
                "No players loaded yet."
            )


    elif page == "🔄 Transfers":

        st.title("🔄 Transfers")

        st.info(
            "Transfer market coming next."
        )


    elif page == "🏆 League":

        st.title("🏆 League")

        st.info(
            "League system coming next."
        )
