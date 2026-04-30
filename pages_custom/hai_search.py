import streamlit as st
from pathlib import Path
import base64
import mimetypes
import textwrap


# =========================
# Path / Link Settings
# =========================
BASE_DIR = Path(__file__).resolve().parents[1]
ASSETS_DIR = BASE_DIR / "assets"

HAI_LOGO_PATH = ASSETS_DIR / "hai_search_logo.jpg.png"

SLACK_URL = "https://app.slack.com/"
UPDATE_NOTES_URL = "#"


# =========================
# Helper
# =========================
def html(content: str):
    st.markdown(textwrap.dedent(content).strip(), unsafe_allow_html=True)


def image_to_data_uri(image_path: Path) -> str:
    if not image_path.exists():
        return ""

    mime_type, _ = mimetypes.guess_type(str(image_path))
    if mime_type is None:
        mime_type = "image/png"

    encoded = base64.b64encode(image_path.read_bytes()).decode("utf-8")
    return f"data:{mime_type};base64,{encoded}"


# =========================
# CSS
# =========================
def apply_css():
    html(
        """
        <style>
        .hai-page-wrap {
            padding-top: 6px;
        }

        .hai-hero-new {
            background:
                radial-gradient(circle at right center, rgba(255,255,255,0.18), transparent 30%),
                linear-gradient(135deg, #1f2a78 0%, #2f62df 58%, #43b0ea 100%);
            border-radius: 32px;
            padding: 40px 46px;
            margin-bottom: 28px;
            box-shadow: 0 16px 36px rgba(34, 58, 120, 0.18);
        }

        .hai-hero-grid {
            display: grid;
            grid-template-columns: minmax(0, 1fr) 330px;
            gap: 36px;
            align-items: center;
        }

        .hai-badge-new {
            display: inline-block;
            padding: 9px 17px;
            border-radius: 999px;
            background: rgba(255,255,255,0.15);
            border: 1px solid rgba(255,255,255,0.22);
            color: #ffffff;
            font-weight: 800;
            font-size: 14px;
            margin-bottom: 22px;
        }

        .hai-hero-text-new {
            color: #ffffff;
            font-size: 19px;
            line-height: 1.9;
            font-weight: 500;
            max-width: 980px;
        }

        .hai-hero-subtext-new {
            margin-top: 18px;
            color: rgba(255,255,255,0.92);
            font-size: 16px;
            line-height: 1.8;
        }

        .hai-logo-panel-new {
            background: rgba(255,255,255,0.14);
            border: 1px solid rgba(255,255,255,0.22);
            border-radius: 28px;
            padding: 22px;
            min-height: 230px;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow:
                inset 0 1px 0 rgba(255,255,255,0.16),
                0 14px 30px rgba(0,0,0,0.12);
        }

        .hai-logo-box-new {
            width: 100%;
            min-height: 185px;
            border-radius: 22px;
            background: rgba(255,255,255,0.96);
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 22px;
        }

        .hai-logo-box-new img {
            max-width: 100%;
            max-height: 150px;
            object-fit: contain;
        }

        .hai-fallback-new {
            color: #667085;
            font-weight: 700;
            text-align: center;
            line-height: 1.7;
        }

        .hai-section-title-new {
            font-size: 32px;
            font-weight: 900;
            color: #1f2a44;
            margin-top: 10px;
            margin-bottom: 8px;
        }

        .hai-section-subtitle-new {
            font-size: 17px;
            color: #667085;
            margin-bottom: 24px;
        }

        .hai-entry-grid-new {
            display: grid;
            grid-template-columns: repeat(2, minmax(320px, 1fr));
            gap: 24px;
            margin-bottom: 30px;
        }

        .hai-entry-card-new {
            background: #ffffff;
            border: 1px solid #e7ebf3;
            border-radius: 26px;
            padding: 30px 30px 26px 30px;
            box-shadow: 0 10px 28px rgba(30, 50, 100, 0.06);
            min-height: 245px;
        }

        .hai-entry-icon-new {
            width: 66px;
            height: 66px;
            border-radius: 18px;
            background: #eef3fb;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 31px;
            margin-bottom: 18px;
        }

        .hai-entry-title-new {
            font-size: 24px;
            font-weight: 900;
            color: #243255;
            margin-bottom: 14px;
        }

        .hai-entry-text-new {
            font-size: 16px;
            color: #63708d;
            line-height: 1.9;
            min-height: 88px;
        }

        .hai-card-button-new {
            display: inline-block;
            margin-top: 16px;
            padding: 12px 22px;
            border-radius: 14px;
            text-decoration: none !important;
            font-weight: 900;
            font-size: 15px;
        }

        .hai-primary-button-new {
            background: linear-gradient(135deg, #2b4cb3 0%, #3a8ee8 100%);
            color: #ffffff !important;
            box-shadow: 0 8px 18px rgba(37,99,235,0.18);
        }

        .hai-secondary-button-new {
            background: #edf3ff;
            color: #2450a9 !important;
            border: 1px solid #dce8ff;
        }

        .hai-note-box-new {
            background: #ffffff;
            border: 1px solid #e7ebf3;
            border-radius: 26px;
            padding: 28px 30px;
            box-shadow: 0 10px 28px rgba(30, 50, 100, 0.05);
            margin-top: 8px;
            margin-bottom: 24px;
        }

        .hai-note-title-new {
            font-size: 24px;
            font-weight: 900;
            color: #22315a;
            margin-bottom: 16px;
        }

        .hai-note-list-new {
            margin: 0;
            padding-left: 20px;
            color: #5f6d8b;
            line-height: 2;
            font-size: 16px;
        }

        .hai-tip-new {
            background: #f6f9ff;
            border: 1px solid #dfe8f8;
            border-radius: 18px;
            padding: 16px 18px;
            color: #4e5f82;
            font-size: 15px;
            line-height: 1.8;
            margin-top: 18px;
        }

        .hai-guide-grid-new {
            display: grid;
            grid-template-columns: repeat(2, minmax(320px, 1fr));
            gap: 24px;
            margin-bottom: 24px;
        }

        .hai-guide-card-new {
            background: #ffffff;
            border: 1px solid #e7ebf3;
            border-radius: 24px;
            padding: 26px 28px;
            box-shadow: 0 8px 22px rgba(30, 50, 100, 0.05);
            min-height: 230px;
        }

        .hai-guide-title-new {
            font-size: 22px;
            font-weight: 900;
            color: #243255;
            margin-bottom: 14px;
        }

        .hai-guide-text-new {
            font-size: 16px;
            color: #63708d;
            line-height: 1.9;
        }

        .hai-command-new {
            background: #f8fbff;
            border: 1px solid #e3eefc;
            border-radius: 16px;
            padding: 15px 16px;
            margin-bottom: 14px;
        }

        .hai-command-label-new {
            display: inline-block;
            padding: 5px 10px;
            border-radius: 9px;
            background: #dcecff;
            color: #2458d3;
            font-weight: 900;
            font-size: 14px;
            margin-bottom: 8px;
        }

        .hai-list-new {
            margin: 0;
            padding-left: 20px;
            color: #63708d;
            line-height: 1.9;
            font-size: 16px;
        }

        @media (max-width: 980px) {
            .hai-hero-grid {
                grid-template-columns: 1fr;
            }

            .hai-entry-grid-new,
            .hai-guide-grid-new {
                grid-template-columns: 1fr;
            }

            .hai-hero-new {
                padding: 32px 28px;
            }

            .hai-logo-panel-new {
                max-width: 360px;
            }
        }
        </style>
        """
    )


# =========================
# Main Render
# =========================
def render_hai_search():
    apply_css()

    logo_data_uri = image_to_data_uri(HAI_LOGO_PATH)

    if logo_data_uri:
        logo_html = f'<img src="{logo_data_uri}" alt="HAI Search Logo">'
    else:
        logo_html = """
        <div class="hai-fallback-new">
            Logo image not found<br>
            assets/hai_search_logo.jpg.png
        </div>
        """

    # =========================
    # Hero
    # =========================
    html(
        f"""
        <div class="hai-page-wrap">
            <div class="hai-hero-new">
                <div class="hai-hero-grid">
                    <div>
                        <div class="hai-badge-new">Internal AI Search Assistant</div>

                        <div class="hai-hero-text-new">
                            HAI Search is an AI-powered search and Q&amp;A tool for service support.
                            It helps users find troubleshooting information, service manuals, bulletins,
                            error code information, and other service-related documents through Slack.
                        </div>

                        <div class="hai-hero-subtext-new">
                            Use this portal as the starting point for HAI Search access and update information.
                        </div>
                    </div>

                    <div class="hai-logo-panel-new">
                        <div class="hai-logo-box-new">
                            {logo_html}
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """
    )

    # =========================
    # Portal Entries
    # =========================
    html(
        """
        <div class="hai-section-title-new">HAI Search Portal</div>
        <div class="hai-section-subtitle-new">
            Choose an entry below to start using HAI Search.
        </div>
        """
    )

    html(
        f"""
        <div class="hai-entry-grid-new">
            <div class="hai-entry-card-new">
                <div class="hai-entry-icon-new">🔎</div>
                <div class="hai-entry-title-new">Search in Slack</div>
                <div class="hai-entry-text-new">
                    Open Slack and use HAI Search through your available workspace and channel.
                    Use <b>/new</b> for questions and <b>/docs</b> for document search.
                </div>
                <a class="hai-card-button-new hai-primary-button-new" href="{SLACK_URL}" target="_blank">
                    🚀 Open Slack
                </a>
            </div>

            <div class="hai-entry-card-new">
                <div class="hai-entry-icon-new">📝</div>
                <div class="hai-entry-title-new">Update Notes</div>
                <div class="hai-entry-text-new">
                    Review version updates, improvement notes, known issues,
                    and future enhancement items for HAI Search.
                </div>
                <a class="hai-card-button-new hai-secondary-button-new" href="#hai-update-notes">
                    📘 View Update Notes
                </a>
            </div>
        </div>
        """
    )

    # =========================
    # Update Notes
    # =========================
    html('<div id="hai-update-notes"></div>')

    html(
        """
        <div class="hai-note-box-new">
            <div class="hai-note-title-new">Update Notes</div>
            <ul class="hai-note-list-new">
                <li>Multiple Search function was added to search documents more precisely.</li>
                <li>Enhanced searching power to give more accurate answers.</li>
                <li>Error code documents were added to improve response quality for error-related questions.</li>
                <li>Japanese document handling and guidance can be updated here in the future.</li>
            </ul>

            <div class="hai-tip-new">
                <b>Recommended use:</b>
                Use <b>/new</b> for Q&amp;A and <b>/docs</b> for document search.
                If the first answer is unclear, try rewriting the question in a simpler way.
            </div>
        </div>
        """
    )

    # =========================
    # Usage Guide
    # =========================
    html(
        """
        <div class="hai-section-title-new">Usage Guide</div>
        <div class="hai-section-subtitle-new">
            A simple overview of how to use HAI Search.
        </div>
        """
    )

    html(
        """
        <div class="hai-guide-grid-new">
            <div class="hai-guide-card-new">
                <div class="hai-guide-title-new">Main Commands</div>

                <div class="hai-command-new">
                    <div class="hai-command-label-new">/new</div>
                    <div class="hai-guide-text-new">
                        Ask a question directly.<br>
                        Example: <b>/new what is error 802 on BQ-500?</b>
                    </div>
                </div>

                <div class="hai-command-new">
                    <div class="hai-command-label-new">/docs</div>
                    <div class="hai-guide-text-new">
                        Search related manuals or documents.<br>
                        Example: <b>/docs BQ500 service manual</b>
                    </div>
                </div>
            </div>

            <div class="hai-guide-card-new">
                <div class="hai-guide-title-new">Usage Tips</div>
                <ul class="hai-list-new">
                    <li>Use a private HAI Search channel when possible.</li>
                    <li>Keep the query simple and clear.</li>
                    <li>Avoid unnecessary symbols or extra spaces.</li>
                    <li>If the result is unclear, ask again with different wording.</li>
                    <li>Adding product name and error code improves accuracy.</li>
                </ul>
            </div>
        </div>
        """
    )
