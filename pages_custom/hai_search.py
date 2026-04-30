import streamlit as st
from pathlib import Path
import base64


# =========================
# Paths
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE_DIR / "assets"

SLACK_URL = "https://app.slack.com/"


# =========================
# Helpers
# =========================
def image_to_base64(path: Path):
    if path.exists():
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None


def find_hai_logo():
    candidates = [
        ASSETS_DIR / "hai_search_logo.jpg",
        ASSETS_DIR / "hai_search_logo.png",
        ASSETS_DIR / "HAI_logo_yoko.jpg",
        ASSETS_DIR / "HAI_logo_yoko.png",
        ASSETS_DIR / "hai_logo.jpg",
        ASSETS_DIR / "hai_logo.png",
    ]
    for p in candidates:
        if p.exists():
            return p
    return None


# =========================
# CSS
# =========================
def apply_hai_css():
    st.markdown("""
    <style>
    .hai-hero-wrap {
        background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 58%, #38bdf8 100%);
        border-radius: 30px;
        padding: 34px 34px 30px 34px;
        box-shadow: 0 18px 36px rgba(37, 99, 235, 0.18);
        margin-bottom: 24px;
    }

    .hai-badge {
        display: inline-block;
        padding: 8px 14px;
        border-radius: 999px;
        background: rgba(255,255,255,0.16);
        border: 1px solid rgba(255,255,255,0.22);
        color: white;
        font-size: 13px;
        font-weight: 800;
        margin-bottom: 18px;
    }

    .hai-title-row {
        display: flex;
        align-items: center;
        gap: 16px;
        margin-bottom: 18px;
    }

    .hai-title-logo {
        width: 58px;
        height: 58px;
        border-radius: 16px;
        background: rgba(255,255,255,0.14);
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        flex-shrink: 0;
        border: 1px solid rgba(255,255,255,0.18);
    }

    .hai-title-logo img {
        max-width: 84%;
        max-height: 84%;
        object-fit: contain;
    }

    .hai-title-text {
        color: white;
        font-size: 54px;
        font-weight: 900;
        line-height: 1.05;
        margin: 0;
        letter-spacing: -0.03em;
    }

    .hai-subtitle {
        color: #eef6ff;
        font-size: 17px;
        line-height: 1.9;
        margin-top: 6px;
        margin-bottom: 10px;
        max-width: 1000px;
    }

    .hai-right-card {
        background: rgba(255,255,255,0.14);
        border: 1px solid rgba(255,255,255,0.18);
        border-radius: 26px;
        padding: 18px;
        min-height: 240px;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: inset 0 1px 0 rgba(255,255,255,0.15);
    }

    .hai-right-inner {
        width: 100%;
        min-height: 190px;
        border-radius: 20px;
        background: rgba(255,255,255,0.96);
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 18px;
    }

    .hai-right-inner img {
        max-width: 100%;
        max-height: 150px;
        object-fit: contain;
    }

    .hai-note {
        background: #eff6ff;
        border: 1px solid #dbeafe;
        color: #1e3a8a;
        border-radius: 16px;
        padding: 14px 18px;
        margin-top: 14px;
        margin-bottom: 26px;
        font-size: 15px;
        line-height: 1.7;
    }

    .hai-note code {
        background: #dbeafe;
        color: #1d4ed8;
        padding: 3px 8px;
        border-radius: 8px;
        font-size: 14px;
        font-weight: 800;
    }

    .hai-section-title {
        font-size: 30px;
        font-weight: 900;
        color: #1f2a44;
        margin-top: 4px;
        margin-bottom: 8px;
    }

    .hai-section-desc {
        font-size: 16px;
        color: #667085;
        margin-bottom: 18px;
    }

    .hai-card {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 22px;
        padding: 24px;
        box-shadow: 0 10px 28px rgba(15,23,42,0.06);
        min-height: 230px;
        margin-bottom: 16px;
    }

    .hai-card-title {
        font-size: 22px;
        font-weight: 900;
        color: #1f2a44;
        margin-bottom: 14px;
    }

    .hai-card-text {
        font-size: 16px;
        color: #667085;
        line-height: 1.8;
    }

    .hai-command {
        background: #f8fafc;
        border: 1px solid #e5e7eb;
        border-radius: 16px;
        padding: 14px 16px;
        margin-bottom: 12px;
    }

    .hai-command-name {
        display: inline-block;
        background: #e0f2fe;
        color: #0369a1;
        border-radius: 9px;
        padding: 5px 10px;
        font-weight: 900;
        font-size: 14px;
        margin-bottom: 8px;
    }

    .hai-list {
        margin: 0;
        padding-left: 20px;
        color: #667085;
        line-height: 1.9;
        font-size: 16px;
    }

    .hai-link-card {
        background: #f8fafc;
        border: 1px solid #e5e7eb;
        border-radius: 16px;
        padding: 15px 16px;
        margin-bottom: 12px;
    }

    .hai-link-title {
        font-size: 17px;
        font-weight: 900;
        color: #1f2a44;
        margin-bottom: 6px;
    }

    .hai-link-desc {
        font-size: 14px;
        color: #667085;
        line-height: 1.6;
        margin-bottom: 10px;
    }

    /* Streamlit link_button style */
    div.stLinkButton > a {
        border-radius: 14px !important;
        font-weight: 900 !important;
        font-size: 16px !important;
        padding: 0.72rem 1.15rem !important;
        text-decoration: none !important;
        box-shadow: 0 10px 22px rgba(0,0,0,0.12) !important;
    }

    /* first main button */
    .hai-main-btn div.stLinkButton > a {
        background: white !important;
        color: #1d4ed8 !important;
        border: 1px solid rgba(255,255,255,0.55) !important;
    }

    /* secondary button */
    .hai-sub-btn div.stLinkButton > a {
        background: rgba(255,255,255,0.12) !important;
        color: white !important;
        border: 1px solid rgba(255,255,255,0.22) !important;
    }

    @media (max-width: 900px) {
        .hai-title-text {
            font-size: 40px;
        }
    }
    </style>
    """, unsafe_allow_html=True)


# =========================
# Render
# =========================
def render_hai_search():
    apply_hai_css()

    logo_path = find_hai_logo()
    logo_b64 = image_to_base64(logo_path) if logo_path else None

    # ---------- Hero ----------
    hero_col1, hero_col2 = st.columns([4.6, 1.4], gap="large")

    with hero_col1:
        st.markdown('<div class="hai-hero-wrap">', unsafe_allow_html=True)
        st.markdown('<div class="hai-badge">Internal AI Search Assistant</div>', unsafe_allow_html=True)

        if logo_b64:
            st.markdown(f"""
            <div class="hai-title-row">
                <div class="hai-title-logo">
                    <img src="data:image/png;base64,{logo_b64}">
                </div>
                <div class="hai-title-text">HAI Search</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="hai-title-row">
                <div class="hai-title-text">HAI Search</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("""
        <div class="hai-subtitle">
            Search internal technical knowledge, service information, manuals, bulletins,
            and troubleshooting data more efficiently.
            <br><br>
            This page is an entrance page for HAI Search guidance, update notes, usage tips,
            and future search links.
        </div>
        """, unsafe_allow_html=True)

        btn_col1, btn_col2, btn_col3 = st.columns([1.2, 1.2, 3.6])

        with btn_col1:
            st.markdown('<div class="hai-main-btn">', unsafe_allow_html=True)
            st.link_button("🚀 Open Slack", SLACK_URL, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with btn_col2:
            st.markdown('<div class="hai-sub-btn">', unsafe_allow_html=True)
            st.link_button("📘 Usage Guide", "#hai-guide", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    with hero_col2:
        st.markdown('<div class="hai-right-card">', unsafe_allow_html=True)
        st.markdown('<div class="hai-right-inner">', unsafe_allow_html=True)
        if logo_path and logo_path.exists():
            st.image(str(logo_path), use_container_width=True)
        else:
            st.markdown(
                "<div style='color:#667085;text-align:center;'>Logo image not found.<br>Please place it in the assets folder.</div>",
                unsafe_allow_html=True
            )
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # ---------- Note ----------
    st.markdown("""
    <div class="hai-note">
        <b>Recommended use:</b>
        Use <code>/new</code> for Q&amp;A and <code>/docs</code> for document search.
        If the first answer is unclear, try rewriting the question in a simpler way.
    </div>
    """, unsafe_allow_html=True)

    # ---------- Section title ----------
    st.markdown('<div id="hai-guide" class="hai-section-title">HAI Search Guide</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="hai-section-desc">A simple overview of what HAI Search does and how to use it.</div>',
        unsafe_allow_html=True
    )

    # ---------- Cards row 1 ----------
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
        <div class="hai-card">
            <div class="hai-card-title">What is HAI Search?</div>
            <div class="hai-card-text">
                HAI Search is an internal AI search tool for quickly finding information from manuals,
                bulletins, service-related documents, and accumulated technical knowledge.
                It helps users shorten troubleshooting time and find the right documents faster.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="hai-card">
            <div class="hai-card-title">Main Commands</div>

            <div class="hai-command">
                <div class="hai-command-name">/new</div>
                <div class="hai-card-text">
                    Ask a question directly.<br>
                    Example: <b>/new what is error 802 on BQ-500?</b>
                </div>
            </div>

            <div class="hai-command">
                <div class="hai-command-name">/docs</div>
                <div class="hai-card-text">
                    Search for related manuals or documents.<br>
                    Example: <b>/docs BQ500 service manual</b>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ---------- Cards row 2 ----------
    col3, col4 = st.columns(2, gap="large")

    with col3:
        st.markdown("""
        <div class="hai-card">
            <div class="hai-card-title">Usage Tips</div>
            <ul class="hai-list">
                <li>Use your private HAI Search channel when possible.</li>
                <li>Keep the question simple and clear.</li>
                <li>Avoid unnecessary symbols or extra spaces.</li>
                <li>If no answer is found, try another wording.</li>
                <li>Include product name and error code for better results.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="hai-card">
            <div class="hai-card-title">Quick Links</div>

            <div class="hai-link-card">
                <div class="hai-link-title">Slack</div>
                <div class="hai-link-desc">
                    Open the Slack login / workspace page.
                </div>
            </div>

            <div class="hai-link-card">
                <div class="hai-link-title">User Guide / Notes</div>
                <div class="hai-link-desc">
                    You can replace this block later with your internal guide link.
                </div>
            </div>

            <div class="hai-link-card">
                <div class="hai-link-title">Update Information</div>
                <div class="hai-link-desc">
                    You can place HAI Search update notes here.
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.info("This page can be expanded later with update history, FAQ, usage data, and search improvement notes.")
