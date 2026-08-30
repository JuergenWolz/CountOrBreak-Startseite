import streamlit as st
from pathlib import Path
import base64
import random


# ============================================================
# COUNT OR BREAK – STARTSEITE
# ============================================================

st.set_page_config(
    page_title="CountOrBreak",
    page_icon="countorbreak_logo.png",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# DATEIPFADE
# ============================================================

BASE_PATH = Path(__file__).parent

logo_path = BASE_PATH / "countorbreak_logo.png"

icon_journal_path = BASE_PATH / "icon_journal.png"
icon_auswertungen_path = BASE_PATH / "icon_auswertungen.png"
icon_strategien_path = BASE_PATH / "icon_strategien.png"
icon_wissen_path = BASE_PATH / "icon_wissen.png"
icon_rechner_path = BASE_PATH / "icon_rechner.png"


# ============================================================
# BILDER IN BASE64 UMWANDELN
# ============================================================

def image_to_base64(path):
    if path.exists():
        return base64.b64encode(path.read_bytes()).decode("utf-8")
    return None


logo_data = image_to_base64(logo_path)

journal_data = image_to_base64(icon_journal_path)
auswertungen_data = image_to_base64(icon_auswertungen_path)
strategien_data = image_to_base64(icon_strategien_path)
wissen_data = image_to_base64(icon_wissen_path)
rechner_data = image_to_base64(icon_rechner_path)


# ============================================================
# MOTIVATIONSSPRÜCHE
# ============================================================

motivation_quotes = [
    "TRADE DEN PLAN. NICHT DIE EMOTION.",
    "RISIKO ZUERST. PROFIT DANACH.",
    "DISZIPLIN SCHLÄGT EMOTION.",
    "KONTROLLE BEGINNT MIT DEM RISIKO.",
    "WARTE AUF DEIN SETUP.",
    "SCHÜTZE DEIN KAPITAL.",
    "EIN GUTER TRADE BEGINNT MIT EINEM GUTEN PLAN.",
    "NICHT JEDER MOVE IST DEIN MOVE.",
]

motivation = random.choice(motivation_quotes)


# ============================================================
# DESIGN / CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ========================================================
       GOLD-FARBPALETTE
       ======================================================== */

    :root {
        --cb-gold: #d5a84f;
        --cb-gold-light: #e6c271;
        --cb-gold-bright: #f0d28a;
        --cb-gold-dark: #8f641d;
        --cb-gold-border: #b88932;
        --cb-text: #f0e5ce;
        --cb-subtext: #a9a399;
        --cb-background: #040404;
    }


    /* ========================================================
       GRUNDLAYOUT
       ======================================================== */

    .stApp {
        background:
            radial-gradient(
                circle at 50% 0%,
                rgba(212, 164, 65, 0.10),
                transparent 34%
            ),
            radial-gradient(
                circle at 50% 45%,
                rgba(151, 106, 30, 0.035),
                transparent 52%
            ),
            #040404;

        color: #f4efe4;
    }


    .block-container {
        max-width: 1450px;

        padding-top: 1.5rem;
        padding-bottom: 3rem;
    }


    /* ========================================================
       STREAMLIT ELEMENTE AUSBLENDEN
       ======================================================== */

    #MainMenu {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }


    /* ========================================================
       LOGO
       ======================================================== */

    .cb-logo {
        width: 100%;

        display: flex;
        align-items: center;
        justify-content: center;

        margin-top: 5px;
        margin-bottom: 28px;
    }


    .cb-logo img {
        width: min(540px, 82%);
        max-height: 280px;

        object-fit: contain;

        filter:
            drop-shadow(
                0 0 15px
                rgba(214, 166, 70, 0.12)
            );
    }


    /* ========================================================
       GOLDENE TRENNLINIE
       ======================================================== */

    .cb-top-line {
        width: 100%;
        height: 1px;

        margin: 0 auto 40px auto;

        background:
            linear-gradient(
                90deg,
                transparent 0%,
                #60400d 15%,
                #95691e 30%,
                #d0a246 44%,
                #edc56f 50%,
                #d0a246 56%,
                #95691e 70%,
                #60400d 85%,
                transparent 100%
            );

        box-shadow:
            0 0 12px
            rgba(213, 169, 76, 0.40);
    }


    /* ========================================================
       MOTIVATIONSSPRUCH
       ======================================================== */

    .cb-motivation {
        width: 100%;

        text-align: center;

        margin-bottom: 45px;
    }


    .cb-motivation-text {
        color: var(--cb-gold-light);

        font-family:
            "Palatino Linotype",
            "Book Antiqua",
            Palatino,
            Georgia,
            serif;

        font-size: clamp(18px, 2vw, 27px);

        font-weight: 600;

        letter-spacing: 0.16em;

        text-shadow:
            0 0 7px
            rgba(213, 168, 79, 0.38),

            0 0 18px
            rgba(213, 168, 79, 0.15);
    }


    .cb-motivation-line {
        width: min(600px, 72%);

        height: 1px;

        margin: 17px auto 0 auto;

        background:
            linear-gradient(
                90deg,
                transparent,
                var(--cb-gold-dark),
                var(--cb-gold-light),
                var(--cb-gold-dark),
                transparent
            );

        box-shadow:
            0 0 8px
            rgba(211, 164, 65, 0.25);
    }


    /* ========================================================
       MENÜ-GRID
       ======================================================== */

    .cb-menu-grid {
        width: min(1120px, 94%);

        margin: 0 auto;

        display: grid;

        grid-template-columns:
            repeat(2, minmax(0, 1fr));

        gap: 24px;
    }


    /* ========================================================
       MENÜ-KARTEN
       ======================================================== */

    .cb-card {
        min-height: 155px;

        box-sizing: border-box;

        display: flex;
        align-items: center;

        padding: 24px 28px;

        background:
            linear-gradient(
                135deg,
                rgba(27, 27, 27, 0.99),
                rgba(7, 7, 7, 0.99)
            );

        border:
            1px solid
            rgba(184, 137, 50, 0.78);

        border-radius: 11px;

        box-shadow:
            inset
            0 0 0 1px
            rgba(240, 194, 102, 0.035),

            inset
            0 0 25px
            rgba(192, 143, 46, 0.035),

            0 0 9px
            rgba(183, 136, 46, 0.12),

            0 10px 32px
            rgba(0, 0, 0, 0.48);

        transition:
            transform 0.22s ease,
            border-color 0.22s ease,
            box-shadow 0.22s ease,
            background 0.22s ease;
    }


    .cb-card:hover {
        transform: translateY(-4px);

        border-color:
            var(--cb-gold-light);

        background:
            linear-gradient(
                135deg,
                rgba(31, 29, 23, 0.99),
                rgba(9, 9, 8, 0.99)
            );

        box-shadow:
            inset
            0 0 0 1px
            rgba(255, 218, 130, 0.055),

            inset
            0 0 30px
            rgba(192, 143, 46, 0.055),

            0 0 15px
            rgba(204, 157, 64, 0.22),

            0 15px 38px
            rgba(0, 0, 0, 0.60);
    }


    /* ========================================================
       PIKTOGRAMME
       ======================================================== */

    .cb-icon-wrapper {
        width: 88px;
        min-width: 88px;

        height: 88px;

        display: flex;

        align-items: center;
        justify-content: center;

        margin-right: 25px;
    }


    .cb-icon-wrapper img {
        width: 88px;
        height: 88px;

        object-fit: contain;

        display: block;

        filter:
            drop-shadow(
                0 0 8px
                rgba(214, 166, 70, 0.18)
            );

        transition:
            filter 0.22s ease,
            transform 0.22s ease;
    }


    .cb-card:hover .cb-icon-wrapper img {
        filter:
            drop-shadow(
                0 0 11px
                rgba(225, 178, 78, 0.32)
            );

        transform: scale(1.035);
    }


    /* ========================================================
       KARTEN-TEXT
       ======================================================== */

    .cb-card-content {
        flex: 1;

        min-width: 0;
    }


    .cb-card-title {
        color: var(--cb-gold-light);

        font-family:
            "Palatino Linotype",
            "Book Antiqua",
            Palatino,
            Georgia,
            serif;

        font-size: 25px;

        font-weight: 600;

        letter-spacing: 0.035em;

        margin-bottom: 8px;

        text-shadow:
            0 0 7px
            rgba(213, 168, 79, 0.18);
    }


    .cb-card-subtitle {
        color: var(--cb-subtext);

        font-family:
            Arial,
            Helvetica,
            sans-serif;

        font-size: 14px;

        line-height: 1.5;
    }


    /* ========================================================
       PFEIL
       ======================================================== */

    .cb-arrow {
        color: var(--cb-gold);

        font-family:
            Arial,
            Helvetica,
            sans-serif;

        font-size: 42px;

        font-weight: 200;

        margin-left: 18px;

        transition:
            transform 0.22s ease,
            color 0.22s ease,
            text-shadow 0.22s ease;
    }


    .cb-card:hover .cb-arrow {
        color: var(--cb-gold-bright);

        transform: translateX(5px);

        text-shadow:
            0 0 10px
            rgba(225, 178, 78, 0.30);
    }


    /* ========================================================
       POSITIONSGRÖSSENRECHNER
       ======================================================== */

    .cb-position-wrapper {
        width: min(1120px, 94%);

        margin: 34px auto 0 auto;
    }


    .cb-position-card {
        width: 100%;

        min-height: 175px;

        box-sizing: border-box;

        display: flex;

        align-items: center;

        justify-content: center;

        padding: 28px;

        background:
            linear-gradient(
                135deg,
                rgba(39, 30, 13, 0.98),
                rgba(8, 8, 8, 0.99)
            );

        border:
            1px solid
            rgba(190, 145, 54, 0.88);

        border-radius: 11px;

        box-shadow:
            inset
            0 0 0 1px
            rgba(240, 194, 102, 0.045),

            inset
            0 0 30px
            rgba(201, 151, 47, 0.045),

            0 0 12px
            rgba(190, 139, 39, 0.13),

            0 12px 38px
            rgba(0, 0, 0, 0.52);

        cursor: pointer;

        transition:
            transform 0.22s ease,
            border-color 0.22s ease,
            box-shadow 0.22s ease,
            background 0.22s ease;
    }


    /* ========================================================
       HOVER-EFFEKT RECHNER
       ======================================================== */

    .cb-position-card:hover {
        transform: translateY(-4px);

        border-color:
            var(--cb-gold-bright);

        background:
            linear-gradient(
                135deg,
                rgba(48, 36, 15, 0.99),
                rgba(10, 10, 9, 0.99)
            );

        box-shadow:
            inset
            0 0 0 1px
            rgba(255, 218, 130, 0.06),

            inset
            0 0 35px
            rgba(201, 151, 47, 0.07),

            0 0 19px
            rgba(210, 164, 68, 0.25),

            0 16px 42px
            rgba(0, 0, 0, 0.62);
    }


    /* ========================================================
       RECHNER ICON
       ======================================================== */

    .cb-position-icon {
        width: 90px;
        min-width: 90px;

        height: 90px;

        display: flex;

        align-items: center;
        justify-content: center;

        margin-right: 28px;
    }


    .cb-position-icon img {
        width: 90px;
        height: 90px;

        object-fit: contain;

        display: block;

        filter:
            drop-shadow(
                0 0 8px
                rgba(220, 171, 72, 0.20)
            );

        transition:
            transform 0.22s ease,
            filter 0.22s ease;
    }


    .cb-position-card:hover .cb-position-icon img {
        transform: scale(1.05);

        filter:
            drop-shadow(
                0 0 13px
                rgba(225, 178, 78, 0.34)
            );
    }


    /* ========================================================
       RECHNER TEXT
       ======================================================== */

    .cb-position-content {
        text-align: center;
    }


    .cb-position-title {
        color: var(--cb-gold-light);

        font-family:
            "Palatino Linotype",
            "Book Antiqua",
            Palatino,
            Georgia,
            serif;

        font-size: 27px;

        font-weight: 600;

        letter-spacing: 0.035em;

        margin-bottom: 9px;

        text-shadow:
            0 0 8px
            rgba(213, 168, 79, 0.20);
    }


    .cb-position-subtitle {
        color: #b2aa9d;

        font-family:
            Arial,
            Helvetica,
            sans-serif;

        font-size: 14px;

        line-height: 1.5;
    }


    /* ========================================================
       FOOTER
       ======================================================== */

    .cb-footer-wrapper {
        width: min(1120px, 94%);

        margin: 38px auto 0 auto;
    }


    .cb-footer {
        padding-top: 18px;

        border-top:
            1px solid
            rgba(157, 113, 32, 0.42);

        display: flex;

        justify-content: space-between;

        align-items: center;

        color: #77736b;

        font-family:
            Arial,
            Helvetica,
            sans-serif;

        font-size: 12px;

        letter-spacing: 0.045em;
    }


    .cb-footer-gold {
        color: var(--cb-gold);

        font-size: 17px;
    }


    .cb-footer-right {
        text-align: right;
    }


    /* ========================================================
       MOBILE
       ======================================================== */

    @media (max-width: 750px) {

        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }


        .cb-logo img {
            width: 92%;
        }


        .cb-top-line {
            margin-bottom: 30px;
        }


        .cb-motivation {
            margin-bottom: 32px;
        }


        .cb-motivation-text {
            font-size: 17px;

            letter-spacing: 0.08em;
        }


        .cb-menu-grid {
            grid-template-columns: 1fr;

            width: 94%;
        }


        .cb-card {
            min-height: 125px;

            padding: 18px;
        }


        .cb-icon-wrapper {
            width: 68px;
            min-width: 68px;

            height: 68px;

            margin-right: 17px;
        }


        .cb-icon-wrapper img {
            width: 68px;
            height: 68px;
        }


        .cb-card-title {
            font-size: 19px;
        }


        .cb-card-subtitle {
            font-size: 13px;
        }


        .cb-arrow {
            font-size: 32px;

            margin-left: 8px;
        }


        .cb-position-wrapper {
            width: 94%;

            margin-top: 24px;
        }


        .cb-position-card {
            min-height: 145px;

            padding: 20px;
        }


        .cb-position-icon {
            width: 65px;
            min-width: 65px;

            height: 65px;

            margin-right: 16px;
        }


        .cb-position-icon img {
            width: 65px;
            height: 65px;
        }


        .cb-position-title {
            font-size: 20px;
        }


        .cb-position-subtitle {
            font-size: 13px;
        }


        .cb-footer-wrapper {
            width: 94%;
        }


        .cb-footer {
            flex-direction: column;

            gap: 13px;

            text-align: center;
        }


        .cb-footer-right {
            text-align: center;
        }

    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# LOGO
# ============================================================

if logo_data:

    st.html(
        f"""
        <div class="cb-logo">

            <img
                src="data:image/png;base64,{logo_data}"
                alt="CountOrBreak Logo"
            >

        </div>
        """
    )


# ============================================================
# GOLDENE TRENNLINIE
# ============================================================

st.html(
    """
    <div class="cb-top-line"></div>
    """
)


# ============================================================
# MOTIVATION
# ============================================================

st.html(
    f"""
    <div class="cb-motivation">

        <div class="cb-motivation-text">
            {motivation}
        </div>

        <div class="cb-motivation-line"></div>

    </div>
    """
)


# ============================================================
# PIKTOGRAMM-BEREICHE
# ============================================================

journal_html = ""

if journal_data:

    journal_html = f"""
    <div class="cb-icon-wrapper">

        <img
            src="data:image/png;base64,{journal_data}"
            alt="Journal"
        >

    </div>
    """


auswertungen_html = ""

if auswertungen_data:

    auswertungen_html = f"""
    <div class="cb-icon-wrapper">

        <img
            src="data:image/png;base64,{auswertungen_data}"
            alt="Auswertungen"
        >

    </div>
    """


strategien_html = ""

if strategien_data:

    strategien_html = f"""
    <div class="cb-icon-wrapper">

        <img
            src="data:image/png;base64,{strategien_data}"
            alt="Strategien"
        >

    </div>
    """


wissen_html = ""

if wissen_data:

    wissen_html = f"""
    <div class="cb-icon-wrapper">

        <img
            src="data:image/png;base64,{wissen_data}"
            alt="Wissen"
        >

    </div>
    """


# ============================================================
# HAUPTMENÜ
# ============================================================

st.html(
    f"""
    <div class="cb-menu-grid">


        <!-- JOURNAL -->

        <div class="cb-card">

            {journal_html}

            <div class="cb-card-content">

                <div class="cb-card-title">
                    Journal
                </div>

                <div class="cb-card-subtitle">
                    Deine Trades. Deine Geschichte.
                </div>

            </div>

            <div class="cb-arrow">
                ›
            </div>

        </div>


        <!-- AUSWERTUNGEN -->

        <div class="cb-card">

            {auswertungen_html}

            <div class="cb-card-content">

                <div class="cb-card-title">
                    Auswertungen
                </div>

                <div class="cb-card-subtitle">
                    Deine Performance. Deine Erkenntnisse.
                </div>

            </div>

            <div class="cb-arrow">
                ›
            </div>

        </div>


        <!-- STRATEGIEN -->

        <div class="cb-card">

            {strategien_html}

            <div class="cb-card-content">

                <div class="cb-card-title">
                    Strategien
                </div>

                <div class="cb-card-subtitle">
                    Deine Setups. Dein Plan.
                </div>

            </div>

            <div class="cb-arrow">
                ›
            </div>

        </div>


        <!-- WISSEN -->

        <div class="cb-card">

            {wissen_html}

            <div class="cb-card-content">

                <div class="cb-card-title">
                    Wissen
                </div>

                <div class="cb-card-subtitle">
                    Lernen. Verstehen. Wachsen.
                </div>

            </div>

            <div class="cb-arrow">
                ›
            </div>

        </div>


    </div>
    """
)


# ============================================================
# POSITIONSGRÖSSENRECHNER
# ============================================================

if rechner_data:

    st.html(
        f"""
        <div class="cb-position-wrapper">

            <div class="cb-position-card">

                <div class="cb-position-icon">

                    <img
                        src="data:image/png;base64,{rechner_data}"
                        alt="Positionsgrößenrechner"
                    >

                </div>


                <div class="cb-position-content">

                    <div class="cb-position-title">
                        Positionsgrößenrechner
                    </div>

                    <div class="cb-position-subtitle">
                        Berechne dein Risiko. Kontrolliere dein Handeln.
                    </div>

                </div>

            </div>

        </div>
        """
    )


# ============================================================
# FOOTER
# ============================================================

st.html(
    """
    <div class="cb-footer-wrapper">

        <div class="cb-footer">

            <div>

                <span class="cb-footer-gold">
                    ♢
                </span>

                &nbsp;&nbsp;

                Risk first. Profits second.

            </div>


            <div class="cb-footer-right">

                Trading Journal
                &nbsp;&nbsp; • &nbsp;&nbsp;
                Risk Management
                &nbsp;&nbsp; • &nbsp;&nbsp;
                Performance

            </div>

        </div>

    </div>
    """
)
