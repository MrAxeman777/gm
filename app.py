import streamlit as st

st.set_page_config(
    page_title="Soccer GM",
    page_icon="⚽",
    layout="wide"
)

# ---------- Sidebar ----------
st.sidebar.title("⚽ Soccer GM")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "👥 Squad",
        "🔄 Transfers",
        "🏆 League",
        "💰 Finances",
        "⚙️ Settings"
    ]
)

# ---------- Dashboard ----------
if page == "🏠 Dashboard":

    st.title("⚽ Soccer GM")

    st.caption("Season 2026/27 • Week 1")

    st.divider()

    st.header("🏟️ Manchester United")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("💰 Transfer Budget", "$150,000,000")

    with col2:
        st.metric("⭐ Reputation", "90")

    with col3:
        st.metric("👥 Squad Size", "23")

    st.divider()

    st.subheader("📅 Next Match")

    st.info(
        "Manchester United vs Chelsea\n\n"
        "Premier League"
    )

    if st.button(
        "▶ Play Match",
        use_container_width=True
    ):
        st.success(
            "Match engine coming next!"
        )

    st.divider()

    st.subheader("📰 Latest News")

    st.write("Welcome to your new club!")

# ---------- Placeholder Pages ----------
else:
    st.title(page)
    st.info("Coming soon...")
