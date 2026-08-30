import streamlit as st
from pathlib import Path
import base64


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
# LOGO LADEN
# ============================================================

logo_path = Path("assets/countorbreak-logo.png")

logo_data = ""

if logo_path.exists():
    logo_bytes = logo_path.read_bytes()
    logo_base64 = base64.b64encode(logo_bytes).decode("utf-8")
    logo_data = f"data:image/png;base64,{logo_base64}"


# ============================================================
# MOTIVATIONSSPRUCH
# ============================================================

motivation = "DEIN VORTEIL LIEGT IN DER DISZIPLIN."


# ============================================================
# SEITEN-DESIGN
# ============================================================

st.markdown(
    f"""
    <style>

    /* ========================================================
       GRUNDLAYOUT
       ======================================================== */

    .stApp {{
        background:
            radial-gradient(
                circle at 50% 42%,
                rgba(120, 78, 8, 0.08) 0%,
                rgba(0, 0, 0, 0) 42%
            ),
            #030303;

        color: #f2f2f2;
    }}

    header {{
        visibility: hidden;
    }}

    footer {{
        visibility: hidden;
    }}

    #MainMenu {{
        visibility: hidden;
    }}

    .block-container {{
        max-width: 1500px !important;
        padding-top: 25px !important;
        padding-bottom: 35px !important;
        padding-left: 45px !important;
        padding-right: 45px !important;
    }}


    /* ========================================================
       GOLD-FARBEN
       ======================================================== */

    :root {{
        --gold-main: #d6a62a;
        --gold-light: #f6d36b;
        --gold-bright: #ffe29a;
        --gold-dark: #805b0c;
        --gold-border: rgba(214, 166, 42, 0.78);
        --black-card: rgba(8, 8, 8, 0.88);
    }}


    /* ========================================================
       HINTERGRUND-LOGO
       ======================================================== */

    .cb-background-logo {{
        position: fixed;
        left: 50%;
        top: 47%;
        transform: translate(-50%, -50%);

        width: min(1050px, 78vw);
        height: auto;

        opacity: 0.105;

        z-index: 0;

        pointer-events: none;

        filter:
            drop-shadow(0 0 35px rgba(190, 130, 20, 0.12));

        user-select: none;
    }}


    /* ========================================================
       FALLBACK, WENN LOGO NOCH NICHT HOCHGELADEN IST
       ======================================================== */

    .cb-logo-placeholder {{
        position: fixed;
        left: 50%;
        top: 47%;
        transform: translate(-50%, -50%);

        width: min(900px, 70vw);
        height: 440px;

        border: 1px solid rgba(214, 166, 42, 0.10);

        opacity: 0.18;

        z-index: 0;

        pointer-events: none;

        box-shadow:
            inset 0 0 100px rgba(150, 100, 15, 0.05);
    }}


    /* ========================================================
       ALLE INHALTE ÜBER DEN HINTERGRUND
       ======================================================== */

    .cb-content {{
        position: relative;
        z-index: 5;
    }}


    /* ========================================================
       OBERE GOLDLINIE
       ======================================================== */

    .cb-top-line {{
        width: 100%;
        height: 1px;

        margin: 5px auto 35px auto;

        background:
            linear-gradient(
                90deg,
                transparent,
                rgba(214, 166, 42, 0.15),
                rgba(246, 211, 107, 0.75),
                rgba(214, 166, 42, 0.15),
                transparent
            );

        position: relative;
    }}

    .cb-top-line::after {{
        content: "";

        position: absolute;

        left: 50%;
        top: 50%;

        width: 9px;
        height: 9px;

        transform:
            translate(-50%, -50%)
            rotate(45deg);

        background: var(--gold-light);

        box-shadow:
            0 0 12px rgba(246, 211, 107, 0.75);
    }}


    /* ========================================================
       MOTIVATION
       ======================================================== */

    .cb-motivation {{
        text-align: center;

        margin-bottom: 30px;
    }}

    .cb-motivation-text {{
        font-family:
            Arial,
            Helvetica,
            sans-serif;

        font-size: clamp(30px, 3.5vw, 58px);

        font-weight: 800;

        letter-spacing: 0.10em;

        line-height: 1.08;

        color: var(--gold-light);

        text-shadow:
            0 0 18px rgba(214, 166, 42, 0.18),
            0 0 45px rgba(214, 166, 42, 0.07);
    }}

    .cb-motivation-line {{
        width: min(780px, 70%);

        height: 1px;

        margin: 28px auto 0 auto;

        background:
            linear-gradient(
                90deg,
                transparent,
                rgba(214, 166, 42, 0.25),
                rgba(246, 211, 107, 0.9),
                rgba(214, 166, 42, 0.25),
                transparent
            );

        position: relative;
    }}

    .cb-motivation-line::after {{
        content: "";

        position: absolute;

        left: 50%;
        top: 50%;

        width: 11px;
        height: 11px;

        transform:
            translate(-50%, -50%)
            rotate(45deg);

        background: var(--gold-light);

        box-shadow:
            0 0 16px rgba(246, 211, 107, 0.85);
    }}


    /* ========================================================
       POSITIONSGRÖSSENRECHNER
       ======================================================== */

    .cb-position-wrapper {{
        width: min(930px, 76%);

        margin: 0 auto 70px auto;
    }}

    .cb-position-card {{
        min-height: 125px;

        display: flex;

        align-items: center;

        padding: 22px 30px;

        background:
            linear-gradient(
                135deg,
                rgba(25, 20, 10, 0.96),
                rgba(5, 5, 5, 0.96)
            );

        border: 1px solid var(--gold-border);

        border-radius: 18px;

        box-shadow:
            0 0 0 1px rgba(214, 166, 42, 0.04),
            0 12px 45px rgba(0, 0, 0, 0.55),
            inset 0 0 35px rgba(214, 166, 42, 0.035);

        transition:
            transform 0.2s ease,
            border-color 0.2s ease,
            box-shadow 0.2s ease;
    }}

    .cb-position-card:hover {{
        transform: translateY(-2px);

        border-color: var(--gold-light);

        box-shadow:
            0 0 25px rgba(214, 166, 42, 0.12),
            0 18px 55px rgba(0, 0, 0, 0.65);
    }}

    .cb-position-icon {{
        width: 68px;
        height: 68px;

        flex-shrink: 0;

        display: flex;
        align-items: center;
        justify-content: center;

        border: 1px solid var(--gold-border);

        border-radius: 50%;

        color: var(--gold-light);

        font-size: 30px;

        margin-right: 26px;

        box-shadow:
            inset 0 0 20px rgba(214, 166, 42, 0.05);
    }}

    .cb-position-content {{
        flex: 1;
    }}

    .cb-position-title {{
        color: var(--gold-light);

        font-size: 23px;

        font-weight: 800;

        letter-spacing: 0.13em;

        text-transform: uppercase;

        margin-bottom: 8px;
    }}

    .cb-position-subtitle {{
        color: rgba(240, 240, 240, 0.72);

        font-size: 16px;

        letter-spacing: 0.02em;
    }}

    .cb-position-arrow {{
        color: var(--gold-light);

        font-size: 34px;

        font-weight: 300;

        margin-left: 25px;
    }}


    /* ========================================================
       MENÜ-GRID
       ======================================================== */

    .cb-menu-grid {{
        display: grid;

        grid-template-columns:
            repeat(2, minmax(0, 1fr));

        gap: 28px;

        width: 100%;

        margin: 0 auto;
    }}


    /* ========================================================
       MENÜ-KARTEN
       ======================================================== */

    .cb-card {{
        min-height: 155px;

        display: flex;

        align-items: center;

        padding: 26px 30px;

        background:
            linear-gradient(
                135deg,
                rgba(22, 18, 10, 0.94),
                rgba(5, 5, 5, 0.96)
            );

        border: 1px solid rgba(214, 166, 42, 0.70);

        border-radius: 18px;

        box-shadow:
            0 12px 38px rgba(0, 0, 0, 0.48),
            inset 0 0 30px rgba(214, 166, 42, 0.025);

        transition:
            transform 0.22s ease,
            border-color 0.22s ease,
            box-shadow 0.22s ease;

        cursor: pointer;
    }}

    .cb-card:hover {{
        transform: translateY(-3px);

        border-color: var(--gold-light);

        box-shadow:
            0 0 30px rgba(214, 166, 42, 0.11),
            0 18px 50px rgba(0, 0, 0, 0.60);
    }}


    /* ========================================================
       PIKTOGRAMME
       ======================================================== */

    .cb-icon {{
        width: 68px;
        height: 68px;

        flex-shrink: 0;

        display: flex;
        align-items: center;
        justify-content: center;

        border: 1px solid rgba(214, 166, 42, 0.82);

        border-radius: 50%;

        color: var(--gold-light);

        margin-right: 25px;

        box-shadow:
            inset 0 0 18px rgba(214, 166, 42, 0.04);

        font-size: 28px;

        line-height: 1;
    }}


    /* ========================================================
       KARTEN-INHALT
       ======================================================== */

    .cb-card-content {{
        flex: 1;
    }}

    .cb-card-title {{
        color: var(--gold-light);

        font-size: 22px;

        font-weight: 800;

        letter-spacing: 0.13em;

        text-transform: uppercase;

        margin-bottom: 9px;
    }}

    .cb-card-subtitle {{
        color: rgba(240, 240, 240, 0.70);

        font-size: 16px;

        line-height: 1.45;

        letter-spacing: 0.015em;
    }}

    .cb-arrow {{
        color: var(--gold-light);

        font-size: 34px;

        font-weight: 300;

        margin-left: 20px;

        transition:
            transform 0.2s ease;
    }}

    .cb-card:hover .cb-arrow {{
        transform: translateX(5px);
    }}


    /* ========================================================
       FOOTER
       ======================================================== */

    .cb-footer {{
        display: flex;

        justify-content: space-between;

        align-items: center;

        margin-top: 65px;

        padding-top: 22px;

        border-top: 1px solid rgba(214, 166, 42, 0.20);

        color: rgba(235, 235, 235, 0.55);

        font-size: 13px;

        letter-spacing: 0.09em;

        text-transform: uppercase;
    }}

    .cb-footer-left {{
        display: flex;

        align-items: center;

        gap: 12px;
    }}

    .cb-footer-shield {{
        color: var(--gold-light);

        font-size: 22px;
    }}

    .cb-footer-right {{
        text-align: right;
    }}


    /* ========================================================
       MOBILE
       ======================================================== */

    @media (max-width: 900px) {{

        .block-container {{
            padding-left: 20px !important;
            padding-right: 20px !important;
        }}

        .cb-menu-grid {{
            grid-template-columns: 1fr;
        }}

        .cb-position-wrapper {{
            width: 100%;
        }}

        .cb-motivation-text {{
            font-size: 31px;
        }}

        .cb-footer {{
            flex-direction: column;

            gap: 18px;

            text-align: center;
        }}

        .cb-footer-right {{
            text-align: center;
        }}
    }}


    @media (max-width: 600px) {{

        .cb-card {{
            min-height: 130px;

            padding: 20px;
        }}

        .cb-icon {{
            width: 55px;
            height: 55px;

            margin-right: 16px;

            font-size: 23px;
        }}

        .cb-card-title {{
            font-size: 17px;
        }}

        .cb-card-subtitle {{
            font-size: 13px;
        }}

        .cb-position-card {{
            padding: 20px;
        }}

        .cb-position-icon {{
            width: 55px;
            height: 55px;

            margin-right: 16px;
        }}

        .cb-position-title {{
            font-size: 17px;
        }}

        .cb-position-subtitle {{
            font-size: 13px;
        }}

        .cb-background-logo {{
            width: 115vw;
        }}
    }}

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# STARTSEITE
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


st.markdown(
    f"""
    <div class="cb-content">

        <!-- OBERE LINIE -->

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


        <!-- MENÜ -->

        <div class="cb-menu-grid">


            <!-- JOURNAL -->

            <div class="cb-card">

                <div class="cb-icon">
                    ♧
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

                <span class="cb-footer-shield">
                    ♢
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
