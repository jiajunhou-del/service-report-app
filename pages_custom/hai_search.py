import streamlit as st
from pathlib import Path
import base64
import mimetypes
import pandas as pd
import streamlit.components.v1 as components


# =========================
# Path / Link Settings
# =========================
BASE_DIR = Path(__file__).resolve().parents[1]
ASSETS_DIR = BASE_DIR / "assets"
REPORT_DIR = BASE_DIR / "hai_search_reports"

HAI_LOGO_PATH = ASSETS_DIR / "hai_search_logo.jpg.png"

SLACK_URL = "https://app.slack.com/"


# =========================
# Helper
# =========================
def image_to_data_uri(image_path: Path) -> str:
    if not image_path.exists():
        return ""

    mime_type, _ = mimetypes.guess_type(str(image_path))
    if mime_type is None:
        mime_type = "image/png"

    encoded = base64.b64encode(image_path.read_bytes()).decode("utf-8")
    return f"data:{mime_type};base64,{encoded}"


def normalize_column_name(col) -> str:
    return str(col).strip()


def find_column(df: pd.DataFrame, candidates: list[str]) -> str | None:
    normalized_map = {normalize_column_name(col).lower(): col for col in df.columns}

    for candidate in candidates:
        key = candidate.lower()
        if key in normalized_map:
            return normalized_map[key]

    return None


# =========================
# CSS for Streamlit native area
# =========================
def apply_css():
    st.markdown(
        """
<style>
.hai-section-title {
    font-size: 32px;
    font-weight: 900;
    color: #1f2a44;
    margin-top: 10px;
    margin-bottom: 8px;
}

.hai-section-subtitle {
    font-size: 17px;
    color: #667085;
    margin-bottom: 24px;
}

div.stLinkButton > a {
    border-radius: 14px !important;
    font-weight: 900 !important;
    font-size: 15px !important;
    padding: 0.75rem 1.1rem !important;
    text-decoration: none !important;
    box-shadow: 0 8px 18px rgba(239,68,68,0.14) !important;
    border: 1px solid #fee2e2 !important;
}

.hai-card-box {
    background: #ffffff;
    border: 1px solid #e7ebf3;
    border-radius: 24px;
    padding: 28px 30px;
    box-shadow: 0 10px 28px rgba(30, 50, 100, 0.06);
    min-height: 230px;
    margin-bottom: 14px;
}

.hai-card-icon {
    width: 66px;
    height: 66px;
    border-radius: 18px;
    background: #fff1f2;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 31px;
    margin-bottom: 18px;
}

.hai-card-title {
    font-size: 24px;
    font-weight: 900;
    color: #243255;
    margin-bottom: 14px;
}

.hai-card-text {
    font-size: 16px;
    color: #63708d;
    line-height: 1.9;
}

.hai-note-box {
    background: #ffffff;
    border: 1px solid #e7ebf3;
    border-radius: 26px;
    padding: 28px 30px;
    box-shadow: 0 10px 28px rgba(30, 50, 100, 0.05);
    margin-top: 12px;
    margin-bottom: 24px;
}

.hai-note-title {
    font-size: 24px;
    font-weight: 900;
    color: #22315a;
    margin-bottom: 16px;
}

.hai-note-list {
    margin: 0;
    padding-left: 20px;
    color: #5f6d8b;
    line-height: 2;
    font-size: 16px;
}

.hai-tip {
    background: #fff7f7;
    border: 1px solid #fee2e2;
    border-radius: 18px;
    padding: 16px 18px;
    color: #4e5f82;
    font-size: 15px;
    line-height: 1.8;
    margin-top: 18px;
}

.hai-report-box {
    background: #ffffff;
    border: 1px solid #e7ebf3;
    border-radius: 26px;
    padding: 28px 30px;
    box-shadow: 0 10px 28px rgba(30, 50, 100, 0.05);
    margin-top: 24px;
    margin-bottom: 24px;
}

.hai-report-title {
    font-size: 28px;
    font-weight: 900;
    color: #1f2a44;
    margin-bottom: 8px;
}

.hai-report-subtitle {
    font-size: 15px;
    color: #667085;
    line-height: 1.8;
    margin-bottom: 18px;
}
</style>
        """,
        unsafe_allow_html=True,
    )


# =========================
# Hero by components.html
# =========================
def render_hero():
    logo_data_uri = image_to_data_uri(HAI_LOGO_PATH)

    if logo_data_uri:
        logo_html = f'<img src="{logo_data_uri}" alt="HAI Search Logo">'
    else:
        logo_html = """
        <div class="logo-fallback">
            Logo image not found<br>
            assets/hai_search_logo.jpg.png
        </div>
        """

    hero_html = f"""
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

.hero {{
    box-sizing: border-box;
    width: 100%;
    min-height: 280px;
    background:
        radial-gradient(circle at right center, rgba(239,68,68,0.24), transparent 34%),
        linear-gradient(135deg, #111827 0%, #26313f 58%, #ef4444 100%);
    border-radius: 32px;
    padding: 40px 46px;
    box-shadow: 0 16px 36px rgba(17,24,39,0.24);
}}

.hero-grid {{
    display: grid;
    grid-template-columns: 360px minmax(0, 1fr);
    gap: 44px;
    align-items: center;
}}

.logo-panel {{
    background: rgba(255,255,255,0.12);
    border: 1px solid rgba(255,255,255,0.20);
    border-radius: 28px;
    padding: 22px;
    min-height: 210px;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow:
        inset 0 1px 0 rgba(255,255,255,0.16),
        0 14px 30px rgba(0,0,0,0.18);
}}

.logo-box {{
    width: 100%;
    min-height: 170px;
    border-radius: 22px;
    background: rgba(255,255,255,0.96);
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 22px;
    box-sizing: border-box;
}}

.logo-box img {{
    max-width: 100%;
    max-height: 145px;
    object-fit: contain;
}}

.badge {{
    display: inline-block;
    padding: 9px 17px;
    border-radius: 999px;
    background: rgba(239,68,68,0.26);
    border: 1px solid rgba(255,255,255,0.22);
    color: #ffffff;
    font-weight: 800;
    font-size: 14px;
    margin-bottom: 22px;
}}

.hero-text {{
    color: #ffffff;
    font-size: 19px;
    line-height: 1.9;
    font-weight: 650;
    max-width: 1080px;
}}

.hero-subtext {{
    margin-top: 22px;
    color: rgba(255,255,255,0.90);
    font-size: 16px;
    line-height: 1.8;
}}

.logo-fallback {{
    color: #667085;
    font-weight: 700;
    text-align: center;
    line-height: 1.7;
}}

@media (max-width: 900px) {{
    .hero {{
        padding: 32px 28px;
    }}

    .hero-grid {{
        grid-template-columns: 1fr;
    }}

    .logo-panel {{
        max-width: 360px;
    }}
}}
</style>
</head>

<body>
<div class="hero">
    <div class="hero-grid">

        <div class="logo-panel">
            <div class="logo-box">
                {logo_html}
            </div>
        </div>

        <div>
            <div class="badge">Internal AI Search Assistant</div>

            <div class="hero-text">
                HAI Search is an AI-powered search and Q&amp;A tool for service support.
                It helps users find troubleshooting information, service manuals, bulletins,
                error code information, and other service-related documents through Slack.
            </div>

            <div class="hero-subtext">
                Use this portal as the starting point for HAI Search access and update information.
            </div>
        </div>

    </div>
</div>
</body>
</html>
"""

    components.html(hero_html, height=310, scrolling=False)


# =========================
# Monthly Report Loader
# =========================
def load_hai_search_reports() -> pd.DataFrame:
    if not REPORT_DIR.exists():
        return pd.DataFrame()

    files = sorted(REPORT_DIR.glob("*.xlsx"), reverse=True)

    if not files:
        return pd.DataFrame()

    all_frames = []

    for file in files:
        try:
            df = pd.read_excel(file)
            df.columns = [normalize_column_name(col) for col in df.columns]
            df["Report File"] = file.name
            df["Report Month"] = file.stem.replace("monthly_report_", "")
            all_frames.append(df)
        except Exception as e:
            st.warning(f"Could not read {file.name}: {e}")

    if not all_frames:
        return pd.DataFrame()

    return pd.concat(all_frames, ignore_index=True)


def prepare_usage_dataframe(raw_df: pd.DataFrame) -> pd.DataFrame:
    if raw_df.empty:
        return pd.DataFrame()

    user_id_col = find_column(raw_df, ["User ID", "ユーザーID", "user_id"])
    channel_col = find_column(raw_df, ["Channel Name", "チャンネル名", "channel_name"])
    user_name_col = find_column(raw_df, ["User Name", "ユーザー名", "user_name", "Name"])
    new_col = find_column(raw_df, ["/newコマンド数", "/new", "new", "new command", "new command count"])
    docs_col = find_column(raw_df, ["/docsコマンド数", "/docs", "docs", "docs command", "docs command count"])

    required = {
        "User ID": user_id_col,
        "Channel Name": channel_col,
        "User Name": user_name_col,
        "/new": new_col,
        "/docs": docs_col,
    }

    missing = [display_name for display_name, col in required.items() if col is None]

    if missing:
        st.error(f"Excel columns are missing or not recognized: {missing}")
        st.caption("Expected columns: User ID, Channel Name, User Name, /newコマンド数, /docsコマンド数")
        st.dataframe(raw_df.head(20), use_container_width=True)
        return pd.DataFrame()

    df = pd.DataFrame(
        {
            "Report Month": raw_df["Report Month"],
            "Report File": raw_df["Report File"],
            "User ID": raw_df[user_id_col].astype(str),
            "Channel Name": raw_df[channel_col].astype(str),
            "User Name": raw_df[user_name_col].astype(str),
            "/new": pd.to_numeric(raw_df[new_col], errors="coerce").fillna(0).astype(int),
            "/docs": pd.to_numeric(raw_df[docs_col], errors="coerce").fillna(0).astype(int),
        }
    )

    df["Total Commands"] = df["/new"] + df["/docs"]

    return df


# =========================
# Monthly Report Section
# =========================
def render_monthly_usage_report():
    st.markdown(
        """
<div class="hai-report-box">
    <div class="hai-report-title">HAI Search Monthly Usage Report</div>
    <div class="hai-report-subtitle">
        View HAI Search usage by month, dealer channel, and user. 
        Monthly Excel files are read from <b>hai_search_reports/</b>.
    </div>
</div>
        """,
        unsafe_allow_html=True,
    )

    raw_df = load_hai_search_reports()

    if raw_df.empty:
        st.info(
            "No monthly report Excel file found. Please upload files to "
            "`hai_search_reports/monthly_report_YYYY-MM.xlsx`."
        )
        return

    df = prepare_usage_dataframe(raw_df)

    if df.empty:
        return

    months = sorted(df["Report Month"].dropna().unique(), reverse=True)

    filter_col1, filter_col2 = st.columns([1, 2])

    with filter_col1:
        selected_month = st.selectbox(
            "Select Month",
            options=["All"] + months,
            index=1 if months else 0,
        )

    with filter_col2:
        keyword = st.text_input(
            "Search dealer / channel / user",
            placeholder="Example: hai-search-sd, pz, Max, Joseph...",
        )

    filtered_df = df.copy()

    if selected_month != "All":
        filtered_df = filtered_df[filtered_df["Report Month"] == selected_month]

    if keyword.strip():
        key = keyword.strip().lower()

        filtered_df = filtered_df[
            filtered_df["Channel Name"].str.lower().str.contains(key, na=False)
            | filtered_df["User Name"].str.lower().str.contains(key, na=False)
            | filtered_df["User ID"].str.lower().str.contains(key, na=False)
        ]

    total_users = filtered_df["User ID"].nunique()
    total_new = int(filtered_df["/new"].sum())
    total_docs = int(filtered_df["/docs"].sum())
    total_commands = int(filtered_df["Total Commands"].sum())

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    kpi1.metric("Users", total_users)
    kpi2.metric("/new", total_new)
    kpi3.metric("/docs", total_docs)
    kpi4.metric("Total Commands", total_commands)

    display_df = filtered_df[
        [
            "Report Month",
            "Channel Name",
            "User Name",
            "/new",
            "/docs",
            "Total Commands",
            "Report File",
        ]
    ].sort_values("Total Commands", ascending=False)

    st.markdown("### Usage Detail")
    st.dataframe(display_df, use_container_width=True, hide_index=True)

    st.markdown("### Top 10 Users by Total Commands")

    chart_df = (
        filtered_df.groupby(["Channel Name", "User Name"], as_index=False)["Total Commands"]
        .sum()
        .sort_values("Total Commands", ascending=False)
        .head(10)
    )

    if chart_df.empty:
        st.info("No usage data to display.")
    else:
        chart_df["User / Channel"] = (
            chart_df["User Name"].astype(str)
            + " / "
            + chart_df["Channel Name"].astype(str)
        )

        st.bar_chart(
            chart_df,
            x="User / Channel",
            y="Total Commands",
            use_container_width=True,
        )

    st.caption(
        "To update this section, upload a new Excel file to `hai_search_reports/`, "
        "for example `monthly_report_2026-05.xlsx`."
    )


# =========================
# Main Render
# =========================
def render_hai_search():
    apply_css()

    render_hero()

    st.markdown(
        """
<div class="hai-section-title">HAI Search Portal</div>
<div class="hai-section-subtitle">
    Choose an entry below to start using HAI Search.
</div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown(
            """
<div class="hai-card-box">
    <div class="hai-card-icon">🔎</div>
    <div class="hai-card-title">Search in Slack</div>
    <div class="hai-card-text">
        Open Slack and use HAI Search through your available workspace and channel.
        Use <b>/new</b> for questions and <b>/docs</b> for document search.
    </div>
</div>
            """,
            unsafe_allow_html=True,
        )
        st.link_button("🚀 Open Slack", SLACK_URL, use_container_width=True)

    with col2:
        st.markdown(
            """
<div class="hai-card-box">
    <div class="hai-card-icon">📝</div>
    <div class="hai-card-title">Update Notes</div>
    <div class="hai-card-text">
        Review version updates, improvement notes, known issues,
        and future enhancement items for HAI Search.
    </div>
</div>
            """,
            unsafe_allow_html=True,
        )
        st.button("📘 View Update Notes", use_container_width=True, disabled=True)

    st.markdown(
        """
<div class="hai-note-box">
    <div class="hai-note-title">Update Notes</div>
    <ul class="hai-note-list">
        <li>Multiple Search function was added to search documents more precisely.</li>
        <li>Enhanced searching power to give more accurate answers.</li>
        <li>Error code documents were added to improve response quality for error-related questions.</li>
        <li>Japanese document handling and guidance can be updated here in the future.</li>
    </ul>

    <div class="hai-tip">
        <b>Recommended use:</b>
        Use <b>/new</b> for Q&amp;A and <b>/docs</b> for document search.
        If the first answer is unclear, try rewriting the question in a simpler way.
    </div>
</div>
        """,
        unsafe_allow_html=True,
    )

    render_monthly_usage_report()
