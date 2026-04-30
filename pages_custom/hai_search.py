import streamlit as st
from pathlib import Path
import base64
import mimetypes
import streamlit.components.v1 as components


# =========================
# Path / Link Settings
# =========================
BASE_DIR = Path(__file__).resolve().parents[1]
ASSETS_DIR = BASE_DIR / "assets"

HAI_LOGO_PATH = ASSETS_DIR / "hai_search_logo.jpg.png"

SLACK_URL = "https://app.slack.com/"


# =========================
# Helper
# =========================
def image_to_data_uri(image_path: Path) -> str:
    if not image_path.exists():
        return ""

    mime_type, _ = mimetypes.guess_type(str(image_path))
    if mime_type is None:
        mime_type = "image/png"

    encoded = base64.b64encode(image_path.read_bytes()).decode("utf-8")
    return f"data:{mime_type};base64,{encoded}"


# =========================
# CSS for Streamlit native area
# =========================
def apply_css():
    st.markdown(
        """
<style>
.hai-section-title {
    font-size: 32px;
    font-weight: 900;
    color: #1f2a44;
    margin-top: 10px;
    margin-bottom: 8px;
}

.hai-section-subtitle {
    font-size: 17px;
    color: #667085;
    margin-bottom: 24px;
}

div.stLinkButton > a {
    border-radius: 14px !important;
    font-weight: 900 !important;
    font-size: 15px !important;
    padding: 0.75rem 1.1rem !important;
    text-decoration: none !important;
    box-shadow: 0 8px 18px rgba(37,99,235,0.12) !important;
    border: 1px solid #dbeafe !important;
}

.hai-card-box {
    background: #ffffff;
    border: 1px solid #e7ebf3;
    border-radius: 24px;
    padding: 28px 30px;
    box-shadow: 0 10px 28px rgba(30, 50, 100, 0.06);
    min-height: 230px;
    margin-bottom: 14px;
}

.hai-card-icon {
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

.hai-card-title {
    font-size: 24px;
    font-weight: 900;
    color: #243255;
    margin-bottom: 14px;
}

.hai-card-text {
    font-size: 16px;
    color: #63708d;
    line-height: 1.9;
}

.hai-note-box {
    background: #ffffff;
    border: 1px solid #e7ebf3;
    border-radius: 26px;
    padding: 28px 30px;
    box-shadow: 0 10px 28px rgba(30, 50, 100, 0.05);
    margin-top: 12px;
    margin-bottom: 24px;
}

.hai-note-title {
    font-size: 24px;
    font-weight: 900;
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
    margin-top: 18px;
}
</style>
        """,
        unsafe_allow_html=True,
    )


# =========================
# Hero by components.html
# =========================
def render_hero():
    logo_data_uri = image_to_data_uri(HAI_LOGO_PATH)

    if logo_data_uri:
        logo_html = f'<img src="{logo_data_uri}" alt="HAI Search Logo">'
    else:
        logo_html = """
        <div class="logo-fallback">
            Logo image not found<br>
            assets/hai_search_logo.jpg.png
        </div>
        """

    hero_html = f"""
<!DOCTYPE html>
<html>
<head>
<style>
body {{
    margin: 0;
    padding: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    background: transparent;
}}

.hero {{
    box-sizing: border-box;
    width: 100%;
    min-height: 280px;
    background:
        radial-gradient(circle at right center, rgba(255,255,255,0.18), transparent 30%),
        linear-gradient(135deg, #1f2a78 0%, #2f62df 58%, #43b0ea 100%);
    border-radius: 32px;
    padding: 40px 46px;
    box-shadow: 0 16px 36px rgba(34, 58, 120, 0.18);
}}

.hero-grid {{
    display: grid;
    grid-template-columns: 360px minmax(0, 1fr);
    gap: 44px;
    align-items: center;
}}

.logo-panel {{
    background: rgba(255,255,255,0.14);
    border: 1px solid rgba(255,255,255,0.22);
    border-radius: 28px;
    padding: 22px;
    min-height: 210px;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow:
        inset 0 1px 0 rgba(255,255,255,0.16),
        0 14px 30px rgba(0,0,0,0.12);
}}

.logo-box {{
    width: 100%;
    min-height: 170px;
    border-radius: 22px;
    background: rgba(255,255,255,0.96);
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 22px;
    box-sizing: border-box;
}}

.logo-box img {{
    max-width: 100%;
    max-height: 145px;
    object-fit: contain;
}}

.badge {{
    display: inline-block;
    padding: 9px 17px;
    border-radius: 999px;
    background: rgba(255,255,255,0.15);
    border: 1px solid rgba(255,255,255,0.22);
    color: #ffffff;
    font-weight: 800;
    font-size: 14px;
    margin-bottom: 22px;
}}

.hero-text {{
    color: #ffffff;
    font-size: 19px;
    line-height: 1.9;
    font-weight: 600;
    max-width: 1080px;
}}

.hero-subtext {{
    margin-top: 22px;
    color: rgba(255,255,255,0.92);
    font-size: 16px;
    line-height: 1.8;
}}

.logo-fallback {{
    color: #667085;
    font-weight: 700;
    text-align: center;
    line-height: 1.7;
}}

@media (max-width: 900px) {{
    .hero {{
        padding: 32px 28px;
    }}

    .hero-grid {{
        grid-template-columns: 1fr;
    }}

    .logo-panel {{
        max-width: 360px;
    }}
}}
</style>
</head>

<body>
<div class="hero">
    <div class="hero-grid">

        <div class="logo-panel">
            <div class="logo-box">
                {logo_html}
            </div>
        </div>

        <div>
            <div class="badge">Internal AI Search Assistant</div>

            <div class="hero-text">
                HAI Search is an AI-powered search and Q&amp;A tool for service support.
                It helps users find troubleshooting information, service manuals, bulletins,
                error code information, and other service-related documents through Slack.
            </div>

            <div class="hero-subtext">
                Use this portal as the starting point for HAI Search access and update information.
            </div>
        </div>

    </div>
</div>
</body>
</html>
"""

    components.html(hero_html, height=310, scrolling=False)


# =========================
# Main Render
# =========================
def render_hai_search():
    apply_css()

    render_hero()

    st.markdown(
        """
<div class="hai-section-title">HAI Search Portal</div>
<div class="hai-section-subtitle">
    Choose an entry below to start using HAI Search.
</div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown(
            """
<div class="hai-card-box">
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

    with col2:
        st.markdown(
            """
<div class="hai-card-box">
    <div class="hai-card-icon">📝</div>
    <div class="hai-card-title">Update Notes</div>
    <div class="hai-card-text">
        Review version updates, improvement notes, known issues,
        and future enhancement items for HAI Search.
    </div>
</div>
            """,
            unsafe_allow_html=True,
        )
        st.button("📘 View Update Notes", use_container_width=True, disabled=True)

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
