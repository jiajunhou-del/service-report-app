import streamlit as st
from pathlib import Path
import base64


# =========================
# Path Settings
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE_DIR / "assets"


def get_image_base64(image_path: Path):
    if image_path.exists():
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None


def find_hai_logo():
    """
    自动寻找 HAI Search logo，避免文件名不一致导致 not found
    你可以把图片放在 assets 文件夹里，名字推荐：
    - hai_search_logo.jpg
    - hai_search_logo.png
    - HAI_logo_yoko.jpg
    - HAI_logo_yoko.png
    """
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


def render_hai_search():
    logo_path = find_hai_logo()
    logo_b64 = get_image_base64(logo_path) if logo_path else None

    st.markdown(
        """
        <style>
        /* ========= Page spacing ========= */
        .block-container {
            padding-top: 1.5rem;
            padding-bottom: 2rem;
        }

        /* ========= Hero ========= */
        .hai-hero-wrap {
            background: linear-gradient(135deg, #1e3c9a 0%, #2f66eb 48%, #42b3f0 100%);
            border-radius: 30px;
            padding: 34px 34px 28px 34px;
            box-shadow: 0 18px 40px rgba(32, 74, 182, 0.18);
            margin-bottom: 22px;
        }

        .hai-hero-title {
            color: white;
            font-size: 56px;
            font-weight: 800;
            line-height: 1.05;
            margin-bottom: 14px;
            letter-spacing: -0.8px;
        }

        .hai-hero-subtitle {
            color: rgba(255,255,255,0.96);
            font-size: 20px;
            line-height: 1.75;
            margin-bottom: 10px;
        }

        .hai-badge {
            display: inline-block;
            padding: 7px 14px;
            border-radius: 999px;
            background: rgba(255,255,255,0.15);
            color: white;
            font-size: 14px;
            font-weight: 700;
            margin-bottom: 18px;
            border: 1px solid rgba(255,255,255,0.22);
            backdrop-filter: blur(4px);
        }

        .hai-logo-card {
            background: rgba(255,255,255,0.14);
            border: 1px solid rgba(255,255,255,0.24);
            border-radius: 26px;
            padding: 18px;
            min-height: 320px;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.12),
                        0 14px 30px rgba(0,0,0,0.10);
            backdrop-filter: blur(8px);
        }

        .hai-logo-inner {
            width: 100%;
            background: rgba(255,255,255,0.93);
            border-radius: 22px;
            padding: 18px;
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 260px;
        }

        .hai-btn-row {
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
            margin-top: 18px;
        }

        .hai-btn {
            display: inline-block;
            padding: 11px 18px;
            border-radius: 14px;
            text-decoration: none;
            font-weight: 700;
            font-size: 15px;
            transition: 0.2s ease;
        }

        .hai-btn-primary {
            background: white;
            color: #2353d1 !important;
            box-shadow: 0 8px 20px rgba(0,0,0,0.12);
        }

        .hai-btn-secondary {
            background: rgba(255,255,255,0.14);
            color: white !important;
            border: 1px solid rgba(255,255,255,0.25);
        }

        /* ========= Section titles ========= */
        .hai-section-title {
            font-size: 30px;
            font-weight: 800;
            color: #1d2f5e;
            margin: 12px 0 6px 0;
        }

        .hai-section-desc {
            font-size: 16px;
            color: #66738f;
            margin-bottom: 16px;
        }

        /* ========= Info Cards ========= */
        .hai-card {
            background: #ffffff;
            border: 1px solid #e8edf7;
            border-radius: 22px;
            padding: 22px 22px 18px 22px;
            box-shadow: 0 10px 24px rgba(40, 71, 139, 0.06);
            height: 100%;
        }

        .hai-card-title {
            font-size: 22px;
            font-weight: 800;
            color: #20325e;
            margin-bottom: 12px;
        }

        .hai-card-text {
            font-size: 16px;
            color: #57657f;
            line-height: 1.8;
        }

        .hai-list {
            margin: 0;
            padding-left: 18px;
            color: #57657f;
            line-height: 1.9;
            font-size: 16px;
        }

        .hai-command-box {
            background: #f6f9ff;
            border: 1px solid #dbe7ff;
            border-radius: 16px;
            padding: 14px 16px;
            margin-bottom: 12px;
        }

        .hai-command-title {
            font-size: 16px;
            font-weight: 800;
            color: #2047a8;
            margin-bottom: 6px;
        }

        .hai-code {
            background: #eef4ff;
            color: #214aaf;
            padding: 3px 8px;
            border-radius: 8px;
            font-family: Consolas, Monaco, monospace;
            font-size: 14px;
            font-weight: 700;
        }

        .hai-link-card {
            background: linear-gradient(180deg, #ffffff 0%, #f8fbff 100%);
            border: 1px solid #e7eefb;
            border-radius: 18px;
            padding: 18px 18px;
            margin-bottom: 12px;
        }

        .hai-link-title {
            font-size: 17px;
            font-weight: 800;
            color: #22345f;
            margin-bottom: 6px;
        }

        .hai-link-desc {
            font-size: 14px;
            color: #6c7891;
            margin-bottom: 8px;
        }

        .hai-link-card a {
            color: #2356db !important;
            text-decoration: none;
            font-weight: 700;
        }

        /* ========= highlight strip ========= */
        .hai-highlight {
            background: linear-gradient(90deg, #f3f7ff 0%, #f9fbff 100%);
            border: 1px solid #e2eafd;
            border-radius: 18px;
            padding: 16px 18px;
            margin: 18px 0 8px 0;
            color: #45546f;
            font-size: 15px;
            line-height: 1.8;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # =========================
    # Hero Section
    # =========================
    left, right = st.columns([2.6, 1], gap="large")

    with left:
        st.markdown('<div class="hai-hero-wrap">', unsafe_allow_html=True)
        st.markdown('<div class="hai-badge">Internal AI Search Assistant</div>', unsafe_allow_html=True)
        st.markdown('<div class="hai-hero-title">HAI Search</div>', unsafe_allow_html=True)
        st.markdown(
            """
            <div class="hai-hero-subtitle">
                Search internal technical knowledge, service information, manuals,
                bulletins, and troubleshooting data more efficiently.
                <br><br>
                This page can be used as an entrance page for HAI Search guidance,
                update notes, and future search links.
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <div class="hai-btn-row">
                <a class="hai-btn hai-btn-primary" href="https://app.slack.com/" target="_blank">
                    Open Slack / HAI Search
                </a>
                <a class="hai-btn hai-btn-secondary" href="#hai-guide">
                    View Usage Guide
                </a>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with right:
        st.markdown('<div class="hai-logo-card"><div class="hai-logo-inner">', unsafe_allow_html=True)
        if logo_b64:
            st.markdown(
                f"""
                <div style="text-align:center; width:100%;">
                    <img src="data:image/png;base64,{logo_b64}" 
                         style="max-width:100%; max-height:220px; object-fit:contain; border-radius:14px;">
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                """
                <div style="
                    text-align:center;
                    color:#7a88a6;
                    font-size:16px;
                    line-height:1.8;
                    padding: 20px;">
                    Logo image not found.<br>
                    Please place the file in <b>assets</b> folder.<br><br>
                    Recommended file name:<br>
                    <code>HAI_logo_yoko.jpg</code>
                </div>
                """,
                unsafe_allow_html=True,
            )
        st.markdown("</div></div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="hai-highlight">
            <b>Recommended use:</b> Use <span class="hai-code">/new</span> for Q&A
            and <span class="hai-code">/docs</span> for document search.
            If the first answer is unclear, try rewriting the question in a simpler way.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # =========================
    # Guide Section
    # =========================
    st.markdown('<div id="hai-guide" class="hai-section-title">HAI Search Guide</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="hai-section-desc">A simple overview of what HAI Search does and how to use it.</div>',
        unsafe_allow_html=True,
    )

    c1, c2 = st.columns(2, gap="large")

    with c1:
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

    with c2:
        st.markdown(
            """
            <div class="hai-card">
                <div class="hai-card-title">Main Commands</div>

                <div class="hai-command-box">
                    <div class="hai-command-title">/new</div>
                    <div class="hai-card-text">
                        Ask a question directly.<br>
                        Example: <span class="hai-code">/new what is error 802 on BQ-500?</span>
                    </div>
                </div>

                <div class="hai-command-box">
                    <div class="hai-command-title">/docs</div>
                    <div class="hai-card-text">
                        Search for related manuals or documents.<br>
                        Example: <span class="hai-code">/docs BQ500 service manual</span>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    c3, c4 = st.columns(2, gap="large")

    with c3:
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

    with c4:
        st.markdown(
            """
            <div class="hai-card">
                <div class="hai-card-title">Quick Links</div>

                <div class="hai-link-card">
                    <div class="hai-link-title">Slack</div>
                    <div class="hai-link-desc">Open Slack workspace and access HAI Search channels.</div>
                    <a href="https://app.slack.com/" target="_blank">Open Slack</a>
                </div>

                <div class="hai-link-card">
                    <div class="hai-link-title">User Guide / Notes</div>
                    <div class="hai-link-desc">You can replace this with your internal guide link later.</div>
                    <a href="#" target="_blank">Set guide link here</a>
                </div>

                <div class="hai-link-card">
                    <div class="hai-link-title">Update Information</div>
                    <div class="hai-link-desc">You can also place HAI Search update notes here.</div>
                    <a href="#" target="_blank">Set update link here</a>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("")
    st.info("If you want, this page can also be expanded later with update history, FAQ, and a mini search guide section.")
