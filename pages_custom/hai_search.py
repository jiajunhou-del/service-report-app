import streamlit as st
from pathlib import Path
import base64
import mimetypes
import pandas as pd
import textwrap
import re
import streamlit.components.v1 as components


# =========================
# Path / Link Settings
# =========================
BASE_DIR = Path(__file__).resolve().parents[1]
ASSETS_DIR = BASE_DIR / "assets"
REPORT_DIR = BASE_DIR / "hai_search_reports"

HAI_LOGO_PATH = ASSETS_DIR / "hai_search_logo.jpg.png"
SLACK_URL = "https://app.slack.com/"

# Accuracy Test Google Sheet
# ↓↓↓ ここにGoogle SheetのURLを入れてください
ACCURACY_TEST_SHEET_URL = "ここにGoogle SheetのURLを入れてください"

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


def extract_report_month(file_stem: str) -> str:
    match = re.search(r"(20\d{2}-\d{2})", file_stem)
    if match:
        return match.group(1)

    return file_stem.replace("monthly_report_", "")


# =========================
# CSS
# =========================
def apply_css():
    html(
        """
        <style>
        .debug-version-box {
            background: #eef6ff;
            border: 1px solid #bfdbfe;
            color: #1e3a8a;
            padding: 10px 14px;
            border-radius: 12px;
            font-size: 14px;
            font-weight: 800;
            margin-bottom: 16px;
        }

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

        .portal-card {
            border-radius: 26px;
            padding: 30px 32px;
            min-height: 245px;
            box-shadow: 0 10px 26px rgba(30, 50, 100, 0.06);
            margin-bottom: 14px;
        }

        .portal-blue {
            background: linear-gradient(180deg, #f7faff 0%, #ffffff 100%);
            border: 1px solid #d7e7ff;
        }

        .portal-orange {
            background: linear-gradient(180deg, #fff8f3 0%, #ffffff 100%);
            border: 1px solid #ffd9c7;
        }

        .portal-icon {
            width: 66px;
            height: 66px;
            border-radius: 18px;
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

        .accuracy-box {
            background: linear-gradient(180deg, #f6f5ff 0%, #ffffff 100%);
            border: 1px solid #ddd6fe;
            border-radius: 26px;
            padding: 28px 30px;
            box-shadow: 0 10px 26px rgba(109, 40, 217, 0.06);
            margin-bottom: 28px;
        }

        .accuracy-title {
            font-size: 26px;
            font-weight: 900;
            color: #3730a3;
            margin-bottom: 12px;
        }

        .accuracy-text {
            font-size: 15px;
            color: #5b5f75;
            line-height: 1.8;
            margin-bottom: 16px;
        }

        .path-box {
            margin-top: 14px;
            padding: 12px 14px;
            border-radius: 12px;
            background: #f8fafc;
            border: 1px solid #e5e7eb;
            color: #475569;
            font-size: 13px;
            line-height: 1.6;
            word-break: break-all;
        }

        .update-box {
            background: #fff8f3;
            border: 1px solid #ffd9c7;
            border-radius: 26px;
            padding: 28px 30px;
            box-shadow: 0 10px 26px rgba(122, 62, 29, 0.05);
            margin-bottom: 26px;
        }

        .update-title {
            font-size: 24px;
            font-weight: 900;
            color: #7a3e1d;
            margin-bottom: 16px;
        }

        .usage-tip {
            background: #fff9e8;
            border: 1px solid #ffe2a8;
            border-radius: 18px;
            padding: 16px 18px;
            color: #6b5a2b;
            font-size: 15px;
            line-height: 1.8;
            margin-top: 18px;
        }

        .report-intro {
            background: linear-gradient(180deg, #f4fbf8 0%, #ffffff 100%);
            border: 1px solid #cfebdd;
            border-radius: 26px;
            padding: 28px 30px;
            box-shadow: 0 10px 26px rgba(31, 92, 70, 0.05);
            margin-bottom: 22px;
        }

        .report-intro-title {
            font-size: 26px;
            font-weight: 900;
            color: #1f5c46;
            margin-bottom: 10px;
        }

        .report-intro-text {
            font-size: 15px;
            color: #5b7469;
            line-height: 1.8;
        }

        .data-card-title {
            font-size: 22px;
            font-weight: 900;
            color: #1f2a44;
            margin: 24px 0 12px 0;
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

        div[data-testid="stMetric"] {
            border-radius: 18px;
            padding: 18px 18px;
            border: 1px solid #e6edf7;
            box-shadow: 0 8px 18px rgba(30, 50, 100, 0.04);
            background: #ffffff;
        }

        div[data-testid="stMetricLabel"] {
            color: #667085;
            font-weight: 800;
        }

        div[data-testid="stMetricValue"] {
            color: #1f2a44;
            font-weight: 900;
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
    min-height: 280px;
    background:
        radial-gradient(circle at right center, rgba(212, 228, 240, 0.55), transparent 36%),
        linear-gradient(135deg, #26384f 0%, #405b78 46%, #7891aa 78%, #d9d7cf 100%);
    border-radius: 32px;
    padding: 40px 46px;
    box-shadow: 0 14px 30px rgba(31, 44, 63, 0.16);
}}

.hero-grid {{
    display: grid;
    grid-template-columns: 360px minmax(0, 1fr);
    gap: 44px;
    align-items: center;
}}

.logo-panel {{
    background: rgba(255, 255, 255, 0.13);
    border: 1px solid rgba(255, 255, 255, 0.20);
    border-radius: 28px;
    padding: 22px;
    min-height: 210px;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow:
        inset 0 1px 0 rgba(255, 255, 255, 0.14),
        0 10px 24px rgba(31, 44, 63, 0.14);
}}

.logo-box {{
    width: 100%;
    min-height: 170px;
    border-radius: 22px;
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
    background: rgba(255, 255, 255, 0.12);
    border: 1px solid rgba(255, 255, 255, 0.24);
    color: #ffffff;
    font-weight: 800;
    font-size: 14px;
    margin-bottom: 22px;
    backdrop-filter: blur(4px);
}}

.hero-text {{
    color: #ffffff;
    font-size: 19px;
    line-height: 1.9;
    font-weight: 650;
    max-width: 1080px;
    text-shadow: 0 1px 10px rgba(31, 44, 63, 0.16);
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
def sheet_has_usage_columns(df: pd.DataFrame) -> bool:
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
            report_month = extract_report_month(file.stem)

            for sheet_name in excel_file.sheet_names:
                try:
                    df = pd.read_excel(file, sheet_name=sheet_name)
                    df.columns = [normalize_column_name(col) for col in df.columns]

                    if not sheet_has_usage_columns(df):
                        continue

                    df["Report File"] = file.name
                    df["Report Month"] = report_month
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
            "User ID": raw_df[user_id_col].astype(str).str.strip(),
            "Channel Name": raw_df[channel_col].astype(str).str.strip(),
            "User Name": raw_df[user_name_col].astype(str).str.strip(),
            "/new": pd.to_numeric(raw_df[new_col], errors="coerce").fillna(0).astype(int),
            "/docs": pd.to_numeric(raw_df[docs_col], errors="coerce").fillna(0).astype(int),
        }
    )

    summary_words = [
        "",
        "none",
        "nan",
        "total",
        "grand total",
        "summary",
        "subtotal",
        "sum",
        "合計",
        "総計",
        "小計",
        "サマリー",
    ]

    for col in ["User ID", "Channel Name", "User Name"]:
        df = df[
            ~df[col].str.strip().str.lower().isin(summary_words)
        ].copy()

        df = df[
            ~df[col].str.contains(
                r"合計|総計|小計|total|grand total|summary|subtotal|sum",
                case=False,
                na=False,
                regex=True,
            )
        ].copy()

    df = df[
        ~((df["/new"] == 0) & (df["/docs"] == 0))
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
            Unique_Users=("User ID", "nunique"),
            New_Commands=("/new", "sum"),
            Docs_Commands=("/docs", "sum"),
            Total_Commands=("Total Commands", "sum"),
        )
        .sort_values("Report Month")
    )

    return summary


def get_delta_text(current_value: int, previous_value: int) -> str:
    if previous_value == 0:
        if current_value == 0:
            return "0%"
        return "New"

    growth = ((current_value - previous_value) / previous_value) * 100
    return f"{growth:+.1f}%"


def classify_user_activity(total_commands: int) -> str:
    if total_commands >= 10:
        return "Heavy Users"
    if total_commands >= 3:
        return "Regular Users"
    if total_commands >= 1:
        return "Light Users"
    return "No Activity"


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
# Accuracy Test Sheet
# =========================
def render_accuracy_test_sheet():
    html(
        """
        <div class="hai-section-header section-purple">
            <span class="hai-section-dot"></span>
            HAI Search Accuracy Test
        </div>
        <div class="hai-section-desc">
            Open the Google Sheet for HAI Search accuracy test, including test questions, result records, and issue tracking.
        </div>
        """
    )

    html(
        """
        <div class="accuracy-box">
            <div class="accuracy-title">✅ Accuracy Test Sheet</div>
            <div class="accuracy-text">
                Open the Google Sheet used for HAI Search accuracy testing.
                This sheet can be used to manage test questions, answer results, issue types, and accuracy rate.
            </div>
        </div>
        """
    )

    if ACCURACY_TEST_SHEET_URL.startswith("http"):
        st.link_button(
            "📊 Open Accuracy Test Sheet",
            ACCURACY_TEST_SHEET_URL,
            use_container_width=False,
        )
        st.caption("This button opens the shared Google Sheet in your browser.")
        st.code(ACCURACY_TEST_SHEET_URL, language="text")
    else:
        st.warning("Google Sheet URL is not set yet. Please update ACCURACY_TEST_SHEET_URL in the script.")
        st.code('ACCURACY_TEST_SHEET_URL = "https://docs.google.com/spreadsheets/d/xxxxx/edit?usp=sharing"', language="python")


# =========================
# Update Notes / Memo
# =========================
def load_update_notes() -> str:
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

    try:
        if UPDATE_NOTES_FILE.exists():
            return UPDATE_NOTES_FILE.read_text(encoding="utf-8")

        UPDATE_NOTES_FILE.write_text(default_text, encoding="utf-8")
        return default_text

    except Exception:
        return default_text


def save_update_notes(content: str) -> bool:
    try:
        UPDATE_NOTES_FILE.write_text(content, encoding="utf-8")
        return True
    except Exception as e:
        st.error(f"Could not save notes: {e}")
        return False


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
                This area can be used like a simple notebook.
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
        key="hai_search_update_notes_area",
    )

    col1, col2 = st.columns([1, 4])

    with col1:
        if st.button("💾 Save Notes", use_container_width=True, key="save_hai_search_notes"):
            if save_update_notes(notes):
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
            <div class="report-intro-title">Executive Usage Dashboard</div>
            <div class="report-intro-text">
                Review HAI Search usage trends, active users, dealer channel activity,
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
        st.info("No valid usage data found after removing summary rows.")
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
    latest_users = int(latest_summary["Unique_Users"])
    latest_new = int(latest_summary["New_Commands"])

    if previous_summary is not None:
        prev_total = int(previous_summary["Total_Commands"])
        prev_users = int(previous_summary["Unique_Users"])
        prev_new = int(previous_summary["New_Commands"])
    else:
        prev_total = 0
        prev_users = 0
        prev_new = 0

    html(
        """
        <div class="hai-section-header section-purple">
            <span class="hai-section-dot"></span>
            Executive Summary
        </div>
        """
    )

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    kpi1.metric("Latest Month", latest_month)
    kpi2.metric("Total Commands", latest_total, delta=get_delta_text(latest_total, prev_total))
    kpi3.metric("Unique Users", latest_users, delta=get_delta_text(latest_users, prev_users))
    kpi4.metric("/new Commands", latest_new, delta=get_delta_text(latest_new, prev_new))

    st.caption(
        f"Comparison target: {previous_month if previous_month else 'No previous month available'}"
    )

    html(
        """
        <div class="dashboard-caption">
            Management view: monitor monthly usage trend, top active channels, and user engagement level.
        </div>
        """
    )

    html('<div class="data-card-title">Monthly Usage Trend</div>')

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

    html('<div class="data-card-title">Monthly Detail Filter</div>')

    filter_col1, filter_col2 = st.columns([1, 2])

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

    total_users = filtered_df["User ID"].nunique()
    total_new = int(filtered_df["/new"].sum())
    total_docs = int(filtered_df["/docs"].sum())
    total_commands = int(filtered_df["Total Commands"].sum())

    k1, k2, k3, k4 = st.columns(4)

    k1.metric("Unique Users", total_users)
    k2.metric("/new", total_new)
    k3.metric("/docs", total_docs)
    k4.metric("Total Commands", total_commands)

    html('<div class="data-card-title">Top Dealer / Channel Ranking</div>')

    channel_df = (
        filtered_df.groupby("Channel Name", as_index=False)
        .agg(
            Unique_Users=("User ID", "nunique"),
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
                    "Unique_Users": "Unique Users",
                    "New_Commands": "/new",
                    "Docs_Commands": "/docs",
                    "Total_Commands": "Total Commands",
                }
            ),
            use_container_width=True,
            hide_index=True,
        )

    html('<div class="data-card-title">User Activity Level</div>')

    user_activity_df = (
        filtered_df.groupby(["User ID", "User Name", "Channel Name"], as_index=False)
        .agg(
            New_Commands=("/new", "sum"),
            Docs_Commands=("/docs", "sum"),
            Total_Commands=("Total Commands", "sum"),
        )
    )

    user_activity_df["Activity Level"] = user_activity_df["Total_Commands"].apply(
        classify_user_activity
    )

    activity_summary = (
        user_activity_df.groupby("Activity Level", as_index=False)
        .agg(Users=("User ID", "nunique"))
    )

    level_order = ["Heavy Users", "Regular Users", "Light Users", "No Activity"]
    activity_summary["Activity Level"] = pd.Categorical(
        activity_summary["Activity Level"],
        categories=level_order,
        ordered=True,
    )

    activity_summary = activity_summary.sort_values("Activity Level")

    if activity_summary.empty:
        st.info("No activity data to display.")
    else:
        st.bar_chart(
            activity_summary,
            x="Activity Level",
            y="Users",
            use_container_width=True,
        )

    with st.expander("Activity level definition"):
        st.markdown(
            """
            - **Heavy Users**: 10 or more commands
            - **Regular Users**: 3 to 9 commands
            - **Light Users**: 1 to 2 commands
            - **No Activity**: 0 command
            """
        )

    html('<div class="data-card-title">Top 10 Users by Total Commands</div>')

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

    html('<div class="data-card-title">Usage Detail</div>')

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

        st.write("Raw rows before cleaning:", len(raw_df))
        st.write("Prepared rows after cleaning:", len(df))

        debug_summary = get_monthly_summary(df).rename(
            columns={
                "Unique_Users": "Unique Users",
                "New_Commands": "/new",
                "Docs_Commands": "/docs",
                "Total_Commands": "Total Commands",
            }
        )

        st.write("Monthly summary after removing total rows:")
        st.dataframe(debug_summary, use_container_width=True, hide_index=True)

    st.caption(
        "To update this dashboard, upload a new Excel file to `hai_search_reports/`, "
        "for example `monthly_report_2026-05.xlsx`."
    )


# =========================
# Main Render
# =========================
def render_hai_search():
    apply_css()

    html(
        """
        <div class="debug-version-box">
            HAI Search page loaded: Google Sheet Accuracy Test Version
        </div>
        """
    )

    render_hero()
    render_portal_entries()
    render_accuracy_test_sheet()
    render_update_notes()
    render_monthly_usage_report()


if __name__ == "__main__":
    render_hai_search()
