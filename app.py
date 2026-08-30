import streamlit as st
from pathlib import Path
import base64


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
# LOGO LADEN
# ============================================================

logo_path = Path("countorbreak_logo.png")

if logo_path.exists():
    logo_bytes = logo_path.read_bytes()
    encoded_logo = base64.b64encode(logo_bytes).decode()
else:
    encoded_logo = None


# ============================================================
# DESIGN
# ============================================================

st.markdown(
    """
    <style>

    /* ========================================================
       GRUNDLAYOUT
       ======================================================== */

    .stApp {
        background:
            radial-gradient(
                circle at 50% 0%,
                rgba(212, 160, 60, 0.08),
                transparent 35%
            ),
            #050505;

        color: #f4f1e8;
    }

    .block-container {
        max-width: 1450px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }


    /* ========================================================
       STREAMLIT ELEMENTE AUSBLENDEN
       ======================================================== */

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }


    /* ========================================================
       LOGO
       ======================================================== */

    .cb-logo {
        text-align: center;
        margin-top: 10px;
        margin-bottom: 35px;
    }

    .cb-logo img {
        width: min(520px, 80%);
        max-height: 260px;
        object-fit: contain;
    }


    /* ========================================================
       GOLDENE TRENNLINIE
       ======================================================== */

    .cb-top-line {
        height: 1px;
        width: 100%;
        margin: 0 auto 40px auto;

        background:
            linear-gradient(
                90deg,
                transparent,
                #8f641b,
                #d5a94f,
                #8f641b,
                transparent
            );

        box-shadow:
            0 0 12px rgba(212, 160, 60, 0.35);
    }


    /* ========================================================
       MOTIVATION
       ======================================================== */

    .cb-motivation {
        text-align: center;
        margin: 10px auto 50px auto;
    }

    .cb-motivation-text {
        font-family:
            Arial,
            Helvetica,
            sans-serif;

        font-size: clamp(18px, 2vw, 27px);
        font-weight: 500;

        letter-spacing: 0.22em;

        color: #d8b66a;

        text-shadow:
            0 0 10px rgba(212, 160, 60, 0.22);

        margin-bottom: 18px;
    }

    .cb-motivation-line {
        width: min(600px, 75%);
        height: 1px;
        margin: 0 auto;

        background:
            linear-gradient(
                90deg,
                transparent,
                #b48731,
                #e2bd63,
                #b48731,
                transparent
            );
    }


    /* ========================================================
       HAUPTMENÜ
       ======================================================== */

    .cb-menu-grid {
        display: grid;

        grid-template-columns:
            repeat(2, minmax(280px, 1fr));

        gap: 24px;

        width: min(1100px, 94%);
        margin: 0 auto;
    }


    /* ========================================================
       MENÜ-KARTEN
       ======================================================== */

    .cb-card {
        min-height: 135px;

        display: flex;
        align-items: center;

        padding: 25px 28px;

        background:
            linear-gradient(
                135deg,
                rgba(22, 22, 22, 0.98),
                rgba(9, 9, 9, 0.98)
            );

        border: 1px solid rgba(172, 126, 39, 0.65);

        border-radius: 10px;

        box-shadow:
            inset 0 0 0 1px rgba(255, 215, 120, 0.035),
            0 8px 30px rgba(0, 0, 0, 0.35);

        transition:
            transform 0.2s ease,
            border-color 0.2s ease,
            box-shadow 0.2s ease;
    }

    .cb-card:hover {
        transform: translateY(-3px);

        border-color: #d4aa50;

        box-shadow:
            0 10px 35px rgba(0, 0, 0, 0.55),
            0 0 18px rgba(190, 140, 45, 0.12);
    }


    /* ========================================================
       PIKTOGRAMME
       ======================================================== */

    .cb-icon {
        width: 52px;
        min-width: 52px;
        height: 52px;

        display: flex;
        align-items: center;
        justify-content: center;

        margin-right: 22px;

        border: 1px solid rgba(194, 148, 58, 0.55);
        border-radius: 8px;

        color: #d7ad54;

        font-size: 25px;

        background:
            linear-gradient(
                145deg,
                rgba(40, 32, 17, 0.8),
                rgba(13, 13, 13, 0.9)
            );

        box-shadow:
            inset 0 0 15px rgba(194, 148, 58, 0.06);
    }


    /* ========================================================
       TEXT
       ======================================================== */

    .cb-card-content {
        flex: 1;
    }

    .cb-card-title {
        font-size: 21px;
        font-weight: 600;

        letter-spacing: 0.04em;

        color: #f0e7d1;

        margin-bottom: 8px;
    }

    .cb-card-subtitle {
        font-size: 14px;

        color: #9c978c;

        line-height: 1.5;
    }


    /* ========================================================
       PFEIL
       ======================================================== */

    .cb-arrow {
        margin-left: 15px;

        color: #b88a35;

        font-size: 30px;
        font-weight: 300;

        transition:
            transform 0.2s ease,
            color 0.2s ease;
    }

    .cb-card:hover .cb-arrow {
        color: #e1b85d;
        transform: translateX(4px);
    }


    /* ========================================================
       POSITIONSGRÖSSENRECHNER
       ======================================================== */

    .cb-position-wrapper {
        width: min(1100px, 94%);
        margin: 38px auto 0 auto;
    }

    .cb-position-card {
        min-height: 115px;

        display: flex;
        align-items: center;

        padding: 22px 28px;

        background:
            linear-gradient(
                135deg,
                rgba(30, 24, 12, 0.92),
                rgba(10, 10, 10, 0.98)
            );

        border: 1px solid #a97924;

        border-radius: 10px;

        box-shadow:
            0 10px 35px rgba(0, 0, 0, 0.45),
            inset 0 0 25px rgba(194, 148, 58, 0.04);
    }

    .cb-position-icon {
        width: 52px;
        min-width: 52px;
        height: 52px;

        display: flex;
        align-items: center;
        justify-content: center;

        margin-right: 22px;

        border: 1px solid #b48731;
        border-radius: 8px;

        color: #ddb45d;

        font-size: 25px;
    }

    .cb-position-content {
        flex: 1;
    }

    .cb-position-title {
        color: #e5c275;

        font-size: 20px;
        font-weight: 600;

        margin-bottom: 7px;
    }

    .cb-position-subtitle {
        color: #a7a196;

        font-size: 14px;
    }

    .cb-position-arrow {
        color: #c5963d;

        font-size: 30px;

        margin-left: 15px;
    }


    /* ========================================================
       FOOTER
       ======================================================== */

    .cb-footer {
        width: min(1100px, 94%);

        margin: 55px auto 0 auto;

        display: flex;
        justify-content: space-between;
        align-items: center;

        color: #77736a;

        font-size: 12px;

        letter-spacing: 0.05em;
    }

    .cb-footer-left {
        display: flex;
        align-items: center;
        gap: 9px;
    }

    .cb-footer-shield {
        color: #b78b38;
        font-size: 17px;
    }

    .cb-footer-right {
        text-align: right;
    }

    .cb-footer-line {
        width: min(1100px, 94%);

        height: 1px;

        margin: 15px auto 0 auto;

        background:
            linear-gradient(
                90deg,
                transparent,
                rgba(170, 125, 38, 0.65),
                transparent
            );
    }


    /* ========================================================
       MOBILE
       ======================================================== */

    @media (max-width: 750px) {

        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }

        .cb-menu-grid {
            grid-template-columns: 1fr;
        }

        .cb-motivation-text {
            letter-spacing: 0.12em;
        }

        .cb-card {
            min-height: 115px;
            padding: 20px;
        }

        .cb-card-title {
            font-size: 18px;
        }

        .cb-card-subtitle {
            font-size: 13px;
        }

        .cb-footer {
            flex-direction: column;
            gap: 15px;
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
# LOGO AUSGEBEN
# ============================================================

if encoded_logo:
    st.markdown(
        f"""
        <div class="cb-logo">
            <img
                src="data:image/png;base64,{encoded_logo}"
                alt="CountOrBreak Logo"
            >
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# GOLDENE TRENNLINIE
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
    """
    <div class="cb-motivation">

        <div class="cb-motivation-text">
            TRADE DEN PLAN. NICHT DIE EMOTION.
        </div>

        <div class="cb-motivation-line"></div>

    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# HAUPTMENÜ
# ============================================================

st.markdown(
    """
    <div class="cb-menu-grid">

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
                ♢
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
