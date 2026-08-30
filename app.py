import streamlit as st
from pathlib import Path
import base64


# ============================================================
# COUNT OR BREAK – STARTSEITE
# ============================================================

st.set_page_config(
    page_title="CountOrBreak",
    page_icon="♢",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# LOGO
# ============================================================

logo_path = Path("countorbreak_logo.png")


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
            rgba(212, 160, 60, 0.08),
            transparent 32%
        ),
        #050505;

    color: #f4f1e8;
}

.block-container {
    max-width: 1450px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}


/* Streamlit UI ausblenden */

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
    text-align: center;
    margin-top: 5px;
    margin-bottom: 28px;
}

.cb-logo img {
    width: min(520px, 82%);
    max-height: 260px;
    object-fit: contain;
}


/* ============================================================
   GOLDENE TRENNLINIE
   ============================================================ */

.cb-gold-line {
    width: 100%;
    height: 1px;

    margin: 0 auto 34px auto;

    background:
        linear-gradient(
            90deg,
            transparent 0%,
            #6f4a10 18%,
            #b98a32 38%,
            #f0c866 50%,
            #b98a32 62%,
            #6f4a10 82%,
            transparent 100%
        );

    box-shadow:
        0 0 8px rgba(212, 160, 60, 0.35),
        0 0 18px rgba(212, 160, 60, 0.12);
}


/* ============================================================
   MOTIVATION
   ============================================================ */

.cb-motivation {
    text-align: center;
    margin-bottom: 32px;
}

.cb-motivation-text {
    color: #d9ad4f;

    font-family:
        Georgia,
        "Times New Roman",
        serif;

    font-size: clamp(17px, 1.8vw, 25px);

    font-weight: 500;

    letter-spacing: 0.24em;

    text-shadow:
        0 0 10px rgba(212, 160, 60, 0.22);
}

.cb-motivation-line {
    width: min(500px, 70%);
    height: 1px;

    margin: 16px auto 0 auto;

    background:
        linear-gradient(
            90deg,
            transparent,
            #8f641b,
            #e2bd63,
            #8f641b,
            transparent
        );
}


/* ============================================================
   MENÜ-KARTEN
   ============================================================ */

.cb-card {
    position: relative;

    width: 100%;
    min-height: 145px;

    box-sizing: border-box;

    display: flex;
    align-items: center;

    padding: 24px 30px;

    margin-bottom: 24px;

    background:
        linear-gradient(
            135deg,
            rgba(24, 24, 24, 0.98),
            rgba(8, 8, 8, 0.98)
        );

    border: 1px solid rgba(191, 145, 47, 0.85);

    border-radius: 12px;

    box-shadow:
        inset 0 0 0 1px rgba(255, 215, 120, 0.025),
        0 10px 35px rgba(0, 0, 0, 0.45);

    transition:
        transform 0.2s ease,
        border-color 0.2s ease,
        box-shadow 0.2s ease;
}

.cb-card:hover {
    transform: translateY(-3px);

    border-color: #e1b653;

    box-shadow:
        0 12px 38px rgba(0, 0, 0, 0.55),
        0 0 22px rgba(207, 157, 48, 0.15);
}


/* ============================================================
   KARTEN-ICON
   ============================================================ */

.cb-card-icon {
    width: 76px;
    min-width: 76px;
    height: 76px;

    display: flex;
    align-items: center;
    justify-content: center;

    margin-right: 27px;

    border: 1px solid #b98a32;

    border-radius: 12px;

    color: #e0b452;

    font-size: 35px;

    background:
        radial-gradient(
            circle,
            rgba(181, 132, 42, 0.13),
            rgba(15, 15, 15, 0.9)
        );

    box-shadow:
        inset 0 0 18px rgba(194, 148, 58, 0.06),
        0 0 12px rgba(194, 148, 58, 0.05);
}


/* ============================================================
   KARTEN-TEXT
   ============================================================ */

.cb-card-content {
    flex: 1;
}

.cb-card-title {
    color: #eee4ce;

    font-family:
        Georgia,
        "Times New Roman",
        serif;

    font-size: 25px;

    font-weight: 500;

    letter-spacing: 0.03em;

    margin-bottom: 8px;
}

.cb-card-subtitle {
    color: #b3ada1;

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

.cb-card-arrow {
    color: #d5a448;

    font-size: 44px;

    font-family: Arial, Helvetica, sans-serif;

    font-weight: 200;

    margin-left: 20px;

    transition:
        transform 0.2s ease,
        color 0.2s ease;
}

.cb-card:hover .cb-card-arrow {
    color: #f0c866;
    transform: translateX(5px);
}


/* ============================================================
   POSITIONSGRÖSSENRECHNER
   ============================================================ */

.cb-calculator {
    position: relative;

    width: 100%;

    min-height: 135px;

    box-sizing: border-box;

    display: flex;
    align-items: center;

    padding: 24px 30px;

    margin-top: 3px;

    background:
        linear-gradient(
            135deg,
            rgba(34, 27, 13, 0.98),
            rgba(8, 8, 8, 0.98)
        );

    border: 1px solid #c09236;

    border-radius: 12px;

    box-shadow:
        0 10px 38px rgba(0, 0, 0, 0.5),
        0 0 18px rgba(196, 147, 46, 0.10),
        inset 0 0 28px rgba(194, 148, 58, 0.035);
}

.cb-calculator-icon {
    width: 76px;
    min-width: 76px;
    height: 76px;

    display: flex;
    align-items: center;
    justify-content: center;

    margin-right: 27px;

    border: 1px solid #c09236;

    border-radius: 12px;

    color: #e3b654;

    font-size: 34px;
}

.cb-calculator-content {
    flex: 1;
}

.cb-calculator-title {
    color: #e5c275;

    font-family:
        Georgia,
        "Times New Roman",
        serif;

    font-size: 25px;

    font-weight: 500;

    margin-bottom: 8px;
}

.cb-calculator-subtitle {
    color: #b5aea1;

    font-family:
        Arial,
        Helvetica,
        sans-serif;

    font-size: 14px;
}

.cb-calculator-arrow {
    color: #d5a448;

    font-size: 44px;

    margin-left: 20px;
}


/* ============================================================
   FOOTER
   ============================================================ */

.cb-footer {
    width: 100%;

    margin-top: 30px;
    padding-top: 18px;

    border-top: 1px solid rgba(165, 119, 35, 0.42);

    display: flex;
    justify-content: space-between;
    align-items: center;

    color: #858077;

    font-family:
        Arial,
        Helvetica,
        sans-serif;

    font-size: 12px;

    letter-spacing: 0.04em;
}

.cb-footer-gold {
    color: #c0943d;

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

    .cb-logo {
        margin-bottom: 25px;
    }

    .cb-logo img {
        width: 90%;
    }

    .cb-motivation-text {
        font-size: 17px;
        letter-spacing: 0.10em;
    }

    .cb-card {
        min-height: 120px;
        padding: 20px;
    }

    .cb-card-icon,
    .cb-calculator-icon {
        width: 58px;
        min-width: 58px;
        height: 58px;

        margin-right: 18px;

        font-size: 27px;
    }

    .cb-card-title,
    .cb-calculator-title {
        font-size: 19px;
    }

    .cb-card-subtitle,
    .cb-calculator-subtitle {
        font-size: 13px;
    }

    .cb-card-arrow,
    .cb-calculator-arrow {
        font-size: 32px;
        margin-left: 10px;
    }

    .cb-calculator {
        min-height: 120px;
        padding: 20px;
    }

    .cb-footer {
        flex-direction: column;
        gap: 14px;
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

if logo_path.exists():

    logo_data = base64.b64encode(
        logo_path.read_bytes()
    ).decode("utf-8")

    logo_html = (
        "<div class='cb-logo'>"
        "<img src='data:image/png;base64,"
        + logo_data
        + "' alt='CountOrBreak Logo'>"
        "</div>"
    )

    st.markdown(
        logo_html,
        unsafe_allow_html=True,
    )

else:

    st.markdown(
        """
        <div style="
            text-align:center;
            color:#d8b66a;
            font-size:30px;
            margin-bottom:35px;
        ">
            COUNT OR BREAK
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# GOLDENE LINIE
# ============================================================

st.markdown(
    "<div class='cb-gold-line'></div>",
    unsafe_allow_html=True,
)


# ============================================================
# MOTIVATION
# ============================================================

st.markdown(
    "<div class='cb-motivation'>"
    "<div class='cb-motivation-text'>"
    "TRADE DEN PLAN. NICHT DIE EMOTION."
    "</div>"
    "<div class='cb-motivation-line'></div>"
    "</div>",
    unsafe_allow_html=True,
)


# ============================================================
# HAUPTMENÜ
# ============================================================

col1, col2 = st.columns(
    2,
    gap="large"
)


# ============================================================
# JOURNAL
# ============================================================

with col1:

    st.markdown(
        "<div class='cb-card'>"
        "<div class='cb-card-icon'>▤</div>"
        "<div class='cb-card-content'>"
        "<div class='cb-card-title'>"
        "Journal"
        "</div>"
        "<div class='cb-card-subtitle'>"
        "Deine Trades. Deine Geschichte."
        "</div>"
        "</div>"
        "<div class='cb-card-arrow'>"
        "›"
        "</div>"
        "</div>",
        unsafe_allow_html=True,
    )


# ============================================================
# AUSWERTUNGEN
# ============================================================

with col2:

    st.markdown(
        "<div class='cb-card'>"
        "<div class='cb-card-icon'>▥</div>"
        "<div class='cb-card-content'>"
        "<div class='cb-card-title'>"
        "Auswertungen"
        "</div>"
        "<div class='cb-card-subtitle'>"
        "Deine Performance. Deine Erkenntnisse."
        "</div>"
        "</div>"
        "<div class='cb-card-arrow'>"
        "›"
        "</div>"
        "</div>",
        unsafe_allow_html=True,
    )


# ============================================================
# STRATEGIEN
# ============================================================

with col1:

    st.markdown(
        "<div class='cb-card'>"
        "<div class='cb-card-icon'>♞</div>"
        "<div class='cb-card-content'>"
        "<div class='cb-card-title'>"
        "Strategien"
        "</div>"
        "<div class='cb-card-subtitle'>"
        "Deine Setups. Dein Plan."
        "</div>"
        "</div>"
        "<div class='cb-card-arrow'>"
        "›"
        "</div>"
        "</div>",
        unsafe_allow_html=True,
    )


# ============================================================
# WISSEN
# ============================================================

with col2:

    st.markdown(
        "<div class='cb-card'>"
        "<div class='cb-card-icon'>◇</div>"
        "<div class='cb-card-content'>"
        "<div class='cb-card-title'>"
        "Wissen"
        "</div>"
        "<div class='cb-card-subtitle'>"
        "Lernen. Verstehen. Wachsen."
        "</div>"
        "</div>"
        "<div class='cb-card-arrow'>"
        "›"
        "</div>"
        "</div>",
        unsafe_allow_html=True,
    )


# ============================================================
# POSITIONSGRÖSSENRECHNER
# ============================================================

st.markdown(
    "<div class='cb-calculator'>"
    "<div class='cb-calculator-icon'>▦</div>"
    "<div class='cb-calculator-content'>"
    "<div class='cb-calculator-title'>"
    "Positionsgrößenrechner"
    "</div>"
    "<div class='cb-calculator-subtitle'>"
    "Berechne dein Risiko. Kontrolliere dein Handeln."
    "</div>"
    "</div>"
    "<div class='cb-calculator-arrow'>"
    "›"
    "</div>"
    "</div>",
    unsafe_allow_html=True,
)


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    "<div class='cb-footer'>"
    "<div>"
    "<span class='cb-footer-gold'>♢</span>"
    "&nbsp;&nbsp;"
    "Risk first. Profits second."
    "</div>"
    "<div class='cb-footer-right'>"
    "Trading Journal"
    "&nbsp;&nbsp; • &nbsp;&nbsp;"
    "Risk Management"
    "&nbsp;&nbsp; • &nbsp;&nbsp;"
    "Performance"
    "</div>"
    "</div>",
    unsafe_allow_html=True,
)
