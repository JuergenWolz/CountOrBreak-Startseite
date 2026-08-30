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
# DATEIEN
# ============================================================

BASE_PATH = Path(__file__).parent

logo_path = BASE_PATH / "countorbreak_logo.png"

icon_journal = BASE_PATH / "icon_journal.png"
icon_auswertungen = BASE_PATH / "icon_auswertungen.png"
icon_strategien = BASE_PATH / "icon_strategien.png"
icon_wissen = BASE_PATH / "icon_wissen.png"
icon_rechner = BASE_PATH / "icon_rechner.png"


# ============================================================
# HILFSFUNKTION FÜR BILDER
# ============================================================

def image_to_base64(path):
    if path.exists():
        return base64.b64encode(path.read_bytes()).decode("utf-8")
    return None


logo_data = image_to_base64(logo_path)

journal_data = image_to_base64(icon_journal)
auswertungen_data = image_to_base64(icon_auswertungen)
strategien_data = image_to_base64(icon_strategien)
wissen_data = image_to_base64(icon_wissen)
rechner_data = image_to_base64(icon_rechner)


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
# DESIGN
# ============================================================

st.markdown(
    """
<style>

/* ============================================================
   GRUNDLAYOUT
   ============================================================ */

.stApp {
    background:
        radial-gradient(
            circle at 50% 0%,
            rgba(211, 163, 65, 0.10),
            transparent 34%
        ),
        radial-gradient(
            circle at 50% 45%,
            rgba(150, 105, 28, 0.035),
            transparent 50%
        ),
        #040404;

    color: #f5f0e5;
}

.block-container {
    max-width: 1450px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}


/* ============================================================
   STREAMLIT UI AUSBLENDEN
   ============================================================ */

#MainMenu {
    visibility: hidden;
}

header {
    visibility: hidden;
}

footer {
    visibility: hidden;
}


/* ============================================================
   LOGO
   ============================================================ */

.cb-logo {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;

    margin-top: 5px;
    margin-bottom: 25px;
}

.cb-logo img {
    width: min(540px, 82%);
    max-height: 280px;
    object-fit: contain;

    filter:
        drop-shadow(0 0 14px rgba(207, 157, 50, 0.10));
}


/* ============================================================
   GOLDENE TRENNLINIE
   ============================================================ */

.cb-top-line {
    width: 100%;
    height: 1px;

    margin: 0 auto 38px auto;

    background:
        linear-gradient(
            90deg,
            transparent 0%,
            #68450e 15%,
            #9f7121 30%,
            #d6a94c 44%,
            #f0cc76 50%,
            #d6a94c 56%,
            #9f7121 70%,
            #68450e 85%,
            transparent 100%
        );

    box-shadow:
        0 0 10px rgba(213, 169, 76, 0.38),
        0 0 22px rgba(213, 169, 76, 0.10);
}


/* ============================================================
   MOTIVATION
   ============================================================ */

.cb-motivation {
    width: 100%;
    text-align: center;

    margin-bottom: 42px;
}

.cb-motivation-text {
    color: #d8ad52;

    font-family:
        Georgia,
        "Times New Roman",
        serif;

    font-size: clamp(18px, 2vw, 27px);

    font-weight: 500;

    letter-spacing: 0.19em;

    text-shadow:
        0 0 8px rgba(216, 173, 82, 0.25),
        0 0 20px rgba(216, 173, 82, 0.08);
}

.cb-motivation-line {
    width: min(600px, 72%);
    height: 1px;

    margin: 16px auto 0 auto;

    background:
        linear-gradient(
            90deg,
            transparent,
            #8b6119,
            #dfb65b,
            #8b6119,
            transparent
        );
}


/* ============================================================
   MENÜ-KARTEN
   ============================================================ */

.cb-card {
    width: 100%;
    min-height: 155px;

    box-sizing: border-box;

    display: flex;
    align-items: center;

    padding: 25px 28px;

    margin-bottom: 24px;

    background:
        linear-gradient(
            135deg,
            rgba(25, 25, 25, 0.98),
            rgba(8, 8, 8, 0.99)
        );

    border: 1px solid rgba(176, 128, 37, 0.75);

    border-radius: 11px;

    box-shadow:
        inset 0 0 0 1px rgba(255, 218, 130, 0.025),
        inset 0 0 28px rgba(192, 143, 46, 0.025),
        0 10px 32px rgba(0, 0, 0, 0.46);

    transition:
        transform 0.20s ease,
        border-color 0.20s ease,
        box-shadow 0.20s ease;
}

.cb-card:hover {
    transform: translateY(-3px);

    border-color: #d5a94e;

    box-shadow:
        inset 0 0 0 1px rgba(255, 218, 130, 0.04),
        0 13px 38px rgba(0, 0, 0, 0.58),
        0 0 20px rgba(194, 143, 46, 0.13);
}


/* ============================================================
   PIKTOGRAMME
   ============================================================ */

.cb-icon-wrapper {
    width: 90px;
    min-width: 90px;
    height: 90px;

    display: flex;
    align-items: center;
    justify-content: center;

    margin-right: 25px;

    overflow: hidden;

    border-radius: 10px;
}

.cb-icon-wrapper img {
    width: 90px;
    height: 90px;

    object-fit: contain;

    display: block;

    filter:
        drop-shadow(0 0 7px rgba(213, 165, 65, 0.14));
}


/* ============================================================
   TEXT
   ============================================================ */

.cb-card-content {
    flex: 1;
}

.cb-card-title {
    color: #f0e5cd;

    font-family:
        Georgia,
        "Times New Roman",
        serif;

    font-size: 25px;

    font-weight: 500;

    letter-spacing: 0.035em;

    margin-bottom: 8px;
}

.cb-card-subtitle {
    color: #a9a399;

    font-family:
        Arial,
        Helvetica,
        sans-serif;

    font-size: 14px;

    line-height: 1.5;
}


/* ============================================================
   PFEIL
   ============================================================ */

.cb-arrow {
    color: #bd8d37;

    font-family:
        Arial,
        Helvetica,
        sans-serif;

    font-size: 43px;

    font-weight: 200;

    margin-left: 18px;

    transition:
        transform 0.2s ease,
        color 0.2s ease;
}

.cb-card:hover .cb-arrow {
    color: #e2b85c;

    transform: translateX(5px);
}


/* ============================================================
   POSITIONSGRÖSSENRECHNER
   ============================================================ */

.cb-calculator {
    width: 100%;
    min-height: 175px;

    box-sizing: border-box;

    display: flex;
    align-items: center;
    justify-content: center;

    margin-top: 6px;
    margin-bottom: 20px;

    padding: 28px;

    background:
        linear-gradient(
            135deg,
            rgba(38, 29, 13, 0.98),
            rgba(8, 8, 8, 0.99)
        );

    border: 1px solid #b8872c;

    border-radius: 11px;

    box-shadow:
        inset 0 0 28px rgba(201, 151, 47, 0.035),
        0 12px 38px rgba(0, 0, 0, 0.52),
        0 0 18px rgba(190, 139, 39, 0.08);
}


/* Rechner Icon */

.cb-calculator-icon {
    width: 90px;
    min-width: 90px;
    height: 90px;

    display: flex;
    align-items: center;
    justify-content: center;

    margin-right: 28px;
}

.cb-calculator-icon img {
    width: 90px;
    height: 90px;

    object-fit: contain;

    filter:
        drop-shadow(0 0 8px rgba(220, 171, 72, 0.17));
}


/* Rechner Text */

.cb-calculator-content {
    text-align: center;
}

.cb-calculator-title {
    color: #e4bd67;

    font-family:
        Georgia,
        "Times New Roman",
        serif;

    font-size: 26px;

    font-weight: 500;

    letter-spacing: 0.035em;

    margin-bottom: 9px;
}

.cb-calculator-subtitle {
    color: #b2aa9d;

    font-family:
        Arial,
        Helvetica,
        sans-serif;

    font-size: 14px;

    line-height: 1.5;
}


/* ============================================================
   FOOTER
   ============================================================ */

.cb-footer {
    width: 100%;

    margin-top: 34px;
    padding-top: 18px;

    border-top:
        1px solid rgba(157, 113, 32, 0.42);

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
    color: #b98a37;

    font-size: 17px;
}

.cb-footer-right {
    text-align: right;
}


/* ============================================================
   MOBILE
   ============================================================ */

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
        margin-bottom: 30px;
    }

    .cb-motivation-text {
        font-size: 17px;
        letter-spacing: 0.09em;
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

    .cb-calculator {
        min-height: 145px;
        padding: 20px;
    }

    .cb-calculator-icon {
        width: 65px;
        min-width: 65px;
        height: 65px;

        margin-right: 16px;
    }

    .cb-calculator-icon img {
        width: 65px;
        height: 65px;
    }

    .cb-calculator-title {
        font-size: 20px;
    }

    .cb-calculator-subtitle {
        font-size: 13px;
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

    st.markdown(
        f"""
        <div class="cb-logo">
            <img
                src="data:image/png;base64,{logo_data}"
                alt="CountOrBreak Logo"
            >
        </div>
        """,
        unsafe_allow_html=True,
    )

else:

    st.markdown(
        """
        <div class="cb-logo">
            <div style="
                color:#d8ad52;
                font-family:Georgia,serif;
                font-size:32px;
                letter-spacing:0.12em;
            ">
                COUNT OR BREAK
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# GOLDENE LINIE
# ============================================================

st.markdown(
    """
    <div class="cb-top-line"></div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# MOTIVATION
# ============================================================

st.markdown(
    f"""
    <div class="cb-motivation">
        <div class="cb-motivation-text">
            {motivation}
        </div>

        <div class="cb-motivation-line"></div>
    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# MENÜ
# ============================================================

col_left, col_right = st.columns(
    2,
    gap="large"
)


# ============================================================
# JOURNAL
# ============================================================

with col_left:

    if journal_data:

        st.markdown(
            f"""
            <div class="cb-card">

                <div class="cb-icon-wrapper">
                    <img
                        src="data:image/png;base64,{journal_data}"
                        alt="Journal"
                    >
                </div>

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
            """,
            unsafe_allow_html=True,
        )


# ============================================================
# AUSWERTUNGEN
# ============================================================

with col_right:

    if auswertungen_data:

        st.markdown(
            f"""
            <div class="cb-card">

                <div class="cb-icon-wrapper">
                    <img
                        src="data:image/png;base64,{auswertungen_data}"
                        alt="Auswertungen"
                    >
                </div>

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
            """,
            unsafe_allow_html=True,
        )


# ============================================================
# STRATEGIEN
# ============================================================

with col_left:

    if strategien_data:

        st.markdown(
            f"""
            <div class="cb-card">

                <div class="cb-icon-wrapper">
                    <img
                        src="data:image/png;base64,{strategien_data}"
                        alt="Strategien"
                    >
                </div>

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
            """,
            unsafe_allow_html=True,
        )


# ============================================================
# WISSEN
# ============================================================

with col_right:

    if wissen_data:

        st.markdown(
            f"""
            <div class="cb-card">

                <div class="cb-icon-wrapper">
                    <img
                        src="data:image/png;base64,{wissen_data}"
                        alt="Wissen"
                    >
                </div>

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
            """,
            unsafe_allow_html=True,
        )


# ============================================================
# POSITIONSGRÖSSENRECHNER
# ============================================================

if rechner_data:

    st.markdown(
        f"""
        <div class="cb-calculator">

            <div class="cb-calculator-icon">
                <img
                    src="data:image/png;base64,{rechner_data}"
                    alt="Positionsgrößenrechner"
                >
            </div>

            <div class="cb-calculator-content">

                <div class="cb-calculator-title">
                    Positionsgrößenrechner
                </div>

                <div class="cb-calculator-subtitle">
                    Berechne dein Risiko. Kontrolliere dein Handeln.
                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="cb-footer">

        <div>
            <span class="cb-footer-gold">♢</span>
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
    """,
    unsafe_allow_html=True,
)
