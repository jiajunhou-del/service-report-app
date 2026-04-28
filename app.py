import os
from io import BytesIO

import pandas as pd
import plotly.express as px
import streamlit as st


# =========================
# Basic settings
# =========================
st.set_page_config(
    page_title="Service Report Dashboard",
    page_icon="🛠",
    layout="wide"
)

DATA_DIR = r"C:\service_report_streamlit\data"
EXCEL_PATH = os.path.join(DATA_DIR, "service_report.xlsx")

REQUIRED_COLUMNS = [
    "Month",
    "Dealer",
    "Country",
    "Machine",
    "Error Code",
    "Problem",
    "Cause",
    "Action",
    "Downtime",
    "Status"
]


# =========================
# CSS
# =========================
st.markdown(
    """
    <style>
    .main {
        background-color: #f5f7fb;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    section[data-testid="stSidebar"] {
        background-color: #1f2740;
    }

    section[data-testid="stSidebar"] * {
        color: white;
    }

    .small-label {
        font-size: 13px;
        color: #6b7280;
        margin-bottom: 4px;
    }

    .big-number {
        font-size: 34px;
        font-weight: 700;
        color: #111827;
    }

    .metric-card {
        background: white;
        padding: 20px 22px;
        border-radius: 14px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 1px 4px rgba(0,0,0,0.04);
        min-height: 105px;
    }

    .dealer-card {
        background: white;
        padding: 18px;
        border-radius: 14px;
        border: 1px solid #d9dee8;
        box-shadow: 0 1px 4px rgba(0,0,0,0.04);
        margin-bottom: 18px;
    }

    .dealer-title {
        font-weight: 700;
        font-size: 16px;
        color: #111827;
    }

    .badge-complete {
        background: #dcfce7;
        color: #166534;
        padding: 5px 12px;
        border-radius: 999px;
        font-size: 12px;
        font-weight: 700;
        display: inline-block;
    }

    .badge-pending {
        background: #eef2f7;
        color: #64748b;
        padding: 5px 12px;
        border-radius: 999px;
        font-size: 12px;
        font-weight: 700;
        display: inline-block;
    }

    .card-label {
        color: #94a3b8;
        font-size: 11px;
        font-weight: 700;
        margin-top: 12px;
    }

    .card-value {
        color: #111827;
        font-size: 22px;
        font-weight: 700;
    }

    .progress-bg {
        width: 100%;
        height: 7px;
        background: #e5e7eb;
        border-radius: 999px;
        margin-top: 14px;
        overflow: hidden;
    }

    .progress-green {
        height: 7px;
        background: #22c55e;
        border-radius: 999px;
    }

    .progress-gray {
        height: 7px;
        background: #cbd5e1;
        border-radius: 999px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# =========================
# Helper functions
# =========================
def ensure_data_dir():
    os.makedirs(DATA_DIR, exist_ok=True)


def create_sample_excel():
    ensure_data_dir()

    sample_data = [
        {
            "Month": "2026-04",
            "Dealer": "Advanced Finishing Systems (HK) Ltd",
            "Country": "Hong Kong",
            "Machine": "BQ-500",
            "Error Code": "802",
            "Problem": "Jam occurred during production",
            "Cause": "Sensor dirty",
            "Action": "Cleaned sensor and checked timing",
            "Downtime": 2.5,
            "Status": "Complete"
        },
        {
            "Month": "2026-04",
            "Dealer": "Advanced Printing Technology",
            "Country": "Thailand",
            "Machine": "SPF-200A",
            "Error Code": "1007",
            "Problem": "Start mark was not detected",
            "Cause": "Sensor position shifted",
            "Action": "Adjusted sensor position",
            "Downtime": 1.0,
            "Status": "Complete"
        },
        {
            "Month": "2026-04",
            "Dealer": "Copylandia",
            "Country": "Philippines",
            "Machine": "HT-300",
            "Error Code": "137",
            "Problem": "Start mark not detected",
            "Cause": "Unknown",
            "Action": "Under checking",
            "Downtime": 0,
            "Status": "Pending"
        },
        {
            "Month": "2026-04",
            "Dealer": "Currie Group",
            "Country": "Australia",
            "Machine": "BQ-500",
            "Error Code": "802",
            "Problem": "Repeated jam",
            "Cause": "Paper dust",
            "Action": "Recommended cleaning procedure",
            "Downtime": 3.0,
            "Status": "Pending"
        },
        {
            "Month": "2026-05",
            "Dealer": "Dainippon Screen Korea",
            "Country": "Korea",
            "Machine": "VAC-1000",
            "Error Code": "E-12",
            "Problem": "Feeder stop",
            "Cause": "Air pressure unstable",
            "Action": "Checked air supply",
            "Downtime": 4.0,
            "Status": "Complete"
        }
    ]

    df = pd.DataFrame(sample_data)
    df.to_excel(EXCEL_PATH, index=False)


def load_excel_data():
    if not os.path.exists(EXCEL_PATH):
        create_sample_excel()

    df = pd.read_excel(EXCEL_PATH)

    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        st.error("Missing columns in Excel: " + ", ".join(missing))
        st.stop()

    df = df.fillna("")
    df["Month"] = df["Month"].astype(str)
    df["Dealer"] = df["Dealer"].astype(str)
    df["Country"] = df["Country"].astype(str)
    df["Machine"] = df["Machine"].astype(str)
    df["Error Code"] = df["Error Code"].astype(str)
    df["Problem"] = df["Problem"].astype(str)
    df["Cause"] = df["Cause"].astype(str)
    df["Action"] = df["Action"].astype(str)
    df["Status"] = df["Status"].astype(str)

    df["Downtime"] = pd.to_numeric(df["Downtime"], errors="coerce").fillna(0)

    return df


def save_uploaded_file(uploaded_file):
    ensure_data_dir()

    with open(EXCEL_PATH, "wb") as f:
        f.write(uploaded_file.getbuffer())


def top_value(series):
    cleaned = series.replace("", pd.NA).dropna()
    if cleaned.empty:
        return "-"
    return str(cleaned.value_counts().idxmax())


def to_excel_bytes(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Service Report")
    return output.getvalue()


def render_metric_card(label, value):
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="small-label">{label}</div>
            <div class="big-number">{value}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_dealer_card(dealer_name, group):
    total_cases = len(group)
    top_machine = top_value(group["Machine"])
    top_error = top_value(group["Error Code"])

    complete_count = (group["Status"].str.lower() == "complete").sum()
    progress = int((complete_count / total_cases) * 100) if total_cases > 0 else 0

    status = "Complete" if progress == 100 else "Pending"
    badge_class = "badge-complete" if status == "Complete" else "badge-pending"
    progress_class = "progress-green" if status == "Complete" else "progress-gray"

    st.markdown(
        f"""
        <div class="dealer-card">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <div class="dealer-title">{dealer_name}</div>
                <div class="{badge_class}">{status}</div>
            </div>

            <div style="display:grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin-top: 18px;">
                <div>
                    <div class="card-label">TOTAL CASES</div>
                    <div class="card-value">{total_cases}</div>
                </div>
                <div>
                    <div class="card-label">TOP MACHINE</div>
                    <div class="card-value">{top_machine}</div>
                </div>
                <div>
                    <div class="card-label">TOP ERROR</div>
                    <div class="card-value">{top_error}</div>
                </div>
            </div>

            <div class="progress-bg">
                <div class="{progress_class}" style="width:{progress}%;"></div>
            </div>
            <div style="text-align:right; color:#64748b; font-size:12px; margin-top:4px;">{progress}%</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    with st.expander("▼ View details"):
        st.dataframe(
            group[["Month", "Country", "Machine", "Error Code", "Problem", "Cause", "Action", "Downtime", "Status"]],
            use_container_width=True,
            hide_index=True
        )


# =========================
# Sidebar
# =========================
st.sidebar.markdown("## 🛠 Service Report")
st.sidebar.markdown("Admin Console")

view = st.sidebar.radio(
    "VIEWS",
    [
        "📊 Dealer overview",
        "🌏 Country view",
        "🛠 Machine view",
        "⚠ Error analysis",
        "📈 Summary charts",
        "📥 Import data"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### TOOLS")
generate_master = st.sidebar.button("↓ Generate Master Excel")
st.sidebar.markdown("---")
st.sidebar.caption("Prototype version")


# =========================
# Load data
# =========================
df = load_excel_data()


# =========================
# Header filters
# =========================
st.title("Service Report Dashboard")

months = ["All"] + sorted(df["Month"].unique().tolist())
countries = ["All"] + sorted(df["Country"].unique().tolist())
dealers = ["All"] + sorted(df["Dealer"].unique().tolist())
statuses = ["All", "Complete", "Pending"]

col_f1, col_f2, col_f3, col_f4 = st.columns(4)

with col_f1:
    selected_month = st.selectbox("Month", months)

with col_f2:
    selected_country = st.selectbox("Country", countries)

with col_f3:
    selected_dealer = st.selectbox("Dealer", dealers)

with col_f4:
    selected_status = st.selectbox("Status", statuses)


filtered = df.copy()

if selected_month != "All":
    filtered = filtered[filtered["Month"] == selected_month]

if selected_country != "All":
    filtered = filtered[filtered["Country"] == selected_country]

if selected_dealer != "All":
    filtered = filtered[filtered["Dealer"] == selected_dealer]

if selected_status != "All":
    filtered = filtered[filtered["Status"] == selected_status]


# =========================
# Summary metrics
# =========================
total_cases = len(filtered)
total_dealers = df["Dealer"].nunique()
dealers_submitted = filtered[filtered["Status"].str.lower() == "complete"]["Dealer"].nunique()
total_countries = filtered["Country"].nunique() if len(filtered) > 0 else 0
top_machine = top_value(filtered["Machine"]) if len(filtered) > 0 else "-"
top_error = top_value(filtered["Error Code"]) if len(filtered) > 0 else "-"

m1, m2, m3, m4, m5 = st.columns(5)

with m1:
    render_metric_card("Total service cases", total_cases)

with m2:
    render_metric_card("Dealers submitted", f"{dealers_submitted}/{total_dealers}")

with m3:
    render_metric_card("Countries submitted", total_countries)

with m4:
    render_metric_card("Top machine", top_machine)

with m5:
    render_metric_card("Top error", top_error)

st.divider()


# =========================
# Master Excel download
# =========================
if generate_master:
    st.download_button(
        label="Download Master Excel",
        data=to_excel_bytes(filtered),
        file_name="service_report_master.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )


# =========================
# Views
# =========================
if view == "📊 Dealer overview":
    st.subheader("Dealer overview")

    if filtered.empty:
        st.info("No data found.")
    else:
        dealer_groups = list(filtered.groupby("Dealer"))

        for i in range(0, len(dealer_groups), 2):
            cols = st.columns(2)

            for j, col in enumerate(cols):
                if i + j < len(dealer_groups):
                    dealer_name, group = dealer_groups[i + j]
                    with col:
                        render_dealer_card(dealer_name, group)


elif view == "🌏 Country view":
    st.subheader("Country view")

    if filtered.empty:
        st.info("No data found.")
    else:
        country_summary = (
            filtered.groupby("Country")
            .agg(
                Total_Cases=("Country", "count"),
                Dealers=("Dealer", "nunique"),
                Top_Machine=("Machine", lambda x: top_value(x)),
                Top_Error=("Error Code", lambda x: top_value(x)),
                Total_Downtime=("Downtime", "sum")
            )
            .reset_index()
        )

        st.dataframe(country_summary, use_container_width=True, hide_index=True)

        fig = px.bar(
            country_summary,
            x="Country",
            y="Total_Cases",
            title="Service cases by country"
        )
        st.plotly_chart(fig, use_container_width=True)


elif view == "🛠 Machine view":
    st.subheader("Machine view")

    if filtered.empty:
        st.info("No data found.")
    else:
        machine_summary = (
            filtered.groupby("Machine")
            .agg(
                Total_Cases=("Machine", "count"),
                Top_Error=("Error Code", lambda x: top_value(x)),
                Total_Downtime=("Downtime", "sum")
            )
            .reset_index()
            .sort_values("Total_Cases", ascending=False)
        )

        st.dataframe(machine_summary, use_container_width=True, hide_index=True)

        fig = px.bar(
            machine_summary,
            x="Machine",
            y="Total_Cases",
            title="Service cases by machine"
        )
        st.plotly_chart(fig, use_container_width=True)


elif view == "⚠ Error analysis":
    st.subheader("Error analysis")

    if filtered.empty:
        st.info("No data found.")
    else:
        error_summary = (
            filtered.groupby("Error Code")
            .agg(
                Total_Cases=("Error Code", "count"),
                Top_Machine=("Machine", lambda x: top_value(x)),
                Total_Downtime=("Downtime", "sum")
            )
            .reset_index()
            .sort_values("Total_Cases", ascending=False)
        )

        st.dataframe(error_summary, use_container_width=True, hide_index=True)

        fig = px.bar(
            error_summary.head(10),
            x="Error Code",
            y="Total_Cases",
            title="Top 10 error codes"
        )
        st.plotly_chart(fig, use_container_width=True)


elif view == "📈 Summary charts":
    st.subheader("Summary charts")

    if filtered.empty:
        st.info("No data found.")
    else:
        monthly = (
            filtered.groupby("Month")
            .size()
            .reset_index(name="Total_Cases")
            .sort_values("Month")
        )

        fig_month = px.line(
            monthly,
            x="Month",
            y="Total_Cases",
            markers=True,
            title="Monthly service cases trend"
        )
        st.plotly_chart(fig_month, use_container_width=True)

        col1, col2 = st.columns(2)

        with col1:
            machine_count = filtered["Machine"].value_counts().reset_index()
            machine_count.columns = ["Machine", "Total_Cases"]
            fig_machine = px.bar(
                machine_count.head(10),
                x="Machine",
                y="Total_Cases",
                title="Top machines"
            )
            st.plotly_chart(fig_machine, use_container_width=True)

        with col2:
            status_count = filtered["Status"].value_counts().reset_index()
            status_count.columns = ["Status", "Count"]
            fig_status = px.pie(
                status_count,
                names="Status",
                values="Count",
                title="Complete vs Pending"
            )
            st.plotly_chart(fig_status, use_container_width=True)


elif view == "📥 Import data":
    st.subheader("Import data")

    st.info(
        "Upload an Excel file with these columns: "
        + ", ".join(REQUIRED_COLUMNS)
    )

    uploaded_file = st.file_uploader("Upload service_report.xlsx", type=["xlsx"])

    if uploaded_file is not None:
        save_uploaded_file(uploaded_file)
        st.success("Excel file uploaded successfully. Please refresh the page or switch view.")

    st.markdown("### Current data preview")
    st.dataframe(df, use_container_width=True, hide_index=True)

    st.download_button(
        label="Download current Excel",
        data=to_excel_bytes(df),
        file_name="service_report_current.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
