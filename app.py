import streamlit as st
import streamlit.components.v1 as components

from pages_custom.care_pack import render_care_pack
from pages_custom.ice_link_report_v2 import render_ice_link_report
from pages_custom.hai_search import render_hai_search


# =========================
# Basic Page Settings
# =========================
st.set_page_config(
    page_title="Service Data Portal",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================
# Login Settings
# =========================
APP_PASSWORD = "ts123"

GOAL_SHEET_URL = "https://docs.google.com/spreadsheets/d/1T5CDML3SiziSR_pJHy58A41DGovEfHYu/edit?pli=1&gid=1976316740#gid=1976316740"


# =========================
# Session State Init
# =========================
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False


# =========================
# Common Page Header
# =========================
def page_header(title: str, subtitle: str):
    st.markdown(f"<div class='main-title'>{title}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='sub-title'>{subtitle}</div>", unsafe_allow_html=True)


# =========================
# Goal Progress Page
# =========================
def render_goal_progress():
    page_header(
        "Goal Progress",
        "Review the current progress of service-related goals and action items."
    )

    components.html(
        f"""
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

                .goal-card {{
                    background:
                        linear-gradient(135deg, rgba(255,255,255,0.98), rgba(248,250,252,0.96));
                    border: 1px solid #e5e7eb;
                    border-radius: 28px;
                    padding: 34px 38px;
                    box-shadow: 0 20px 55px rgba(15,23,42,0.08);
                    max-width: 880px;
                    box-sizing: border-box;
                }}

                .goal-badge {{
                    display: inline-block;
                    padding: 7px 14px;
                    border-radius: 999px;
                    background: #eef2ff;
                    color: #3730a3;
                    font-size: 13px;
                    font-weight: 800;
                    margin-bottom: 18px;
                }}

                .goal-title {{
                    font-size: 30px;
                    font-weight: 900;
                    color: #1f2a44;
                    margin-bottom: 12px;
                    letter-spacing: -0.03em;
                }}

                .goal-desc {{
                    font-size: 15px;
                    color: #667085;
                    line-height: 1.8;
                    margin-bottom: 26px;
                }}

                .goal-info-grid {{
                    display: grid;
                    grid-template-columns: repeat(3, 1fr);
                    gap: 14px;
                    margin-bottom: 28px;
                }}

                .goal-info-box {{
                    background: #f8fafc;
                    border: 1px solid #e5e7eb;
                    border-radius: 18px;
                    padding: 16px 18px;
                }}

                .goal-info-label {{
                    font-size: 12px;
                    font-weight: 800;
                    color: #94a3b8;
                    margin-bottom: 6px;
                    text-transform: uppercase;
                    letter-spacing: 0.06em;
                }}

                .goal-info-value {{
                    font-size: 16px;
                    font-weight: 900;
                    color: #1f2a44;
                }}

                .goal-button {{
                    display: inline-block;
                    text-decoration: none;
                    padding: 14px 24px;
                    border-radius: 16px;
                    background: linear-gradient(135deg, #4f46e5 0%, #2563eb 100%);
                    color: white;
                    font-weight: 900;
                    box-shadow: 0 12px 24px rgba(37,99,235,0.22);
                }}

                .goal-button:hover {{
                    filter: brightness(1.05);
                }}

                @media (max-width: 900px) {{
                    .goal-info-grid {{
                        grid-template-columns: 1fr;
                    }}
                }}
            </style>
        </head>

        <body>
            <div class="goal-card">
                <div class="goal-badge">🎯 Goal Management</div>

                <div class="goal-title">Goal Progress Sheet for SP Family</div>

                <div class="goal-desc">
                    This page provides quick access to the shared goal progress sheet.
                    Please use the Google Spreadsheet below to check the latest progress,
                    status updates, and remaining action items.
                </div>

                <div class="goal-info-grid">
                    <div class="goal-info-box">
                        <div class="goal-info-label">View</div>
                        <div class="goal-info-value">Goal Progress</div>
                    </div>

                    <div class="goal-info-box">
                        <div class="goal-info-label">Format</div>
                        <div class="goal-info-value">Google Sheet</div>
                    </div>

                    <div class="goal-info-box">
                        <div class="goal-info-label">Purpose</div>
                        <div class="goal-info-value">Progress Check</div>
                    </div>
                </div>

                <a class="goal-button" href="{GOAL_SHEET_URL}" target="_blank">
                    Open Goal Progress Sheet →
                </a>
            </div>
        </body>
        </html>
        """,
        height=430,
    )


# =========================
# Login Page
# =========================
def login_page():
    st.markdown(
        """
        <style>
        .stApp {
            background:
                radial-gradient(circle at top left, rgba(59,130,246,0.28), transparent 32%),
                radial-gradient(circle at bottom right, rgba(14,165,233,0.18), transparent 30%),
                linear-gradient(135deg, #0f172a 0%, #1e293b 48%, #0b1120 100%);
        }

        header[data-testid="stHeader"] {
            background: transparent;
        }

        .login-shell {
            display: flex;
            justify-content: center;
            align-items: center;
            padding-top: 55px;
            padding-bottom: 20px;
        }

        .login-card {
            width: 100%;
            max-width: 980px;
            border-radius: 32px;
            padding: 0;
            overflow: hidden;
            background: rgba(255,255,255,0.96);
            box-shadow: 0 30px 90px rgba(0,0,0,0.35);
            border: 1px solid rgba(255,255,255,0.35);
        }

        .login-grid {
            display: grid;
            grid-template-columns: 1.05fr 0.95fr;
            min-height: 430px;
        }

        .login-left {
            padding: 48px 50px;
            background:
                linear-gradient(135deg, rgba(30,64,175,0.95), rgba(15,23,42,0.96)),
                radial-gradient(circle at top left, rgba(255,255,255,0.18), transparent 35%);
            color: white;
        }

        .login-right {
            padding: 48px 46px;
            background: #ffffff;
        }

        .portal-badge {
            display: inline-block;
            padding: 7px 15px;
            border-radius: 999px;
            background: rgba(255,255,255,0.16);
            border: 1px solid rgba(255,255,255,0.28);
            color: #dbeafe;
            font-size: 13px;
            font-weight: 800;
            margin-bottom: 22px;
        }

        .portal-title {
            font-size: 46px;
            font-weight: 900;
            line-height: 1.08;
            letter-spacing: -0.04em;
            margin-bottom: 18px;
        }

        .portal-subtitle {
            font-size: 16px;
            line-height: 1.8;
            color: #dbeafe;
            margin-bottom: 28px;
        }

        .portal-mini-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
            margin-top: 24px;
        }

        .portal-mini-card {
            padding: 14px 15px;
            border-radius: 16px;
            background: rgba(255,255,255,0.12);
            border: 1px solid rgba(255,255,255,0.18);
            font-size: 13px;
            color: #eff6ff;
        }

        .login-title {
            font-size: 28px;
            font-weight: 900;
            color: #1f2a44;
            margin-bottom: 8px;
        }

        .login-desc {
            color: #667085;
            font-size: 14px;
            line-height: 1.7;
            margin-bottom: 26px;
        }

        .feature-list {
            padding: 18px 20px;
            border-radius: 20px;
            background: #f8fafc;
            border: 1px solid #e5e7eb;
            margin-bottom: 24px;
        }

        .feature-title {
            font-size: 14px;
            font-weight: 800;
            color: #1f2a44;
            margin-bottom: 12px;
        }

        .feature-item {
            font-size: 14px;
            color: #475467;
            line-height: 2;
        }

        div[data-testid="stTextInput"] input {
            border-radius: 14px !important;
            border: 1px solid #cbd5e1 !important;
            min-height: 48px !important;
            background-color: #ffffff !important;
        }

        div[data-testid="stButton"] button {
            border-radius: 14px !important;
            min-height: 48px !important;
            font-weight: 800 !important;
            background: linear-gradient(135deg, #1d4ed8 0%, #2563eb 100%) !important;
            color: white !important;
            border: none !important;
            box-shadow: 0 10px 20px rgba(37,99,235,0.22);
        }

        div[data-testid="stButton"] button:hover {
            filter: brightness(1.05);
        }

        @media (max-width: 900px) {
            .login-grid {
                grid-template-columns: 1fr;
            }

            .login-left {
                padding: 34px 30px;
            }

            .login-right {
                padding: 34px 30px;
            }

            .portal-title {
                font-size: 34px;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="login-shell">
            <div class="login-card">
                <div class="login-grid">
                    <div class="login-left">
                        <div class="portal-badge">Horizon International</div>
                        <div class="portal-title">Service Data<br>Portal</div>
                        <div class="portal-subtitle">
                            A centralized portal for iCE LiNK reports, Care Pack bulletins,
                            HAI Search support information, and goal progress tracking.
                        </div>
                        <div class="portal-mini-grid">
                            <div class="portal-mini-card">📊 iCE LiNK Report</div>
                            <div class="portal-mini-card">📦 Care Pack</div>
                            <div class="portal-mini-card">🤖 HAI Search</div>
                            <div class="portal-mini-card">🎯 Goal Progress</div>
                        </div>
                    </div>
                    <div class="login-right">
                        <div class="login-title">Welcome back</div>
                        <div class="login-desc">
                            Please enter the access password to continue.
                            This portal is designed for internal service data review and document access.
                        </div>
                        <div class="feature-list">
                            <div class="feature-title">Available views</div>
                            <div class="feature-item">
                                📊 iCE LiNK Report<br>
                                📦 Care Pack<br>
                                🤖 HAI Search<br>
                                🎯 Goal Progress
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    left, center, right = st.columns([1.25, 1.5, 1.25])

    with center:
        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter password",
            key="login_password",
        )

        if st.button("Login", use_container_width=True):
            if password.strip() == APP_PASSWORD:
                st.session_state["logged_in"] = True
                st.rerun()
            else:
                st.error("Password is incorrect.")


# =========================
# Login Check
# =========================
if not st.session_state["logged_in"]:
    login_page()
    st.stop()


# =========================
# Main CSS
# =========================
st.markdown(
    """
    <style>
    .stApp {
        background: #f6f8fb;
    }

    section[data-testid="stSidebar"] {
        background:
            radial-gradient(circle at top left, rgba(37,99,235,0.28), transparent 34%),
            linear-gradient(180deg, #17233d 0%, #111827 100%);
        padding-top: 26px;
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    section[data-testid="stSidebar"] h2 {
        font-size: 22px !important;
        font-weight: 900 !important;
        letter-spacing: 0.08em;
        margin-bottom: 24px !important;
        color: #ffffff !important;
    }

    section[data-testid="stSidebar"] div[role="radiogroup"] {
        display: flex;
        flex-direction: column;
        gap: 18px;
    }

    section[data-testid="stSidebar"] label[data-baseweb="radio"] {
        background: rgba(255,255,255,0.08);
        border: 1px solid rgba(255,255,255,0.13);
        border-radius: 18px;
        padding: 16px 18px !important;
        margin: 0 !important;
        transition: all 0.18s ease;
        box-shadow: 0 8px 18px rgba(0,0,0,0.08);
    }

    section[data-testid="stSidebar"] label[data-baseweb="radio"]:hover {
        background: rgba(255,255,255,0.16);
        transform: translateX(4px);
        border-color: rgba(255,255,255,0.24);
    }

    section[data-testid="stSidebar"] label[data-baseweb="radio"] > div:first-child {
        margin-right: 13px;
    }

    section[data-testid="stSidebar"] label[data-baseweb="radio"] p {
        font-size: 17px !important;
        font-weight: 800 !important;
        line-height: 1.3 !important;
    }

    section[data-testid="stSidebar"] hr {
        margin-top: 44px !important;
        margin-bottom: 28px !important;
        border-color: rgba(255,255,255,0.12) !important;
    }

    section[data-testid="stSidebar"] button {
        border-radius: 16px !important;
        min-height: 46px !important;
        font-weight: 800 !important;
        background: rgba(255,255,255,0.12) !important;
        border: 1px solid rgba(255,255,255,0.18) !important;
    }

    section[data-testid="stSidebar"] button:hover {
        background: rgba(255,255,255,0.22) !important;
    }

    .main-title {
        font-size: 38px;
        font-weight: 900;
        color: #1f2a44;
        margin-bottom: 6px;
        letter-spacing: -0.03em;
    }

    .sub-title {
        font-size: 16px;
        color: #667085;
        margin-bottom: 28px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# =========================
# Sidebar
# =========================
st.sidebar.markdown("## VIEWS")

view = st.sidebar.radio(
    "",
    [
        "📊  iCE LiNK Report",
        "📦  Care Pack",
        "🤖  HAI Search",
        "🎯  Goal Progress",
    ],
    index=1,
)

st.sidebar.markdown("---")
st.sidebar.caption("Service Data Portal")
st.sidebar.caption("Horizon International")

if st.sidebar.button("Logout", use_container_width=True):
    st.session_state["logged_in"] = False
    st.rerun()


# =========================
# Page Switch
# =========================
if view == "📊  iCE LiNK Report":
    render_ice_link_report()

elif view == "📦  Care Pack":
    render_care_pack()

elif view == "🤖  HAI Search":
    render_hai_search()

elif view == "🎯  Goal Progress":
    render_goal_progress()
