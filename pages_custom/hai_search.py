import streamlit as st
from pathlib import Path
import base64
import mimetypes
import pandas as pd
import textwrap
import streamlit.components.v1 as components


# =========================
# Path / Link Settings
# =========================
BASE_DIR = Path(__file__).resolve().parents[1]
ASSETS_DIR = BASE_DIR / "assets"
REPORT_DIR = BASE_DIR / "hai_search_reports"

HAI_LOGO_PATH = ASSETS_DIR / "hai_search_logo.jpg.png"

SLACK_URL = "https://app.slack.com/"

# Editable memo file for HAI Search update notes
UPDATE_NOTES_FILE = BASE_DIR / "hai_search_update_notes.md"


# =========================
# Helper
# =========================
def html(content: str):
    st.markdown(textwrap.dedent(content).strip(), unsafe_allow_html=True)


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


def format_number(value: int) -> str:
    return f"{int(value):,}"


def get_delta_text(current_value: int, previous_value: int) -> str:
    if previous_value == 0:
        if current_value == 0:
            return "0%"
        return "New"

    growth = ((current_value - previous_value) / previous_value) * 100
    return f"{growth:+.1f}%"


def render_metric_card(title: str, value: str, delta: str | None = None, icon: str = "📊"):
    delta_html = ""
    if delta is not None:
        delta_class = "metric-delta-neutral"

        if delta.startswith("+") or delta == "New":
            delta_class = "metric-delta-up"
        elif delta.startswith("-"):
            delta_class = "metric-delta-down"

        delta_html = f'<div class="metric-delta {delta_class}">{delta}</div>'

    html(
        f"""
        <div class="custom-metric-card">
            <div class="metric-top">
                <div class="metric-title">{title}</div>
                <div class="metric-icon">{icon}</div>
            </div>
            <div class="metric-value">{value}</div>
            {delta_html}
        </div>
        """
    )


# =========================
# CSS
# =========================
def apply_css():
    html(
        """
        <style>
        /* =========================
           Global
        ========================= */
        .block-container {
            padding-top: 2rem;
            padding-bottom: 3rem;
        }

        html, body, [class*="css"] {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        }

        /* =========================
           Section Header
        ========================= */
        .hai-section-header {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 15px 18px;
            border-radius: 18px;
            margin: 28px 0 16px 0;
            font-size: 28px;
            font-weight: 900;
            letter-spacing: -0.02em;
        }

        .hai-section-dot {
            width: 10px;
            height: 30px;
            border-radius: 999px;
            display: inline-block;
        }

        .hai-section-desc {
            font-size: 16px;
            color: #667085;
            margin: -6px 0 18px 4px;
            line-height: 1.7;
        }

        .section-blue {
            background: #f5f9ff;
            color: #22315a;
            border: 1px solid #d8e7ff;
        }

        .section-blue .hai-section-dot {
            background: #4f46e5;
        }

        .section-orange {
            background: #fff8f3;
            color: #7a3e1d;
            border: 1px solid #ffd9c7;
        }

        .section-orange .hai-section-dot {
            background: #f2994a;
        }

        .section-green {
            background: #f4fbf8;
            color: #1f5c46;
            border: 1px solid #cfebdd;
        }

        .section-green .hai-section-dot {
            background: #2cb67d;
        }

        .section-purple {
            background: #f6f5ff;
            color: #3730a3;
            border: 1px solid #ddd6fe;
        }

        .section-purple .hai-section-dot {
            background: #7c3aed;
        }

        /* =========================
           Portal Cards
        ========================= */
        .portal-card {
            border-radius: 28px;
            padding: 30px 32px;
            min-height: 250px;
            box-shadow: 0 16px 36px rgba(30, 50, 100, 0.08);
            margin-bottom: 14px;
            transition: all 0.25s ease;
        }

        .portal-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 20px 42px rgba(30, 50, 100, 0.12);
        }

        .portal-blue {
            background:
                radial-gradient(circle at top left, rgba(59, 130, 246, 0.10), transparent 32%),
                linear-gradient(180deg, #f7faff 0%, #ffffff 100%);
            border: 1px solid #d7e7ff;
        }

        .portal-orange {
            background:
                radial-gradient(circle at top left, rgba(249, 115, 22, 0.10), transparent 32%),
                linear-gradient(180deg, #fff8f3 0%, #ffffff 100%);
            border: 1px solid #ffd9c7;
        }

        .portal-icon {
            width: 66px;
            height: 66px;
            border-radius: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 32px;
            margin-bottom: 18px;
        }

        .portal-blue .portal-icon {
            background: #eaf3ff;
        }

        .portal-orange .portal-icon {
            background: #fff0e8;
        }

        .portal-title {
            font-size: 25px;
            font-weight: 900;
            color: #243255;
            margin-bottom: 12px;
        }

        .portal-text {
            font-size: 16px;
            color: #63708d;
            line-height: 1.9;
            min-height: 88px;
        }

        .portal-button {
            display: inline-block;
            margin-top: 18px;
            padding: 12px 22px;
            border-radius: 14px;
            text-decoration: none !important;
            font-weight: 900;
            font-size: 15px;
        }

        .portal-button-blue {
            background: linear-gradient(135deg, #2b4cb3 0%, #3a8ee8 100%);
            color: #ffffff !important;
            box-shadow: 0 8px 18px rgba(37, 99, 235, 0.18);
        }

        .portal-button-orange {
            background: #fff0e8;
            color: #a24618 !important;
            border: 1px solid #ffd9c7;
        }

        /* =========================
           Update Notes / Memo
        ========================= */
        .update-box {
            background:
                radial-gradient(circle at top left, rgba(249, 115, 22, 0.08), transparent 30%),
                linear-gradient(180deg, #fff8f3 0%, #ffffff 100%);
            border: 1px solid #ffd9c7;
            border-radius: 28px;
            padding: 28px 30px;
            box-shadow: 0 14px 32px rgba(122, 62, 29, 0.06);
            margin-bottom: 22px;
        }

        .update-title {
            font-size: 24px;
            font-weight: 900;
            color: #7a3e1d;
            margin-bottom: 14px;
        }

        .usage-tip {
            background: #fff9e8;
            border: 1px solid #ffe2a8;
            border-radius: 18px;
            padding: 16px 18px;
            color: #6b5a2b;
            font-size: 15px;
            line-height: 1.8;
            margin-top: 12px;
        }

        /* =========================
           Dashboard
        ========================= */
        .report-intro {
            background:
                radial-gradient(circle at top left, rgba(44, 182, 125, 0.10), transparent 30%),
                linear-gradient(180deg, #f4fbf8 0%, #ffffff 100%);
            border: 1px solid #cfebdd;
            border-radius: 28px;
            padding: 30px 32px;
            box-shadow: 0 14px 32px rgba(31, 92, 70, 0.06);
            margin-bottom: 22px;
        }

        .report-intro-title {
            font-size: 28px;
            font-weight: 900;
            color: #1f5c46;
            margin-bottom: 10px;
        }

        .report-intro-text {
            font-size: 15px;
            color: #5b7469;
            line-height: 1.8;
        }

        .dashboard-caption {
            background: #f8fafc;
            border: 1px solid #e5e7eb;
            border-radius: 16px;
            padding: 13px 16px;
            color: #475569;
            font-size: 14px;
            margin: 10px 0 18px 0;
            line-height: 1.7;
        }

        .data-card-title {
            font-size: 24px;
            font-weight: 900;
            color: #1f2a44;
            margin: 32px 0 14px 0;
            letter-spacing: -0.02em;
        }

        .data-card-subtitle {
            color: #667085;
            font-size: 15px;
            margin: -8px 0 16px 0;
            line-height: 1.7;
        }

        /* =========================
           Custom Metric Cards
        ========================= */
        .custom-metric-card {
            background:
                radial-gradient(circle at top right, rgba(59, 130, 246, 0.08), transparent 34%),
                linear-gradient(180deg, #ffffff 0%, #fbfdff 100%);
            border: 1px solid #e4ebf5;
            border-radius: 26px;
            padding: 24px 26px;
            box-shadow: 0 14px 30px rgba(31, 42, 68, 0.08);
            min-height: 150px;
            margin-bottom: 12px;
        }

        .metric-top {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 10px;
        }

        .metric-title {
            color: #667085;
            font-size: 15px;
            font-weight: 800;
        }

        .metric-icon {
            width: 42px;
            height: 42px;
            border-radius: 14px;
            background: #f2f6ff;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
        }

        .metric-value {
            font-size: 44px;
            font-weight: 950;
            color: #1f2a44;
            letter-spacing: -0.04em;
            margin-top: 12px;
            line-height: 1.05;
        }

        .metric-delta {
            display: inline-block;
            margin-top: 12px;
            padding: 5px 10px;
            border-radius: 999px;
            font-size: 13px;
            font-weight: 850;
        }

        .metric-delta-up {
            color: #047857;
            background: #ecfdf5;
            border: 1px solid #a7f3d0;
        }

        .metric-delta-down {
            color: #b42318;
            background: #fff1f2;
            border: 1px solid #fecdd3;
        }

        .metric-delta-neutral {
            color: #475569;
            background: #f8fafc;
            border: 1px solid #e2e8f0;
        }

        /* =========================
           Streamlit Widgets
        ========================= */
        div[data-testid="stTextInput"] input {
            border-radius: 18px;
            border: 1px solid #e5eaf3;
            background: #f8fafc;
        }

        div[data-baseweb="select"] > div {
            border-radius: 18px;
            border-color: #e5eaf3;
            background: #f8fafc;
        }

        textarea {
            border-radius: 20px !important;
            border: 1px solid #e5eaf3 !important;
            background: #fbfdff !important;
        }

        div.stButton > button {
            border-radius: 14px;
            font-weight: 900;
            border: 1px solid #dbeafe;
            box-shadow: 0 8px 18px rgba(37, 99, 235, 0.12);
        }

        div.stLinkButton > a {
            border-radius: 14px !important;
            font-weight: 900 !important;
            font-size: 15px !important;
            padding: 0.75rem 1.1rem !important;
            text-decoration: none !important;
            box-shadow: 0 8px 18px rgba(37, 99, 235, 0.12) !important;
            border: 1px solid #dbeafe !important;
        }

        /* =========================
           Dataframe Area
        ========================= */
        div[data-testid="stDataFrame"] {
            border-radius: 18px;
            overflow: hidden;
            box-shadow: 0 10px 26px rgba(31, 42, 68, 0.05);
        }
        </style>
        """
    )


# =========================
# Hero
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
    min-height: 285px;
    background:
        radial-gradient(circle at right center, rgba(239, 68, 68, 0.30), transparent 34%),
        radial-gradient(circle at left top, rgba(59, 130, 246, 0.16), transparent 28%),
        linear-gradient(135deg, #0f172a 0%, #26313f 58%, #ef4444 100%);
    border-radius: 34px;
    padding: 40px 46px;
    box-shadow: 0 20px 46px rgba(17, 24, 39, 0.26);
}}

.hero-grid {{
    display: grid;
    grid-template-columns: 360px minmax(0, 1fr);
    gap: 44px;
    align-items: center;
}}

.logo-panel {{
    background: rgba(255, 255, 255, 0.12);
    border: 1px solid rgba(255, 255, 255, 0.20);
    border-radius: 30px;
    padding: 22px;
    min-height: 210px;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow:
        inset 0 1px 0 rgba(255, 255, 255, 0.16),
        0 14px 30px rgba(0, 0, 0, 0.18);
}}

.logo-box {{
    width: 100%;
    min-height: 170px;
    border-radius: 24px;
    background: rgba(255, 255, 255, 0.96);
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
    background: rgba(239, 68, 68, 0.26);
    border: 1px solid rgba(255, 255, 255, 0.22);
    color: #ffffff;
    font-weight: 850;
    font-size: 14px;
    margin-bottom: 22px;
}}

.hero-title {{
    color: #ffffff;
    font-size: 26px;
    font-weight: 950;
    letter-spacing: -0.03em;
    margin-bottom: 12px;
}}

.hero-text {{
    color: #ffffff;
    font-size: 18px;
    line-height: 1.9;
    font-weight: 650;
    max-width: 1080px;
}}

.hero-subtext {{
    margin-top: 22px;
    color: rgba(255, 255, 255, 0.90);
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

            <div class="hero-title">HAI Search Service Portal</div>

            <div class="hero-text">
                HAI Search is an AI-powered search and Q&amp;A tool for service support.
                It helps users find troubleshooting information, service manuals, bulletins,
                error code information, and other service-related documents through Slack.
            </div>

            <div class="hero-subtext">
                Use this portal as the starting point for HAI Search access, update memo, and usage review.
            </div>
        </div>

    </div>
</div>
</body>
</html>
"""

    components.html(hero_html, height=325, scrolling=False)


# =========================
# Monthly Report Loader
# =========================
def sheet_has_usage_columns(df: pd.DataFrame) -> bool:
    """Check whether a sheet looks like the real user-level usage detail sheet."""
    if df.empty:
        return False

    df = df.copy()
    df.columns = [normalize_column_name(col) for col in df.columns]

    user_id_col = find_column(df, ["User ID", "ユーザーID", "user_id"])
    channel_col = find_column(df, ["Channel Name", "チャンネル名", "channel_name"])
    user_name_col = find_column(df, ["User Name", "ユーザー名", "user_name", "Name"])
    new_col = find_column(df, ["/newコマンド数", "/new", "new", "new command", "new command count"])
    docs_col = find_column(df, ["/docsコマンド数", "/docs", "docs", "docs command", "docs command count"])

    return all([user_id_col, channel_col, user_name_col, new_col, docs_col])


def load_hai_search_reports() -> pd.DataFrame:
    if not REPORT_DIR.exists():
        return pd.DataFrame()

    files = sorted(REPORT_DIR.glob("*.xlsx"), reverse=True)

    if not files:
        return pd.DataFrame()

    all_frames = []

    for file in files:
        try:
            excel_file = pd.ExcelFile(file)

            for sheet_name in excel_file.sheet_names:
                try:
                    df = pd.read_excel(file, sheet_name=sheet_name)
                    df.columns = [normalize_column_name(col) for col in df.columns]

                    if not sheet_has_usage_columns(df):
                        continue

                    df["Report File"] = file.name
                    df["Report Month"] = file.stem.replace("monthly_report_", "")
                    df["Report Sheet"] = sheet_name

                    all_frames.append(df)

                except Exception as sheet_error:
                    st.warning(f"Could not read {file.name} / {sheet_name}: {sheet_error}")

        except Exception as file_error:
            st.warning(f"Could not open {file.name}: {file_error}")

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
            "Report Sheet": raw_df.get("Report Sheet", ""),
            "User ID": raw_df[user_id_col].astype(str),
            "Channel Name": raw_df[channel_col].astype(str),
            "User Name": raw_df[user_name_col].astype(str),
            "/new": pd.to_numeric(raw_df[new_col], errors="coerce").fillna(0).astype(int),
            "/docs": pd.to_numeric(raw_df[docs_col], errors="coerce").fillna(0).astype(int),
        }
    )

    # Remove empty rows
    df = df[
        (df["User ID"].str.lower() != "nan")
        & (df["User ID"].str.strip() != "")
        & (df["Channel Name"].str.lower() != "nan")
        & (df["Channel Name"].str.strip() != "")
        & (df["User Name"].str.lower() != "nan")
        & (df["User Name"].str.strip() != "")
    ].copy()

    # Remove summary-like rows
    df = df[
        ~df["Channel Name"].str.lower().isin(["none", "total", "合計", "summary"])
    ].copy()

    df = df[
        ~df["User Name"].str.lower().isin(["none", "total", "合計", "summary"])
    ].copy()

    df["Total Commands"] = df["/new"] + df["/docs"]

    return df


# =========================
# Dashboard Helper
# =========================
def get_monthly_summary(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame()

    summary = (
        df.groupby("Report Month", as_index=False)
        .agg(
            New_Commands=("/new", "sum"),
            Docs_Commands=("/docs", "sum"),
            Total_Commands=("Total Commands", "sum"),
        )
        .sort_values("Report Month")
    )

    return summary


# =========================
# Portal Entries
# =========================
def render_portal_entries():
    html(
        """
        <div class="hai-section-header section-blue">
            <span class="hai-section-dot"></span>
            HAI Search Portal
        </div>
        <div class="hai-section-desc">
            Choose an entry below to start using or reviewing HAI Search.
        </div>
        """
    )

    col1, col2 = st.columns(2, gap="large")

    with col1:
        html(
            f"""
            <div class="portal-card portal-blue">
                <div class="portal-icon">🔎</div>
                <div class="portal-title">Search in Slack</div>
                <div class="portal-text">
                    Open Slack and use HAI Search through your available workspace and channel.
                    Use <b>/new</b> for questions and <b>/docs</b> for document search.
                </div>
                <a class="portal-button portal-button-blue" href="{SLACK_URL}" target="_blank">
                    🚀 Open Slack
                </a>
            </div>
            """
        )

    with col2:
        html(
            """
            <div class="portal-card portal-orange">
                <div class="portal-icon">📝</div>
                <div class="portal-title">Memo / Update Notes</div>
                <div class="portal-text">
                    Write and save HAI Search update history, known issues,
                    improvement ideas, and internal notes.
                </div>
                <a class="portal-button portal-button-orange" href="#hai-update-notes">
                    ✍️ Open Notes
                </a>
            </div>
            """
        )


# =========================
# Update Notes / Memo
# =========================
def load_update_notes() -> str:
    if UPDATE_NOTES_FILE.exists():
        return UPDATE_NOTES_FILE.read_text(encoding="utf-8")

    default_text = """# HAI Search Update Notes

## Latest Improvements
- Multiple Search function was added to search documents more precisely.
- Enhanced searching power to give more accurate answers.
- Error code documents were added to improve response quality for error-related questions.
- Japanese document handling and guidance can be updated here in the future.

## Known Issues
- 

## Future Enhancement Ideas
- 

## Memo
- 
"""
    UPDATE_NOTES_FILE.write_text(default_text, encoding="utf-8")
    return default_text


def save_update_notes(content: str):
    UPDATE_NOTES_FILE.write_text(content, encoding="utf-8")


def render_update_notes():
    html('<div id="hai-update-notes"></div>')

    html(
        """
        <div class="hai-section-header section-orange">
            <span class="hai-section-dot"></span>
            Memo / Update Notes
        </div>
        <div class="hai-section-desc">
            Record HAI Search version updates, known issues, future ideas, and internal notes here.
        </div>
        """
    )

    html(
        """
        <div class="update-box">
            <div class="update-title">Editable Update Notes</div>
            <div class="usage-tip">
                Use this area like a simple notebook.
                Write update history, issues, improvement ideas, or meeting notes, then click <b>Save Notes</b>.
            </div>
        </div>
        """
    )

    current_notes = load_update_notes()

    notes = st.text_area(
        "Update Notes Memo",
        value=current_notes,
        height=420,
        placeholder="Write HAI Search update notes here...",
        label_visibility="collapsed",
    )

    col1, col2 = st.columns([1, 4])

    with col1:
        if st.button("💾 Save Notes", use_container_width=True):
            save_update_notes(notes)
            st.success("Update Notes saved successfully.")

    with col2:
        st.caption(f"Saved file: `{UPDATE_NOTES_FILE}`")

    with st.expander("Preview Notes"):
        st.markdown(notes)


# =========================
# Management Dashboard
# =========================
def render_monthly_usage_report():
    html(
        """
        <div class="hai-section-header section-green">
            <span class="hai-section-dot"></span>
            HAI Search Management Dashboard
        </div>
        """
    )

    html(
        """
        <div class="report-intro">
            <div class="report-intro-title">Command Usage Dashboard</div>
            <div class="report-intro-text">
                Review HAI Search command usage trends, dealer channel activity,
                and monthly command volume. Monthly Excel files are read from
                <b>hai_search_reports/</b>.
            </div>
        </div>
        """
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

    months = sorted(df["Report Month"].dropna().unique())

    if not months:
        st.info("No month data found.")
        return

    latest_month = months[-1]
    previous_month = months[-2] if len(months) >= 2 else None

    monthly_summary = get_monthly_summary(df)

    latest_summary = monthly_summary[monthly_summary["Report Month"] == latest_month].iloc[0]

    if previous_month:
        previous_summary = monthly_summary[monthly_summary["Report Month"] == previous_month].iloc[0]
    else:
        previous_summary = None

    latest_total = int(latest_summary["Total_Commands"])
    latest_new = int(latest_summary["New_Commands"])
    latest_docs = int(latest_summary["Docs_Commands"])

    if previous_summary is not None:
        prev_total = int(previous_summary["Total_Commands"])
        prev_new = int(previous_summary["New_Commands"])
        prev_docs = int(previous_summary["Docs_Commands"])
    else:
        prev_total = 0
        prev_new = 0
        prev_docs = 0

    # =========================
    # Executive Summary
    # =========================
    html(
        """
        <div class="hai-section-header section-purple">
            <span class="hai-section-dot"></span>
            Executive Summary
        </div>
        """
    )

    c1, c2, c3, c4 = st.columns(4, gap="large")

    with c1:
        render_metric_card(
            title="Latest Month",
            value=latest_month,
            delta=None,
            icon="📅",
        )

    with c2:
        render_metric_card(
            title="Total Commands",
            value=format_number(latest_total),
            delta=get_delta_text(latest_total, prev_total),
            icon="📈",
        )

    with c3:
        render_metric_card(
            title="/new Commands",
            value=format_number(latest_new),
            delta=get_delta_text(latest_new, prev_new),
            icon="💬",
        )

    with c4:
        render_metric_card(
            title="/docs Commands",
            value=format_number(latest_docs),
            delta=get_delta_text(latest_docs, prev_docs),
            icon="📘",
        )

    st.caption(
        f"Comparison target: {previous_month if previous_month else 'No previous month available'}"
    )

    html(
        """
        <div class="dashboard-caption">
            Management view: monitor monthly command trends and top active dealer channels.
            User-count based indicators have been removed to keep the dashboard focused on command usage.
        </div>
        """
    )

    # =========================
    # Monthly Trend
    # =========================
    html('<div class="data-card-title">Monthly Usage Trend</div>')
    html(
        """
        <div class="data-card-subtitle">
            Monthly trend of /new, /docs, and total command volume.
        </div>
        """
    )

    trend_df = monthly_summary.rename(
        columns={
            "Report Month": "Month",
            "New_Commands": "/new",
            "Docs_Commands": "/docs",
            "Total_Commands": "Total Commands",
        }
    )

    st.line_chart(
        trend_df,
        x="Month",
        y=["/new", "/docs", "Total Commands"],
        use_container_width=True,
    )

    # =========================
    # Filter
    # =========================
    html('<div class="data-card-title">Monthly Detail Filter</div>')
    html(
        """
        <div class="data-card-subtitle">
            Select a month or search by dealer channel / user name to review command usage.
        </div>
        """
    )

    filter_col1, filter_col2 = st.columns([1, 2], gap="large")

    with filter_col1:
        selected_month = st.selectbox(
            "Select Month",
            options=["All"] + sorted(months, reverse=True),
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

    total_new = int(filtered_df["/new"].sum())
    total_docs = int(filtered_df["/docs"].sum())
    total_commands = int(filtered_df["Total Commands"].sum())

    fc1, fc2, fc3 = st.columns(3, gap="large")

    with fc1:
        render_metric_card(
            title="/new",
            value=format_number(total_new),
            icon="💬",
        )

    with fc2:
        render_metric_card(
            title="/docs",
            value=format_number(total_docs),
            icon="📘",
        )

    with fc3:
        render_metric_card(
            title="Total Commands",
            value=format_number(total_commands),
            icon="📊",
        )

    # =========================
    # Channel Ranking
    # =========================
    html('<div class="data-card-title">Top Dealer / Channel Ranking</div>')
    html(
        """
        <div class="data-card-subtitle">
            Ranking by total command count. This view focuses on channel activity, not user count.
        </div>
        """
    )

    channel_df = (
        filtered_df.groupby("Channel Name", as_index=False)
        .agg(
            New_Commands=("/new", "sum"),
            Docs_Commands=("/docs", "sum"),
            Total_Commands=("Total Commands", "sum"),
        )
        .sort_values("Total_Commands", ascending=False)
    )

    if channel_df.empty:
        st.info("No channel data to display.")
    else:
        top_channel_chart = channel_df.head(10).rename(
            columns={
                "Channel Name": "Channel",
                "Total_Commands": "Total Commands",
            }
        )

        st.bar_chart(
            top_channel_chart,
            x="Channel",
            y="Total Commands",
            use_container_width=True,
        )

        st.dataframe(
            channel_df.rename(
                columns={
                    "New_Commands": "/new",
                    "Docs_Commands": "/docs",
                    "Total_Commands": "Total Commands",
                }
            ),
            use_container_width=True,
            hide_index=True,
        )

    # =========================
    # Top 10 Users
    # =========================
    html('<div class="data-card-title">Top 10 Users by Total Commands</div>')
    html(
        """
        <div class="data-card-subtitle">
            This section shows who used HAI Search most actively based on total command count.
        </div>
        """
    )

    top_user_df = (
        filtered_df.groupby(["Channel Name", "User Name"], as_index=False)["Total Commands"]
        .sum()
        .sort_values("Total Commands", ascending=False)
        .head(10)
    )

    if top_user_df.empty:
        st.info("No user data to display.")
    else:
        top_user_df["User / Channel"] = (
            top_user_df["User Name"].astype(str)
            + " / "
            + top_user_df["Channel Name"].astype(str)
        )

        st.bar_chart(
            top_user_df,
            x="User / Channel",
            y="Total Commands",
            use_container_width=True,
        )

    # =========================
    # Usage Detail
    # =========================
    html('<div class="data-card-title">Usage Detail</div>')
    html(
        """
        <div class="data-card-subtitle">
            Detailed usage rows by month, channel, and user.
        </div>
        """
    )

    display_df = filtered_df[
        [
            "Report Month",
            "Channel Name",
            "User Name",
            "/new",
            "/docs",
            "Total Commands",
            "Report File",
            "Report Sheet",
        ]
    ].sort_values("Total Commands", ascending=False)

    st.dataframe(display_df, use_container_width=True, hide_index=True)

    with st.expander("Debug: loaded Excel data"):
        st.write("Loaded files:", raw_df["Report File"].dropna().unique().tolist())

        if "Report Sheet" in raw_df.columns:
            st.write("Loaded sheets:", raw_df["Report Sheet"].dropna().unique().tolist())

        st.write("Raw rows:", len(raw_df))
        st.write("Prepared rows:", len(df))
        st.dataframe(df.head(30), use_container_width=True)

    st.caption(
        "To update this dashboard, upload a new Excel file to `hai_search_reports/`, "
        "for example `monthly_report_2026-05.xlsx`."
    )


# =========================
# Main Render
# =========================
def render_hai_search():
    apply_css()

    render_hero()

    render_portal_entries()

    render_update_notes()

    render_monthly_usage_report()


# If this file is used as a standalone Streamlit page
if __name__ == "__main__":
    render_hai_search()
