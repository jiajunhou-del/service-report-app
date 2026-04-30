import streamlit as st
from pathlib import Path


# =========================
# Paths
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent
HAI_LOGO_PATH = BASE_DIR / "assets" / "hai_search_logo.jpg"


# =========================
# Helper: Page Header
# =========================
def render_hai_header():
    left, right = st.columns([4.2, 1.3])

    with left:
        st.markdown(
            """
            <div style="
                background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 55%, #38bdf8 100%);
                border-radius: 28px;
                padding: 28px 34px;
                min-height: 180px;
                display: flex;
                flex-direction: column;
                justify-content: center;
                box-shadow: 0 14px 36px rgba(37, 99, 235, 0.20);
            ">
                <div style="
                    color: white;
                    font-size: 2.2rem;
                    font-weight: 800;
                    margin-bottom: 10px;
                ">
                    🤖 HAI Search
                </div>
                <div style="
                    color: rgba(255,255,255,0.95);
                    font-size: 1.02rem;
                    line-height: 1.8;
                    max-width: 900px;
                ">
                    Search internal technical knowledge, service information, manuals,
                    bulletins, and troubleshooting data more efficiently.
                    This page can be used as an entrance page for HAI Search guidance,
                    update notes, and future search links.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with right:
        st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)

        if HAI_LOGO_PATH.exists():
            st.markdown(
                """
                <div style="
                    background: linear-gradient(180deg, rgba(255,255,255,0.20), rgba(255,255,255,0.10));
                    border-radius: 24px;
                    padding: 14px;
                    box-shadow: 0 12px 28px rgba(0,0,0,0.12);
                    border: 1px solid rgba(255,255,255,0.25);
                ">
                """,
                unsafe_allow_html=True,
            )
            st.image(str(HAI_LOGO_PATH), use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.warning("Logo image not found: assets/hai_search_logo.jpg")


# =========================
# Main Render
# =========================
def render_hai_search():
    render_hai_header()

    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div style="
            background: white;
            border-radius: 22px;
            padding: 24px 28px;
            box-shadow: 0 10px 24px rgba(15, 23, 42, 0.06);
            border: 1px solid #e5e7eb;
        ">
            <div style="
                font-size: 1.35rem;
                font-weight: 800;
                color: #1f2a44;
                margin-bottom: 14px;
            ">
                HAI Search Portal
            </div>
            <div style="
                color: #667085;
                line-height: 1.9;
                font-size: 1rem;
            ">
                You can use this area to introduce HAI Search, add usage guidance,
                share update notes, or link to Slack channels and documents.
                If needed, this page can later be expanded into:
                <ul>
                    <li>How to use HAI Search</li>
                    <li>Command examples (/new, /docs)</li>
                    <li>Version update notes</li>
                    <li>Useful tips for better search results</li>
                </ul>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div style='height: 22px;'></div>", unsafe_allow_html=True)

    # Optional: big centered image section
    st.markdown(
        """
        <div style="
            background: #ffffff;
            border-radius: 22px;
            padding: 18px 24px 26px 24px;
            box-shadow: 0 10px 24px rgba(15, 23, 42, 0.06);
            border: 1px solid #e5e7eb;
        ">
            <div style="
                font-size: 1.15rem;
                font-weight: 800;
                color: #1f2a44;
                margin-bottom: 14px;
            ">
                HAI Search Logo
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if HAI_LOGO_PATH.exists():
        st.image(str(HAI_LOGO_PATH), width=420)
    else:
        st.info("Please upload the logo image to assets/hai_search_logo.jpg")

    st.markdown("<div style='height: 24px;'></div>", unsafe_allow_html=True)

    # Example buttons
    col1, col2 = st.columns(2)
    with col1:
        st.button("Open HAI Search Guide", use_container_width=True)
    with col2:
        st.button("Check Latest Updates", use_container_width=True)
