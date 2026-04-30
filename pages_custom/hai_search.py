import streamlit as st
from pathlib import Path


# =========================
# Paths / Links
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE_DIR / "assets"

HAI_LOGO_PATH = ASSETS_DIR / "hai_search_logo.jpg"

SLACK_URL = "https://app.slack.com/"


# =========================
# CSS
# =========================
def apply_hai_css():
    st.markdown(
        """
<style>
.hai-hero-title {
    font-size: 48px;
    font-weight: 900;
    color: white;
    line-height: 1.1;
    margin-bottom: 12px;
}

.hai-hero-subtitle {
    font-size: 17px;
    color: rgba(255,255,255,0.95);
    line-height: 1.8;
    margin-bottom: 20px;
}

.hai-badge {
    display: inline-block;
    padding: 8px 16px;
    border-radius: 999px;
    background: rgba(255,255,255,0.16);
    border: 1px solid rgba(255,255,255,0.25);
    color: white;
    font-size: 13px;
    font-weight: 800;
    margin-bottom: 20px;
}

.hai-note {
    background: #eff6ff;
    border: 1px solid #dbeafe;
    color: #1e3a8a;
    border-radius: 18px;
    padding: 15px 18px;
    margin-top: 18px;
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

div[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: 24px !important;
}

div.stLinkButton > a {
    border-radius: 14px !important;
    font-weight: 900 !important;
    font-size: 15px !important;
    padding: 0.72rem 1.1rem !important;
    text-decoration: none !important;
}
</style>
        """,
        unsafe_allow_html=True,
    )


# =========================
# Components
# =========================
def render_hero():
    with st.container():
        st.markdown(
            """
<div style="
    background: linear-gradient(135deg, #1f3f9d 0%, #2f63e0 58%, #43b2ee 100%);
    border-radius: 34px;
    padding: 42px 48px;
    box-shadow: 0 10px 28px rgba(0,0,0,0.08);
    margin-bottom: 28px;
">
            """,
            unsafe_allow_html=True,
        )

        left, right = st.columns([4.2, 1.5], gap="large")

        with left:
            st.markdown('<div class="hai-badge">Internal AI Search Assistant</div>', unsafe_allow_html=True)

            title_col1, title_col2 = st.columns([0.35, 4])

            with title_col1:
                if HAI_LOGO_PATH.exists():
                    st.image(str(HAI_LOGO_PATH), use_container_width=True)
                else:
                    st.write("🤖")

            with title_col2:
                st.markdown('<div class="hai-hero-title">HAI Search</div>', unsafe_allow_html=True)

            st.markdown(
                """
<div class="hai-hero-subtitle">
Search internal technical knowledge, service information, manuals,
bulletins, and troubleshooting data more efficiently.
<br><br>
This page is an entrance portal for HAI Search guidance, update notes,
usage tips, and future support links.
</div>
                """,
                unsafe_allow_html=True,
            )

            btn1, btn2, _ = st.columns([1.2, 1.2, 3])

            with btn1:
                st.link_button("🚀 Open Slack", SLACK_URL, use_container_width=True)

            with btn2:
                st.link_button("📘 Usage Guide", "#hai-guide", use_container_width=True)

        with right:
            with st.container(border=True):
                if HAI_LOGO_PATH.exists():
                    st.image(str(HAI_LOGO_PATH), use_container_width=True)
                else:
                    st.warning("Logo image not found: assets/hai_search_logo.jpg")

        st.markdown("</div>", unsafe_allow_html=True)


def render_entry_cards():
    st.markdown('<div class="hai-section-title">HAI Search Portal</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="hai-section-desc">Choose an entry below to start using HAI Search.</div>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2, gap="large")

    with col1:
        with st.container(border=True):
            st.markdown("### 🔎 Search in Slack")
            st.write(
                "Open Slack and use HAI Search through your available workspace and channel. "
                "Use `/new` for questions and `/docs` for document search."
            )
            st.link_button("🚀 Open Slack", SLACK_URL, use_container_width=True)

    with col2:
        with st.container(border=True):
            st.markdown("### 📝 Update Notes")
            st.write(
                "Review HAI Search improvement history, version update notes, "
                "known issues, and future enhancement items."
            )
            st.button("📘 View Update Notes", use_container_width=True, disabled=True)


def render_guide():
    st.markdown('<div id="hai-guide" class="hai-section-title">Usage Guide</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="hai-section-desc">A simple overview of what HAI Search does and how to use it.</div>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2, gap="large")

    with col1:
        with st.container(border=True):
            st.markdown("### What is HAI Search?")
            st.write(
                "HAI Search is an internal AI search tool for quickly finding information "
                "from manuals, bulletins, service-related documents, and accumulated "
                "technical knowledge. It helps users shorten troubleshooting time and find "
                "the right documents faster."
            )

    with col2:
        with st.container(border=True):
            st.markdown("### Main Commands")
            st.markdown("#### `/new`")
            st.write("Ask a question directly.")
            st.code("/new what is error 802 on BQ-500?")

            st.markdown("#### `/docs`")
            st.write("Search for related manuals or documents.")
            st.code("/docs BQ500 service manual")

    col3, col4 = st.columns(2, gap="large")

    with col3:
        with st.container(border=True):
            st.markdown("### Usage Tips")
            st.markdown(
                """
- Use your private HAI Search channel when possible.
- Keep the question simple and clear.
- Avoid unnecessary symbols or extra spaces.
- If no answer is found, try another wording.
- Include product name and error code for better results.
                """
            )

    with col4:
        with st.container(border=True):
            st.markdown("### Future Content")
            st.write(
                "This area can be expanded later with FAQ, update history, "
                "usage analytics, known retrieval issues, and search improvement notes."
            )


# =========================
# Main Render
# =========================
def render_hai_search():
    apply_hai_css()

    render_hero()

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

    render_entry_cards()
    render_guide()

    st.info(
        "This page can later be expanded with update history, FAQ, usage analytics, and search improvement notes."
    )
