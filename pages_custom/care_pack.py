import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import pandas as pd
import re
import base64
import html


# =========================
# Care Pack Settings
# =========================
CAREPACK_DIR = Path("carepack_bulletins")
ASSET_DIR = Path("assets")
CAREPACK_IMAGE = ASSET_DIR / "carepack.png"
TARGET_MODELS = 60

PROGRESS_SHEET_URL = (
    "https://docs.google.com/spreadsheets/d/"
    "1thjeBf37HlxTTtW_etUJS1ZIiv7ZwCptBvOoL0th-rU/edit?usp=sharing"
)


# =========================
# CSS
# =========================
def apply_care_pack_css():
    st.markdown(
        """
<style>
.block-container {
    padding-top: 1.6rem;
}

/* =========================
   Overall Theme
========================= */
:root {
    --cp-navy: #0f172a;
    --cp-blue: #2563eb;
    --cp-blue-light: #eff6ff;
    --cp-border: #dbe3ef;
    --cp-text: #1e293b;
    --cp-muted: #64748b;
    --cp-bg: #f8fafc;
}

/* =========================
   Hero - Management Dashboard Style
========================= */
.carepack-hero {
    padding: 34px 40px;
    border-radius: 28px;
    background:
        linear-gradient(135deg, #ffffff 0%, #f8fbff 48%, #eef5ff 100%);
    color: #0f172a;
    box-shadow: 0 14px 36px rgba(15,23,42,0.08);
    border: 1px solid #dbeafe;
    margin-bottom: 22px;
    display: grid;
    grid-template-columns: minmax(0, 1fr) 320px;
    align-items: center;
    gap: 34px;
    min-height: 230px;
    position: relative;
    overflow: hidden;
}

.carepack-hero::before {
    content: "";
    position: absolute;
    left: 0;
    top: 0;
    width: 9px;
    height: 100%;
    background: linear-gradient(180deg, #1d4ed8 0%, #60a5fa 100%);
}

.carepack-hero::after {
    content: "";
    position: absolute;
    right: -70px;
    top: -80px;
    width: 240px;
    height: 240px;
    background: rgba(37,99,235,0.08);
    border-radius: 999px;
}

.carepack-hero-text,
.carepack-hero-image-wrap {
    position: relative;
    z-index: 1;
}

.carepack-hero-badge {
    display: inline-flex;
    align-items: center;
    padding: 7px 13px;
    border-radius: 999px;
    background: #eff6ff;
    border: 1px solid #bfdbfe;
    color: #1d4ed8;
    font-size: 12px;
    font-weight: 900;
    margin-bottom: 14px;
    letter-spacing: 0.02em;
}

.carepack-hero-title {
    font-size: 44px;
    font-weight: 950;
    margin-bottom: 12px;
    letter-spacing: -0.04em;
    line-height: 1.05;
    color: #0f172a;
}

.carepack-hero-subtitle {
    font-size: 15px;
    color: #475569;
    line-height: 1.8;
    max-width: 860px;
}

.carepack-hero-image-wrap {
    width: 310px;
    height: 190px;
    border-radius: 24px;
    background: #ffffff;
    border: 1px solid #dbeafe;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    box-shadow: 0 10px 26px rgba(15,23,42,0.08);
    padding: 14px;
}

.carepack-hero-image {
    width: 100%;
    height: 100%;
    object-fit: contain;
    border-radius: 18px;
}

.carepack-hero-fallback {
    font-size: 76px;
}

/* =========================
   Summary Cards
========================= */
.cp-summary-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 14px;
    margin-bottom: 18px;
}

.cp-summary-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 18px;
    padding: 17px 18px;
    box-shadow: 0 8px 20px rgba(15,23,42,0.04);
}

.cp-summary-label {
    font-size: 12px;
    font-weight: 850;
    color: #64748b;
    margin-bottom: 8px;
}

.cp-summary-value {
    font-size: 27px;
    font-weight: 950;
    color: #0f172a;
    line-height: 1;
}

.cp-summary-note {
    font-size: 12px;
    color: #64748b;
    margin-top: 8px;
}

/* =========================
   Search Panel
========================= */
.search-wrap {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 18px;
    padding: 16px 16px 10px 16px;
    box-shadow: 0 8px 18px rgba(15,23,42,0.04);
    margin-bottom: 14px;
}

/* =========================
   Info Message
========================= */
.carepack-info-box {
    background: #f8fbff;
    border: 1px solid #dbeafe;
    border-left: 6px solid #2563eb;
    border-radius: 16px;
    padding: 14px 17px;
    color: #1e40af;
    font-size: 14px;
    font-weight: 750;
    margin: 14px 0 16px 0;
}

/* =========================
   Section Header
========================= */
.table-header-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-left: 6px solid #2563eb;
    border-radius: 18px;
    padding: 16px 18px;
    margin: 18px 0 12px 0;
    box-shadow: 0 8px 18px rgba(15,23,42,0.04);
}

.table-header-title {
    font-size: 19px;
    font-weight: 950;
    color: #0f172a;
    margin-bottom: 4px;
}

.table-header-subtitle {
    font-size: 13px;
    color: #64748b;
    line-height: 1.5;
}

/* =========================
   Custom Care Pack Table
========================= */
.carepack-table-wrap {
    width: 100%;
    border-radius: 18px;
    overflow: hidden;
    border: 1px solid #dbe3ef;
    box-shadow: 0 10px 24px rgba(15,23,42,0.05);
    background: white;
    margin-bottom: 22px;
}

.carepack-table-scroll {
    width: 100%;
    max-height: 450px;
    overflow: auto;
}

.carepack-table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    font-size: 14px;
}

.carepack-table thead th {
    position: sticky;
    top: 0;
    z-index: 2;
    background: #1e3a8a;
    color: #ffffff;
    text-align: left;
    padding: 13px 14px;
    font-weight: 900;
    border-right: 1px solid rgba(255,255,255,0.18);
    white-space: nowrap;
}

.carepack-table thead th:last-child {
    border-right: none;
}

.carepack-table tbody td {
    padding: 12px 14px;
    border-bottom: 1px solid #edf2f7;
    border-right: 1px solid #f1f5f9;
    color: #334155;
    vertical-align: middle;
    background: #ffffff;
}

.carepack-table tbody tr:nth-child(even) td {
    background: #f8fafc;
}

.carepack-table tbody tr:hover td {
    background: #eff6ff;
}

.carepack-table tbody td:last-child {
    border-right: none;
}

.carepack-model-cell {
    font-weight: 850;
    color: #1d4ed8 !important;
}

.carepack-machine-cell {
    font-weight: 700;
    color: #0f172a !important;
}

.bulletin-badge {
    display: inline-block;
    padding: 5px 10px;
    border-radius: 999px;
    background: #eff6ff;
    color: #1d4ed8;
    font-size: 12px;
    font-weight: 850;
    border: 1px solid #bfdbfe;
    white-space: nowrap;
}

.date-badge {
    display: inline-block;
    padding: 5px 10px;
    border-radius: 999px;
    background: #f8fafc;
    color: #475569;
    font-size: 12px;
    font-weight: 800;
    border: 1px solid #e2e8f0;
    white-space: nowrap;
}

.file-name-cell {
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", monospace;
    font-size: 13px;
    color: #475569 !important;
}

/* =========================
   Metric Cards in Result
========================= */
div[data-testid="stMetric"] {
    background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%);
    border: 1px solid #e2e8f0;
    padding: 14px 16px;
    border-radius: 16px;
    box-shadow: 0 6px 16px rgba(15,23,42,0.04);
}

div[data-testid="stMetricLabel"] {
    color: #64748b;
    font-weight: 800;
}

div[data-testid="stMetricValue"] {
    color: #0f172a;
    font-weight: 950;
    font-size: 19px;
}

/* =========================
   Tags / Result
========================= */
.carepack-pill {
    display: inline-block;
    padding: 8px 15px;
    border-radius: 999px;
    background: #eff6ff;
    color: #1d4ed8;
    font-size: 13px;
    font-weight: 900;
    text-align: center;
    margin-top: 6px;
    border: 1px solid #bfdbfe;
}

.result-title {
    font-size: 24px;
    font-weight: 950;
    color: #0f172a;
    margin-bottom: 4px;
}

.result-file {
    color: #64748b;
    font-size: 13px;
    font-weight: 700;
}

.stButton > button,
.stDownloadButton > button {
    border-radius: 12px !important;
    font-weight: 700 !important;
}

/* =========================
   Responsive
========================= */
@media (max-width: 900px) {
    .carepack-hero {
        grid-template-columns: 1fr;
        padding: 28px 24px;
        min-height: auto;
    }

    .carepack-hero-image-wrap {
        width: 100%;
        height: 230px;
    }

    .carepack-hero-title {
        font-size: 38px;
    }

    .cp-summary-grid {
        grid-template-columns: 1fr;
    }
}
</style>
        """,
        unsafe_allow_html=True,
    )


# =========================
# Text / PDF Helper Functions
# =========================
def image_to_base64(image_path: Path) -> str:
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


def normalize_spaces(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def clean_text_value(text: str) -> str:
    text = text.strip()
    text = text.strip(" .,:;/-")
    text = re.sub(r"\s{2,}", " ", text)
    return text


def get_machine_prefix(machine_name: str) -> str:
    machine_name = machine_name.strip()
    match = re.match(r"^([A-Z]+-?[A-Z]*)(?=\d)", machine_name, flags=re.IGNORECASE)

    if match:
        return match.group(1)

    return ""


def expand_slash_machine_name(machine_text: str) -> str:
    machine_text = clean_text_value(machine_text)
    machine_text = re.sub(r"\s*/\s*", "/", machine_text)

    if "/" not in machine_text:
        return machine_text

    parts = [part.strip() for part in machine_text.split("/") if part.strip()]

    if not parts:
        return machine_text

    first = parts[0]
    prefix = get_machine_prefix(first)
    expanded = [first]

    for part in parts[1:]:
        if get_machine_prefix(part):
            expanded.append(part)
        else:
            expanded.append(prefix + part)

    return " / ".join(expanded)


def normalize_machine_separator(text: str) -> str:
    text = clean_text_value(text)
    text = re.sub(r"\s+and\s+", " / ", text, flags=re.IGNORECASE)
    text = re.sub(r"\s+＆\s+", " / ", text)
    text = re.sub(r"\s*&\s*", " / ", text)
    text = re.sub(r"\s*,\s*", " / ", text)
    text = re.sub(r"\s{2,}", " ", text)

    groups = [group.strip() for group in re.split(r"\s*/\s*", text) if group.strip()]

    if len(groups) >= 2:
        joined = "/".join(groups)
        return expand_slash_machine_name(joined)

    return text.strip()


def is_bulletin_code_like(value: str) -> bool:
    value = value.strip()

    if re.match(r"^[A-Z]{1,6}[0-9]{6,12}-[0-9A-Z]+$", value, flags=re.IGNORECASE):
        return True

    return False


def looks_like_machine_value(value: str) -> bool:
    value = clean_text_value(value)

    if not value:
        return False

    if len(value) > 120:
        return False

    low = value.lower()

    ng_words = [
        "carepack",
        "information bulletin",
        "product release information",
        "spare parts",
        "downtime",
        "release of the",
        "this bulletin informs you",
        "included",
        "includes",
        "most frequent",
        "machine will help",
    ]

    if any(word in low for word in ng_words):
        return False

    if is_bulletin_code_like(value):
        return False

    if re.fullmatch(r"[A-Z0-9][A-Z0-9\-\/\s\.]+", value, flags=re.IGNORECASE):
        return True

    if re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9\s\-\/\.]+", value):
        return True

    return False


def extract_machine_candidates(raw_text: str):
    raw_text = normalize_spaces(raw_text)

    patterns = [
        r"[A-Z]{1,10}-?[A-Z]*\d{1,5}[A-Z0-9]*"
        r"(?:\s*/\s*(?:[A-Z]{1,10}-?[A-Z]*)?\d{1,5}[A-Z0-9]*)*",
        r"[A-Z]{2,10}-[A-Z]{1,10}"
        r"(?:\s*/\s*[A-Z]{2,10}-[A-Z]{1,10})*",
    ]

    candidates = []

    for pattern in patterns:
        matches = re.findall(pattern, raw_text, flags=re.IGNORECASE)

        for candidate in matches:
            candidate = clean_text_value(candidate)

            if not candidate:
                continue

            if is_bulletin_code_like(candidate):
                continue

            if candidate not in candidates:
                candidates.append(candidate)

    return candidates


def extract_target_machine_from_text(page_text: str, fallback_machine: str) -> str:
    text = normalize_spaces(page_text)

    def finalize_candidate_list(machine_candidates):
        normalized_list = [
            normalize_machine_separator(candidate)
            for candidate in machine_candidates
            if candidate and not is_bulletin_code_like(candidate)
        ]

        value = " / ".join(normalized_list)
        value = re.sub(r"\s*/\s*", " / ", value)
        value = re.sub(r"\s{2,}", " ", value).strip()

        if value and len(value) <= 150:
            return value

        return None

    carepack_for_match = re.search(
        r"\(Carepack\)\s+for\s+(.+?)(?:\.|\s+It\s+is|\s+This\s+is|\s+which\s+|$)",
        text,
        flags=re.IGNORECASE,
    )

    if carepack_for_match:
        raw_value = carepack_for_match.group(1).strip()
        machine_candidates = extract_machine_candidates(raw_value)

        if machine_candidates:
            value = finalize_candidate_list(machine_candidates)
            if value:
                return value

        direct_value = normalize_machine_separator(raw_value)
        if looks_like_machine_value(direct_value):
            return direct_value

    for_match = re.search(
        r"\bfor\s+(.+?)(?:\.|\s+It\s+is|\s+This\s+is|\s+which\s+|\s+includes|\s+with\s+the|$)",
        text,
        flags=re.IGNORECASE,
    )

    if for_match:
        raw_value = for_match.group(1).strip()

        raw_value = re.split(
            r"\s+(?:and\s+it|which|that|including|includes|with|for\s+the)\s+",
            raw_value,
            flags=re.IGNORECASE,
        )[0].strip()

        machine_candidates = extract_machine_candidates(raw_value)

        if machine_candidates:
            value = finalize_candidate_list(machine_candidates)
            if value:
                return value

        direct_value = normalize_machine_separator(raw_value)
        if looks_like_machine_value(direct_value):
            return direct_value

    label_patterns = [
        r"\bApplicable\s+models?\s*:\s*(.*?)(?:\s+Subject\b|\s+Date\s*:|\s+Title\s*:|\s+Code\s*:|\s+Ref\s*No\.?\s*:|$)",
        r"\bModels?\s*:\s*(.*?)(?:\s+Subject\b|\s+Date\s*:|\s+Title\s*:|\s+Code\s*:|\s+Ref\s*No\.?\s*:|$)",
        r"\bMachine\s*:\s*(.*?)(?:\s+Subject\b|\s+Date\s*:|\s+Title\s*:|\s+Code\s*:|\s+Ref\s*No\.?\s*:|$)",
        r"\bModel\s*:\s*(.*?)(?:\s+Subject\b|\s+Date\s*:|\s+Title\s*:|\s+Code\s*:|\s+Ref\s*No\.?\s*:|$)",
    ]

    for pattern in label_patterns:
        match = re.search(pattern, text, re.IGNORECASE)

        if match:
            value = normalize_machine_separator(match.group(1))
            value = value.replace("-CRP", "")
            value = clean_text_value(value)

            if looks_like_machine_value(value):
                return value

    return fallback_machine


def extract_pdf_info(pdf_path: Path):
    date_value = "-"
    bulletin_code = "-"

    fallback_model = pdf_path.stem

    if fallback_model.startswith("IB_"):
        fallback_model = fallback_model[3:]

    fallback_machine = fallback_model.replace("-CRP", "")
    machine_value = fallback_machine

    try:
        import fitz

        with fitz.open(pdf_path) as doc:
            if len(doc) == 0:
                return date_value, bulletin_code, machine_value

            page_text = doc.load_page(0).get_text()
            text_one_line = normalize_spaces(page_text)

            date_patterns = [
                r"Date\s*:\s*(.*?)(?:\s+Title\s*:|\s+Code\s*:|\s+Ref\s*No\.?\s*:|\s+Model\s*:|\s+Machine\s*:|$)",
                r"Issued\s+on\s*:\s*(.*?)(?:\s+Title\s*:|\s+Code\s*:|\s+Ref\s*No\.?\s*:|\s+Model\s*:|\s+Machine\s*:|$)",
            ]

            for pattern in date_patterns:
                match = re.search(pattern, text_one_line, re.IGNORECASE)

                if match:
                    candidate = clean_text_value(match.group(1))
                    if candidate:
                        date_value = candidate
                        break

            code_patterns = [
                r"Bulletin\s*Code\s*:\s*([A-Z0-9\-]+)",
                r"Carepack\s*Code\s*:\s*([A-Z0-9\-]+)",
                r"Ref\s*No\.?\s*:\s*([A-Z0-9\-]+)",
                r"Code\s*:\s*([A-Z]{1,6}[0-9]{4,12}(?:-[0-9A-Z]+)?)",
            ]

            for pattern in code_patterns:
                match = re.search(pattern, text_one_line, re.IGNORECASE)

                if match:
                    candidate = clean_text_value(match.group(1))
                    if candidate:
                        bulletin_code = candidate
                        break

            machine_value = extract_target_machine_from_text(page_text, fallback_machine)

    except Exception:
        machine_value = fallback_machine

    return date_value, bulletin_code, machine_value


def get_folder_mtime() -> float:
    if not CAREPACK_DIR.exists():
        return 0.0

    latest = CAREPACK_DIR.stat().st_mtime

    for file in CAREPACK_DIR.glob("*.pdf"):
        latest = max(latest, file.stat().st_mtime)

    return latest


def build_carepack_data(folder_mtime: float):
    data = []

    if not CAREPACK_DIR.exists():
        return data

    pdf_files = sorted(CAREPACK_DIR.glob("*.pdf"))

    for pdf_file in pdf_files:
        file_name = pdf_file.name
        model = pdf_file.stem

        if model.startswith("IB_"):
            model = model[3:]

        date_value, bulletin_code, machine = extract_pdf_info(pdf_file)

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


def search_carepack(data, keyword: str, show_all: bool):
    keyword = keyword.lower().strip()

    if show_all and not keyword:
        return data

    if not keyword:
        return []

    results = []

    for item in data:
        search_target = " ".join(
            [
                str(item.get("model", "")),
                str(item.get("machine", "")),
                str(item.get("bulletin_code", "")),
                str(item.get("date", "")),
                str(item.get("file", "")),
            ]
        ).lower()

        if keyword in search_target:
            results.append(item)

    return results


def show_pdf_preview(pdf_path: Path, max_pages: int = 5):
    try:
        import fitz

        with fitz.open(pdf_path) as doc:
            total_pages = len(doc)
            preview_pages = min(total_pages, max_pages)

            if total_pages > max_pages:
                st.caption(f"Showing first {max_pages} pages only. Total pages: {total_pages}")

            for page_number in range(preview_pages):
                page = doc.load_page(page_number)
                pix = page.get_pixmap(matrix=fitz.Matrix(1.5, 1.5), alpha=False)
                image_bytes = pix.tobytes("png")

                st.image(
                    image_bytes,
                    caption=f"Page {page_number + 1}",
                    use_container_width=True,
                )

    except Exception as e:
        st.error(f"PDF preview failed: {e}")


# =========================
# Render Parts
# =========================
def render_carepack_hero():
    image_src = image_to_base64(CAREPACK_IMAGE)

    if image_src:
        image_html = f"""
<div class="carepack-hero-image-wrap">
    <img class="carepack-hero-image" src="{image_src}" alt="Care Pack image">
</div>
"""
    else:
        image_html = """
<div class="carepack-hero-image-wrap">
    <div class="carepack-hero-fallback">📦</div>
</div>
"""

    hero_html = f"""
<div class="carepack-hero">
    <div class="carepack-hero-text">
        <div class="carepack-hero-badge">SERVICE DATA PORTAL · CARE PACK</div>
        <div class="carepack-hero-title">Care Pack</div>
        <div class="carepack-hero-subtitle">
            Search, preview, and download Care Pack Information Bulletins.<br>
            Search by Care Pack model, target machine, file name, Bulletin Code, or Date.
            New PDFs will be displayed automatically after being uploaded to the carepack_bulletins folder.
        </div>
    </div>
    {image_html}
</div>
"""
    st.markdown(hero_html, unsafe_allow_html=True)


def render_summary_cards(carepack_data):
    current_count = len(carepack_data)

    if TARGET_MODELS <= 0:
        percent = 0
        remaining = 0
    else:
        percent = round((current_count / TARGET_MODELS) * 100)
        remaining = max(TARGET_MODELS - current_count, 0)

    summary_html = f"""
<div class="cp-summary-grid">
    <div class="cp-summary-card">
        <div class="cp-summary-label">Uploaded Bulletins</div>
        <div class="cp-summary-value">{current_count}</div>
        <div class="cp-summary-note">PDF files currently available</div>
    </div>
    <div class="cp-summary-card">
        <div class="cp-summary-label">Completion Rate</div>
        <div class="cp-summary-value">{percent}%</div>
        <div class="cp-summary-note">{current_count} / {TARGET_MODELS} models completed</div>
    </div>
    <div class="cp-summary-card">
        <div class="cp-summary-label">Remaining Models</div>
        <div class="cp-summary-value">{remaining}</div>
        <div class="cp-summary-note">Models remaining to target</div>
    </div>
</div>
"""
    st.markdown(summary_html, unsafe_allow_html=True)


def render_table_header(total_count: int):
    table_header_html = f"""
<div class="table-header-card">
    <div class="table-header-title">Care Pack Bulletin List</div>
    <div class="table-header-subtitle">
        Uploaded bulletin overview: <b>{total_count}</b> files. 
        Search by model, machine, Bulletin Code, date, or file name.
    </div>
</div>
"""
    st.markdown(table_header_html, unsafe_allow_html=True)


def render_carepack_table(carepack_data):
    render_table_header(len(carepack_data))

    rows_html = ""

    for item in carepack_data:
        model = html.escape(str(item.get("model", "")))
        machine = html.escape(str(item.get("machine", "")))
        bulletin_code = html.escape(str(item.get("bulletin_code", "")))
        date = html.escape(str(item.get("date", "")))
        file_name = html.escape(str(item.get("file", "")))

        rows_html += f"""
<tr>
    <td class="carepack-model-cell">{model}</td>
    <td class="carepack-machine-cell">{machine}</td>
    <td><span class="bulletin-badge">{bulletin_code}</span></td>
    <td><span class="date-badge">{date}</span></td>
    <td class="file-name-cell">{file_name}</td>
</tr>
"""

    table_html = f"""
<div class="carepack-table-wrap">
    <div class="carepack-table-scroll">
        <table class="carepack-table">
            <thead>
                <tr>
                    <th>Care Pack Model</th>
                    <th>Machine</th>
                    <th>Bulletin Code</th>
                    <th>Date</th>
                    <th>File Name</th>
                </tr>
            </thead>
            <tbody>
                {rows_html}
            </tbody>
        </table>
    </div>
</div>
"""

    st.markdown(table_html, unsafe_allow_html=True)


def render_carepack_progress(data):
    current_count = len(data)

    if TARGET_MODELS <= 0:
        percent = 0
        progress_ratio = 0.0
    else:
        percent = round((current_count / TARGET_MODELS) * 100)
        progress_ratio = min(current_count / TARGET_MODELS, 1.0)

    fill_width = round(progress_ratio * 100)
    remaining = max(TARGET_MODELS - current_count, 0)

    if percent >= 80:
        status_text = "On Track"
        status_bg = "#dcfce7"
        status_color = "#166534"
        status_border = "#86efac"
    else:
        status_text = "In Progress"
        status_bg = "#eff6ff"
        status_color = "#1d4ed8"
        status_border = "#bfdbfe"

    progress_html = f"""
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

.progress-card {{
    box-sizing: border-box;
    width: 100%;
    background: #ffffff;
    border-radius: 22px;
    padding: 24px 26px;
    color: #0f172a;
    position: relative;
    overflow: hidden;
    border: 1px solid #dbe3ef;
    box-shadow: 0 10px 24px rgba(15,23,42,0.06);
}}

.progress-card::before {{
    content: "";
    position: absolute;
    left: 0;
    top: 0;
    height: 100%;
    width: 7px;
    background: linear-gradient(180deg, #1d4ed8 0%, #60a5fa 100%);
}}

.progress-inner {{
    position: relative;
    z-index: 1;
}}

.progress-top-row {{
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 18px;
    margin-bottom: 18px;
}}

.progress-title {{
    font-size: 21px;
    font-weight: 900;
    margin-bottom: 7px;
    color: #0f172a;
}}

.progress-subtitle {{
    font-size: 13px;
    color: #64748b;
    line-height: 1.6;
}}

.progress-percent {{
    min-width: 112px;
    text-align: center;
    padding: 12px 16px;
    border-radius: 18px;
    background: #eff6ff;
    border: 1px solid #bfdbfe;
}}

.progress-percent-number {{
    font-size: 32px;
    font-weight: 950;
    line-height: 1;
    color: #1d4ed8;
}}

.progress-percent-label {{
    font-size: 12px;
    color: #64748b;
    margin-top: 5px;
    font-weight: 750;
}}

.progress-bar-bg {{
    width: 100%;
    height: 14px;
    border-radius: 999px;
    background: #e2e8f0;
    overflow: hidden;
    margin: 18px 0 16px 0;
}}

.progress-bar-fill {{
    height: 100%;
    width: {fill_width}%;
    border-radius: 999px;
    background: linear-gradient(90deg, #1d4ed8 0%, #60a5fa 100%);
}}

.progress-bottom-row {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 16px;
    flex-wrap: wrap;
}}

.progress-count {{
    font-size: 18px;
    font-weight: 900;
    color: #0f172a;
}}

.progress-target {{
    font-size: 13px;
    color: #64748b;
    margin-top: 4px;
}}

.progress-status {{
    display: inline-flex;
    align-items: center;
    padding: 8px 13px;
    border-radius: 999px;
    background: {status_bg};
    color: {status_color};
    border: 1px solid {status_border};
    font-size: 13px;
    font-weight: 850;
}}

@media (max-width: 700px) {{
    .progress-top-row {{
        flex-direction: column;
    }}

    .progress-percent {{
        width: 100%;
        box-sizing: border-box;
    }}
}}
</style>
</head>

<body>
<div class="progress-card">
    <div class="progress-inner">
        <div class="progress-top-row">
            <div>
                <div class="progress-title">Care Pack Progress</div>
                <div class="progress-subtitle">
                    Target: All {TARGET_MODELS} models to be ready by the end of this fiscal year.
                </div>
            </div>

            <div class="progress-percent">
                <div class="progress-percent-number">{percent}%</div>
                <div class="progress-percent-label">Completed</div>
            </div>
        </div>

        <div class="progress-bar-bg">
            <div class="progress-bar-fill"></div>
        </div>

        <div class="progress-bottom-row">
            <div>
                <div class="progress-count">{current_count} / {TARGET_MODELS} models completed</div>
                <div class="progress-target">{remaining} models remaining</div>
            </div>

            <div class="progress-status">
                {status_text}
            </div>
        </div>
    </div>
</div>
</body>
</html>
"""

    components.html(progress_html, height=210, scrolling=False)

    st.link_button(
        "View Progress Sheet / 進捗状況を確認",
        PROGRESS_SHEET_URL,
        use_container_width=False,
    )


def render_result_card(item):
    pdf_path = CAREPACK_DIR / item["file"]

    with st.container(border=True):
        top_col1, top_col2 = st.columns([5, 1])

        with top_col1:
            result_title_html = f"""
<div class="result-title">{html.escape(str(item['model']))}</div>
<div class="result-file">File: {html.escape(str(item['file']))}</div>
"""
            st.markdown(result_title_html, unsafe_allow_html=True)

        with top_col2:
            st.markdown(
                """
<div class="carepack-pill">
    Care Pack
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
            col_a, col_b = st.columns([1.3, 5])

            with col_a:
                with open(pdf_path, "rb") as f:
                    pdf_bytes = f.read()

                st.download_button(
                    label="Download PDF",
                    data=pdf_bytes,
                    file_name=item["file"],
                    mime="application/pdf",
                    use_container_width=True,
                )

            with col_b:
                st.caption("PDF is available. You can download it or preview it below.")

            with st.expander("Preview PDF", expanded=False):
                show_pdf_preview(pdf_path)

        else:
            st.error(
                f"PDF file not found: {pdf_path}. "
                "Please check whether the PDF is saved in the carepack_bulletins folder."
            )


def set_show_all():
    st.session_state["carepack_show_all"] = True


def clear_carepack_search():
    st.session_state["carepack_keyword"] = ""
    st.session_state["carepack_show_all"] = False


# =========================
# Main Render Function
# =========================
def render_care_pack():
    apply_care_pack_css()

    if "carepack_keyword" not in st.session_state:
        st.session_state["carepack_keyword"] = ""

    if "carepack_show_all" not in st.session_state:
        st.session_state["carepack_show_all"] = False

    folder_mtime = get_folder_mtime()
    carepack_data = build_carepack_data(folder_mtime)

    render_carepack_hero()
    render_summary_cards(carepack_data)

    if not CAREPACK_DIR.exists():
        st.error(
            "The carepack_bulletins folder was not found. "
            "Please create the folder and upload PDF files."
        )
        st.stop()

    # Search Area
    st.markdown('<div class="search-wrap">', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([5, 1.2, 1.2])

    with col1:
        st.text_input(
            "Search Care Pack",
            placeholder="Example: BQ300, Stitch Liner MarkIV, CBF-SB, AFV-564, AS23122025-1...",
            key="carepack_keyword",
        )

    with col2:
        st.write("")
        st.write("")
        st.button(
            "Show All",
            use_container_width=True,
            on_click=set_show_all,
        )

    with col3:
        st.write("")
        st.write("")
        st.button(
            "Clear",
            use_container_width=True,
            on_click=clear_carepack_search,
        )

    st.markdown('</div>', unsafe_allow_html=True)

    results = search_carepack(
        carepack_data,
        st.session_state["carepack_keyword"],
        st.session_state["carepack_show_all"],
    )

    # Default View
    if not st.session_state["carepack_keyword"] and not st.session_state["carepack_show_all"]:
        st.markdown(
            """
<div class="carepack-info-box">
    Enter a keyword or click <b>Show All</b> to display Care Pack bulletins.
</div>
            """,
            unsafe_allow_html=True,
        )

        render_carepack_table(carepack_data)
        render_carepack_progress(carepack_data)

    # Search Result View
    else:
        search_result_html = f"""
<div class="table-header-card">
    <div class="table-header-title">Search Results</div>
    <div class="table-header-subtitle">
        Found <b>{len(results)}</b> Care Pack bulletin(s).
    </div>
</div>
"""
        st.markdown(search_result_html, unsafe_allow_html=True)

        if not results:
            st.warning("No Care Pack bulletin found.")

        for item in results:
            render_result_card(item)
            st.write("")

        render_carepack_progress(carepack_data)
