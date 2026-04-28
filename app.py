import streamlit as st
from pathlib import Path
import pandas as pd
import re
import base64


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
                            A centralized dashboard for service report analysis, machine trends,
                            error review, and Carepack Bulletin management.
                        </div>
                        <div class="portal-mini-grid">
                            <div class="portal-mini-card">📊 Dealer analysis</div>
                            <div class="portal-mini-card">🌏 Country view</div>
                            <div class="portal-mini-card">🛠️ Machine trends</div>
                            <div class="portal-mini-card">📦 Carepack Bulletin</div>
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
                                📊 Dealer overview<br>
                                🌏 Country view<br>
                                🛠️ Machine view<br>
                                ⚠️ Error analysis<br>
                                📈 Summary charts<br>
                                📥 Import data<br>
                                📦 Carepack Bulletin
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


if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

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
            linear-gradient(180deg, #1f2a44 0%, #111827 100%);
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
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

    .metric-card {
        padding: 24px;
        border-radius: 24px;
        background: #ffffff;
        box-shadow: 0 12px 32px rgba(15,23,42,0.08);
        border: 1px solid #e5e7eb;
    }

    .metric-label {
        color: #667085;
        font-size: 14px;
        margin-bottom: 8px;
    }

    .metric-value {
        color: #1f2a44;
        font-size: 32px;
        font-weight: 900;
    }

    .carepack-hero {
        padding: 34px 42px;
        border-radius: 30px;
        background:
            radial-gradient(circle at right center, rgba(255,255,255,0.18), transparent 28%),
            linear-gradient(135deg, #1e3a8a 0%, #2563eb 58%, #0ea5e9 100%);
        color: white;
        box-shadow: 0 18px 45px rgba(37,99,235,0.24);
        margin-bottom: 24px;
        display: grid;
        grid-template-columns: minmax(0, 1fr) 390px;
        align-items: center;
        gap: 34px;
        min-height: 260px;
    }

    .carepack-hero-text {
        max-width: 1050px;
    }

    .carepack-hero-title {
        font-size: 40px;
        font-weight: 900;
        margin-bottom: 16px;
        letter-spacing: -0.03em;
    }

    .carepack-hero-subtitle {
        font-size: 16px;
        color: #e0f2fe;
        line-height: 1.8;
        max-width: 1050px;
    }

    .carepack-hero-image-wrap {
        width: 360px;
        height: 230px;
        border-radius: 30px;
        background: rgba(255,255,255,0.18);
        border: 1px solid rgba(255,255,255,0.28);
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        box-shadow:
            inset 0 1px 0 rgba(255,255,255,0.22),
            0 18px 35px rgba(0,0,0,0.18);
        padding: 16px;
    }

    .carepack-hero-image {
        width: 100%;
        height: 100%;
        object-fit: contain;
        border-radius: 20px;
        filter: drop-shadow(0 8px 14px rgba(0,0,0,0.18));
    }

    .carepack-hero-fallback {
        font-size: 82px;
        filter: drop-shadow(0 12px 20px rgba(0,0,0,0.22));
    }

    .small-note {
        color: #667085;
        font-size: 13px;
    }

    .carepack-pill {
        display: inline-block;
        padding: 7px 14px;
        border-radius: 999px;
        background: #e0f2fe;
        color: #0369a1;
        font-size: 13px;
        font-weight: 800;
        text-align: center;
        margin-top: 6px;
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
        font-size: 18px;
    }

    .progress-card {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 22px;
        padding: 22px 24px;
        margin-top: 18px;
        margin-bottom: 18px;
        box-shadow: 0 10px 28px rgba(15,23,42,0.06);
    }

    .progress-title {
        font-size: 20px;
        font-weight: 900;
        color: #1f2a44;
        margin-bottom: 10px;
    }

    .progress-text {
        font-size: 22px;
        font-weight: 900;
        color: #1f2a44;
        letter-spacing: 0.5px;
        margin-bottom: 8px;
        line-height: 1.5;
    }

    .progress-target {
        font-size: 14px;
        color: #667085;
        line-height: 1.6;
    }

    @media (max-width: 900px) {
        .carepack-hero {
            grid-template-columns: 1fr;
            padding: 28px 26px;
            min-height: auto;
        }

        .carepack-hero-image-wrap {
            width: 100%;
            height: 240px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# =========================
# Data Settings
# =========================
CAREPACK_DIR = Path("carepack_bulletins")
ASSET_DIR = Path("assets")
CAREPACK_IMAGE = ASSET_DIR / "carepack.png"
TARGET_MODELS = 60


def image_to_base64(image_path: Path):
    if not image_path.exists():
        return ""

    suffix = image_path.suffix.lower()

    if suffix in [".jpg", ".jpeg"]:
        mime = "image/jpeg"
    elif suffix == ".webp":
        mime = "image/webp"
    else:
        mime = "image/png"

    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode("utf-8")

    return f"data:{mime};base64,{encoded}"


def extract_pdf_info(pdf_path: Path):
    date_value = "-"
    bulletin_code = "-"

    try:
        import fitz

        doc = fitz.open(pdf_path)

        if len(doc) == 0:
            return date_value, bulletin_code

        text = doc.load_page(0).get_text()
        text_one_line = " ".join(text.split())

        date_match = re.search(
            r"Date:\s*(.*?)(?:\s+Title:|\s+Ref No\.:|\s+Model:|\n)",
            text_one_line,
            re.IGNORECASE,
        )

        if date_match:
            date_value = date_match.group(1).strip()

        bulletin_match = re.search(
            r"Title:\s*Carepack\s*Code:\s*([A-Z0-9-]+)",
            text_one_line,
            re.IGNORECASE,
        )

        if bulletin_match:
            bulletin_code = bulletin_match.group(1).strip()

        if bulletin_code == "-":
            fallback_match = re.search(
                r"Code:\s*([A-Z]{1,4}[0-9]{6,8}-[0-9]+)",
                text_one_line,
                re.IGNORECASE,
            )
            if fallback_match:
                bulletin_code = fallback_match.group(1).strip()

    except Exception:
        pass

    return date_value, bulletin_code


def build_carepack_data():
    data = []

    if not CAREPACK_DIR.exists():
        return data

    pdf_files = sorted(CAREPACK_DIR.glob("*.pdf"))

    for pdf_file in pdf_files:
        file_name = pdf_file.name

        model = pdf_file.stem
        if model.startswith("IB_"):
            model = model[3:]

        machine = model.replace("-CRP", "")

        date_value, bulletin_code = extract_pdf_info(pdf_file)

        data.append(
            {
                "model": model,
                "machine": machine,
                "bulletin_code": bulletin_code,
                "date": date_value,
                "file": file_name,
            }
        )

    return data


CAREPACK_DATA = build_carepack_data()


# =========================
# Helper Functions
# =========================
def render_carepack_hero():
    image_src = image_to_base64(CAREPACK_IMAGE)

    if image_src:
        image_html = f"""
        <div class="carepack-hero-image-wrap">
            <img class="carepack-hero-image" src="{image_src}" alt="Carepack image">
        </div>
        """
    else:
        image_html = """
        <div class="carepack-hero-image-wrap">
            <div class="carepack-hero-fallback">📦</div>
        </div>
        """

    st.markdown(
        f"""
        <div class="carepack-hero">
            <div class="carepack-hero-text">
                <div class="carepack-hero-title">📦 Carepack Bulletin</div>
                <div class="carepack-hero-subtitle">
                    Search, preview, and download Carepack Information Bulletins.
                    You can search by model name, file name, Bulletin Code, or Date.
                    New PDFs will be displayed automatically after being uploaded to the carepack_bulletins folder.
                </div>
            </div>
            {image_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_carepack_progress():
    current_count = len(CAREPACK_DATA)

    if TARGET_MODELS <= 0:
        percent = 0
        progress_ratio = 0
    else:
        percent = round((current_count / TARGET_MODELS) * 100)
        progress_ratio = min(current_count / TARGET_MODELS, 1.0)

    total_blocks = 20
    if TARGET_MODELS <= 0:
        filled_blocks = 0
    else:
        filled_blocks = round((current_count / TARGET_MODELS) * total_blocks)

    filled_blocks = max(0, min(filled_blocks, total_blocks))

    bar_text = "■" * filled_blocks + "□" * (total_blocks - filled_blocks)

    st.markdown(
        f"""
        <div class="progress-card">
            <div class="progress-title">Carepack Bulletin Progress</div>
            <div class="progress-text">
                {bar_text} {current_count}/{TARGET_MODELS} models ({percent}%)
            </div>
            <div class="progress-target">
                (Target: All {TARGET_MODELS} models to be ready by the end of this fiscal year)
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.progress(progress_ratio)


def show_pdf_preview(pdf_path: Path):
    try:
        import fitz

        doc = fitz.open(pdf_path)

        for page_number in range(len(doc)):
            page = doc.load_page(page_number)
            pix = page.get_pixmap(matrix=fitz.Matrix(1.6, 1.6))
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
                item["bulletin_code"],
                item["date"],
                item["file"],
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
st.sidebar.caption("Service Data Portal")
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
    render_carepack_hero()

    if not CAREPACK_DIR.exists():
        st.error(
            "The carepack_bulletins folder was not found. "
            "Please create the folder and upload PDF files."
        )
        st.stop()

    with st.container(border=True):
        col1, col2, col3 = st.columns([5, 1.25, 1.25])

        with col1:
            keyword = st.text_input(
                "Search Carepack Bulletin",
                placeholder="Example: BQ300, CF400, VAC1, AF406F, AS23122025-1, Dec. 23rd...",
            )

        with col2:
            st.write("")
            st.write("")
            show_all = st.button("Show All", use_container_width=True)

        with col3:
            st.write("")
            st.write("")
            clear_search = st.button("Clear", use_container_width=True)

    if clear_search:
        keyword = ""
        show_all = False

    results = search_carepack(keyword, show_all)

    if not keyword and not show_all:
        st.info("Enter a keyword or click **Show All** to display Carepack Bulletins.")

        overview_df = pd.DataFrame(
            [
                {
                    "Carepack Model": item["model"],
                    "Machine": item["machine"],
                    "Bulletin Code": item["bulletin_code"],
                    "Date": item["date"],
                    "File Name": item["file"],
                }
                for item in CAREPACK_DATA
            ]
        )

        st.dataframe(overview_df, use_container_width=True, hide_index=True)

        render_carepack_progress()

    else:
        st.markdown(f"### Search results: {len(results)}")

        if not results:
            st.warning("No Carepack Bulletin found.")

        for item in results:
            pdf_path = CAREPACK_DIR / item["file"]

            with st.container(border=True):
                top_col1, top_col2 = st.columns([5, 1])

                with top_col1:
                    st.markdown(f"### {item['model']}")
                    st.caption(f"File: {item['file']}")

                with top_col2:
                    st.markdown(
                        """
                        <div class="carepack-pill">
                            Carepack
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                st.write("")

                info_col1, info_col2, info_col3 = st.columns(3)

                with info_col1:
                    st.metric("Machine", item["machine"])

                with info_col2:
                    st.metric("Bulletin Code", item["bulletin_code"])

                with info_col3:
                    st.metric("Date", item["date"])

                st.write("")

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
                        st.caption("PDF is available.")

                    with st.expander("📄 Preview PDF", expanded=False):
                        show_pdf_preview(pdf_path)

                else:
                    st.error(
                        f"PDF file not found: {pdf_path}. "
                        "Please check whether the PDF is saved in the carepack_bulletins folder."
                    )

            st.write("")

        render_carepack_progress()
