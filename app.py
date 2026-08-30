import streamlit as st
from pathlib import Path
import base64
import random


# ============================================================
# COUNTORBREAK – STARTSEITE
# ============================================================

st.set_page_config(
    page_title="CountOrBreak",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# MOTIVATIONSSPRÜCHE
# ============================================================

motivation_quotes = [
    "TRADE DEN PLAN. NICHT DIE EMOTION.",
    "DEIN VORTEIL LIEGT IN DER DISZIPLIN.",
    "RISIKO ZUERST. GEWINNE ZWEIT.",
    "KONSEQUENZ SCHLÄGT INTUITION.",
    "NICHT JEDER TRADE MUSS GEHANDELT WERDEN.",
    "DEIN SYSTEM. DEINE REGELN. DEIN VORTEIL.",
]

motivation = random.choice(motivation_quotes)


# ============================================================
# LOGO LADEN
# ============================================================

logo_path = Path("countorbreak_logo.png")

logo_data = ""

if logo_path.exists():
    logo_bytes = logo_path.read_bytes()
    logo_base64 = base64.b64encode(logo_bytes).decode("utf-8")
    logo_data = f"data:image/png;base64,{logo_base64}"


# ============================================================
# DESIGN / CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ========================================================
       GRUNDLAYOUT
       ======================================================== */

    html,
    body,
    [data-testid="stAppViewContainer"] {
        background: #020202 !important;
    }

    [data-testid="stAppViewContainer"] {
        background:
            radial-gradient(
                circle at 50% 38%,
                rgba(150, 100, 20, 0.055) 0%,
                rgba(0, 0, 0, 0) 38%
            ),
            #020202 !important;
    }

    [data-testid="stHeader"] {
        background: transparent !important;
        visibility: hidden !important;
        height: 0 !important;
    }

    header {
        visibility: hidden !important;
    }

    footer {
        visibility: hidden !important;
    }

    #MainMenu {
        visibility: hidden !important;
    }

    .block-container {
        max-width: 1450px !important;
        padding-top: 22px !important;
        padding-bottom: 45px !important;
        padding-left: 45px !important;
        padding-right: 45px !important;
        position: relative;
        z-index: 5;
    }


    /* ========================================================
       FARBEN
       ======================================================== */

    :root {
        --cb-gold-deep: #8f6410;
        --cb-gold: #c9982b;
        --cb-gold-light: #f0c85b;
        --cb-gold-bright: #ffe6a0;
        --cb-gold-soft: rgba(240, 200, 91, 0.72);
        --cb-border: rgba(201, 152, 43, 0.70);
        --cb-card: rgba(9, 9, 9, 0.91);
        --cb-text: rgba(245, 245, 245, 0.76);
    }


    /* ========================================================
       HINTERGRUND-LOGO
       ======================================================== */

    .cb-background-logo {
        position: fixed;
        left: 50%;
        top: 51%;
        transform: translate(-50%, -50%);

        width: min(1080px, 76vw);
        height: auto;

        opacity: 0.105;

        z-index: 0;
        pointer-events: none;
        user-select: none;

        filter:
            drop-shadow(0 0 35px rgba(205, 150, 30, 0.10));
    }


    /* ========================================================
       FALLBACK
       ======================================================== */

    .cb-logo-placeholder {
        position: fixed;
        left: 50%;
        top: 51%;
        transform: translate(-50%, -50%);

        width: min(1000px, 72vw);
        height: 520px;

        opacity: 0.12;

        z-index: 0;
        pointer-events: none;

        border: 1px solid rgba(201, 152, 43, 0.07);

        box-shadow:
            inset 0 0 120px rgba(170, 110, 15, 0.04);
    }


    /* ========================================================
       INHALT
       ======================================================== */

    .cb-page {
        position: relative;
        z-index: 5;
    }


    /* ========================================================
       OBERE LINIE
       ======================================================== */

    .cb-top-line {
        width: 100%;
        height: 1px;

        margin: 3px auto 34px auto;

        background:
            linear-gradient(
                90deg,
                transparent 0%,
                rgba(201, 152, 43, 0.10) 20%,
                rgba(240, 200, 91, 0.75) 50%,
                rgba(201, 152, 43, 0.10) 80%,
                transparent 100%
            );

        position: relative;
    }

    .cb-top-line::after {
        content: "";

        position: absolute;

        left: 50%;
        top: 50%;

        width: 9px;
        height: 9px;

        transform:
            translate(-50%, -50%)
            rotate(45deg);

        background: var(--cb-gold-light);

        box-shadow:
            0 0 13px rgba(240, 200, 91, 0.85);
    }


    /* ========================================================
       MOTIVATION
       ======================================================== */

    .cb-motivation {
        text-align: center;

        margin: 0 auto 30px auto;
    }

    .cb-motivation-text {
        font-family:
            Arial,
            Helvetica,
            sans-serif;

        font-size: clamp(30px, 3.35vw, 56px);

        font-weight: 800;

        letter-spacing: 0.105em;

        line-height: 1.08;

        color: var(--cb-gold-bright);

        text-shadow:
            0 0 16px rgba(240, 200, 91, 0.20),
            0 0 38px rgba(201, 152, 43, 0.10);

        text-transform: uppercase;
    }

    .cb-motivation-line {
        width: min(780px, 68%);

        height: 1px;

        margin: 27px auto 0 auto;

        background:
            linear-gradient(
                90deg,
                transparent,
                rgba(201, 152, 43, 0.18),
                rgba(240, 200, 91, 0.82),
                rgba(201, 152, 43, 0.18),
                transparent
            );

        position: relative;
    }

    .cb-motivation-line::after {
        content: "";

        position: absolute;

        left: 50%;
        top: 50%;

        width: 10px;
        height: 10px;

        transform:
            translate(-50%, -50%)
            rotate(45deg);

        background: var(--cb-gold-light);

        box-shadow:
            0 0 15px rgba(240, 200, 91, 0.80);
    }


    /* ========================================================
       POSITIONSGRÖSSENRECHNER
       ======================================================== */

    .cb-position-wrapper {
        width: min(960px, 76%);

        margin: 0 auto 72px auto;
    }

    .cb-position-card {
        min-height: 122px;

        display: flex;
        align-items: center;

        padding: 22px 30px;

        background:
            linear-gradient(
                135deg,
                rgba(28, 22, 10, 0.97),
                rgba(5, 5, 5, 0.97)
            );

        border: 1px solid var(--cb-border);

        border-radius: 18px;

        box-shadow:
            0 0 0 1px rgba(240, 200, 91, 0.035),
            0 15px 48px rgba(0, 0, 0, 0.62),
            inset 0 0 42px rgba(201, 152, 43, 0.035);

        transition:
            transform 0.22s ease,
            border-color 0.22s ease,
            box-shadow 0.22s ease;
    }

    .cb-position-card:hover {
        transform: translateY(-3px);

        border-color: var(--cb-gold-light);

        box-shadow:
            0 0 30px rgba(201, 152, 43, 0.13),
            0 20px 58px rgba(0, 0, 0, 0.68);
    }

    .cb-position-icon {
        width: 68px;
        height: 68px;

        flex-shrink: 0;

        display: flex;
        align-items: center;
        justify-content: center;

        border: 1px solid var(--cb-border);

        border-radius: 50%;

        color: var(--cb-gold-bright);

        font-size: 28px;

        margin-right: 27px;

        box-shadow:
            inset 0 0 22px rgba(201, 152, 43, 0.05),
            0 0 18px rgba(201, 152, 43, 0.035);
    }

    .cb-position-content {
        flex: 1;
    }

    .cb-position-title {
        color: var(--cb-gold-bright);

        font-size: 22px;

        font-weight: 800;

        letter-spacing: 0.14em;

        text-transform: uppercase;

        margin-bottom: 8px;
    }

    .cb-position-subtitle {
        color: rgba(245, 245, 245, 0.68);

        font-size: 15px;

        letter-spacing: 0.025em;
    }

    .cb-position-arrow {
        color: var(--cb-gold-light);

        font-size: 35px;

        font-weight: 300;

        margin-left: 25px;

        transition: transform 0.2s ease;
    }

    .cb-position-card:hover .cb-position-arrow {
        transform: translateX(5px);
    }


    /* ========================================================
       MENÜ
       ======================================================== */

    .cb-menu-grid {
        display: grid;

        grid-template-columns:
            repeat(2, minmax(0, 1fr));

        gap: 28px;

        width: 100%;

        margin: 0 auto;
    }


    /* ========================================================
       MENÜ-KARTEN
       ======================================================== */

    .cb-card {
        min-height: 153px;

        display: flex;
        align-items: center;

        padding: 25px 30px;

        background:
            linear-gradient(
                135deg,
                rgba(23, 18, 9, 0.95),
                rgba(5, 5, 5, 0.97)
            );

        border: 1px solid rgba(201, 152, 43, 0.68);

        border-radius: 18px;

        box-shadow:
            0 13px 40px rgba(0, 0, 0, 0.50),
            inset 0 0 35px rgba(201, 152, 43, 0.025);

        transition:
            transform 0.22s ease,
            border-color 0.22s ease,
            box-shadow 0.22s ease;
    }

    .cb-card:hover {
        transform: translateY(-3px);

        border-color: var(--cb-gold-light);

        box-shadow:
            0 0 30px rgba(201, 152, 43, 0.12),
            0 19px 52px rgba(0, 0, 0, 0.65);
    }


    /* ========================================================
       PIKTOGRAMME
       ======================================================== */

    .cb-icon {
        width: 68px;
        height: 68px;

        flex-shrink: 0;

        display: flex;
        align-items: center;
        justify-content: center;

        border: 1px solid rgba(201, 152, 43, 0.82);

        border-radius: 50%;

        color: var(--cb-gold-bright);

        margin-right: 25px;

        font-size: 27px;

        line-height: 1;

        box-shadow:
            inset 0 0 20px rgba(201, 152, 43, 0.045),
            0 0 17px rgba(201, 152, 43, 0.025);
    }


    /* ========================================================
       KARTEN-TEXT
       ======================================================== */

    .cb-card-content {
        flex: 1;
    }

    .cb-card-title {
        color: var(--cb-gold-bright);

        font-size: 21px;

        font-weight: 800;

        letter-spacing: 0.14em;

        text-transform: uppercase;

        margin-bottom: 9px;
    }

    .cb-card-subtitle {
        color: rgba(245, 245, 245, 0.69);

        font-size: 15px;

        line-height: 1.45;

        letter-spacing: 0.02em;
    }

    .cb-arrow {
        color: var(--cb-gold-light);

        font-size: 34px;

        font-weight: 300;

        margin-left: 20px;

        transition: transform 0.2s ease;
    }

    .cb-card:hover .cb-arrow {
        transform: translateX(5px);
    }


    /* ========================================================
       FOOTER
       ======================================================== */

    .cb-footer {
        display: flex;

        justify-content: space-between;

        align-items: center;

        margin-top: 65px;

        padding-top: 22px;

        border-top: 1px solid rgba(201, 152, 43, 0.19);

        color: rgba(235, 235, 235, 0.49);

        font-size: 12px;

        letter-spacing: 0.09em;

        text-transform: uppercase;
    }

    .cb-footer-left {
        display: flex;

        align-items: center;

        gap: 12px;
    }

    .cb-footer-symbol {
        color: var(--cb-gold-light);

        font-size: 20px;
    }

    .cb-footer-right {
        text-align: right;
    }


    /* ========================================================
       MOBILE
       ======================================================== */

    @media (max-width: 900px) {

        .block-container {
            padding-left: 20px !important;
            padding-right: 20px !important;
        }

        .cb-menu-grid {
            grid-template-columns: 1fr;
        }

        .cb-position-wrapper {
            width: 100%;
        }

        .cb-motivation-text {
            font-size: 30px;
        }

        .cb-footer {
            flex-direction: column;

            gap: 17px;

            text-align: center;
        }

        .cb-footer-right {
            text-align: center;
        }

    }


    @media (max-width: 600px) {

        .block-container {
            padding-top: 15px !important;
        }

        .cb-top-line {
            margin-bottom: 27px;
        }

        .cb-motivation-text {
            font-size: 25px;

            letter-spacing: 0.075em;
        }

        .cb-motivation-line {
            width: 82%;
        }

        .cb-position-wrapper {
            margin-bottom: 45px;
        }

        .cb-position-card {
            min-height: 105px;

            padding: 18px;
        }

        .cb-position-icon {
            width: 54px;
            height: 54px;

            margin-right: 15px;

            font-size: 22px;
        }

        .cb-position-title {
            font-size: 16px;
        }

        .cb-position-subtitle {
            font-size: 12px;
        }

        .cb-card {
            min-height: 125px;

            padding: 18px;
        }

        .cb-icon {
            width: 54px;
            height: 54px;

            margin-right: 15px;

            font-size: 22px;
        }

        .cb-card-title {
            font-size: 16px;
        }

        .cb-card-subtitle {
            font-size: 12px;
        }

        .cb-background-logo {
            width: 125vw;
        }

        .cb-footer {
            margin-top: 45px;
        }

    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# HINTERGRUND-LOGO AUSGEBEN
# ============================================================

if logo_data:
    st.markdown(
        f"""
        <img
            class="cb-background-logo"
            src="{logo_data}"
            alt=""
        >
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        """
        <div class="cb-logo-placeholder"></div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# STARTSEITE
# ============================================================

st.markdown(
    f"""
    <div class="cb-page">

        <!-- OBERE GOLDLINIE -->

        <div class="cb-top-line"></div>


        <!-- MOTIVATION -->

        <div class="cb-motivation">

            <div class="cb-motivation-text">
                {motivation}
            </div>

            <div class="cb-motivation-line"></div>

        </div>


        <!-- POSITIONSGRÖSSENRECHNER -->

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


        <!-- HAUPTMENÜ -->

        <div class="cb-menu-grid">


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


        <!-- FOOTER -->

        <div class="cb-footer">

            <div class="cb-footer-left">

                <span class="cb-footer-symbol">
                    ◈
                </span>

                <span>
                    Risk first. Profits second.
                </span>

            </div>

            <div class="cb-footer-right">
                Trading Journal
                &nbsp; • &nbsp;
                Risk Management
                &nbsp; • &nbsp;
                Performance
            </div>

        </div>


    </div>
    """,
    unsafe_allow_html=True,
)
