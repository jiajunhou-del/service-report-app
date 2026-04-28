import streamlit as st
from pathlib import Path
import pandas as pd


# =========================
# Basic Page Settings
# =========================
st.set_page_config(
    page_title="Service Report Portal",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================
# Login Settings
# =========================
APP_PASSWORD = "ts123"


def login_page():
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(135deg, #eef2f7 0%, #f8fafc 100%);
        }

        .login-wrapper {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 35px;
            margin-bottom: 15px;
        }

        .login-card {
            width: 100%;
            max-width: 760px;
            border-radius: 28px;
            padding: 38px 42px;
            background: linear-gradient(135deg, #ffffff 0%, #f8fbff 100%);
            box-shadow: 0 18px 45px rgba(31, 42, 68, 0.12);
            border: 1px solid #e7edf5;
        }

        .login-badge {
            display: inline-block;
            padding: 6px 14px;
            border-radius: 999px;
            background: #e9f2ff;
            color: #2457a7;
            font-size: 13px;
            font-weight: 700;
            margin-bottom: 16px;
        }

        .login-title {
            font-size: 42px;
            font-weight: 800;
            color: #1f2a44;
            margin-bottom: 10px;
            line-height: 1.15;
        }

        .login-subtitle {
            font-size: 16px;
            color: #667085;
            margin-bottom: 22px;
        }

        .login-feature-box {
            margin-top: 20px;
            padding: 18px 20px;
            border-radius: 18px;
            background: #f7faff;
            border: 1px solid #e6eef8;
        }

        .login-feature-title {
            font-size: 15px;
            font-weight: 700;
            color: #1f2a44;
            margin-bottom: 10px;
        }

        .login-feature-list {
            color: #475467;
            font-size: 14px;
            line-height: 1.9;
        }

        .login-note {
            margin-top: 14px;
            color: #98a2b3;
            font-size: 13px;
        }

        div[data-testid="stTextInput"] input {
            border-radius: 12px !important;
            border: 1px solid #d0d5dd !important;
            min-height: 48px !important;
            background-color: #ffffff !important;
        }

        div[data-testid="stButton"] button {
            border-radius: 12px !important;
            min-height: 46px !important;
            font-weight: 700 !important;
            background: linear-gradient(135deg, #2457a7 0%, #1f6feb 100%) !important;
            color: white !important;
            border: none !important;
        }

        div[data-testid="stButton"] button:hover {
            filter: brightness(1.03);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    left, center, right = st.columns([1, 1.9, 1])

    with center:
        st.markdown(
            """
            <div class="login-wrapper">
                <div class="login-card">
                    <div class="login-badge">Horizon International</div>
                    <div class="login-title">Service Report Portal</div>
                    <div class="login-subtitle">
                        Centralized access for service analysis, report management, and Carepack bulletin search.
                    </div>

                    <div class="login-feature-box">
                        <div class="login-feature-title">Available features</div>
                        <div class="login-feature-list">
                            📊 Dealer overview<br>
                            🌏 Country view<br>
                            🛠️ Machine view<br>
                            ⚠️ Error analysis<br>
                            📈 Summary charts<br>
                            📥 Import data<br>
                            📦 Carepack Bulletin
                        </div>
                    </div>

                    <div class="login-note">
                        Please enter your access password to continue.
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.write("")
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


if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    login_page()
    st.stop()


# =========================
# Custom CSS
# =========================
st.markdown(
    """
    <style>
    section[data-testid="stSidebar"] {
        background-color: #1f2a44;
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    .main-title {
        font-size: 36px;
        font-weight: 800;
        color: #1f2a44;
        margin-bottom: 5px;
    }

    .sub-title {
        font-size: 16px;
        color: #667085;
        margin-bottom: 25px;
    }

    .metric-card {
        padding: 22px;
        border-radius: 20px;
        background: #ffffff;
        box-shadow: 0 10px 28px rgba(0,0,0,0.08);
        border: 1px solid #eef2f7;
    }

    .metric-label {
        color: #667085;
        font-size: 14px;
    }

    .metric-value {
        color: #1f2a44;
        font-size: 30px;
        font-weight: 800;
    }

    .carepack-card {
        padding: 22px;
        border-radius: 18px;
        background: #ffffff;
        border: 1px solid #e5e7eb;
        box-shadow: 0 8px 24px rgba(0,0,0,0.06);
        margin-bottom: 18px;
    }

    .carepack-title {
        font-size: 22px;
        font-weight: 800;
        color: #1f2a44;
        margin-bottom: 8px;
    }

    .carepack-info {
        font-size: 14px;
        color: #475467;
        line-height: 1.8;
    }

    .small-note {
        color: #667085;
        font-size: 13px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# =========================
# Data Settings
# =========================
CAREPACK_DIR = Path("carepack_bulletins")

CAREPACK_DATA = [
    {
        "model": "SLMK5-CRP",
        "machine": "iCE Stitch Liner MarkV",
        "code": "AP00010-00",
        "bulletin_code": "AS23122025-1",
        "file": "IB_SLMK5-CRP.pdf",
        "order_start_date": "Dec. 23rd, 2025",
        "release_date": "Dec. 23rd, 2025",
    },
    {
        "model": "BQ300-CRP",
        "machine": "BQ-300",
        "code": "AP00031-00",
        "bulletin_code": "AS16042025-1",
        "file": "IB_BQ300-CRP.pdf",
        "order_start_date": "Apr. 16th, 2025",
        "release_date": "Apr. 16th, 2025",
    },
    {
        "model": "VAC1-CRP",
        "machine": "VAC-1000",
        "code": "AP00025-00",
        "bulletin_code": "TH26112024-1",
        "file": "IB_VAC1-CRP.pdf",
        "order_start_date": "Nov. 26th, 2024",
        "release_date": "Nov. 26th, 2024",
    },
    {
        "model": "CF400-CRP",
        "machine": "CF-400",
        "code": "AP00019-00",
        "bulletin_code": "AS23122025-5",
        "file": "IB_CF400-CRP.pdf",
        "order_start_date": "Dec. 23rd, 2025",
        "release_date": "Dec. 23rd, 2025",
    },
]


# =========================
# Helper Functions
# =========================
def show_pdf_preview(pdf_path: Path):
    try:
        import fitz  # PyMuPDF

        doc = fitz.open(pdf_path)

        for page_number in range(len(doc)):
            page = doc.load_page(page_number)
            pix = page.get_pixmap(matrix=fitz.Matrix(1.5, 1.5))
            image_bytes = pix.tobytes("png")

            st.image(
                image_bytes,
                caption=f"Page {page_number + 1}",
                use_container_width=True,
            )

    except Exception as e:
        st.error(f"PDF preview failed: {e}")


def search_carepack(keyword: str, show_all: bool):
    if show_all:
        return CAREPACK_DATA

    keyword = keyword.lower().strip()

    if not keyword:
        return []

    results = []

    for item in CAREPACK_DATA:
        search_target = " ".join(
            [
                item["model"],
                item["machine"],
                item["code"],
                item["bulletin_code"],
                item["file"],
                item["release_date"],
            ]
        ).lower()

        if keyword in search_target:
            results.append(item)

    return results


def page_header(title, subtitle):
    st.markdown(f"<div class='main-title'>{title}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='sub-title'>{subtitle}</div>", unsafe_allow_html=True)


# =========================
# Sidebar
# =========================
st.sidebar.markdown("## VIEWS")

view = st.sidebar.radio(
    "",
    [
        "📊 Dealer overview",
        "🌏 Country view",
        "🛠️ Machine view",
        "⚠️ Error analysis",
        "📈 Summary charts",
        "📥 Import data",
        "📦 Carepack Bulletin",
    ],
)

st.sidebar.markdown("---")
st.sidebar.caption("Service Report Portal")
st.sidebar.caption("Horizon International")

if st.sidebar.button("Logout", use_container_width=True):
    st.session_state["logged_in"] = False
    st.rerun()


# =========================
# Page: Dealer Overview
# =========================
if view == "📊 Dealer overview":
    page_header(
        "📊 Dealer overview",
        "Overview of dealer service activity and key performance indicators.",
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            """
            <div class="metric-card">
                <div class="metric-label">Total Dealers</div>
                <div class="metric-value">--</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="metric-card">
                <div class="metric-label">Total Reports</div>
                <div class="metric-value">--</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
            <div class="metric-card">
                <div class="metric-label">Active Countries</div>
                <div class="metric-value">--</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col4:
        st.markdown(
            """
            <div class="metric-card">
                <div class="metric-label">Open Issues</div>
                <div class="metric-value">--</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.info("ここに Dealer overview のグラフや集計を追加できます。")


# =========================
# Page: Country View
# =========================
elif view == "🌏 Country view":
    page_header(
        "🌏 Country view",
        "Analyze service report status by country or region.",
    )

    st.info("ここに国別の集計、ランキング、比較グラフを追加できます。")


# =========================
# Page: Machine View
# =========================
elif view == "🛠️ Machine view":
    page_header(
        "🛠️ Machine view",
        "Analyze service report trends by machine model.",
    )

    st.info("ここに機種別の件数、エラー傾向、稼働状況などを追加できます。")


# =========================
# Page: Error Analysis
# =========================
elif view == "⚠️ Error analysis":
    page_header(
        "⚠️ Error analysis",
        "Analyze frequent errors and machine trouble trends.",
    )

    st.info("ここにエラーコード別の分析、Top 10 エラー、発生推移などを追加できます。")


# =========================
# Page: Summary Charts
# =========================
elif view == "📈 Summary charts":
    page_header(
        "📈 Summary charts",
        "Summary charts for service reports and machine activity.",
    )

    sample_df = pd.DataFrame(
        {
            "Month": ["Jan", "Feb", "Mar", "Apr"],
            "Reports": [12, 18, 15, 22],
        }
    )

    st.bar_chart(sample_df.set_index("Month"))


# =========================
# Page: Import Data
# =========================
elif view == "📥 Import data":
    page_header(
        "📥 Import data",
        "Upload CSV or Excel files for service report analysis.",
    )

    uploaded_file = st.file_uploader(
        "Upload CSV or Excel file",
        type=["csv", "xlsx"],
    )

    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith(".csv"):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)

            st.success("File uploaded successfully.")
            st.dataframe(df, use_container_width=True)

        except Exception as e:
            st.error(f"Failed to read file: {e}")
    else:
        st.info("Please upload a CSV or Excel file.")


# =========================
# Page: Carepack Bulletin
# =========================
elif view == "📦 Carepack Bulletin":
    page_header(
        "📦 Carepack Bulletin",
        "Search, preview, and download Carepack Information Bulletins.",
    )

    st.markdown(
        """
        <div class="small-note">
        You can search by Carepack model, machine name, code, bulletin code, file name, or release date.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    col1, col2 = st.columns([5, 1.2])

    with col1:
        keyword = st.text_input(
            "Search Carepack Bulletin",
            placeholder="Example: BQ300, CF-400, AP00019-00, VAC1, SLMK5...",
        )

    with col2:
        st.write("")
        st.write("")
        show_all = st.button("Show All", use_container_width=True)

    results = search_carepack(keyword, show_all)

    if not keyword and not show_all:
        st.info("Enter a keyword or click **Show All** to display Carepack Bulletins.")

        st.markdown("### Available Carepack Bulletins")

        overview_df = pd.DataFrame(
            [
                {
                    "Carepack Model": item["model"],
                    "Machine": item["machine"],
                    "Code": item["code"],
                    "Release Date": item["release_date"],
                }
                for item in CAREPACK_DATA
            ]
        )

        st.dataframe(overview_df, use_container_width=True, hide_index=True)

    else:
        st.markdown(f"### Search results: {len(results)}")

        if not results:
            st.warning("No Carepack Bulletin found.")

        for item in results:
            pdf_path = CAREPACK_DIR / item["file"]

            st.markdown(
                f"""
                <div class="carepack-card">
                    <div class="carepack-title">{item["model"]} / {item["machine"]}</div>
                    <div class="carepack-info">
                        <b>Carepack Code:</b> {item["code"]}<br>
                        <b>Bulletin Code:</b> {item["bulletin_code"]}<br>
                        <b>Order Start Date:</b> {item["order_start_date"]}<br>
                        <b>Release Date:</b> {item["release_date"]}<br>
                        <b>File:</b> {item["file"]}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            if pdf_path.exists():
                col_a, col_b = st.columns([1.2, 5])

                with col_a:
                    with open(pdf_path, "rb") as f:
                        st.download_button(
                            label="📥 Download PDF",
                            data=f,
                            file_name=item["file"],
                            mime="application/pdf",
                            use_container_width=True,
                        )

                with col_b:
                    st.caption(f"PDF file found: {pdf_path}")

                with st.expander("📄 Preview PDF", expanded=False):
                    show_pdf_preview(pdf_path)

            else:
                st.error(
                    f"PDF file not found: {pdf_path}. "
                    "Please check whether the PDF is saved in the carepack_bulletins folder."
                )

            st.divider()
