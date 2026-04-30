import streamlit as st
from pathlib import Path
import base64


# =========================
# Path / Link Settings
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE_DIR / "assets"

# Open Slack login / workspace page only, not a specific HAI Search channel
SLACK_HAI_SEARCH_URL = "https://app.slack.com/"


# =========================
# Image Helper
# =========================
def get_image_base64(image_path: Path):
    if image_path and image_path.exists():
        with open(image_path, "rb") as f:
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
def apply_hai_search_css():
    st.markdown(
        """
        <style>
        .hai-hero {
            display: grid;
            grid-template-columns: minmax(0, 1fr) 360px;
            gap: 32px;
            align-items: center;
            padding: 38px 42px;
            border-radius: 30px;
            background:
                radial-gradient(circle at right center, rgba(255,255,255,0.20), transparent 30%),
                linear-gradient(135deg, #1e3a8a 0%, #2563eb 58%, #0ea5e9 100%);
            color: white;
            box-shadow: 0 18px 45px rgba(37,99,235,0.24);
            margin-bottom: 24px;
        }

        .hai-hero-title {
            font-size: 48px;
            font-weight: 900;
            letter-spacing: -0.04em;
            margin-bottom: 18px;
            color: white;
        }

        .hai-hero-subtitle {
            font-size: 18px;
            line-height: 1.8;
            color: #e0f2fe;
            max-width: 1100px;
        }

        .hai-badge {
            display: inline-block;
            padding: 8px 15px;
            border-radius: 999px;
            background: rgba(255,255,255,0.16);
            border: 1px solid rgba(255,255,255,0.25);
            font-size: 14px;
            font-weight: 800;
            color: #ffffff;
            margin-bottom: 18px;
        }

        .hai-logo-box {
            background: rgba(255,255,255,0.20);
            border: 1px solid rgba(255,255,255,0.30);
            border-radius: 28px;
            padding: 18px;
            min-height: 230px;
            display: flex;
            justify-content: center;
            align-items: center;
            box-shadow:
                inset 0 1px 0 rgba(255,255,255,0.20),
                0 18px 36px rgba(0,0,0,0.16);
        }

        .hai-logo-inner {
            background: white;
            border-radius: 22px;
            padding: 20px;
            width: 100%;
            min-height: 190px;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .hai-logo-inner img {
            max-width: 100%;
            max-height: 160px;
            object-fit: contain;
        }

        .hai-button-row {
            display: flex;
            gap: 14px;
            flex-wrap: wrap;
            margin-top: 26px;
        }

        .hai-main-button {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            padding: 14px 24px;
            border-radius: 16px;
            background: white;
            color: #1d4ed8 !important;
            font-size: 16px;
            font-weight: 900;
            text-decoration: none !important;
            box-shadow: 0 12px 26px rgba(0,0,0,0.16);
            border: 1px solid rgba(255,255,255,0.25);
        }

        .hai-sub-button {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            padding: 14px 24px;
            border-radius: 16px;
            background: rgba(255,255,255,0.15);
            color: white !important;
            font-size: 16px;
            font-weight: 900;
            text-decoration: none !important;
            border: 1px solid rgba(255,255,255,0.28);
        }

        .hai-note {
            background: #eff6ff;
            border: 1px solid #dbeafe;
            color: #1e3a8a;
            border-radius: 18px;
            padding: 16px 20px;
            margin-bottom: 26px;
            font-size: 15px;
            line-height: 1.7;
        }

        .hai-section-title {
            font-size: 30px;
            font-weight: 900;
            color: #1f2a44;
            margin-top: 16px;
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
            border-radius: 24px;
            padding: 24px 26px;
            box-shadow: 0 10px 28px rgba(15,23,42,0.06);
            min-height: 230px;
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
            border-radius: 18px;
            padding: 16px 18px;
            margin-bottom: 14px;
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

        .hai-code {
            background: #eef4ff;
            color: #1d4ed8;
            border-radius: 8px;
            padding: 4px 8px;
            font-weight: 800;
            font-family: Consolas, Monaco, monospace;
            font-size: 14px;
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
            border-radius: 18px;
            padding: 16px 18px;
            margin-bottom: 14px;
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

        .hai-link-button {
            display: inline-block;
            padding: 9px 15px;
            border-radius: 12px;
            background: linear-gradient(135deg, #2563eb 0%, #0ea5e9 100%);
            color: white !important;
            font-weight: 900;
            text-decoration: none !important;
            font-size: 14px;
            box-shadow: 0 8px 18px rgba(37,99,235,0.20);
        }

        @media (max-width: 900px) {
            .hai-hero {
                grid-template-columns: 1fr;
                padding: 30px 26px;
            }

            .hai-hero-title {
                font-size: 38px;
            }

            .hai-logo-box {
                min-height: 200px;
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
    apply_hai_search_css()

    logo_path = find_hai_logo()
    logo_b64 = get_image_base64(logo_path)

    if logo_b64:
        logo_html = f"""
        <div class="hai-logo-box">
            <div class="hai-logo-inner">
                <img src="data:image/png;base64,{logo_b64}">
            </div>
        </div>
        """
    else:
        logo_html = """
        <div class="hai-logo-box">
            <div class="hai-logo-inner" style="color:#667085; text-align:center; line-height:1.8;">
                Logo image not found.<br>
                Please upload it to <b>assets</b> folder.
            </div>
        </div>
        """

    st.markdown(
        f"""
        <div class="hai-hero">
            <div>
                <div class="hai-badge">Internal AI Search Assistant</div>
                <div class="hai-hero-title">🤖 HAI Search</div>
                <div class="hai-hero-subtitle">
                    Search internal technical knowledge, service information, manuals,
                    bulletins, and troubleshooting data more efficiently.
                    <br><br>
                    This page is an entrance page for HAI Search guidance,
                    update notes, usage tips, and future search links.
                </div>

                <div class="hai-button-row">
                    <a class="hai-main-button" href="{SLACK_HAI_SEARCH_URL}" target="_blank">
                        🚀 Open Slack
                    </a>
                    <a class="hai-sub-button" href="#hai-guide">
                        📘 View Usage Guide
                    </a>
                </div>
            </div>

            {logo_html}
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="hai-note">
            <b>Recommended use:</b>
            Use <span class="hai-code">/new</span> for Q&A and
            <span class="hai-code">/docs</span> for document search.
            If the first answer is unclear, try rewriting the question in a simpler way.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div id="hai-guide" class="hai-section-title">HAI Search Guide</div>', unsafe_allow_html=True)
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
                    technical knowledge. It helps users shorten troubleshooting time and
                    find the right documents faster.
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
                        Example:
                        <span class="hai-code">/new what is error 802 on BQ-500?</span>
                    </div>
                </div>

                <div class="hai-command">
                    <div class="hai-command-name">/docs</div>
                    <div class="hai-card-text">
                        Search for related manuals or documents.<br>
                        Example:
                        <span class="hai-code">/docs BQ500 service manual</span>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")

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
            f"""
            <div class="hai-card">
                <div class="hai-card-title">Quick Links</div>

                <div class="hai-link-card">
                    <div class="hai-link-title">Slack</div>
                    <div class="hai-link-desc">
                        Open Slack login / workspace page.
                    </div>
                    <a class="hai-link-button" href="{SLACK_HAI_SEARCH_URL}" target="_blank">
                        Open Slack →
                    </a>
                </div>

                <div class="hai-link-card">
                    <div class="hai-link-title">User Guide / Notes</div>
                    <div class="hai-link-desc">
                        You can replace this with your internal guide link later.
                    </div>
                    <a class="hai-link-button" href="#" target="_blank">
                        Set guide link here →
                    </a>
                </div>

                <div class="hai-link-card">
                    <div class="hai-link-title">Update Information</div>
                    <div class="hai-link-desc">
                        You can place HAI Search update notes here.
                    </div>
                    <a class="hai-link-button" href="#" target="_blank">
                        Set update link here →
                    </a>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.info("This page can be expanded later with update history, FAQ, usage data, and search improvement notes.")
