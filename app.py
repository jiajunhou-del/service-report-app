import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path


# =========================
# Page settings
# =========================
st.set_page_config(
    page_title="Service Report Portal",
    page_icon="🛠️",
    layout="wide"
)


# =========================
# Login users
# ここでパスワードを変更できます
# =========================
USERS = {
    "TS Admin": "admin123",
    "Service Viewer": "viewer123"
}


# =========================
# Login page design
# =========================
def login_page():
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(135deg, #eef3f8 0%, #f8fafc 45%, #e7eff7 100%);
        }

        .login-wrapper {
            max-width: 980px;
            margin: 80px auto 0 auto;
            display: grid;
            grid-template-columns: 1.1fr 0.9fr;
            gap: 0;
            border-radius: 28px;
            overflow: hidden;
            box-shadow: 0 24px 70px rgba(15, 40, 70, 0.16);
            background: white;
        }

        .login-left {
            background: linear-gradient(145deg, #0f2742 0%, #153c63 55%, #0e5f75 100%);
            color: white;
            padding: 48px;
            position: relative;
        }

        .login-left::after {
            content: "";
            position: absolute;
            right: -80px;
            bottom: -80px;
            width: 220px;
            height: 220px;
            border-radius: 50%;
            background: rgba(255,255,255,0.08);
        }

        .portal-badge {
            display: inline-block;
            padding: 8px 14px;
            border-radius: 999px;
            background: rgba(255,255,255,0.14);
            font-size: 13px;
            letter-spacing: 0.08em;
            margin-bottom: 28px;
        }

        .portal-title {
            font-size: 38px;
            font-weight: 800;
            line-height: 1.15;
            margin-bottom: 18px;
        }

        .portal-subtitle {
            font-size: 15px;
            line-height: 1.8;
            color: rgba(255,255,255,0.78);
            margin-bottom: 34px;
        }

        .data-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }

        .data-tag {
            padding: 9px 12px;
            border: 1px solid rgba(255,255,255,0.22);
            border-radius: 12px;
            color: rgba(255,255,255,0.86);
            font-size: 13px;
            background: rgba(255,255,255,0.08);
        }

        .login-right {
            padding: 48px 44px;
            background: rgba(255,255,255,0.96);
        }

        .login-heading {
            font-size: 26px;
            font-weight: 800;
            color: #142033;
            margin-bottom: 8px;
        }

        .login-caption {
            font-size: 14px;
            color: #718096;
            margin-bottom: 28px;
        }

        .footer-note {
            text-align: center;
            margin-top: 22px;
            color: #9aa7b5;
            font-size: 12px;
        }

        div.stButton > button {
            width: 100%;
            height: 48px;
            border-radius: 14px;
            background: linear-gradient(90deg, #153c63 0%, #0e7490 100%);
            color: white;
            border: none;
            font-weight: 700;
        }

        div.stButton > button:hover {
            background: linear-gradient(90deg, #0f2742 0%, #155e75 100%);
            color: white;
            border: none;
        }
        </style>

        <div class="login-wrapper">
            <div class="login-left">
                <div class="portal-badge">SERVICE INTELLIGENCE</div>
                <div class="portal-title">
                    Service Report<br>
                    Portal
                </div>
                <div class="portal-subtitle">
                    A technical support dashboard for reviewing service reports,
                    machine status, field issues, and operation insights.
                </div>
                <div class="data-tags">
                    <div class="data-tag">Machine Data</div>
                    <div class="data-tag">Service Reports</div>
                    <div class="data-tag">Error Trends</div>
                    <div class="data-tag">Support Activity</div>
                </div>
            </div>

            <div class="login-right">
                <div class="login-heading">Welcome back</div>
                <div class="login-caption">
                    Please sign in to access the Service Report Dashboard.
                </div>
        """,
        unsafe_allow_html=True
    )

    role = st.selectbox("Access Role", list(USERS.keys()))
    password = st.text_input("Password", type="password", placeholder="Enter your password")

    login_button = st.button("Enter Dashboard →")

    st.markdown(
        """
            </div>
        </div>
        <div class="footer-note">
            Horizon International Technical Support / Service Report System
        </div>
        """,
        unsafe_allow_html=True
    )

    if login_button:
        if password == USERS[role]:
            st.session_state["logged_in"] = True
            st.session_state["role"] = role
            st.rerun()
        else:
            st.error("Password is incorrect. Please try again.")


# =========================
# Login check
# =========================
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if "role" not in st.session_state:
    st.session_state["role"] = None

if not st.session_state["logged_in"]:
    login_page()
    st.stop()


# =========================
# Dashboard style
# =========================
st.markdown(
    """
    <style>
    .main-header {
        padding: 18px 0 8px 0;
    }

    .main-title {
        font-size: 34px;
        font-weight: 800;
        color: #142033;
        margin-bottom: 4px;
    }

    .main-subtitle {
        font-size: 15px;
        color: #718096;
        margin-bottom: 24px;
    }

    .role-badge {
        display: inline-block;
        padding: 7px 12px;
        border-radius: 999px;
        background: #e6f3f7;
        color: #0e7490;
        font-weight: 700;
        font-size: 13px;
    }

    div[data-testid="metric-container"] {
        background: #ffffff;
        border: 1px solid #e5eaf0;
        padding: 18px;
        border-radius: 18px;
        box-shadow: 0 8px 22px rgba(15, 40, 70, 0.06);
    }
    </style>
    """,
    unsafe_allow_html=True
)


# =========================
# Sidebar
# =========================
with st.sidebar:
    st.title("🛠️ Service Portal")
    st.caption("Technical Support Dashboard")
    st.markdown("---")

    st.write("Login role:")
    st.success(st.session_state["role"])

    if st.button("Logout"):
        st.session_state["logged_in"] = False
        st.session_state["role"] = None
        st.rerun()

    st.markdown("---")
    st.caption("Data source")
    st.code("service_report.xlsx")


# =========================
# Main header
# =========================
st.markdown(
    f"""
    <div class="main-header">
        <div class="main-title">Service Report Dashboard</div>
        <div class="main-subtitle">
            Review service report data, machine trends, and support activity.
        </div>
        <div class="role-badge">Access Role: {st.session_state["role"]}</div>
    </div>
    """,
    unsafe_allow_html=True
)


# =========================
# Load Excel data
# =========================
excel_path = Path("service_report.xlsx")

if not excel_path.exists():
    st.error("service_report.xlsx が見つかりません。GitHub に service_report.xlsx がアップロードされているか確認してください。")
    st.stop()

try:
    df = pd.read_excel(excel_path)
except Exception as e:
    st.error("Excel ファイルの読み込みに失敗しました。")
    st.exception(e)
    st.stop()


# =========================
# Basic data cleaning
# =========================
df.columns = [str(col).strip() for col in df.columns]


# =========================
# Data Overview
# =========================
st.markdown("### Data Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Records", len(df))

with col2:
    st.metric("Columns", len(df.columns))

with col3:
    st.metric("Login Role", st.session_state["role"])

with col4:
    st.metric("Data File", "Loaded")


# =========================
# Filters
# =========================
st.markdown("### Filters")

filtered_df = df.copy()

categorical_columns = []
for col in df.columns:
    if df[col].nunique() <= 30 and df[col].dtype == "object":
        categorical_columns.append(col)

if len(categorical_columns) > 0:
    filter_cols = st.columns(min(3, len(categorical_columns)))

    for i, col in enumerate(categorical_columns[:3]):
        with filter_cols[i]:
            options = ["All"] + sorted(df[col].dropna().astype(str).unique().tolist())
            selected = st.selectbox(f"Filter by {col}", options)

            if selected != "All":
                filtered_df = filtered_df[filtered_df[col].astype(str) == selected]
else:
    st.info("フィルターに使用できるカテゴリ列が見つかりませんでした。")


# =========================
# Charts
# =========================
st.markdown("### Visual Analysis")

numeric_columns = filtered_df.select_dtypes(include=["number"]).columns.tolist()
text_columns = filtered_df.select_dtypes(include=["object"]).columns.tolist()

chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    if text_columns:
        x_col = st.selectbox("Category column", text_columns, key="category_chart")
        count_df = filtered_df[x_col].astype(str).value_counts().reset_index()
        count_df.columns = [x_col, "Count"]

        fig = px.bar(
            count_df.head(15),
            x=x_col,
            y="Count",
            title=f"Top categories by {x_col}"
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("カテゴリ列が見つかりませんでした。")

with chart_col2:
    if numeric_columns:
        y_col = st.selectbox("Numeric column", numeric_columns, key="numeric_chart")
        fig = px.histogram(
            filtered_df,
            x=y_col,
            title=f"Distribution of {y_col}"
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("数値列が見つかりませんでした。")


# =========================
# Role based display
# =========================
st.markdown("### Report Data")

if st.session_state["role"] == "Service Viewer":
    st.info("Service Viewer mode: 通常閲覧モードです。")
    st.dataframe(filtered_df, use_container_width=True)

elif st.session_state["role"] == "TS Admin":
    st.info("TS Admin mode: 管理者向けに全データを表示しています。")
    st.dataframe(filtered_df, use_container_width=True)

    csv = filtered_df.to_csv(index=False).encode("utf-8-sig")

    st.download_button(
        label="Download filtered data as CSV",
        data=csv,
        file_name="filtered_service_report.csv",
        mime="text/csv"
    )


# =========================
# Footer
# =========================
st.markdown("---")
st.caption("Horizon International Technical Support / Service Report Portal")
