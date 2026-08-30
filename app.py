import streamlit as st
from pathlib import Path
import base64


# ============================================================
# COUNT OR BREAK – STARTSEITE
# ============================================================

st.set_page_config(
    page_title="CountOrBreak",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# LOGO
# ============================================================

LOGO_PATH = Path("countorbreak_logo.png")


def get_logo_base64():
    if LOGO_PATH.exists():
        try:
            return base64.b64encode(LOGO_PATH.read_bytes()).decode("utf-8")
        except Exception:
            return None
    return None


logo_base64 = get_logo_base64()


# ============================================================
# MOTIVATIONSSPRUCH
# ============================================================

motivation = "TRADE DEN PLAN. NICHT DIE EMOTION."


# ============================================================
# CSS
# ============================================================

st.markdown(
    """
    <style>

    /* --------------------------------------------------------
       GRUNDLAYOUT
       -------------------------------------------------------- */

    .stApp {
        background:
            radial-gradient(
                circle at 50% 35%,
                rgba(70, 50, 15, 0.10) 0%,
                rgba(0, 0, 0, 0) 42%
            ),
            #050505;

        color: #f3e3b0;
    }


    /* Streamlit Standard-Abstände entfernen */

    .block-container {
        max-width: 1450px;
        padding-top: 2.2rem;
        padding-bottom: 3rem;
    }


    /* Header / Menü von Streamlit ausblenden */

    header {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }


    /* --------------------------------------------------------
       GOLD-FARBEN
       -------------------------------------------------------- */

    :root {
        --gold-main: #d6a936;
        --gold-light: #f5d778;
        --gold-bright: #ffe49a;
        --gold-dark: #8f6919;
        --gold-border: rgba(214, 169, 54, 0.72);
        --gold-soft: rgba(214, 169, 54, 0.16);
    }


    /* --------------------------------------------------------
       OBERER TRENNER
       -------------------------------------------------------- */

    .cb-top-line {
        width: 62%;
        height: 1px;
        margin: 0 auto 12px auto;

        background:
            linear-gradient(
                90deg,
                transparent,
                rgba(214,169,54,0.12),
                rgba(214,169,54,0.85),
                rgba(214,169,54,0.12),
                transparent
            );

        position: relative;
    }

    .cb-top-line::after {
        content: "";
        position: absolute;

        width: 9px;
        height: 9px;

        left: 50%;
        top: -4px;

        transform: translateX(-50%) rotate(45deg);

        background: #e5bd50;

        box-shadow:
            0 0 10px rgba(214,169,54,0.65);
    }


    /* --------------------------------------------------------
       LOGO ALS HINTERGRUND
       -------------------------------------------------------- */

    .cb-logo-background {
        position: fixed;

        left: 50%;
        top: 46%;

        transform: translate(-50%, -50%);

        width: min(820px, 70vw);

        opacity: 0.075;

        z-index: 0;

        pointer-events: none;

        filter:
            grayscale(0.05)
            contrast(1.05)
            brightness(0.9);
    }


    .cb-logo-background img {
        width: 100%;
        height: auto;
        display: block;
    }


    /* --------------------------------------------------------
       MOTIVATION
       -------------------------------------------------------- */

    .cb-motivation {
        position: relative;
        z-index: 2;

        text-align: center;

        margin-top: 46px;
        margin-bottom: 48px;
    }


    .cb-motivation-text {
        font-family:
            Arial,
            Helvetica,
            sans-serif;

        font-size: clamp(30px, 3.3vw, 55px);

        font-weight: 800;

        letter-spacing: 0.095em;

        line-height: 1.12;

        color: #f2ce67;

        text-shadow:
            0 0 12px rgba(214,169,54,0.18),
            0 0 30px rgba(214,169,54,0.08);
    }


    .cb-motivation-line {
        width: 46%;

        height: 1px;

        margin: 27px auto 0 auto;

        background:
            linear-gradient(
                90deg,
                transparent,
                rgba(214,169,54,0.70),
                transparent
            );

        position: relative;
    }


    .cb-motivation-line::after {
        content: "";

        position: absolute;

        width: 9px;
        height: 9px;

        background: #e4bd51;

        left: 50%;
        top: -4px;

        transform: translateX(-50%) rotate(45deg);

        box-shadow:
            0 0 12px rgba(214,169,54,0.60);
    }


    /* --------------------------------------------------------
       MENÜ
       -------------------------------------------------------- */

    .cb-menu {
        position: relative;
        z-index: 2;

        width: 94%;
        max-width: 1280px;

        margin: 0 auto;
    }


    .cb-grid {
        display: grid;

        grid-template-columns: 1fr 1fr;

        gap: 28px;

        margin-top: 18px;
    }


    /* --------------------------------------------------------
       MENÜ-KARTEN
       -------------------------------------------------------- */

    .cb-card {
        min-height: 145px;

        display: flex;

        align-items: center;

        position: relative;

        padding: 26px 30px;

        border-radius: 20px;

        border: 1px solid var(--gold-border);

        background:
            linear-gradient(
                135deg,
                rgba(32,27,18,0.92),
                rgba(8,8,8,0.96)
            );

        box-shadow:
            inset 0 0 30px rgba(214,169,54,0.035),
            0 14px 35px rgba(0,0,0,0.35);

        overflow: hidden;

        transition:
            transform 0.2s ease,
            border-color 0.2s ease,
            box-shadow 0.2s ease;
    }


    .cb-card::before {
        content: "";

        position: absolute;

        left: 0;
        top: 0;

        width: 45%;
        height: 100%;

        background:
            radial-gradient(
                circle at 0% 50%,
                rgba(214,169,54,0.10),
                transparent 68%
            );

        pointer-events: none;
    }


    .cb-card:hover {
        transform: translateY(-3px);

        border-color: rgba(245,215,120,0.92);

        box-shadow:
            inset 0 0 35px rgba(214,169,54,0.055),
            0 18px 42px rgba(0,0,0,0.46),
            0 0 22px rgba(214,169,54,0.08);
    }


    /* --------------------------------------------------------
       PIKTOGRAMM
       -------------------------------------------------------- */

    .cb-icon {
        flex: 0 0 74px;

        width: 74px;
        height: 74px;

        border-radius: 50%;

        border: 1px solid rgba(214,169,54,0.70);

        display: flex;

        align-items: center;
        justify-content: center;

        margin-right: 25px;

        font-size: 31px;

        color: #e4bf5b;

        background:
            radial-gradient(
                circle,
                rgba(214,169,54,0.12),
                rgba(0,0,0,0.05) 68%
            );

        box-shadow:
            inset 0 0 18px rgba(214,169,54,0.055);
    }


    /* --------------------------------------------------------
       TEXT
       -------------------------------------------------------- */

    .cb-card-content {
        position: relative;
        z-index: 2;

        flex: 1;
    }


    .cb-card-title {
        color: #e7bf56;

        font-family:
            Arial,
            Helvetica,
            sans-serif;

        font-size: 21px;

        font-weight: 800;

        letter-spacing: 0.14em;

        text-transform: uppercase;

        margin-bottom: 9px;
    }


    .cb-card-subtitle {
        color: rgba(238,231,214,0.72);

        font-family:
            Arial,
            Helvetica,
            sans-serif;

        font-size: 15px;

        letter-spacing: 0.025em;
    }


    /* --------------------------------------------------------
       PFEIL
       -------------------------------------------------------- */

    .cb-arrow {
        color: #e4bd51;

        font-size: 35px;

        font-family:
            Arial,
            Helvetica,
            sans-serif;

        margin-left: 20px;

        line-height: 1;
    }


    /* --------------------------------------------------------
       POSITIONENSGRÖSSENRECHNER
       -------------------------------------------------------- */

    .cb-position-wrapper {
        position: relative;

        z-index: 2;

        width: 70%;
        max-width: 930px;

        margin: 34px auto 0 auto;
    }


    .cb-position-card {
        min-height: 122px;

        display: flex;

        align-items: center;

        padding: 22px 30px;

        border-radius: 19px;

        border: 1px solid rgba(224,182,66,0.82);

        background:
            linear-gradient(
                135deg,
                rgba(31,26,17,0.94),
                rgba(8,8,8,0.97)
            );

        box-shadow:
            inset 0 0 30px rgba(214,169,54,0.045),
            0 15px 38px rgba(0,0,0,0.36);
    }


    .cb-position-icon {
        flex: 0 0 68px;

        width: 68px;
        height: 68px;

        border-radius: 50%;

        border: 1px solid rgba(214,169,54,0.72);

        display: flex;

        align-items: center;
        justify-content: center;

        margin-right: 23px;

        font-size: 29px;

        color: #e8c35f;

        background:
            radial-gradient(
                circle,
                rgba(214,169,54,0.13),
                transparent 70%
            );
    }


    .cb-position-content {
        flex: 1;
    }


    .cb-position-title {
        color: #e8c35f;

        font-size: 20px;

        font-weight: 800;

        letter-spacing: 0.13em;

        text-transform: uppercase;

        margin-bottom: 7px;
    }


    .cb-position-subtitle {
        color: rgba(238,231,214,0.68);

        font-size: 14px;

        letter-spacing: 0.025em;
    }


    .cb-position-arrow {
        color: #e4bd51;

        font-size: 34px;

        margin-left: 20px;
    }


    /* --------------------------------------------------------
       FOOTER
       -------------------------------------------------------- */

    .cb-footer {
        position: relative;

        z-index: 2;

        width: 88%;

        margin: 52px auto 0 auto;

        display: flex;

        justify-content: space-between;

        align-items: center;

        color: rgba(230,210,160,0.45);

        font-size: 11px;

        letter-spacing: 0.12em;

        text-transform: uppercase;
    }


    .cb-footer-left {
        display: flex;

        align-items: center;

        gap: 9px;
    }


    .cb-footer-shield {
        color: #d8ae40;

        font-size: 15px;
    }


    .cb-footer-line {
        position: relative;

        z-index: 2;

        width: 88%;

        height: 1px;

        margin: 14px auto 0 auto;

        background:
            linear-gradient(
                90deg,
                transparent,
                rgba(214,169,54,0.22),
                transparent
            );
    }


    /* --------------------------------------------------------
       STREAMLIT BUTTONS
       -------------------------------------------------------- */

    div.stButton > button {
        background: transparent !important;

        border: none !important;

        color: transparent !important;

        width: 100% !important;

        height: 100% !important;
    }


    /* --------------------------------------------------------
       MOBILE
       -------------------------------------------------------- */

    @media (max-width: 850px) {

        .block-container {
            padding-top: 1rem;
        }

        .cb-motivation {
            margin-top: 32px;
        }

        .cb-motivation-text {
            font-size: 27px;
            letter-spacing: 0.07em;
        }

        .cb-grid {
            grid-template-columns: 1fr;
            gap: 18px;
        }

        .cb-card {
            min-height: 125px;
            padding: 20px;
        }

        .cb-icon {
            width: 60px;
            height: 60px;
            flex-basis: 60px;
            font-size: 25px;
            margin-right: 17px;
        }

        .cb-card-title {
            font-size: 17px;
        }

        .cb-card-subtitle {
            font-size: 13px;
        }

        .cb-position-wrapper {
            width: 94%;
        }

        .cb-footer {
            width: 94%;
            flex-direction: column;
            gap: 12px;
            text-align: center;
        }

        .cb-footer-line {
            width: 94%;
        }

    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# HINTERGRUNDLOGO
# ============================================================

if logo_base64:
    st.markdown(
        f"""
        <div class="cb-logo-background">
            <img src="data:image/png;base64,{logo_base64}">
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# OBERER BEREICH
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

st.markdown(
    """
    <div class="cb-menu">

        <div class="cb-grid">

            <!-- JOURNAL -->

            <div class="cb-card">

                <div class="cb-icon">
                    ▤
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


            <!-- AUSWERTUNGEN -->

            <div class="cb-card">

                <div class="cb-icon">
                    ▥
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


            <!-- STRATEGIEN -->

            <div class="cb-card">

                <div class="cb-icon">
                    ♞
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


            <!-- WISSEN -->

            <div class="cb-card">

                <div class="cb-icon">
                    ◇
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

        </div>

    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# POSITIONSGRÖSSENRECHNER
# ============================================================

st.markdown(
    """
    <div class="cb-position-wrapper">

        <div class="cb-position-card">

            <div class="cb-position-icon">
                ▦
            </div>

            <div class="cb-position-content">

                <div class="cb-position-title">
                    Positionsgrößenrechner
                </div>

                <div class="cb-position-subtitle">
                    Berechne dein Risiko. Kontrolliere dein Handeln.
                </div>

            </div>

            <div class="cb-position-arrow">
                ›
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

        <div class="cb-footer-left">

            <span class="cb-footer-shield">
                ◇
            </span>

            <span>
                Risk first. Profits second.
            </span>

        </div>

        <div class="cb-footer-right">
            Trading Journal &nbsp; • &nbsp;
            Risk Management &nbsp; • &nbsp;
            Performance
        </div>

    </div>

    <div class="cb-footer-line"></div>
    """,
    unsafe_allow_html=True,
)
