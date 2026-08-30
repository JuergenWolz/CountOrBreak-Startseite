import streamlit as st
from pathlib import Path


st.set_page_config(
    page_title="CountOrBreak",
    page_icon="♢",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# DESIGN
# ============================================================

st.markdown("""
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


/* LOGO */

.logo-container {
    text-align: center;
    margin-top: 10px;
    margin-bottom: 35px;
}

.logo-container img {
    width: min(520px, 80%);
    max-height: 260px;
    object-fit: contain;
}


/* GOLDENE LINIE */

.gold-line {
    height: 1px;
    width: 100%;
    margin-bottom: 40px;

    background: linear-gradient(
        90deg,
        transparent,
        #8f641b,
        #d5a94f,
        #8f641b,
        transparent
    );
}


/* MOTIVATION */

.motivation {
    text-align: center;
    margin-bottom: 50px;
}

.motivation-text {
    color: #d8b66a;
    font-family: Arial, Helvetica, sans-serif;
    font-size: clamp(18px, 2vw, 27px);
    font-weight: 500;
    letter-spacing: 0.18em;
}

.motivation-line {
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


/* KARTEN */

.card {
    background: linear-gradient(
        135deg,
        #161616,
        #090909
    );

    border: 1px solid #8f641b;
    border-radius: 10px;

    padding: 25px;

    min-height: 135px;

    margin-bottom: 24px;

    box-sizing: border-box;
}

.icon {
    color: #d7ad54;
    font-size: 27px;
    margin-bottom: 12px;
}

.title {
    color: #f0e7d1;
    font-size: 21px;
    font-weight: 600;
    margin-bottom: 8px;
}

.subtitle {
    color: #9c978c;
    font-size: 14px;
    line-height: 1.5;
}


/* RECHNER */

.calculator {
    background: linear-gradient(
        135deg,
        #1e180c,
        #0a0a0a
    );

    border: 1px solid #a97924;
    border-radius: 10px;

    padding: 25px;

    margin-top: 10px;
}

.calculator-title {
    color: #e5c275;
    font-size: 20px;
    font-weight: 600;
    margin-bottom: 7px;
}

.calculator-subtitle {
    color: #a7a196;
    font-size: 14px;
}


/* FOOTER */

.footer {
    margin-top: 50px;
    padding-top: 15px;

    border-top: 1px solid #4d3a18;

    display: flex;
    justify-content: space-between;

    color: #77736a;

    font-size: 12px;
}

.footer-gold {
    color: #b78b38;
}


@media (max-width: 750px) {

    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .motivation-text {
        font-size: 17px;
        letter-spacing: 0.08em;
    }

    .title {
        font-size: 18px;
    }

    .footer {
        flex-direction: column;
        gap: 12px;
        text-align: center;
    }

}

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOGO
# ============================================================

logo_path = Path("countorbreak_logo.png")

if logo_path.exists():

    st.markdown(
        """
        <div class="logo-container">
            <img src="data:image/png;base64,PLACEHOLDER">
        </div>
        """.replace(
            "PLACEHOLDER",
            __import__("base64").b64encode(
                logo_path.read_bytes()
            ).decode()
        ),
        unsafe_allow_html=True,
    )

else:

    st.markdown(
        """
        <div style="
            text-align:center;
            color:#d8b66a;
            font-size:28px;
            margin-bottom:40px;
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
    '<div class="gold-line"></div>',
    unsafe_allow_html=True,
)


# ============================================================
# MOTIVATION
# ============================================================

st.markdown(
    """
    <div class="motivation">

        <div class="motivation-text">
            TRADE DEN PLAN. NICHT DIE EMOTION.
        </div>

        <div class="motivation-line"></div>

    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# MENÜ
# ============================================================

col1, col2 = st.columns(2)


with col1:

    st.markdown(
        """
        <div class="card">

            <div class="icon">▤</div>

            <div class="title">
                Journal
            </div>

            <div class="subtitle">
                Deine Trades. Deine Geschichte.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


with col2:

    st.markdown(
        """
        <div class="card">

            <div class="icon">▥</div>

            <div class="title">
                Auswertungen
            </div>

            <div class="subtitle">
                Deine Performance. Deine Erkenntnisse.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


with col1:

    st.markdown(
        """
        <div class="card">

            <div class="icon">♞</div>

            <div class="title">
                Strategien
            </div>

            <div class="subtitle">
                Deine Setups. Dein Plan.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


with col2:

    st.markdown(
        """
        <div class="card">

            <div class="icon">◇</div>

            <div class="title">
                Wissen
            </div>

            <div class="subtitle">
                Lernen. Verstehen. Wachsen.
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
    <div class="calculator">

        <div class="icon">▦</div>

        <div class="calculator-title">
            Positionsgrößenrechner
        </div>

        <div class="calculator-subtitle">
            Berechne dein Risiko. Kontrolliere dein Handeln.
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
    <div class="footer">

        <div>
            <span class="footer-gold">♢</span>
            &nbsp;
            Risk first. Profits second.
        </div>

        <div>
            Trading Journal
            &nbsp; • &nbsp;
            Risk Management
            &nbsp; • &nbsp;
            Performance
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)
