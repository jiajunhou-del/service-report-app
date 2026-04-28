import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path


# =========================================================
# Page Settings
# =========================================================
st.set_page_config(
    page_title="Service Report Admin Console",
    page_icon="🛠️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# Login Settings
# =========================================================
USERS = {
    "TS Admin": "admin123",
    "Service Viewer": "viewer123"
}


# =========================================================
# Login Page
# =========================================================
def login_page():
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(135deg, #111827 0%, #1f2a44 45%, #eef3f8 45%, #f8fafc 100%);
        }

        [data-testid="stSidebar"] {
            display: none;
        }

        .login-card {
            max-width: 980px;
            margin: 110px auto 0 auto;
            display: grid;
            grid-template-columns: 1.05fr 0.95fr;
            background: white;
            border-radius: 28px;
            overflow: hidden;
            box-shadow: 0 30px 90px rgba(0,0,0,0.25);
        }

        .login-left {
            background: linear-gradient(150deg, #1f2a44 0%, #24314f 55%, #0f766e 120%);
            color: white;
            padding: 52px 48px;
            position: relative;
        }

        .login-left::after {
            content: "";
            position: absolute;
            width: 220px;
            height: 220px;
            right: -80px;
            bottom: -80px;
            border-radius: 999px;
            background: rgba(255,255,255,0.08);
        }

        .login-badge {
            display: inline-block;
            background: rgba(255,255,255,0.12);
            border: 1px solid rgba(255,255,255,0.18);
            padding: 8px 14px;
            border-radius: 999px;
            font-size: 12px;
            letter-spacing: 0.08em;
            margin-bottom: 30px;
        }

        .login-title {
            font-size: 40px;
            font-weight: 850;
            line-height: 1.15;
            margin-bottom: 20px;
        }

        .login-text {
            color: rgba(255,255,255,0.74);
            font-size: 15px;
            line-height: 1.8;
            margin-bottom: 34px;
            max-width: 430px;
        }

        .login-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }

        .login-tag {
            padding: 9px 12px;
            border-radius: 13px;
            background: rgba(255,255,255,0.08);
            border: 1px solid rgba(255,255,255,0.18);
            font-size: 13px;
            color: rgba(255,255,255,0.92);
        }

        .login-right {
            padding: 52px 46px;
            background: #ffffff;
        }

        .login-heading {
            font-size: 28px;
            font-weight: 850;
            color: #1f2a44;
            margin-bottom: 8px;
        }

        .login-caption {
            color: #718096;
            font-size: 14px;
            margin-bottom: 28px;
            line-height: 1.7;
        }

        div.stButton > button {
            width: 100%;
            height: 48px;
            border-radius: 14px;
            background: #1f2a44;
            color: white;
            border: none;
            font-weight: 700;
            margin-top: 10px;
        }

        div.stButton > button:hover {
            background: #263552;
            color: white;
            border: none;
        }

        .footer-note {
            text-align: center;
            color: #8a95a8;
            font-size: 12px;
            margin-top: 22px;
        }
        </style>

        <div class="login-card">
            <div class="login-left">
                <div class="login-badge">SERVICE REPORT SYSTEM</div>
                <div class="login-title">
                    Service Report<br>
                    Admin Console
                </div>
                <div class="login-text">
                    Access dealer overview, country view, machine analysis,
                    error trends, and service summary charts from one portal.
                </div>
                <div class="login-tags">
                    <div class="login-tag">📊 Dealer overview</div>
                    <div class="login-tag">🌏 Country view</div>
                    <div class="login-tag">🛠 Machine view</div>
                    <div class="login-tag">⚠️ Error analysis</div>
                    <div class="login-tag">📈 Summary charts</div>
                </div>
            </div>

            <div class="login-right">
                <div class="login-heading">Welcome back</div>
                <div class="login-caption">
                    Please sign in to continue to the Service Report Console.
                </div>
        """,
        unsafe_allow_html=True
    )

    role = st.selectbox("Access Role", list(USERS.keys()))
    password = st.text_input("Password", type="password", placeholder="Enter your password")

    if st.button("Enter Console →"):
        if password == USERS[role]:
            st.session_state["logged_in"] = True
            st.session_state["role"] = role
            st.rerun()
        else:
            st.error("Password is incorrect. Please try again.")

    st.markdown(
        """
            </div>
        </div>
        <div class="footer-note">
            Horizon International Technical Support / Service Report Portal
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# Login Check
# =========================================================
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if "role" not in st.session_state:
    st.session_state["role"] = None

if not st.session_state["logged_in"]:
    login_page()
    st.stop()


# =========================================================
# Main App Style
# =========================================================
st.markdown(
    """
    <style>
    .stApp {
        background: #f4f6fa;
    }

    [data-testid="stSidebar"] {
        background: #1f2a44;
    }

    [data-testid="stSidebar"] * {
        color: white;
    }

    [data-testid="stSidebar"] .stRadio label {
        color: white !important;
        font-size: 18px;
        font-weight: 600;
    }

    [data-testid="stSidebar"] .stButton button {
        background: rgba(255,255,255,0.08);
        color: white;
        border: 1px solid rgba(255,255,255,0.18);
        border-radius: 12px;
        width: 100%;
    }

    [data-testid="stSidebar"] .stButton button:hover {
        background: rgba(255,255,255,0.16);
        color: white;
        border: 1px solid rgba(255,255,255,0.28);
    }

    .main-title {
        font-size: 34px;
        font-weight: 850;
        color: #1f2a44;
        margin-bottom: 4px;
    }

    .main-subtitle {
        color: #6b7280;
        font-size: 15px;
        margin-bottom: 24px;
    }

    .section-card {
        background: white;
        padding: 24px;
        border-radius: 22px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 10px 28px rgba(15, 23, 42, 0.06);
        margin-bottom: 20px;
    }

    div[data-testid="metric-container"] {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        padding: 18px;
        border-radius: 18px;
        box-shadow: 0 8px 22px rgba(15, 23, 42, 0.05);
    }

    .role-badge {
        display: inline-block;
        background: #e6f3f7;
        color: #0e7490;
        padding: 7px 12px;
        border-radius: 999px;
        font-size: 13px;
        font-weight: 700;
        margin-bottom: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# Data Loading
# =========================================================
DATA_FILE = Path("service_report.xlsx")


@st.cache_data
def load_data():
    if DATA_FILE.exists():
        df = pd.read_excel(DATA_FILE)
        df.columns = [str(c).strip() for c in df.columns]
        return df
    else:
        return pd.DataFrame()


df = load_data()


# =========================================================
# Sidebar
# =========================================================
with st.sidebar:
    st.markdown("## 🛠 Service Report")
    st.markdown("### Admin Console")
    st.markdown("---")

    st.markdown("#### VIEWS")

    view = st.radio(
        label="",
        options=[
            "📊 Dealer overview",
            "🌏 Country view",
            "🛠 Machine view",
            "⚠️ Error analysis",
            "📈 Summary charts",
            "📥 Import data"
        ],
        index=0
    )

    st.markdown("---")
    st.markdown("#### LOGIN")
    st.success(st.session_state["role"])

    if st.button("Logout"):
        st.session_state["logged_in"] = False
        st.session_state["role"] = None
        st.rerun()

    st.markdown("---")
    st.markdown("#### TOOLS")

    if st.button("↓ Generate Master Excel"):
        st.info("This function can be connected later.")


# =========================================================
# Common Header
# =========================================================
st.markdown('<div class="main-title">Service Report Admin Console</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="main-subtitle">Technical support data dashboard for service reports, machines, countries, and error trends.</div>',
    unsafe_allow_html=True
)
st.markdown(
    f'<div class="role-badge">Access Role: {st.session_state["role"]}</div>',
    unsafe_allow_html=True
)


# =========================================================
# No Data Warning
# =========================================================
if df.empty and view != "📥 Import data":
    st.warning(
        "service_report.xlsx が見つからない、またはデータを読み込めませんでした。"
        " GitHub に service_report.xlsx があるか確認してください。"
    )


# =========================================================
# Helper Functions
# =========================================================
def get_text_columns(data):
    return data.select_dtypes(include=["object"]).columns.tolist()


def get_numeric_columns(data):
    return data.select_dtypes(include=["number"]).columns.tolist()


def show_basic_kpis(data):
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Records", len(data))

    with col2:
        st.metric("Columns", len(data.columns))

    with col3:
        st.metric("Text Columns", len(get_text_columns(data)))

    with col4:
        st.metric("Numeric Columns", len(get_numeric_columns(data)))


def show_dataframe(data):
    st.dataframe(data, use_container_width=True)


# =========================================================
# View: Dealer overview
# =========================================================
if view == "📊 Dealer overview":
    st.markdown("### 📊 Dealer overview")

    if not df.empty:
        show_basic_kpis(df)

        st.markdown("#### Dealer / Category Summary")

        text_cols = get_text_columns(df)

        if text_cols:
            selected_col = st.selectbox("Select dealer or category column", text_cols)

            summary = (
                df[selected_col]
                .astype(str)
                .value_counts()
                .reset_index()
            )
            summary.columns = [selected_col, "Count"]

            fig = px.bar(
                summary.head(20),
                x=selected_col,
                y="Count",
                title=f"Top 20 by {selected_col}"
            )
            st.plotly_chart(fig, use_container_width=True)

            show_dataframe(summary)
        else:
            st.info("カテゴリ列が見つかりませんでした。")

    else:
        st.info("データがありません。")


# =========================================================
# View: Country view
# =========================================================
elif view == "🌏 Country view":
    st.markdown("### 🌏 Country view")

    if not df.empty:
        text_cols = get_text_columns(df)

        country_candidates = [
            c for c in text_cols
            if "country" in c.lower()
            or "region" in c.lower()
            or "area" in c.lower()
        ]

        if country_candidates:
            country_col = st.selectbox("Country column", country_candidates)
        elif text_cols:
            country_col = st.selectbox("Country column", text_cols)
        else:
            country_col = None

        if country_col:
            country_summary = (
                df[country_col]
                .astype(str)
                .value_counts()
                .reset_index()
            )
            country_summary.columns = [country_col, "Count"]

            col1, col2 = st.columns([1.2, 1])

            with col1:
                fig = px.bar(
                    country_summary.head(20),
                    x=country_col,
                    y="Count",
                    title=f"Service Report Count by {country_col}"
                )
                st.plotly_chart(fig, use_container_width=True)

            with col2:
                st.markdown("#### Country Summary")
                show_dataframe(country_summary)

        else:
            st.info("Country view に使用できる列が見つかりませんでした。")

    else:
        st.info("データがありません。")


# =========================================================
# View: Machine view
# =========================================================
elif view == "🛠 Machine view":
    st.markdown("### 🛠 Machine view")

    if not df.empty:
        text_cols = get_text_columns(df)

        machine_candidates = [
            c for c in text_cols
            if "machine" in c.lower()
            or "model" in c.lower()
            or "product" in c.lower()
            or "機種" in c
            or "製品" in c
        ]

        if machine_candidates:
            machine_col = st.selectbox("Machine / Model column", machine_candidates)
        elif text_cols:
            machine_col = st.selectbox("Machine / Model column", text_cols)
        else:
            machine_col = None

        if machine_col:
            machine_summary = (
                df[machine_col]
                .astype(str)
                .value_counts()
                .reset_index()
            )
            machine_summary.columns = [machine_col, "Count"]

            fig = px.bar(
                machine_summary.head(20),
                x=machine_col,
                y="Count",
                title=f"Top Machines by {machine_col}"
            )
            st.plotly_chart(fig, use_container_width=True)

            show_dataframe(machine_summary)
        else:
            st.info("Machine view に使用できる列が見つかりませんでした。")

    else:
        st.info("データがありません。")


# =========================================================
# View: Error analysis
# =========================================================
elif view == "⚠️ Error analysis":
    st.markdown("### ⚠️ Error analysis")

    if not df.empty:
        text_cols = get_text_columns(df)
        numeric_cols = get_numeric_columns(df)

        error_candidates = [
            c for c in df.columns
            if "error" in c.lower()
            or "fault" in c.lower()
            or "alarm" in c.lower()
            or "エラー" in c
        ]

        if error_candidates:
            error_col = st.selectbox("Error column", error_candidates)
        elif text_cols:
            error_col = st.selectbox("Error column", text_cols)
        elif numeric_cols:
            error_col = st.selectbox("Error column", numeric_cols)
        else:
            error_col = None

        if error_col:
            error_summary = (
                df[error_col]
                .astype(str)
                .value_counts()
                .reset_index()
            )
            error_summary.columns = [error_col, "Count"]

            fig = px.bar(
                error_summary.head(20),
                x=error_col,
                y="Count",
                title=f"Top Error / Issue Trends by {error_col}"
            )
            st.plotly_chart(fig, use_container_width=True)

            show_dataframe(error_summary)
        else:
            st.info("Error analysis に使用できる列が見つかりませんでした。")

    else:
        st.info("データがありません。")


# =========================================================
# View: Summary charts
# =========================================================
elif view == "📈 Summary charts":
    st.markdown("### 📈 Summary charts")

    if not df.empty:
        show_basic_kpis(df)

        text_cols = get_text_columns(df)
        numeric_cols = get_numeric_columns(df)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("#### Category Chart")
            if text_cols:
                category_col = st.selectbox("Category column", text_cols, key="summary_category")
                category_summary = df[category_col].astype(str).value_counts().reset_index()
                category_summary.columns = [category_col, "Count"]

                fig = px.pie(
                    category_summary.head(10),
                    names=category_col,
                    values="Count",
                    title=f"Share by {category_col}"
                )
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("カテゴリ列がありません。")

        with col2:
            st.markdown("#### Numeric Distribution")
            if numeric_cols:
                numeric_col = st.selectbox("Numeric column", numeric_cols, key="summary_numeric")
                fig = px.histogram(
                    df,
                    x=numeric_col,
                    title=f"Distribution of {numeric_col}"
                )
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("数値列がありません。")

        st.markdown("#### Raw Data")
        show_dataframe(df)

    else:
        st.info("データがありません。")


# =========================================================
# View: Import data
# =========================================================
elif view == "📥 Import data":
    st.markdown("### 📥 Import data")

    st.info(
        "ここでは、Excelファイルをアップロードして一時的に内容を確認できます。"
        "正式にアプリへ反映する場合は、GitHub の service_report.xlsx を更新してください。"
    )

    uploaded_file = st.file_uploader(
        "Upload Excel file",
        type=["xlsx", "xls"]
    )

    if uploaded_file is not None:
        try:
            uploaded_df = pd.read_excel(uploaded_file)
            uploaded_df.columns = [str(c).strip() for c in uploaded_df.columns]

            st.success("Excel file loaded successfully.")
            show_basic_kpis(uploaded_df)
            show_dataframe(uploaded_df)

        except Exception as e:
            st.error("Excel ファイルの読み込みに失敗しました。")
            st.exception(e)

    st.markdown("---")
    st.markdown("#### Current data file")
    st.code("service_report.xlsx")

    if DATA_FILE.exists():
        st.success("service_report.xlsx is available.")
    else:
        st.warning("service_report.xlsx is not found.")


# =========================================================
# Footer
# =========================================================
st.markdown("---")
st.caption("Horizon International Technical Support / Service Report Admin Console")
