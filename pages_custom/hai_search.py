import streamlit as st
from pathlib import Path
import base64


# =========================
# Basic paths
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE_DIR / "assets"

SLACK_URL = "https://app.slack.com/"
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
    for p in candidates:
        if p.exists():
            return p
    return None


# =========================
# CSS
# =========================
def apply_hai_css():
    st.markdown(
        """
        <style>
        .hai-hero {
            display: grid;
            grid-template-columns: minmax(0, 1fr) 360px;
            gap: 34px;
            align-items: center;
            background: linear-gradient(135deg, #1f3f9d 0%, #2f63e0 58%, #43b2ee 100%);
            border-radius: 34px;
            padding: 42px 48px;
            box-shadow: 0 10px 28px rgba(0,0,0,0.08);
            margin-bottom: 28px;
        }

        .hai-left {
            min-width: 0;
        }

        .hai-title-row {
            display: flex;
            align-items: center;
            gap: 18px;
            margin-bottom: 22px;
        }

        .hai-logo-small {
            width: 72px;
            height: 72px;
            border-radius: 18px;
            background: rgba(255,255,255,0.18);
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 8px;
            flex-shrink: 0;
        }

        .hai-logo-small img {
            max-width: 100%;
            max-height: 100%;
            object-fit: contain;
            border-radius: 10px;
            background: white;
        }

        .hai-title {
            color: white;
            font-size: 56px;
            font-weight: 900;
            line-height: 1.05;
            margin: 0;
        }

        .hai-subtitle {
            color: rgba(255,255,255,0.95);
            font-size: 18px;
            line-height: 1.9;
            margin-top: 8px;
            margin-bottom: 26px;
        }

        .hai-badge {
            display: inline-block;
            padding: 8px 16px;
            border-radius: 999px;
            background: rgba(255,255,255,0.14);
            border: 1px solid rgba(255,255,255,0.22);
            color: white;
            font-size: 13px;
            font-weight: 700;
            margin-bottom: 18px;
        }

        .hai-btn-row {
            display: flex;
            gap: 14px;
            flex-wrap: wrap;
            margin-top: 8px;
        }

        .hai-main-btn {
            display: inline-block;
            padding: 12px 20px;
            border-radius: 14px;
            background: white;
            color: #2458d3 !important;
            font-size: 15px;
            font-weight: 800;
            text-decoration: none !important;
            box-shadow: 0 8px 20px rgba(0,0,0,0.12);
        }

        .hai-sub-btn {
            display: inline-block;
            padding: 12px 20px;
            border-radius: 14px;
            background: rgba(255,255,255,0.14);
            border: 1px solid rgba(255,255,255,0.22);
            color: white !important;
            font-size: 15px;
            font-weight: 800;
            text-decoration: none !important;
        }

        .hai-right-wrap {
            background: rgba(255,255,255,0.14);
            border: 1px solid rgba(255,255,255,0.2);
            border-radius: 28px;
            padding: 20px;
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.15);
        }

        .hai-right-box {
            background: rgba(255,255,255,0.96);
            border-radius: 22px;
            min-height: 250px;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 24px;
        }

        .hai-right-box img {
            max-width: 100%;
            max-height: 200px;
            object-fit: contain;
        }

        .hai-note {
            background: #f3f8ff;
            border: 1px solid #d9e8ff;
            border-radius: 18px;
            padding: 15px 18px;
            margin-bottom: 24px;
            color: #35507c;
            font-size: 15px;
            line-height: 1.8;
        }

        .hai-note code {
            background: #e4efff;
            color: #2751c3;
            border-radius: 8px;
            padding: 3px 8px;
            font-weight: 700;
        }

        .hai-section-title {
            font-size: 34px;
            font-weight: 900;
            color: #24395d;
            margin-top: 8px;
            margin-bottom: 8px;
        }

        .hai-section-desc {
            font-size: 16px;
            color: #6a7b96;
            margin-bottom: 20px;
        }

        .hai-card {
            background: white;
            border: 1px solid #e6edf7;
            border-radius: 24px;
            padding: 26px;
            box-shadow: 0 6px 18px rgba(0,0,0,0.04);
            min-height: 220px;
            margin-bottom: 14px;
        }

        .hai-card-icon {
            width: 54px;
            height: 54px;
            border-radius: 16px;
            background: #edf4ff;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 28px;
            margin-bottom: 16px;
        }

        .hai-card-title {
            font-size: 24px;
            font-weight: 900;
            color: #24395d;
            margin-bottom: 10px;
        }

        .hai-card-text {
            font-size: 16px;
            color: #6a7b96;
            line-height: 1.85;
        }

        .hai-mini-card {
            background: white;
            border: 1px solid #e6edf7;
            border-radius: 22px;
            padding: 24px;
            box-shadow: 0 6px 18px rgba(0,0,0,0.04);
            min-height: 240px;
            margin-bottom: 14px;
        }

        .hai-mini-title {
            font-size: 22px;
            font-weight: 900;
            color: #24395d;
            margin-bottom: 14px;
        }

        .hai-command-box {
            background: #f7fbff;
            border: 1px solid #e3eefc;
            border-radius: 14px;
            padding: 14px 16px;
            margin-bottom: 12px;
        }

        .hai-command-label {
            display: inline-block;
            padding: 4px 10px;
            border-radius: 8px;
            background: #dcecff;
            color: #2458d3;
            font-weight: 800;
            font-size: 14px;
            margin-bottom: 8px;
        }

        .hai-list {
            margin: 0;
            padding-left: 20px;
            color: #6a7b96;
            line-height: 1.9;
            font-size: 16px;
        }

        div.stLinkButton > a {
            border-radius: 14px !important;
            font-weight: 800 !important;
            border: 1px solid #dbe7fb !important;
            box-shadow: 0 6px 14px rgba(0,0,0,0.05) !important;
        }

        @media (max-width: 900px) {
            .hai-hero {
                grid-template-columns: 1fr;
                padding: 32px 26px;
            }

            .hai-title {
                font-size: 42px;
            }

            .hai-logo-small {
                width: 58px;
                height: 58px;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


# =========================
# Main render
# =========================
def render_hai_search():
    apply_hai_css()

    logo_path = find_hai_logo()
    logo_b64 = image_to_base64(logo_path) if logo_path else None

    if logo_b64:
        logo_html_small = f"""
            <div class="hai-logo-small">
                <img src="data:image/png;base64,{logo_b64}">
            </div>
        """
        logo_html_big = f"""
            <div class="hai-right-wrap">
                <div class="hai-right-box">
                    <img src="data:image/png;base64,{logo_b64}">
                </div>
            </div>
        """
    else:
        logo_html_small = ""
        logo_html_big = """
            <div class="hai-right-wrap">
                <div class="hai-right-box" style="color:#7c8ca8; text-align:center;">
                    Logo not found<br>
                    Put image in assets folder
                </div>
            </div>
        """

    # =========================
    # HERO (one complete HTML block)
    # =========================
    st.markdown(
        f"""
        <div class="hai-hero">
            <div class="hai-left">
                <div class="hai-badge">Internal AI Search Assistant</div>

                <div class="hai-title-row">
                    {logo_html_small}
                    <h1 class="hai-title">HAI Search</h1>
                </div>

                <div class="hai-subtitle">
                    Search internal technical knowledge, service information, manuals,
                    bulletins, and troubleshooting data more efficiently.
                    <br><br>
                    This page is an entrance portal for HAI Search guidance, update notes,
                    usage tips, and future support links.
                </div>

                <div class="hai-btn-row">
                    <a class="hai-main-btn" href="{SLACK_URL}" target="_blank">
                        🚀 Open Slack
                    </a>
                    <a class="hai-sub-btn" href="#hai-guide">
                        📘 Usage Guide
                    </a>
                </div>
            </div>

            <div>
                {logo_html_big}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # =========================
    # Recommended note
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
    # Portal Cards
    # =========================
    st.markdown(
        '<div class="hai-section-title">HAI Search Portal</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="hai-section-desc">Choose an entry below to start using HAI Search.</div>',
        unsafe_allow_html=True,
    )

    c1, c2 = st.columns(2, gap="large")

    with c1:
        st.markdown(
            """
            <div class="hai-card">
                <div class="hai-card-icon">🔎</div>
                <div class="hai-card-title">Search in Slack</div>
                <div class="hai-card-text">
                    Open Slack and use HAI Search through your available workspace and channel.
                    Use <b>/new</b> for questions and <b>/docs</b> for document search.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.link_button("🚀 Open Slack", SLACK_URL, use_container_width=True)

    with c2:
        st.markdown(
            """
            <div class="hai-card">
                <div class="hai-card-icon">📝</div>
                <div class="hai-card-title">Update Notes</div>
                <div class="hai-card-text">
                    Review version updates, improvement notes, recent changes,
                    and future enhancement items for HAI Search.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.link_button("📘 View Update Notes", UPDATE_NOTES_URL, use_container_width=True)

    # =========================
    # Guide section
    # =========================
    st.markdown(
        '<div id="hai-guide" class="hai-section-title">HAI Search Guide</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="hai-section-desc">A simple overview of what HAI Search does and how to use it.</div>',
        unsafe_allow_html=True,
    )

    g1, g2 = st.columns(2, gap="large")

    with g1:
        st.markdown(
            """
            <div class="hai-mini-card">
                <div class="hai-mini-title">What is HAI Search?</div>
                <div class="hai-card-text">
                    HAI Search is an internal AI search tool for quickly finding
                    information from manuals, bulletins, service-related documents,
                    and technical knowledge. It helps users shorten troubleshooting time
                    and reach the right documents faster.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with g2:
        st.markdown(
            """
            <div class="hai-mini-card">
                <div class="hai-mini-title">Main Commands</div>

                <div class="hai-command-box">
                    <div class="hai-command-label">/new</div>
                    <div class="hai-card-text">
                        Ask a question directly.<br>
                        Example: <b>/new what is error 802 on BQ-500?</b>
                    </div>
                </div>

                <div class="hai-command-box">
                    <div class="hai-command-label">/docs</div>
                    <div class="hai-card-text">
                        Search related manuals or documents.<br>
                        Example: <b>/docs BQ500 service manual</b>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    g3, g4 = st.columns(2, gap="large")

    with g3:
        st.markdown(
            """
            <div class="hai-mini-card">
                <div class="hai-mini-title">Usage Tips</div>
                <ul class="hai-list">
                    <li>Use a private HAI Search channel when possible.</li>
                    <li>Keep the query simple and clear.</li>
                    <li>Avoid unnecessary symbols or extra spaces.</li>
                    <li>If the result is unclear, ask again with different wording.</li>
                    <li>Adding product name and error code improves accuracy.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with g4:
        st.markdown(
            """
            <div class="hai-mini-card">
                <div class="hai-mini-title">Future Content</div>
                <div class="hai-card-text">
                    This section can later be expanded with FAQ, update history,
                    usage analytics, known issues, and search improvement summaries.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.info(
        "This page can later be expanded with update history, FAQ, usage analytics, and search improvement notes."
    )
