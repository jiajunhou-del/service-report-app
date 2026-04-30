import streamlit as st
from pathlib import Path
import base64


# =========================
# Paths / Links
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE_DIR / "assets"

# Slack login / workspace page only
SLACK_URL = "https://app.slack.com/"

# Update Notes link
# 以后如果你有正式的 HAI Search 更新说明链接，把这里替换掉即可
UPDATE_NOTES_URL = "#"


# =========================
# Helpers
# =========================
def image_to_base64(path: Path):
    if path and path.exists():
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
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

    for path in candidates:
        if path.exists():
            return path

    return None


# =========================
# CSS
# =========================
def apply_hai_css():
    st.markdown(
        """
        <style>
        .hai-hero {
            background:
                radial-gradient(circle at right top, rgba(255,255,255,0.18), transparent 32%),
                linear-gradient(135deg, #1e3a8a 0%, #2563eb 58%, #38bdf8 100%);
            border-radius: 32px;
            padding: 36px 40px;
            box-shadow: 0 18px 42px rgba(37,99,235,0.22);
            margin-bottom: 26px;
        }

        .hai-badge {
            display: inline-block;
            padding: 8px 15px;
            border-radius: 999px;
            background: rgba(255,255,255,0.16);
            border: 1px solid rgba(255,255,255,0.24);
            color: white;
            font-size: 13px;
            font-weight: 800;
            margin-bottom: 18px;
        }

        .hai-title-row {
            display: flex;
            align-items: center;
            gap: 18px;
            margin-bottom: 16px;
        }

        .hai-title-logo {
            width: 64px;
            height: 64px;
            border-radius: 18px;
            background: rgba(255,255,255,0.16);
            border: 1px solid rgba(255,255,255,0.25);
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
            flex-shrink: 0;
        }

        .hai-title-logo img {
            max-width: 88%;
            max-height: 88%;
            object-fit: contain;
        }

        .hai-title-text {
            color: white;
            font-size: 56px;
            font-weight: 900;
            letter-spacing: -0.04em;
            line-height: 1.05;
        }

        .hai-subtitle {
            color: #eef6ff;
            font-size: 17px;
            line-height: 1.9;
            max-width: 1050px;
            margin-top: 12px;
        }

        .hai-hero-logo-panel {
            background: rgba(255,255,255,0.14);
            border: 1px solid rgba(255,255,255,0.22);
            border-radius: 26px;
            padding: 18px;
            min-height: 240px;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.18);
        }

        .hai-hero-logo-inner {
            width: 100%;
            min-height: 190px;
            border-radius: 20px;
            background: rgba(255,255,255,0.96);
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 18px;
        }

        .hai-hero-logo-inner img {
            max-width: 100%;
            max-height: 150px;
            object-fit: contain;
        }

        .hai-note {
            background: #eff6ff;
            border: 1px solid #dbeafe;
            color: #1e3a8a;
            border-radius: 18px;
            padding: 15px 18px;
            margin-bottom: 26px;
            font-size: 15px;
            line-height: 1.7;
        }

        .hai-note code {
            background: #dbeafe;
            color: #1d4ed8;
            padding: 3px 8px;
            border-radius: 8px;
            font-weight: 800;
        }

        .portal-card {
            background: #ffffff;
            border: 1px solid #e5e7eb;
            border-radius: 26px;
            padding: 28px;
            min-height: 245px;
            box-shadow: 0 12px 30px rgba(15,23,42,0.07);
            margin-bottom: 18px;
        }

        .portal-card-icon {
            width: 54px;
            height: 54px;
            border-radius: 16px;
            background: #eff6ff;
            color: #2563eb;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 28px;
            margin-bottom: 18px;
        }

        .portal-card-title {
            font-size: 24px;
            font-weight: 900;
            color: #1f2a44;
            margin-bottom: 10px;
        }

        .portal-card-text {
            font-size: 16px;
            color: #667085;
            line-height: 1.8;
            margin-bottom: 18px;
        }

        .hai-section-title {
            font-size: 30px;
            font-weight: 900;
            color: #1f2a44;
            margin-top: 12px;
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
            min-height: 230px;
            box-shadow: 0 10px 28px rgba(15,23,42,0.06);
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

        div.stLinkButton > a {
            border-radius: 14px !important;
            font-weight: 900 !important;
            font-size: 15px !important;
            padding: 0.72rem 1.1rem !important;
            text-decoration: none !important;
            box-shadow: 0 10px 22px rgba(37,99,235,0.16) !important;
            border: 1px solid #dbeafe !important;
        }

        .primary-link div.stLinkButton > a {
            background: linear-gradient(135deg, #2563eb 0%, #0ea5e9 100%) !important;
            color: white !important;
            border: none !important;
        }

        .secondary-link div.stLinkButton > a {
            background: #ffffff !important;
            color: #2563eb !important;
        }

        @media (max-width: 900px) {
            .hai-title-text {
                font-size: 40px;
            }

            .hai-title-logo {
                width: 52px;
                height: 52px;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


# =========================
# Render Function
# =========================
def render_hai_search():
    apply_hai_css()

    logo_path = find_hai_logo()
    logo_b64 = image_to_base64(logo_path) if logo_path else None

    # =========================
    # Hero
    # =========================
    hero_left, hero_right = st.columns([4.3, 1.5], gap="large")

    with hero_left:
        st.markdown('<div class="hai-hero">', unsafe_allow_html=True)

        st.markdown(
            '<div class="hai-badge">Internal AI Search Assistant</div>',
            unsafe_allow_html=True,
        )

        if logo_b64:
            st.markdown(
                f"""
                <div class="hai-title-row">
                    <div class="hai-title-logo">
                        <img src="data:image/png;base64,{logo_b64}">
                    </div>
                    <div class="hai-title-text">HAI Search</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                """
                <div class="hai-title-row">
                    <div class="hai-title-text">HAI Search</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown(
            """
            <div class="hai-subtitle">
                Search internal technical knowledge, service information, manuals, bulletins,
                and troubleshooting data more efficiently.
                <br><br>
                This page is an entrance portal for HAI Search guidance, update notes,
                usage tips, and future support links.
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("</div>", unsafe_allow_html=True)

    with hero_right:
        st.markdown('<div class="hai-hero-logo-panel">', unsafe_allow_html=True)
        st.markdown('<div class="hai-hero-logo-inner">', unsafe_allow_html=True)

        if logo_path and logo_path.exists():
            st.image(str(logo_path), use_container_width=True)
        else:
            st.markdown(
                "<div style='color:#667085;text-align:center;'>Logo image not found.<br>Please place it in the assets folder.</div>",
                unsafe_allow_html=True,
            )

        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # =========================
    # Recommended Use
    # =========================
    st.markdown(
        """
        <div class="hai-note">
            <b>Recommended use:</b>
            Use <code>/new</code> for Q&amp;A and <code>/docs</code> for document search.
            If the first answer is unclear, try rewriting the question in a simpler way.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # =========================
    # Portal Entry Cards
    # =========================
    st.markdown(
        '<div class="hai-section-title">HAI Search Portal</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="hai-section-desc">Choose an action below to start using or reviewing HAI Search.</div>',
        unsafe_allow_html=True,
    )

    entry_col1, entry_col2 = st.columns(2, gap="large")

    with entry_col1:
        st.markdown(
            """
            <div class="portal-card">
                <div class="portal-card-icon">🔎</div>
                <div class="portal-card-title">Search in Slack</div>
                <div class="portal-card-text">
                    Open Slack and use HAI Search from your available HAI Search channel.
                    Use <b>/new</b> for questions and <b>/docs</b> for document search.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown('<div class="primary-link">', unsafe_allow_html=True)
        st.link_button("🚀 Open Slack", SLACK_URL, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with entry_col2:
        st.markdown(
            """
            <div class="portal-card">
                <div class="portal-card-icon">📝</div>
                <div class="portal-card-title">Update Notes</div>
                <div class="portal-card-text">
                    Check HAI Search improvement history, version update notes,
                    known issues, and future enhancement items.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown('<div class="secondary-link">', unsafe_allow_html=True)
        st.link_button("📘 View Update Notes", UPDATE_NOTES_URL, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # =========================
    # Guide
    # =========================
    st.markdown(
        '<div id="hai-guide" class="hai-section-title">Usage Guide</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="hai-section-desc">A simple overview of what HAI Search does and how to use it.</div>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown(
            """
            <div class="hai-card">
                <div class="hai-card-title">What is HAI Search?</div>
                <div class="hai-card-text">
                    HAI Search is an internal AI search tool for quickly finding information
                    from manuals, bulletins, service-related documents, and accumulated
                    technical knowledge. It helps users shorten troubleshooting time and find
                    the right documents faster.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
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
            """,
            unsafe_allow_html=True,
        )

    col3, col4 = st.columns(2, gap="large")

    with col3:
        st.markdown(
            """
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
            """,
            unsafe_allow_html=True,
        )

    with col4:
        st.markdown(
            """
            <div class="hai-card">
                <div class="hai-card-title">Future Content</div>
                <div class="hai-card-text">
                    This area can be expanded later with FAQ, update history,
                    usage analytics, known retrieval issues, and search improvement notes.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.info(
        "This HAI Search page can later be expanded with update history, FAQ, usage data, and search improvement notes."
    )
