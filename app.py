import streamlit as st

from pages_custom.care_pack import render_care_pack
from pages_custom.ice_link_report import render_ice_link_report
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
                            and HAI Search support information.
                        </div>
                        <div class="portal-mini-grid">
                            <div class="portal-mini-card">📊 iCE LiNK Report</div>
                            <div class="portal-mini-card">📦 Care Pack</div>
                            <div class="portal-mini-card">🤖 HAI Search</div>
                            <div class="portal-mini-card">📘 Service Data</div>
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
                                🤖 HAI Search
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
