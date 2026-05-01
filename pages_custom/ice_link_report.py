import streamlit as st
import pandas as pd
from pathlib import Path
from io import BytesIO
import textwrap


# =========================
# iCE LiNK Report Settings
# =========================
BASE_DIR = Path(__file__).resolve().parents[1]

# Excel file location:
# service-report-app/icelink_reports/iCE LiNK ライセンスなど.xlsx
REPORT_DIR = BASE_DIR / "icelink_reports"
REPORT_EXCEL_NAME = "iCE LiNK ライセンスなど.xlsx"
REPORT_EXCEL_PATH = REPORT_DIR / REPORT_EXCEL_NAME


# =========================
# Common Helper
# =========================
def html(content: str):
    st.markdown(textwrap.dedent(content).strip(), unsafe_allow_html=True)


def apply_ice_link_css():
    html(
        """
        <style>
        .ice-hero {
            padding: 34px 42px;
            border-radius: 30px;
            background:
                radial-gradient(circle at right center, rgba(255,255,255,0.18), transparent 30%),
                linear-gradient(135deg, #243b53 0%, #36506b 52%, #90a4b8 100%);
            color: white;
            box-shadow: 0 16px 36px rgba(36,59,83,0.18);
            margin-bottom: 24px;
        }

        .ice-hero-title {
            font-size: 40px;
            font-weight: 900;
            margin-bottom: 16px;
            letter-spacing: -0.03em;
        }

        .ice-hero-subtitle {
            font-size: 16px;
            color: rgba(255,255,255,0.92);
            line-height: 1.8;
            max-width: 1150px;
        }

        .ice-section-title {
            font-size: 24px;
            font-weight: 900;
            color: #1f2a44;
            margin: 26px 0 12px 0;
        }

        .ice-note {
            background: #f8fafc;
            border: 1px solid #e5e7eb;
            border-radius: 16px;
            padding: 13px 16px;
            color: #475569;
            font-size: 14px;
            line-height: 1.7;
            margin-bottom: 16px;
        }

        .ice-warning {
            background: #fff7ed;
            border: 1px solid #fed7aa;
            border-radius: 16px;
            padding: 13px 16px;
            color: #9a3412;
            font-size: 14px;
            line-height: 1.7;
            margin-bottom: 16px;
        }

        .ice-success {
            background: #ecfdf5;
            border: 1px solid #bbf7d0;
            border-radius: 14px;
            padding: 11px 14px;
            color: #166534;
            font-size: 14px;
            font-weight: 800;
            margin-bottom: 16px;
        }

        div[data-testid="stMetric"] {
            background: #ffffff;
            border: 1px solid #e5edf6;
            padding: 16px 16px;
            border-radius: 18px;
            box-shadow: 0 8px 18px rgba(30,50,100,0.05);
        }

        div[data-testid="stMetricLabel"] {
            color: #667085;
            font-weight: 800;
        }

        div[data-testid="stMetricValue"] {
            color: #1f2a44;
            font-weight: 900;
            font-size: 28px;
        }
        </style>
        """
    )


def excel_obj(source):
    if isinstance(source, bytes):
        return BytesIO(source)
    return source


def get_excel_source():
    """
    Priority:
    1. Excel file saved in /icelink_reports/
    2. Uploaded file from Streamlit UI
    """
    if REPORT_EXCEL_PATH.exists():
        return str(REPORT_EXCEL_PATH), REPORT_EXCEL_PATH.name

    uploaded = st.file_uploader(
        "Upload iCE LiNK Excel",
        type=["xlsx"],
        help="Upload iCE LiNK ライセンスなど.xlsx",
    )

    if uploaded is not None:
        return uploaded.getvalue(), uploaded.name

    return None, None


def parse_month_label(col):
    if isinstance(col, pd.Timestamp):
        return col.strftime("%Y-%m")

    text = str(col).strip()

    for fmt in ["%Y/%m", "%Y-%m", "%Y-%m-%d %H:%M:%S", "%Y-%m-%d"]:
        try:
            return pd.to_datetime(text, format=fmt).strftime("%Y-%m")
        except Exception:
            pass

    dt = pd.to_datetime(text, errors="coerce")
    if pd.notna(dt):
        return dt.strftime("%Y-%m")

    return text


# =========================
# Excel Parser
# =========================
@st.cache_data(show_spinner=False)
def parse_summary_sheet(source, sheet_name: str, metric_name: str):
    """
    Parse user / device sheet.

    Expected structure:
    Row 1: Agency / Month / Agency names
    Row 2: active_user or active_device labels
    Row 3 onwards: data
    """
    raw = pd.read_excel(excel_obj(source), sheet_name=sheet_name)
    raw.columns = [str(c).strip() for c in raw.columns]

    # The first Excel data row contains active_user / active_device labels.
    # Real data starts from the next row.
    raw = raw.iloc[1:].copy()

    first_col = raw.columns[0]
    second_col = raw.columns[1]

    raw = raw.rename(columns={first_col: "Year", second_col: "Month"})

    raw["Year"] = raw["Year"].ffill()
    raw["Year"] = pd.to_numeric(raw["Year"], errors="coerce")
    raw["Month"] = pd.to_numeric(raw["Month"], errors="coerce")

    raw = raw[raw["Year"].notna() & raw["Month"].notna()].copy()

    raw["Date"] = pd.to_datetime(
        dict(
            year=raw["Year"].astype(int),
            month=raw["Month"].astype(int),
            day=1,
        )
    )

    total_col = "Total" if "Total" in raw.columns else raw.columns[-2]
    raw["Total"] = pd.to_numeric(raw[total_col], errors="coerce")

    exclude_cols = {
        "Year",
        "Month",
        "Date",
        "Total",
        "Unnamed: 27",
    }

    agency_cols = [c for c in raw.columns if c not in exclude_cols]

    long_df = raw.melt(
        id_vars=["Date", "Total"],
        value_vars=agency_cols,
        var_name="Agency",
        value_name=metric_name,
    )

    long_df[metric_name] = pd.to_numeric(
        long_df[metric_name],
        errors="coerce",
    ).fillna(0)

    long_df = long_df[long_df[metric_name] > 0].copy()

    total_df = raw[["Date", "Total"]].dropna().copy()
    total_df = total_df.sort_values("Date")

    long_df = long_df.sort_values(
        ["Date", metric_name],
        ascending=[True, False],
    )

    return total_df, long_df


@st.cache_data(show_spinner=False)
def parse_report_sheet(source):
    """
    Parse report sheet.

    Main outputs:
    1. Monthly reported machine count from the summary row:
       License end == 一か月の間にレポートを送った機械の数

    2. Machine license list with status:
       Expired / Expiring within 30 days / Expiring within 90 days / Active / Unknown
    """
    report = pd.read_excel(excel_obj(source), sheet_name="report")
    report.columns = [str(c).strip() for c in report.columns]

    summary_mask = report["License end"].astype(str).str.contains(
        "一か月の間にレポートを送った機械の数",
        na=False,
    )

    if not summary_mask.any():
        raise ValueError("The summary row was not found in the report sheet.")

    summary_idx = report.index[summary_mask][0]

    meta_cols = [
        "Agent",
        "Unnamed: 1",
        "Customer",
        "Model",
        "s/n",
        "License end",
    ]

    month_cols = [c for c in report.columns if c not in meta_cols]

    summary_row = report.loc[summary_idx]

    trend_rows = []

    for col in month_cols:
        value = pd.to_numeric(
            pd.Series([summary_row[col]]),
            errors="coerce",
        ).iloc[0]

        if pd.notna(value):
            month_label = parse_month_label(col)
            date_value = pd.to_datetime(month_label + "-01", errors="coerce")

            if pd.notna(date_value):
                trend_rows.append(
                    {
                        "Date": date_value,
                        "Month": month_label,
                        "Reported Machines": int(value),
                    }
                )

    report_trend_df = pd.DataFrame(trend_rows).sort_values("Date")

    machines = report.loc[: summary_idx - 1].copy()

    machines["Agent"] = machines["Agent"].ffill()
    machines["Customer"] = machines["Customer"].ffill()
    machines["License end"] = pd.to_datetime(
        machines["License end"],
        errors="coerce",
    )

    machines = machines[machines["Model"].notna()].copy()

    today = pd.Timestamp.today().normalize()
    machines["Days Left"] = (machines["License end"] - today).dt.days

    def get_status(days):
        if pd.isna(days):
            return "Unknown"
        if days < 0:
            return "Expired"
        if days <= 30:
            return "Expiring within 30 days"
        if days <= 90:
            return "Expiring within 90 days"
        return "Active"

    machines["Status"] = machines["Days Left"].apply(get_status)

    status_order = {
        "Expired": 0,
        "Expiring within 30 days": 1,
        "Expiring within 90 days": 2,
        "Active": 3,
        "Unknown": 4,
    }

    machines["Status Order"] = machines["Status"].map(status_order).fillna(99)

    return report_trend_df, machines


# =========================
# Display Helpers
# =========================
def format_month(value):
    return pd.to_datetime(value).strftime("%Y-%m")


def format_delta(current, previous):
    if pd.isna(previous) or previous == 0:
        return "New"

    growth = ((current - previous) / previous) * 100
    return f"{growth:+.1f}%"


def render_kpis(user_total_df, report_trend_df, machines_df):
    latest_user = user_total_df.iloc[-1]
    previous_user = user_total_df.iloc[-2] if len(user_total_df) >= 2 else None

    latest_report = report_trend_df.iloc[-1]
    previous_report = report_trend_df.iloc[-2] if len(report_trend_df) >= 2 else None

    expired_count = int((machines_df["Status"] == "Expired").sum())

    expiring_soon_count = int(
        machines_df["Status"].isin(
            [
                "Expiring within 30 days",
                "Expiring within 90 days",
            ]
        ).sum()
    )

    k1, k2, k3, k4 = st.columns(4)

    with k1:
        st.metric(
            "Active Users",
            int(latest_user["Total"]),
            delta=format_delta(
                int(latest_user["Total"]),
                int(previous_user["Total"]) if previous_user is not None else 0,
            ),
        )
        st.caption(f"Latest month: {format_month(latest_user['Date'])}")

    with k2:
        st.metric(
            "Reported Machines",
            int(latest_report["Reported Machines"]),
            delta=format_delta(
                int(latest_report["Reported Machines"]),
                int(previous_report["Reported Machines"])
                if previous_report is not None
                else 0,
            ),
        )
        st.caption(f"Latest month: {latest_report['Month']}")

    with k3:
        st.metric("Expired Licenses", expired_count)
        st.caption("Need immediate follow-up")

    with k4:
        st.metric("Expiring Soon", expiring_soon_count)
        st.caption("Within 90 days")


def render_dashboard(user_total_df, user_long_df, device_total_df, report_trend_df, machines_df):
    html('<div class="ice-section-title">Executive Summary</div>')

    render_kpis(user_total_df, report_trend_df, machines_df)

    html(
        """
        <div class="ice-note">
            Main KPIs use the <b>user</b> sheet and the monthly summary row from the
            <b>report</b> sheet. The <b>device</b> sheet is shown as supplementary information
            because recent rows may be incomplete.
        </div>
        """
    )

    html('<div class="ice-section-title">Trend Overview</div>')

    c1, c2 = st.columns(2)

    with c1:
        st.caption("Active User Trend")
        chart_df = user_total_df.copy()
        chart_df["Month"] = chart_df["Date"].dt.strftime("%Y-%m")

        st.line_chart(
            chart_df,
            x="Month",
            y="Total",
            use_container_width=True,
        )

    with c2:
        st.caption("Reported Machines Trend")
        st.line_chart(
            report_trend_df,
            x="Month",
            y="Reported Machines",
            use_container_width=True,
        )

    html('<div class="ice-section-title">Active Users by Agency</div>')

    latest_date = user_long_df["Date"].max()

    latest_agency_df = (
        user_long_df[user_long_df["Date"] == latest_date][
            ["Agency", "Active Users"]
        ]
        .sort_values("Active Users", ascending=False)
        .head(12)
    )

    st.caption(f"Latest month: {format_month(latest_date)}")

    st.bar_chart(
        latest_agency_df,
        x="Agency",
        y="Active Users",
        use_container_width=True,
    )

    st.dataframe(
        latest_agency_df,
        use_container_width=True,
        hide_index=True,
    )

    with st.expander("Supplement: Device Sheet Overview"):
        st.caption(
            "The device sheet is shown as supplementary information. "
            "If 2026-03 / 2026-04 are incomplete, please update the source Excel."
        )

        valid_device_df = device_total_df.dropna(subset=["Total"]).copy()
        valid_device_df["Month"] = valid_device_df["Date"].dt.strftime("%Y-%m")

        st.line_chart(
            valid_device_df,
            x="Month",
            y="Total",
            use_container_width=True,
        )

        st.dataframe(
            valid_device_df[["Month", "Total"]],
            use_container_width=True,
            hide_index=True,
        )


def render_license_followup(machines_df):
    html('<div class="ice-section-title">License Follow-up</div>')

    html(
        """
        <div class="ice-warning">
            This table is designed for action. Please focus first on
            <b>Expired</b>, <b>Expiring within 30 days</b>, and
            <b>Expiring within 90 days</b>.
        </div>
        """
    )

    status_options = [
        "Expired",
        "Expiring within 30 days",
        "Expiring within 90 days",
        "Active",
        "Unknown",
    ]

    agent_options = sorted(
        [
            str(a)
            for a in machines_df["Agent"].dropna().unique().tolist()
            if str(a).strip()
        ]
    )

    c1, c2, c3 = st.columns([1.2, 1.2, 1.6])

    with c1:
        selected_status = st.multiselect(
            "Status",
            options=status_options,
            default=[
                "Expired",
                "Expiring within 30 days",
                "Expiring within 90 days",
            ],
        )

    with c2:
        selected_agents = st.multiselect(
            "Agent",
            options=agent_options,
        )

    with c3:
        keyword = st.text_input(
            "Keyword",
            placeholder="Customer / Model / S/N",
        )

    filtered_df = machines_df.copy()

    if selected_status:
        filtered_df = filtered_df[filtered_df["Status"].isin(selected_status)]

    if selected_agents:
        filtered_df = filtered_df[filtered_df["Agent"].isin(selected_agents)]

    if keyword.strip():
        key = keyword.strip().lower()

        filtered_df = filtered_df[
            filtered_df["Customer"].astype(str).str.lower().str.contains(key, na=False)
            | filtered_df["Model"].astype(str).str.lower().str.contains(key, na=False)
            | filtered_df["s/n"].astype(str).str.lower().str.contains(key, na=False)
        ]

    status_count_df = (
        filtered_df.groupby("Status", as_index=False)
        .size()
        .rename(columns={"size": "Count"})
    )

    if not status_count_df.empty:
        order_map = {
            "Expired": 0,
            "Expiring within 30 days": 1,
            "Expiring within 90 days": 2,
            "Active": 3,
            "Unknown": 4,
        }

        status_count_df["order"] = status_count_df["Status"].map(order_map)
        status_count_df = status_count_df.sort_values("order").drop(columns=["order"])

        st.bar_chart(
            status_count_df,
            x="Status",
            y="Count",
            use_container_width=True,
        )

    filtered_df = filtered_df.sort_values(
        [
            "Status Order",
            "License end",
            "Agent",
            "Customer",
        ]
    )

    display_df = filtered_df[
        [
            "Status",
            "Agent",
            "Customer",
            "Model",
            "s/n",
            "License end",
            "Days Left",
        ]
    ].copy()

    display_df["License end"] = display_df["License end"].dt.strftime("%Y-%m-%d")

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True,
    )

    st.caption(f"Displayed rows: {len(display_df)}")


def render_raw_data(user_total_df, user_long_df, device_total_df, report_trend_df, machines_df):
    html('<div class="ice-section-title">Raw / Processed Data Preview</div>')

    with st.expander("user sheet: Monthly Total"):
        preview = user_total_df.copy()
        preview["Month"] = preview["Date"].dt.strftime("%Y-%m")

        st.dataframe(
            preview[["Month", "Total"]],
            use_container_width=True,
            hide_index=True,
        )

    with st.expander("user sheet: Latest Agency Detail"):
        latest_date = user_long_df["Date"].max()

        preview = user_long_df[user_long_df["Date"] == latest_date].copy()
        preview["Month"] = preview["Date"].dt.strftime("%Y-%m")

        st.dataframe(
            preview[["Month", "Agency", "Active Users"]],
            use_container_width=True,
            hide_index=True,
        )

    with st.expander("device sheet: Monthly Total"):
        preview = device_total_df.copy()
        preview["Month"] = preview["Date"].dt.strftime("%Y-%m")

        st.dataframe(
            preview[["Month", "Total"]],
            use_container_width=True,
            hide_index=True,
        )

    with st.expander("report sheet: Monthly Reported Machines"):
        st.dataframe(
            report_trend_df[["Month", "Reported Machines"]],
            use_container_width=True,
            hide_index=True,
        )

    with st.expander("report sheet: License Machine List Preview"):
        preview = machines_df[
            [
                "Agent",
                "Customer",
                "Model",
                "s/n",
                "License end",
                "Status",
            ]
        ].copy()

        preview["License end"] = preview["License end"].dt.strftime("%Y-%m-%d")

        st.dataframe(
            preview.head(300),
            use_container_width=True,
            hide_index=True,
        )


# =========================
# Main Render Function
# =========================
def render_ice_link_report():
    apply_ice_link_css()

    html(
        """
        <div class="ice-success">
            New ice_link_report.py is running. Source path setting is icelink_reports.
        </div>
        """
    )

    html(
        """
        <div class="ice-hero">
            <div class="ice-hero-title">📊 iCE LiNK Report Dashboard</div>
            <div class="ice-hero-subtitle">
                Review iCE LiNK usage, monthly reported machines, and license follow-up items.
                This page converts the three-sheet Excel file into a management-friendly dashboard.
            </div>
        </div>
        """
    )

    source, file_name = get_excel_source()

    if source is None:
        st.warning(
            "iCE LiNK Excel file was not found. "
            "Please place the Excel file under "
            "`icelink_reports/iCE LiNK ライセンスなど.xlsx`, "
            "or upload it from this page."
        )
        return

    st.caption(f"Current source: {file_name}")
    st.caption(f"Expected path: {REPORT_EXCEL_PATH}")

    try:
        user_total_df, user_long_df = parse_summary_sheet(
            source,
            "user",
            "Active Users",
        )

        device_total_df, device_long_df = parse_summary_sheet(
            source,
            "device",
            "Active Devices",
        )

        report_trend_df, machines_df = parse_report_sheet(source)

    except Exception as e:
        st.error(f"Failed to read iCE LiNK Excel correctly: {e}")
        return

    dashboard_tab, license_tab, raw_tab = st.tabs(
        [
            "Dashboard",
            "License Follow-up",
            "Raw Data",
        ]
    )

    with dashboard_tab:
        render_dashboard(
            user_total_df,
            user_long_df,
            device_total_df,
            report_trend_df,
            machines_df,
        )

    with license_tab:
        render_license_followup(machines_df)

    with raw_tab:
        render_raw_data(
            user_total_df,
            user_long_df,
            device_total_df,
            report_trend_df,
            machines_df,
        )


# =========================
# Standalone Test
# =========================
if __name__ == "__main__":
    render_ice_link_report()
