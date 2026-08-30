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

.stApp {
    background: #050505;
    color: #f4f1e8;
}

.block-container {
    max-width: 1400px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

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
    margin-top: 10px;
    margin-bottom: 35px;
}

.cb-logo img {
    width: min(520px, 80%);
    max-height: 260px;
    object-fit: contain;
}


/* ============================================================
   GOLDENE LINIE
   ============================================================ */

.cb-gold-line {
    width: 100%;
    height: 1px;
    margin-bottom: 40px;

    background: linear-gradient(
        90deg,
        transparent,
        #8f641b,
        #d5a94f,
        #8f641b,
        transparent
    );

    box-shadow: 0 0 12px rgba(212, 160, 60, 0.35);
}


/* ============================================================
   MOTIVATION
   ============================================================ */

.cb-motivation {
    text-align: center;
    margin-bottom: 50px;
}

.cb-motivation-text {
    color: #d8b66a;
    font-family: Arial, Helvetica, sans-serif;
    font-size: clamp(18px, 2vw, 27px);
    font-weight: 500;
    letter-spacing: 0.18em;
    text-shadow: 0 0 10px rgba(212, 160, 60, 0.22);
}

.cb-motivation-line {
    width: min(600px, 75%);
    height: 1px;
    margin: 18px auto 0 auto;

    background: linear-gradient(
        90deg,
        transparent,
        #b48731,
        #e2bd63,
        #b48731,
        transparent
    );
}


/* ============================================================
   MENÜ
   ============================================================ */

.cb-card {
    background: linear-gradient(
        135deg,
        #161616,
        #090909
    );

    border: 1px solid rgba(172, 126, 39, 0.65);
    border-radius: 10px;

    padding: 25px 28px;

    min-height: 135px;

    margin-bottom: 24px;

    box-sizing: border-box;

    box-shadow:
        inset 0 0 0 1px rgba(255, 215, 120, 0.035),
        0 8px 30px rgba(0, 0, 0, 0.35);
}

.cb-card-icon {
    color: #d7ad54;
    font-size: 27px;
    margin-bottom: 12px;
}

.cb-card-title {
    color: #f0e7d1;
    font-size: 21px;
    font-weight: 600;
    letter-spacing: 0.04em;
    margin-bottom: 8px;
}

.cb-card-subtitle {
    color: #9c978c;
    font-size: 14px;
    line-height: 1.5;
}


/* ============================================================
   POSITIONSGRÖSSENRECHNER
   ============================================================ */

.cb-calculator {
    background: linear-gradient(
        135deg,
        #1e180c,
        #0a0a0a
    );

    border: 1px solid #a97924;
    border-radius: 10px;

    padding: 25px 28px;

    margin-top: 10px;
    margin-bottom: 20px;

    box-shadow:
        0 10px 35px rgba(0, 0, 0, 0.45),
        inset 0 0 25px rgba(194, 148, 58, 0.04);
}

.cb-calculator-icon {
    color: #ddb45d;
    font-size: 27px;
    margin-bottom: 12px;
}

.cb-calculator-title {
    color: #e5c275;
    font-size: 20px;
    font-weight: 600;
    margin-bottom: 7px;
}

.cb-calculator-subtitle {
    color: #a7a196;
    font-size: 14px;
}


/* ============================================================
   FOOTER
   ============================================================ */

.cb-footer {
    margin-top: 50px;
    padding-top: 15px;

    border-top: 1px solid rgba(170, 125, 38, 0.35);

    display: flex;
    justify-content: space-between;
    align-items: center;

    color: #77736a;

    font-size: 12px;
    letter-spacing: 0.05em;
}

.cb-footer-gold {
    color: #b78b38;
}


/* ============================================================
   MOBILE
   ============================================================ */

@media (max-width: 750px) {

    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .cb-motivation-text {
        font-size: 18px;
        letter-spacing: 0.08em;
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
        gap: 12px;
        text-align: center;
    }

}

</style>
""",
    unsafe_allow_html=True,
)


# ============================================================
# LOGO ANZEIGEN
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
        "<h1 style='text-align:center; "
        "color:#d8b66a;'>"
        "COUNT OR BREAK"
        "</h1>",
        unsafe_allow_html=True,
    )


# ============================================================
# GOLDENE TRENNLINIE
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

col1, col2 = st.columns(2)


# ============================================================
# JOURNAL
# ============================================================

with col1:

    st.markdown(
        "<div class='cb-card'>"
        "<div class='cb-card-icon'>▤</div>"
        "<div class='cb-card-title'>Journal</div>"
        "<div class='cb-card-subtitle'>"
        "Deine Trades. Deine Geschichte."
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
        "<div class='cb-card-title'>Auswertungen</div>"
        "<div class='cb-card-subtitle'>"
        "Deine Performance. Deine Erkenntnisse."
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
        "<div class='cb-card-title'>Strategien</div>"
        "<div class='cb-card-subtitle'>"
        "Deine Setups. Dein Plan."
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
        "<div class='cb-card-title'>Wissen</div>"
        "<div class='cb-card-subtitle'>"
        "Lernen. Verstehen. Wachsen."
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
    "<div class='cb-calculator-title'>"
    "Positionsgrößenrechner"
    "</div>"
    "<div class='cb-calculator-subtitle'>"
    "Berechne dein Risiko. Kontrolliere dein Handeln."
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
    "&nbsp; Risk first. Profits second."
    "</div>"
    "<div>"
    "Trading Journal"
    "&nbsp; • &nbsp;"
    "Risk Management"
    "&nbsp; • &nbsp;"
    "Performance"
    "</div>"
    "</div>",
    unsafe_allow_html=True,
)
