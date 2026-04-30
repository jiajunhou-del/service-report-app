import streamlit as st
from pathlib import Path
import base64
import textwrap


# =========================
# Basic Paths
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE_DIR / "assets"

# Slack login / top page only
SLACK_HAI_SEARCH_URL = "https://app.slack.com/"


# =========================
# Helpers
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
        textwrap.dedent("""
        <style>
        .hai-hero {
            display: grid;
            grid-template-columns: minmax(0, 1fr) 280px;
            gap: 26px;
            align-items: center;
            padding: 38px 40px;
            border-radius: 30px;
            background:
                radial-gradient(circle at right top, rgba(255,255,255,0.18), transparent 32%),
                linear-gradient(135deg, #1e3a8a 0%, #2563eb 58%, #38bdf8 100%);
            color: white;
            box-shadow: 0 18px 40px rgba(37,99,235,0.22);
            margin-bottom: 24px;
        }

        .hai-badge {
            display: inline-block;
            padding: 8px 14px;
            border-radius: 999px;
            background: rgba(255,255,255,0.14);
            border: 1px solid rgba(255,255,255,0.22);
            font-size: 13px;
            font-weight: 800;
            color: #ffffff;
            margin-bottom: 16px;
        }

        .hai-hero-title {
            font-size: 50px;
            font-weight: 900;
            line-height: 1.1;
            margin-bottom: 16px;
            color: #ffffff;
            letter-spacing: -0.03em;
        }

        .hai-hero-subtitle {
            font-size: 17px;
            line-height: 1.9;
            color: #eaf4ff;
            max-width: 980px;
        }

        .hai-button-row {
            display: flex;
            gap: 14px;
            flex-wrap: wrap;
            margin-top: 28px;
        }

        .hai-main-button {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            padding: 14px 22px;
            border-radius: 14px;
            background: #ffffff;
            color: #1d4ed8 !important;
            font-size: 16px;
            font-weight: 900;
            text-decoration: none !important;
            box-shadow: 0 10px 24px rgba(0,0,0,0.14);
        }

        .hai-main-button:hover {
            text-decoration: none !important;
            transform: translateY(-1px);
        }

        .hai-sub-button {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            padding: 14px 22px;
            border-radius: 14px;
            background: rgba(255,255,255,0.14);
            color: #ffffff !important;
            font-size: 16px;
            font-weight: 900;
            text-decoration: none !important;
            border: 1px solid rgba(255,255,255,0.24);
        }

        .hai-sub-button:hover {
            text-decoration: none !important;
            transform: translateY(-1px);
        }

        .hai-logo-shell {
            background: rgba(255,255,255,0.16);
            border: 1px solid rgba(255,255,255,0.20);
            border-radius: 24px;
            padding: 16px;
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 220px;
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.18);
        }

        .hai-logo-box {
            width: 100%;
            min-height: 180px;
            border-radius: 18px;
            background: rgba(255,255,255,0.95);
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 16px;
        }

        .hai-logo-box img {
            max-width: 100%;
            max-height: 130px;
            object-fit: contain;
        }

        .hai-note {
            background: #eff6ff;
            border: 1px solid #dbeafe;
            color: #1e3a8a;
            border-radius: 16px;
            padding: 15px 18px;
            margin-bottom: 26px;
            font-size: 15px;
            line-height: 1.7;
        }

        .hai-section-title {
            font-size: 28px;
            font-weight: 900;
            color: #1f2a44;
            margin-top: 6px;
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

        .hai-link-button {
            display: inline-block;
            padding: 9px 14px;
            border-radius: 12px;
            background: linear-gradient(135deg, #2563eb 0%, #0ea5e9 100%);
            color: #ffffff !important;
            font-weight: 900;
            text-decoration: none !important;
            font-size: 14px;
            box-shadow: 0 8px 18px rgba(37,99,235,0.18);
        }

        .hai-link-button:hover {
            text-decoration: none !important;
        }

        @media (max-width: 900px) {
            .hai-hero {
                grid-template-columns: 1fr;
                padding: 30px 24px;
            }

            .hai-hero-title {
                font-size: 38px;
            }
        }
        </style>
        """),
        unsafe_allow_html=True,
    )


# =========================
# Render
# =========================
def render_hai_search():
    apply_hai_search_css()

    logo_path = find_hai_logo()
    logo_b64 = get_image_base64(logo_path)

    if logo_b64:
        logo_html = f"""
<div class="hai-logo-shell">
    <div class="hai-logo-box">
        <img src="data:image/png;base64,{logo_b64}">
    </div>
</div>
"""
    else:
        logo_html = """
<div class="hai-logo-shell">
    <div class="hai-logo-box" style="color:#667085; text-align:center; line-height:1.8;">
        Logo image not found.<br>
        Please upload a logo file to the <b>assets</b> folder.
    </div>
</div>
"""

    hero_html = f"""
<div class="hai-hero">
    <div>
        <div class="hai-badge">Internal AI Search Assistant</div>
        <div class="hai-hero-title">HAI Search</div>
        <div class="hai-hero-subtitle">
            Search internal technical knowledge, service information, manuals, bulletins,
            and troubleshooting data more efficiently.
            <br><br>
            This page is an entrance page for HAI Search guidance, update notes, usage tips,
            and future search links.
        </div>

        <div class="hai-button-row">
            <a class="hai-main-button" href="{SLACK_HAI_SEARCH_URL}" target="_blank">🚀 Open Slack</a>
            <a class="hai-sub-button" href="#hai-guide">📘 View Usage Guide</a>
        </div>
    </div>

    {logo_html}
</div>
"""
    st.markdown(textwrap.dedent(hero_html), unsafe_allow_html=True)

    st.markdown(
        textwrap.dedent("""
<div class="hai-note">
    <b>Recommended use:</b>
    Use <span class="hai-code">/new</span> for Q&amp;A and
    <span class="hai-code">/docs</span> for document search.
    If the first answer is unclear, try rewriting the question in a simpler way.
</div>
"""),
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
            textwrap.dedent("""
<div class="hai-card">
    <div class="hai-card-title">What is HAI Search?</div>
    <div class="hai-card-text">
        HAI Search is an internal AI search tool for quickly finding information from manuals,
        bulletins, service-related documents, and accumulated technical knowledge.
        It helps users shorten troubleshooting time and find the right documents faster.
    </div>
</div>
"""),
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            textwrap.dedent("""
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
"""),
            unsafe_allow_html=True,
        )

    col3, col4 = st.columns(2, gap="large")

    with col3:
        st.markdown(
            textwrap.dedent("""
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
"""),
            unsafe_allow_html=True,
        )

    with col4:
        quick_links_html = f"""
<div class="hai-card">
    <div class="hai-card-title">Quick Links</div>

    <div class="hai-link-card">
        <div class="hai-link-title">Slack</div>
        <div class="hai-link-desc">
            Open Slack login / workspace page.
        </div>
        <a class="hai-link-button" href="{SLACK_HAI_SEARCH_URL}" target="_blank">Open Slack →</a>
    </div>

    <div class="hai-link-card">
        <div class="hai-link-title">User Guide / Notes</div>
        <div class="hai-link-desc">
            You can replace this with your internal guide link later.
        </div>
        <a class="hai-link-button" href="#" target="_blank">Set guide link here →</a>
    </div>

    <div class="hai-link-card">
        <div class="hai-link-title">Update Information</div>
        <div class="hai-link-desc">
            You can place HAI Search update notes here.
        </div>
        <a class="hai-link-button" href="#" target="_blank">Set update link here →</a>
    </div>
</div>
"""
        st.markdown(textwrap.dedent(quick_links_html), unsafe_allow_html=True)

    st.info("This page can be expanded later with update history, FAQ, usage data, and search improvement notes.")
