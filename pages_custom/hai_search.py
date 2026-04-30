import streamlit as st
import pandas as pd


# =========================
# CSS
# =========================
def apply_hai_search_css():
    st.markdown(
        """
        <style>
        .hai-hero {
            padding: 34px 42px;
            border-radius: 30px;
            background:
                radial-gradient(circle at right center, rgba(255,255,255,0.18), transparent 28%),
                linear-gradient(135deg, #1e1b4b 0%, #2563eb 55%, #0ea5e9 100%);
            color: white;
            box-shadow: 0 18px 45px rgba(37,99,235,0.24);
            margin-bottom: 24px;
        }

        .hai-hero-title {
            font-size: 40px;
            font-weight: 900;
            margin-bottom: 16px;
            letter-spacing: -0.03em;
        }

        .hai-hero-subtitle {
            font-size: 16px;
            color: #e0f2fe;
            line-height: 1.8;
            max-width: 1100px;
        }

        .hai-card {
            background: #ffffff;
            border: 1px solid #e5e7eb;
            border-radius: 22px;
            padding: 22px 24px;
            margin-top: 18px;
            margin-bottom: 18px;
            box-shadow: 0 10px 28px rgba(15,23,42,0.06);
        }

        .hai-card-title {
            font-size: 20px;
            font-weight: 900;
            color: #1f2a44;
            margin-bottom: 10px;
        }

        .hai-card-text {
            font-size: 14px;
            color: #667085;
            line-height: 1.8;
        }

        .hai-command-box {
            background: #f8fafc;
            border: 1px solid #e5e7eb;
            border-radius: 18px;
            padding: 18px 20px;
            margin-bottom: 16px;
        }

        .hai-command-title {
            font-size: 16px;
            font-weight: 900;
            color: #1f2a44;
            margin-bottom: 8px;
        }

        .hai-command-code {
            display: inline-block;
            padding: 5px 9px;
            border-radius: 8px;
            background: #e0f2fe;
            color: #0369a1;
            font-weight: 900;
            font-size: 13px;
            margin-right: 6px;
        }

        div[data-testid="stMetric"] {
            background: #f8fafc;
            border: 1px solid #e5e7eb;
            padding: 14px 16px;
            border-radius: 16px;
        }

        div[data-testid="stMetricLabel"] {
            color: #667085;
            font-weight: 700;
        }

        div[data-testid="stMetricValue"] {
            color: #1f2a44;
            font-weight: 900;
            font-size: 22px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


# =========================
# Data
# =========================
def get_hai_search_summary_data():
    return pd.DataFrame(
        {
            "Item": [
                "Main Entry",
                "Question Command",
                "Document Search Command",
                "Main Users",
                "Main Purpose",
            ],
            "Value": [
                "Slack",
                "/new",
                "/docs",
                "Service / Support / Dealers",
                "Troubleshooting, document search, and service knowledge access",
            ],
        }
    )


def get_hai_search_tips_data():
    return pd.DataFrame(
        {
            "No.": [1, 2, 3, 4],
            "Tip": [
                "Use the private HAI Search channel when asking questions.",
                "Use /new when asking a question.",
                "Use /docs when searching for a document.",
                "Try another wording if the answer is unclear or no document is found.",
            ],
            "Example": [
                "#hai-search-pz",
                "/new what is error 802 on BQ-500",
                "/docs BQ500 service manual",
                "error 802 → error code 802 on BQ-500",
            ],
        }
    )


def get_update_history_data():
    return pd.DataFrame(
        {
            "Version / Topic": [
                "Ver 2.33",
                "Multiple Search",
                "Error Code Search",
                "Japanese Document Link",
                "Product Scope Rule",
            ],
            "Content": [
                "Enhanced searching power to provide more accurate answers.",
                "Multiple Search function was added to search documents more precisely.",
                "Error code documents were added to provide more accurate answers for error-related questions.",
                "Japanese documents can be shown when a Japanese version exists and the user asks in Japanese.",
                "When a product name is included, HAI Search should focus on the specified product unless the question is about connectivity between multiple products.",
            ],
        }
    )


def get_future_items_data():
    return pd.DataFrame(
        {
            "Item": [
                "Document naming normalization",
                "Hyphen handling",
                "Error code retrieval accuracy",
                "Usage promotion",
                "FAQ improvement",
            ],
            "Status": [
                "To be improved",
                "In review",
                "In progress",
                "Ongoing",
                "To be added",
            ],
            "Memo": [
                "File names should be easier to match between English and Japanese documents.",
                "Search results may differ depending on hyphen usage in model names.",
                "Queries like error 802 may need to be normalized to error code 802.",
                "Need to encourage more active usage among global users.",
                "Useful examples and tips can be added to this page.",
            ],
        }
    )


# =========================
# Render Parts
# =========================
def render_hero():
    st.markdown(
        """
        <div class="hai-hero">
            <div class="hai-hero-title">🤖 HAI Search</div>
            <div class="hai-hero-subtitle">
                HAI Search is an AI-powered search and Q&A tool for service support.
                It helps users find troubleshooting information, service manuals,
                bulletins, error code information, and other service-related documents through Slack.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_command_guide():
    st.markdown("### Command Guide")

    st.markdown(
        """
        <div class="hai-command-box">
            <div class="hai-command-title">Ask a question</div>
            <div class="hai-card-text">
                <span class="hai-command-code">/new</span>
                Use this command when you want to ask HAI Search a question.
                <br><br>
                Example: <b>/new what is error 802 on BQ-500</b>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="hai-command-box">
            <div class="hai-command-title">Search documents</div>
            <div class="hai-card-text">
                <span class="hai-command-code">/docs</span>
                Use this command when you want to search for a document directly.
                <br><br>
                Example: <b>/docs BQ500 service manual</b>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_usage_metrics():
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Current Entry", "Slack")

    with col2:
        st.metric("Question Cmd", "/new")

    with col3:
        st.metric("Docs Cmd", "/docs")

    with col4:
        st.metric("Main Users", "Global")


# =========================
# Main Render Function
# =========================
def render_hai_search():
    apply_hai_search_css()
    render_hero()

    render_usage_metrics()

    st.markdown(
        """
        <div class="hai-card">
            <div class="hai-card-title">Overview</div>
            <div class="hai-card-text">
                This page summarizes how to use HAI Search, current improvement items,
                version update notes, and points to be shared with users.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### HAI Search Summary")
    summary_df = get_hai_search_summary_data()
    st.dataframe(summary_df, use_container_width=True, hide_index=True)

    render_command_guide()

    st.markdown("### Usage Tips")
    tips_df = get_hai_search_tips_data()
    st.dataframe(tips_df, use_container_width=True, hide_index=True)

    st.markdown("### Update History / Improvement Notes")
    update_df = get_update_history_data()
    st.dataframe(update_df, use_container_width=True, hide_index=True)

    st.markdown("### Future Improvement Items")
    future_df = get_future_items_data()
    st.dataframe(future_df, use_container_width=True, hide_index=True)

    st.markdown(
        """
        <div class="hai-card">
            <div class="hai-card-title">Memo</div>
            <div class="hai-card-text">
                You can add actual usage data, search logs, frequently asked questions,
                known search issues, and improvement history here later.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
