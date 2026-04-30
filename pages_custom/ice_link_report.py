import streamlit as st
import pandas as pd
from pathlib import Path


# =========================
# iCE LiNK Report Settings
# =========================
REPORT_EXCEL = Path("service_report.xlsx")


# =========================
# CSS
# =========================
def apply_ice_link_css():
    st.markdown(
        """
        <style>
        .ice-hero {
            padding: 34px 42px;
            border-radius: 30px;
            background:
                radial-gradient(circle at right center, rgba(255,255,255,0.18), transparent 28%),
                linear-gradient(135deg, #0f766e 0%, #2563eb 58%, #1d4ed8 100%);
            color: white;
            box-shadow: 0 18px 45px rgba(37,99,235,0.24);
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
            color: #e0f2fe;
            line-height: 1.8;
            max-width: 1100px;
        }

        .ice-card {
            background: #ffffff;
            border: 1px solid #e5e7eb;
            border-radius: 22px;
            padding: 22px 24px;
            margin-top: 18px;
            margin-bottom: 18px;
            box-shadow: 0 10px 28px rgba(15,23,42,0.06);
        }

        .ice-card-title {
            font-size: 20px;
            font-weight: 900;
            color: #1f2a44;
            margin-bottom: 10px;
        }

        .ice-card-text {
            font-size: 14px;
            color: #667085;
            line-height: 1.7;
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
# Helper Functions
# =========================
def find_column(df: pd.DataFrame, keywords):
    """
    Find a column by keyword list.
    Example:
      keywords = ["dealer", "customer"]
    """
    columns = list(df.columns)

    for col in columns:
        col_lower = str(col).lower()
        for keyword in keywords:
            if keyword.lower() in col_lower:
                return col

    return None


def get_numeric_columns(df: pd.DataFrame):
    return list(df.select_dtypes(include="number").columns)


def load_excel_file():
    if not REPORT_EXCEL.exists():
        st.warning(
            "service_report.xlsx was not found. "
            "Please upload service_report.xlsx to the root folder of the repository."
        )
        return None

    try:
        xls = pd.ExcelFile(REPORT_EXCEL)
        return xls

    except Exception as e:
        st.error(f"Failed to open service_report.xlsx: {e}")
        return None


def load_sheet(xls: pd.ExcelFile, sheet_name: str):
    try:
        df = pd.read_excel(REPORT_EXCEL, sheet_name=sheet_name)

        # Remove fully empty rows and columns
        df = df.dropna(how="all")
        df = df.dropna(axis=1, how="all")

        return df

    except Exception as e:
        st.error(f"Failed to load sheet '{sheet_name}': {e}")
        return pd.DataFrame()


def apply_filters(df: pd.DataFrame):
    filtered_df = df.copy()

    st.markdown("### Filters")

    col1, col2, col3 = st.columns(3)

    dealer_col = find_column(df, ["dealer", "customer", "company"])
    country_col = find_column(df, ["country", "region", "area"])
    machine_col = find_column(df, ["machine", "model", "equipment"])

    with col1:
        if dealer_col:
            dealer_options = sorted(
                [str(x) for x in df[dealer_col].dropna().unique()]
            )
            selected_dealers = st.multiselect(
                "Dealer / Customer",
                dealer_options,
                default=[],
            )

            if selected_dealers:
                filtered_df = filtered_df[
                    filtered_df[dealer_col].astype(str).isin(selected_dealers)
                ]
        else:
            st.caption("Dealer column was not found.")

    with col2:
        if country_col:
            country_options = sorted(
                [str(x) for x in df[country_col].dropna().unique()]
            )
            selected_countries = st.multiselect(
                "Country / Region",
                country_options,
                default=[],
            )

            if selected_countries:
                filtered_df = filtered_df[
                    filtered_df[country_col].astype(str).isin(selected_countries)
                ]
        else:
            st.caption("Country column was not found.")

    with col3:
        if machine_col:
            machine_options = sorted(
                [str(x) for x in df[machine_col].dropna().unique()]
            )
            selected_machines = st.multiselect(
                "Machine / Model",
                machine_options,
                default=[],
            )

            if selected_machines:
                filtered_df = filtered_df[
                    filtered_df[machine_col].astype(str).isin(selected_machines)
                ]
        else:
            st.caption("Machine column was not found.")

    keyword = st.text_input(
        "Keyword Search",
        placeholder="Search text in all columns...",
    )

    if keyword:
        keyword_lower = keyword.lower()

        mask = filtered_df.apply(
            lambda row: row.astype(str).str.lower().str.contains(keyword_lower).any(),
            axis=1,
        )

        filtered_df = filtered_df[mask]

    return filtered_df


def render_metrics(df: pd.DataFrame):
    total_rows = len(df)
    total_columns = len(df.columns)
    numeric_cols = get_numeric_columns(df)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Records", total_rows)

    with col2:
        st.metric("Total Columns", total_columns)

    with col3:
        st.metric("Numeric Columns", len(numeric_cols))

    with col4:
        st.metric("Excel File", "Loaded")


def render_charts(df: pd.DataFrame):
    st.markdown("### Summary Charts")

    numeric_cols = get_numeric_columns(df)

    if not numeric_cols:
        st.info("No numeric columns were found for chart display.")
        return

    chart_col = st.selectbox(
        "Select numeric column for chart",
        numeric_cols,
    )

    category_candidates = []

    for col in df.columns:
        if col != chart_col and df[col].nunique(dropna=True) <= 30:
            category_candidates.append(col)

    if category_candidates:
        category_col = st.selectbox(
            "Group by",
            category_candidates,
        )

        chart_df = (
            df.groupby(category_col, dropna=False)[chart_col]
            .sum()
            .reset_index()
            .sort_values(chart_col, ascending=False)
            .head(20)
        )

        st.bar_chart(
            chart_df,
            x=category_col,
            y=chart_col,
            use_container_width=True,
        )

    else:
        st.line_chart(df[numeric_cols], use_container_width=True)


# =========================
# Main Render Function
# =========================
def render_ice_link_report():
    apply_ice_link_css()

    st.markdown(
        """
        <div class="ice-hero">
            <div class="ice-hero-title">📊 iCE LiNK Report</div>
            <div class="ice-hero-subtitle">
                Review iCE LiNK report data, production trends, run hours,
                error information, and hourly productivity.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    xls = load_excel_file()

    if xls is None:
        return

    sheet_names = xls.sheet_names

    if not sheet_names:
        st.warning("No sheets were found in service_report.xlsx.")
        return

    selected_sheet = st.selectbox(
        "Select sheet",
        sheet_names,
    )

    df = load_sheet(xls, selected_sheet)

    if df.empty:
        st.warning("The selected sheet is empty.")
        return

    render_metrics(df)

    st.markdown(
        """
        <div class="ice-card">
            <div class="ice-card-title">Report Summary</div>
            <div class="ice-card-text">
                The Excel file was loaded successfully. You can filter the data,
                check the table, and review simple summary charts.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    filtered_df = apply_filters(df)

    st.markdown(f"### Report Data: {len(filtered_df)} records")

    st.dataframe(
        filtered_df,
        use_container_width=True,
        hide_index=True,
    )

    render_charts(filtered_df)
