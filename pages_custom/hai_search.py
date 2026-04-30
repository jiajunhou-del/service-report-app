import streamlit as st
from pathlib import Path
import base64
import mimetypes


def _image_to_data_uri(image_path: Path) -> str:
    if not image_path.exists():
        return ""

    mime_type, _ = mimetypes.guess_type(str(image_path))
    if mime_type is None:
        mime_type = "image/png"

    encoded = base64.b64encode(image_path.read_bytes()).decode()
    return f"data:{mime_type};base64,{encoded}"


def render_hai_search():
    # =========================
    # Path
    # =========================
    base_dir = Path(__file__).resolve().parents[1]
    logo_path = base_dir / "assets" / "hai_search_logo.jpg.png"

    logo_data_uri = _image_to_data_uri(logo_path)

    # =========================
    # CSS
    # =========================
    st.markdown(
        """
        <style>
        .hai-page {
            padding-top: 6px;
        }

        .hai-hero {
            background: linear-gradient(135deg, #1f2a78 0%, #2f62df 55%, #43b0ea 100%);
            border-radius: 30px;
            padding: 34px 34px;
            margin-bottom: 24px;
            box-shadow: 0 14px 30px rgba(34, 58, 120, 0.18);
        }

        .hai-hero-inner {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 28px;
            flex-wrap: wrap;
        }

        .hai-hero-left {
            flex: 1 1 520px;
            min-width: 320px;
        }

        .hai-badge {
            display: inline-block;
            padding: 10px 18px;
            border-radius: 999px;
            background: rgba(255,255,255,0.15);
            border: 1px solid rgba(255,255,255,0.18);
            color: #ffffff;
            font-weight: 700;
            font-size: 14px;
            margin-bottom: 22px;
        }

        .hai-hero-text {
            color: #ffffff;
            font-size: 19px;
            line-height: 1.9;
            font-weight: 500;
            max-width: 900px;
        }

        .hai-hero-subtext {
            margin-top: 18px;
            color: rgba(255,255,255,0.92);
            font-size: 16px;
            line-height: 1.8;
        }

        .hai-hero-right {
            flex: 0 0 300px;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .hai-logo-card {
            width: 280px;
            min-height: 220px;
            background: rgba(255,255,255,0.12);
            border: 1px solid rgba(255,255,255,0.18);
            border-radius: 28px;
            padding: 24px;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.15);
            backdrop-filter: blur(3px);
        }

        .hai-logo-card img {
            max-width: 100%;
            max-height: 170px;
            object-fit: contain;
            border-radius: 14px;
            background: #ffffff;
            padding: 12px;
        }

        .hai-logo-fallback {
            color: #ffffff;
            font-weight: 700;
            text-align: center;
            line-height: 1.6;
        }

        .hai-entry-title {
            font-size: 34px;
            font-weight: 800;
            color: #1f2e5c;
            margin: 10px 0 10px 0;
        }

        .hai-entry-subtitle {
            font-size: 18px;
            color: #5a6785;
            margin-bottom: 26px;
        }

        .hai-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(320px, 1fr));
            gap: 22px;
            margin-bottom: 24px;
        }

        .hai-card {
            background: #ffffff;
            border: 1px solid #e7ebf3;
            border-radius: 24px;
            padding: 28px 26px 24px 26px;
            box-shadow: 0 8px 22px rgba(30, 50, 100, 0.06);
        }

        .hai-card-icon {
            width: 66px;
            height: 66px;
            border-radius: 18px;
            background: #eef3fb;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 30px;
            margin-bottom: 18px;
        }

        .hai-card-title {
            font-size: 22px;
            font-weight: 800;
            color: #243255;
            margin-bottom: 14px;
        }

        .hai-card-text {
            font-size: 16px;
            color: #63708d;
            line-height: 1.9;
            min-height: 90px;
        }

        .hai-card-btn {
            display: inline-block;
            margin-top: 12px;
            padding: 12px 20px;
            border-radius: 12px;
            text-decoration: none;
            font-weight: 700;
            font-size: 15px;
        }

        .hai-btn-primary {
            background: linear-gradient(135deg, #2b4cb3 0%, #3a8ee8 100%);
            color: #ffffff !important;
        }

        .hai-btn-secondary {
            background: #edf3ff;
            color: #2450a9 !important;
        }

        .hai-note-box {
            background: #ffffff;
            border: 1px solid #e7ebf3;
            border-radius: 24px;
            padding: 26px 28px;
            box-shadow: 0 8px 22px rgba(30, 50, 100, 0.05);
            margin-top: 4px;
            margin-bottom: 20px;
        }

        .hai-note-title {
            font-size: 24px;
            font-weight: 800;
            color: #22315a;
            margin-bottom: 16px;
        }

        .hai-note-list {
            margin: 0;
            padding-left: 20px;
            color: #5f6d8b;
            line-height: 2;
            font-size: 16px;
        }

        .hai-tip {
            background: #f6f9ff;
            border: 1px solid #dfe8f8;
            border-radius: 18px;
            padding: 16px 18px;
            color: #4e5f82;
            font-size: 15px;
            line-height: 1.8;
            margin-top: 16px;
        }

        @media (max-width: 980px) {
            .hai-grid {
                grid-template-columns: 1fr;
            }

            .hai-hero-right {
                width: 100%;
            }

            .hai-logo-card {
                width: 100%;
                max-width: 340px;
            }

            .hai-hero-text {
                font-size: 17px;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # =========================
    # Hero block
    # =========================
    if logo_data_uri:
        logo_html = f'<img src="{logo_data_uri}" alt="HAI Search Logo">'
    else:
        logo_html = '<div class="hai-logo-fallback">Logo image not found<br>assets/hai_search_logo.jpg.png</div>'

    st.markdown(
        f"""
        <div class="hai-page">
            <div class="hai-hero">
                <div class="hai-hero-inner">
                    <div class="hai-hero-left">
                        <div class="hai-badge">Internal AI Search Assistant</div>

                        <div class="hai-hero-text">
                            HAI Search is an AI-powered search and Q&amp;A tool for service support.
                            It helps users find troubleshooting information, service manuals, bulletins,
                            error code information, and other service-related documents through Slack.
                        </div>

                        <div class="hai-hero-subtext">
                            Use this portal as the starting point for HAI Search access and update information.
                        </div>
                    </div>

                    <div class="hai-hero-right">
                        <div class="hai-logo-card">
                            {logo_html}
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # =========================
    # Portal title
    # =========================
    st.markdown(
        """
        <div class="hai-entry-title">HAI Search Portal</div>
        <div class="hai-entry-subtitle">
            Choose an entry below to start using HAI Search.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # =========================
    # Two entry cards
    # =========================
    st.markdown(
        """
        <div class="hai-grid">
            <div class="hai-card">
                <div class="hai-card-icon">🔎</div>
                <div class="hai-card-title">Search in Slack</div>
                <div class="hai-card-text">
                    Open Slack and use HAI Search through your available workspace and channel.
                    Use <b>/new</b> for questions and <b>/docs</b> for document search.
                </div>
                <a class="hai-card-btn hai-btn-primary" href="https://app.slack.com/" target="_blank">
                    🚀 Open Slack
                </a>
            </div>

            <div class="hai-card">
                <div class="hai-card-icon">📝</div>
                <div class="hai-card-title">Update Notes</div>
                <div class="hai-card-text">
                    Review version updates, improvement notes, known issues, and future enhancement items for HAI Search.
                </div>
                <a class="hai-card-btn hai-btn-secondary" href="#hai-update-notes">
                    📘 View Update Notes
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # =========================
    # Update notes
    # =========================
    st.markdown('<div id="hai-update-notes"></div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="hai-note-box">
            <div class="hai-note-title">Update Notes</div>
            <ul class="hai-note-list">
                <li>Multiple Search function was added to search documents more precisely.</li>
                <li>Enhanced searching power to give more accurate answers.</li>
                <li>Error code documents were added to improve response quality for error-related questions.</li>
                <li>Japanese document handling and guidance can be updated here in the future.</li>
            </ul>

            <div class="hai-tip">
                <b>Recommended use:</b>
                Use <b>/new</b> for Q&amp;A and <b>/docs</b> for document search.
                If the first answer is unclear, try rewriting the question in a simpler way.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
