import streamlit as st
from pathlib import Path
import base64
import textwrap


# =========================
# Paths / Links
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE_DIR / "assets"

HAI_LOGO_PATH = ASSETS_DIR / "hai_search_logo.jpg"

SLACK_URL = "https://app.slack.com/"
UPDATE_NOTES_URL = "#"


# =========================
# Helper
# =========================
def image_to_data_uri(path: Path) -> str:
    if not path.exists():
        return ""

    suffix = path.suffix.lower()

    if suffix in [".jpg", ".jpeg"]:
        mime = "image/jpeg"
    elif suffix == ".png":
        mime = "image/png"
    elif suffix == ".webp":
        mime = "image/webp"
    else:
        mime = "image/png"

    with open(path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("utf-8")

    return f"data:{mime};base64,{encoded}"


def html_block(content: str):
    st.markdown(
        textwrap.dedent(content).strip(),
        unsafe_allow_html=True,
    )


# =========================
# CSS
# =========================
def apply_hai_css():
    html_block(
        """
        <style>
        .hs2-hero {
            display: grid;
            grid-template-columns: minmax(0, 1fr) 380px;
            gap: 42px;
            align-items: center;
            background:
                radial-gradient(circle at right center, rgba(255,255,255,0.18), transparent 30%),
                linear-gradient(135deg, #1f3f9d 0%, #2f63e0 58%, #43b2ee 100%);
            border-radius: 34px;
            padding: 46px 54px;
            box-shadow: 0 18px 42px rgba(37,99,235,0.18);
            margin-bottom: 28px;
            min-height: 310px;
        }

        .hs2-badge {
            display: inline-block;
            padding: 8px 16px;
            border-radius: 999px;
            background: rgba(255,255,255,0.16);
            border: 1px solid rgba(255,255,255,0.25);
            color: #ffffff;
            font-size: 13px;
            font-weight: 800;
            margin-bottom: 22px;
        }

        .hs2-title-row {
            display: flex;
            align-items: center;
            gap: 18px;
            margin-bottom: 22px;
        }

        .hs2-logo-small {
            width: 74px;
            height: 74px;
            border-radius: 18px;
            background: rgba(255,255,255,0.96);
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 9px;
            flex-shrink: 0;
            box-shadow: 0 8px 20px rgba(0,0,0,0.10);
        }

        .hs2-logo-small img {
            max-width: 100%;
            max-height: 100%;
            object-fit: contain;
        }

        .hs2-title {
            color: #ffffff;
            font-size: 58px;
            font-weight: 900;
            line-height: 1.05;
            letter-spacing: -0.04em;
        }

        .hs2-subtitle {
            color: rgba(255,255,255,0.96);
            font-size: 18px;
            line-height: 1.85;
            max-width: 1060px;
            margin-bottom: 28px;
        }

        .hs2-button-row {
            display: flex;
            gap: 14px;
            flex-wrap: wrap;
        }

        .hs2-main-button {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            padding: 13px 22px;
            border-radius: 15px;
            background: #ffffff;
            color: #2458d3 !important;
            font-size: 15px;
            font-weight: 900;
            text-decoration: none !important;
            box-shadow: 0 10px 22px rgba(0,0,0,0.14);
        }

        .hs2-sub-button {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            padding: 13px 22px;
            border-radius: 15px;
            background: rgba(255,255,255,0.15);
            border: 1px solid rgba(255,255,255,0.28);
            color: #ffffff !important;
            font-size: 15px;
            font-weight: 900;
            text-decoration: none !important;
        }

        .hs2-logo-panel {
            background: rgba(255,255,255,0.16);
            border: 1px solid rgba(255,255,255,0.25);
            border-radius: 30px;
            padding: 20px;
            min-height: 250px;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow:
                inset 0 1px 0 rgba(255,255,255,0.18),
                0 14px 34px rgba(0,0,0,0.12);
        }

        .hs2-logo-inner {
            width: 100%;
            min-height: 210px;
            border-radius: 22px;
            background: rgba(255,255,255,0.96);
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 24px;
        }

        .hs2-logo-inner img {
            max-width: 100%;
            max-height: 180px;
            object-fit: contain;
        }

        .hs2-note {
            background: #eff6ff;
            border: 1px solid #dbeafe;
            color: #1e3a8a;
            border-radius: 18px;
            padding: 15px 18px;
            margin-bottom: 26px;
            font-size: 15px;
            line-height: 1.7;
        }

        .hs2-note code {
            background: #dbeafe;
            color: #1d4ed8;
            padding: 3px 8px;
            border-radius: 8px;
            font-weight: 800;
        }

        .hs2-section-title {
            font-size: 30px;
            font-weight: 900;
            color: #1f2a44;
            margin-top: 12px;
            margin-bottom: 8px;
        }

        .hs2-section-desc {
            font-size: 16px;
            color: #667085;
            margin-bottom: 18px;
        }

        .hs2-card {
            background: #ffffff;
            border: 1px solid #e5e7eb;
            border-radius: 24px;
            padding: 26px;
            box-shadow: 0 10px 26px rgba(15,23,42,0.06);
            min-height: 230px;
            margin-bottom: 16px;
        }

        .hs2-card-icon {
            width: 54px;
            height: 54px;
            border-radius: 16px;
            background: #eff6ff;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 28px;
            margin-bottom: 16px;
        }

        .hs2-card-title {
            font-size: 24px;
            font-weight: 900;
            color: #1f2a44;
            margin-bottom: 10px;
        }

        .hs2-card-text {
            font-size: 16px;
            color: #667085;
            line-height: 1.8;
        }

        .hs2-mini-card {
            background: #ffffff;
            border: 1px solid #e5e7eb;
            border-radius: 22px;
            padding: 24px;
            box-shadow: 0 10px 24px rgba(15,23,42,0.05);
            min-height: 230px;
            margin-bottom: 16px;
        }

        .hs2-mini-title {
            font-size: 22px;
            font-weight: 900;
            color: #1f2a44;
            margin-bottom: 14px;
        }

        .hs2-command-box {
            background: #f8fafc;
            border: 1px solid #e5e7eb;
            border-radius: 16px;
            padding: 14px 16px;
            margin-bottom: 12px;
        }

        .hs2-command-name {
            display: inline-block;
            background: #e0f2fe;
            color: #0369a1;
            border-radius: 9px;
            padding: 5px 10px;
            font-weight: 900;
            font-size: 14px;
            margin-bottom: 8px;
        }

        .hs2-list {
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
            box-shadow: 0 8px 18px rgba(37,99,235,0.12) !important;
            border: 1px solid #dbeafe !important;
        }

        @media (max-width: 900px) {
            .hs2-hero {
                grid-template-columns: 1fr;
                padding: 32px 26px;
            }

            .hs2-title {
                font-size: 42px;
            }

            .hs2-logo-small {
                width: 58px;
                height: 58px;
            }
        }
        </style>
        """
    )


# =========================
# Main Render
# =========================
def render_hai_search():
    apply_hai_css()

    logo_uri = image_to_data_uri(HAI_LOGO_PATH)

    if logo_uri:
        small_logo = f"""
        <div class="hs2-logo-small">
            <img src="{logo_uri}">
        </div>
        """

        big_logo = f"""
        <div class="hs2-logo-panel">
            <div class="hs2-logo-inner">
                <img src="{logo_uri}">
            </div>
        </div>
        """
    else:
        small_logo = ""

        big_logo = """
        <div class="hs2-logo-panel">
            <div class="hs2-logo-inner" style="color:#667085;text-align:center;line-height:1.8;">
                Logo image not found.<br>
                Please upload: assets/hai_search_logo.jpg
            </div>
        </div>
        """

    # =========================
    # Hero
    # =========================
    html_block(
        f"""
        <div class="hs2-hero">
            <div>
                <div class="hs2-badge">Internal AI Search Assistant</div>

                <div class="hs2-title-row">
                    {small_logo}
                    <div class="hs2-title">HAI Search</div>
                </div>

                <div class="hs2-subtitle">
                    Search internal technical knowledge, service information, manuals,
                    bulletins, and troubleshooting data more efficiently.
                    <br><br>
                    This page is an entrance portal for HAI Search guidance, update notes,
                    usage tips, and future support links.
                </div>

                <div class="hs2-button-row">
                    <a class="hs2-main-button" href="{SLACK_URL}" target="_blank">
                        🚀 Open Slack
                    </a>
                    <a class="hs2-sub-button" href="#hai-guide">
                        📘 Usage Guide
                    </a>
                </div>
            </div>

            <div>
                {big_logo}
            </div>
        </div>
        """
    )

    # =========================
    # Recommended Use
    # =========================
    html_block(
        """
        <div class="hs2-note">
            <b>Recommended use:</b>
            Use <code>/new</code> for Q&amp;A and <code>/docs</code> for document search.
            If the first answer is unclear, try rewriting the question in a simpler way.
        </div>
        """
    )

    # =========================
    # Portal Cards
    # =========================
    html_block('<div class="hs2-section-title">HAI Search Portal</div>')
    html_block('<div class="hs2-section-desc">Choose an entry below to start using HAI Search.</div>')

    c1, c2 = st.columns(2, gap="large")

    with c1:
        html_block(
            """
            <div class="hs2-card">
                <div class="hs2-card-icon">🔎</div>
                <div class="hs2-card-title">Search in Slack</div>
                <div class="hs2-card-text">
                    Open Slack and use HAI Search through your available workspace and channel.
                    Use <b>/new</b> for questions and <b>/docs</b> for document search.
                </div>
            </div>
            """
        )
        st.link_button("🚀 Open Slack", SLACK_URL, use_container_width=True)

    with c2:
        html_block(
            """
            <div class="hs2-card">
                <div class="hs2-card-icon">📝</div>
                <div class="hs2-card-title">Update Notes</div>
                <div class="hs2-card-text">
                    Review version updates, improvement notes, known issues,
                    and future enhancement items for HAI Search.
                </div>
            </div>
            """
        )
        st.link_button("📘 View Update Notes", UPDATE_NOTES_URL, use_container_width=True)

    # =========================
    # Guide
    # =========================
    html_block('<div id="hai-guide" class="hs2-section-title">Usage Guide</div>')
    html_block('<div class="hs2-section-desc">A simple overview of what HAI Search does and how to use it.</div>')

    g1, g2 = st.columns(2, gap="large")

    with g1:
        html_block(
            """
            <div class="hs2-mini-card">
                <div class="hs2-mini-title">What is HAI Search?</div>
                <div class="hs2-card-text">
                    HAI Search is an internal AI search tool for quickly finding
                    information from manuals, bulletins, service-related documents,
                    and technical knowledge. It helps users shorten troubleshooting time
                    and reach the right documents faster.
                </div>
            </div>
            """
        )

    with g2:
        html_block(
            """
            <div class="hs2-mini-card">
                <div class="hs2-mini-title">Main Commands</div>

                <div class="hs2-command-box">
                    <div class="hs2-command-name">/new</div>
                    <div class="hs2-card-text">
                        Ask a question directly.<br>
                        Example: <b>/new what is error 802 on BQ-500?</b>
                    </div>
                </div>

                <div class="hs2-command-box">
                    <div class="hs2-command-name">/docs</div>
                    <div class="hs2-card-text">
                        Search related manuals or documents.<br>
                        Example: <b>/docs BQ500 service manual</b>
                    </div>
                </div>
            </div>
            """
        )

    g3, g4 = st.columns(2, gap="large")

    with g3:
        html_block(
            """
            <div class="hs2-mini-card">
                <div class="hs2-mini-title">Usage Tips</div>
                <ul class="hs2-list">
                    <li>Use a private HAI Search channel when possible.</li>
                    <li>Keep the query simple and clear.</li>
                    <li>Avoid unnecessary symbols or extra spaces.</li>
                    <li>If the result is unclear, ask again with different wording.</li>
                    <li>Adding product name and error code improves accuracy.</li>
                </ul>
            </div>
            """
        )

    with g4:
        html_block(
            """
            <div class="hs2-mini-card">
                <div class="hs2-mini-title">Future Content</div>
                <div class="hs2-card-text">
                    This section can later be expanded with FAQ, update history,
                    usage analytics, known issues, and search improvement summaries.
                </div>
            </div>
            """
        )

    st.info(
        "This page can later be expanded with update history, FAQ, usage analytics, and search improvement notes."
    )
