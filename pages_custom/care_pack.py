import streamlit as st
from pathlib import Path
import pandas as pd
import re
import base64


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
/* =========================
   Care Pack Base Theme
========================= */
.block-container {
    padding-top: 2rem;
}

/* =========================
   Hero Area
========================= */
.carepack-hero {
    padding: 38px 46px;
    border-radius: 34px;
    background:
        radial-gradient(circle at 88% 18%, rgba(255,255,255,0.28), transparent 26%),
        radial-gradient(circle at 12% 90%, rgba(251,146,60,0.30), transparent 24%),
        linear-gradient(135deg, #0f172a 0%, #1d4ed8 52%, #06b6d4 100%);
    color: white;
    box-shadow: 0 24px 60px rgba(15,23,42,0.28);
    margin-bottom: 28px;
    display: grid;
    grid-template-columns: minmax(0, 1fr) 380px;
    align-items: center;
    gap: 36px;
    min-height: 270px;
    position: relative;
    overflow: hidden;
}

.carepack-hero::before {
    content: "";
    position: absolute;
    inset: 0;
    background-image:
        linear-gradient(rgba(255,255,255,0.06) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,0.06) 1px, transparent 1px);
    background-size: 28px 28px;
    opacity: 0.35;
}

.carepack-hero-text,
.carepack-hero-image-wrap {
    position: relative;
    z-index: 1;
}

.carepack-hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 8px 14px;
    border-radius: 999px;
    background: rgba(255,255,255,0.16);
    border: 1px solid rgba(255,255,255,0.24);
    color: #ffffff;
    font-size: 13px;
    font-weight: 800;
    margin-bottom: 14px;
}

.carepack-hero-title {
    font-size: 42px;
    font-weight: 950;
    margin-bottom: 14px;
    letter-spacing: -0.04em;
}

.carepack-hero-subtitle {
    font-size: 16px;
    color: #e0f2fe;
    line-height: 1.85;
    max-width: 900px;
}

.carepack-hero-image-wrap {
    width: 360px;
    height: 230px;
    border-radius: 32px;
    background:
        linear-gradient(145deg, rgba(255,255,255,0.30), rgba(255,255,255,0.10));
    border: 1px solid rgba(255,255,255,0.34);
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    box-shadow:
        inset 0 1px 0 rgba(255,255,255,0.30),
        0 22px 42px rgba(0,0,0,0.24);
    padding: 16px;
}

.carepack-hero-image {
    width: 100%;
    height: 100%;
    object-fit: contain;
    border-radius: 22px;
    filter: drop-shadow(0 10px 16px rgba(0,0,0,0.22));
}

.carepack-hero-fallback {
    font-size: 82px;
    filter: drop-shadow(0 12px 20px rgba(0,0,0,0.22));
}

/* =========================
   Info Message
========================= */
.carepack-info-box {
    background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
    border: 1px solid #bfdbfe;
    border-left: 7px solid #2563eb;
    border-radius: 18px;
    padding: 16px 18px;
    color: #1e3a8a;
    font-size: 15px;
    font-weight: 700;
    margin: 16px 0 16px 0;
}

/* =========================
   Table Header
========================= */
.table-header-card {
    background:
        linear-gradient(135deg, #f8fafc 0%, #eff6ff 100%);
    border: 1px solid #dbeafe;
    border-left: 7px solid #2563eb;
    border-radius: 18px;
    padding: 16px 18px;
    margin: 18px 0 12px 0;
}

.table-header-title {
    font-size: 20px;
    font-weight: 900;
    color: #0f172a;
    margin-bottom: 4px;
}

.table-header-subtitle {
    font-size: 13px;
    color: #64748b;
    line-height: 1.5;
}

/* =========================
   Dataframe Styling
========================= */
div[data-testid="stDataFrame"] {
    border-radius: 18px;
    overflow: hidden;
    box-shadow: 0 14px 34px rgba(15,23,42,0.08);
    border: 1px solid #e2e8f0;
}

/* =========================
   Metric Cards
========================= */
div[data-testid="stMetric"] {
    background:
        linear-gradient(180deg, #ffffff 0%, #f8fafc 100%);
    border: 1px solid #e2e8f0;
    padding: 16px 18px;
    border-radius: 18px;
    box-shadow: 0 8px 20px rgba(15,23,42,0.05);
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
   Care Pack Tag
========================= */
.carepack-pill {
    display: inline-block;
    padding: 8px 15px;
    border-radius: 999px;
    background: linear-gradient(135deg, #ffedd5, #fed7aa);
    color: #9a3412;
    font-size: 13px;
    font-weight: 900;
    text-align: center;
    margin-top: 6px;
    border: 1px solid #fdba74;
}

/* =========================
   Progress Card
========================= */
.progress-card {
    background:
        linear-gradient(135deg, #0f172a 0%, #1e3a8a 55%, #0ea5e9 100%);
    border-radius: 28px;
    padding: 28px 30px;
    margin-top: 28px;
    margin-bottom: 18px;
    box-shadow: 0 24px 58px rgba(15,23,42,0.24);
    color: white;
    position: relative;
    overflow: hidden;
}

.progress-card::after {
    content: "";
    position: absolute;
    width: 240px;
    height: 240px;
    border-radius: 50%;
    background: rgba(251,146,60,0.26);
    right: -80px;
    top: -80px;
}

.progress-inner {
    position: relative;
    z-index: 1;
}

.progress-top-row {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 20px;
    margin-bottom: 18px;
}

.progress-title {
    font-size: 22px;
    font-weight: 950;
    color: #ffffff;
    margin-bottom: 6px;
}

.progress-subtitle {
    font-size: 13px;
    color: #bfdbfe;
    line-height: 1.6;
}

.progress-percent {
    min-width: 112px;
    text-align: center;
    padding: 12px 16px;
    border-radius: 20px;
    background: rgba(255,255,255,0.16);
    border: 1px solid rgba(255,255,255,0.22);
    backdrop-filter: blur(8px);
}

.progress-percent-number {
    font-size: 30px;
    font-weight: 950;
    line-height: 1;
    color: #ffffff;
}

.progress-percent-label {
    font-size: 12px;
    color: #dbeafe;
    margin-top: 4px;
    font-weight: 700;
}

.progress-bar-bg {
    width: 100%;
    height: 18px;
    border-radius: 999px;
    background: rgba(255,255,255,0.18);
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.18);
    margin: 18px 0 14px 0;
}

.progress-bar-fill {
    height: 100%;
    border-radius: 999px;
    background: linear-gradient(90deg, #f97316 0%, #facc15 100%);
    box-shadow: 0 0 22px rgba(250,204,21,0.45);
}

.progress-bottom-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 16px;
    flex-wrap: wrap;
}

.progress-count {
    font-size: 20px;
    font-weight: 950;
    color: #ffffff;
}

.progress-target {
    font-size: 13px;
    color: #dbeafe;
}

.progress-status-good {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    padding: 8px 13px;
    border-radius: 999px;
    background: rgba(34,197,94,0.18);
    color: #dcfce7;
    border: 1px solid rgba(134,239,172,0.32);
    font-size: 13px;
    font-weight: 850;
}

.progress-status-warning {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    padding: 8px 13px;
    border-radius: 999px;
    background: rgba(251,146,60,0.18);
    color: #ffedd5;
    border: 1px solid rgba(253,186,116,0.34);
    font-size: 13px;
    font-weight: 850;
}

/* =========================
   Result Card
========================= */
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

@media (max-width: 900px) {
    .carepack-hero {
        grid-template-columns: 1fr;
        padding: 30px 28px;
        min-height: auto;
    }

    .carepack-hero-image-wrap {
        width: 100%;
        height: 240px;
    }

    .progress-top-row {
        flex-direction: column;
    }

    .progress-percent {
        width: 100%;
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

    match = re.match(r"^([A-Z]+-?[A-Z]*)(?=\\d)", machine_name, flags=re.IGNORECASE)

    if match:
        return match.group(1)

    return ""


def expand_slash_machine_name(machine_text: str) -> str:
    """
    Examples:
      AFV-564/566SA -> AFV-564 / AFV-566SA
      AF-762KL/782KL -> AF-762KL / AF-782KL
      RD-N4055/4055DM -> RD-N4055 / RD-N4055DM
    """
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
    """
    Examples:
      AFV-564/566SA -> AFV-564 / AFV-566SA
      RD-N4055 and RD-N4055DM -> RD-N4055 / RD-N4055DM
      CBF-SB -> CBF-SB
      Stitch Liner MarkIV -> Stitch Liner MarkIV
    """
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
    """
    Accept:
      CBF-SB
      AFV-564
      AFV-564/566SA
      BBF-480 / EL-480
      Stitch Liner MarkIV
    """
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
    """
    Supports:
      AFV-564/566SA
      AF-762KL/782KL
      RD-N4055 and RD-N4055DM
      BQ-300
      VAC-1000
      CBF-SB
      CBF-SB / CBF-SS
    """
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
    """
    Priority:
      1. Text after "(Carepack) for ..."
      2. Text after "for ..."
      3. Model / Machine label
      4. Fallback from filename
    """
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


def make_overview_dataframe(carepack_data):
    overview_df = pd.DataFrame(
        [
            {
                "Care Pack Model": item["model"],
                "Machine": item["machine"],
                "Bulletin Code": item["bulletin_code"],
                "Date": item["date"],
                "File Name": item["file"],
            }
            for item in carepack_data
        ]
    )

    return overview_df


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
        <div class="carepack-hero-title">📦 Care Pack Bulletin Library</div>
        <div class="carepack-hero-subtitle">
            Search, preview, and download Care Pack Information Bulletins.<br>
            You can search by Care Pack model, target machine, file name, Bulletin Code, or Date.
            New PDFs will be displayed automatically after being uploaded to the carepack_bulletins folder.
        </div>
    </div>
    {image_html}
</div>
"""

    st.markdown(hero_html, unsafe_allow_html=True)


def render_table_header(total_count: int):
    table_header_html = f"""
<div class="table-header-card">
    <div class="table-header-title">📋 Care Pack Bulletin List</div>
    <div class="table-header-subtitle">
        Uploaded bulletin overview: <b>{total_count}</b> files.
        Search by model, machine, Bulletin Code, date, or file name.
    </div>
</div>
"""
    st.markdown(table_header_html, unsafe_allow_html=True)


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
        status_class = "progress-status-good"
        status_text = "🟢 On Track"
    else:
        status_class = "progress-status-warning"
        status_text = "🟠 In Progress"

    progress_html = f"""
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
            <div class="progress-bar-fill" style="width: {fill_width}%;"></div>
        </div>

        <div class="progress-bottom-row">
            <div>
                <div class="progress-count">{current_count} / {TARGET_MODELS} models completed</div>
                <div class="progress-target">{remaining} models remaining</div>
            </div>

            <div class="{status_class}">
                {status_text}
            </div>
        </div>
    </div>
</div>
"""

    st.markdown(progress_html, unsafe_allow_html=True)

    st.link_button(
        "📊 View Progress Sheet / 進捗状況を確認",
        PROGRESS_SHEET_URL,
        use_container_width=False,
    )


def render_overview_table(carepack_data):
    overview_df = make_overview_dataframe(carepack_data)

    render_table_header(len(carepack_data))

    st.dataframe(
        overview_df,
        use_container_width=True,
        hide_index=True,
        height=420,
        column_config={
            "Care Pack Model": st.column_config.TextColumn(
                "Care Pack Model",
                width="medium",
            ),
            "Machine": st.column_config.TextColumn(
                "Machine",
                width="large",
            ),
            "Bulletin Code": st.column_config.TextColumn(
                "Bulletin Code",
                width="medium",
            ),
            "Date": st.column_config.TextColumn(
                "Date",
                width="medium",
            ),
            "File Name": st.column_config.TextColumn(
                "File Name",
                width="large",
            ),
        },
    )


def render_result_card(item):
    pdf_path = CAREPACK_DIR / item["file"]

    with st.container(border=True):
        top_col1, top_col2 = st.columns([5, 1])

        with top_col1:
            result_title_html = f"""
<div class="result-title">{item['model']}</div>
<div class="result-file">File: {item['file']}</div>
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
                    label="📥 Download PDF",
                    data=pdf_bytes,
                    file_name=item["file"],
                    mime="application/pdf",
                    use_container_width=True,
                )

            with col_b:
                st.caption("PDF is available. You can download it or preview it below.")

            with st.expander("📄 Preview PDF", expanded=False):
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

    if not CAREPACK_DIR.exists():
        st.error(
            "The carepack_bulletins folder was not found. "
            "Please create the folder and upload PDF files."
        )
        st.stop()

    # =========================
    # Search Area
    # =========================
    with st.container(border=True):
        col1, col2, col3 = st.columns([5, 1.25, 1.25])

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

    results = search_carepack(
        carepack_data,
        st.session_state["carepack_keyword"],
        st.session_state["carepack_show_all"],
    )

    # =========================
    # Default View
    # =========================
    if not st.session_state["carepack_keyword"] and not st.session_state["carepack_show_all"]:
        st.markdown(
            """
<div class="carepack-info-box">
    🔎 Enter a keyword or click <b>Show All</b> to display Care Pack bulletins.
</div>
            """,
            unsafe_allow_html=True,
        )

        render_overview_table(carepack_data)
        render_carepack_progress(carepack_data)

    # =========================
    # Search Result View
    # =========================
    else:
        search_result_html = f"""
<div class="table-header-card">
    <div class="table-header-title">🔎 Search Results</div>
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
