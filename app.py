import time
import base64
import textwrap
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="For My Birthday Boy 💜",
    page_icon="💜",
    layout="centered",
    initial_sidebar_state="collapsed",
)

ASSETS = Path(__file__).parent / "assets"

# =========================================================================
# ✍️  THE FINAL LETTER
# Replace the text below (between the triple quotes) with your own words
# whenever you're ready. Everything else in the app will update itself.
# =========================================================================
FINAL_LETTER = """
Hi bunny,

Happiest birthday to you, my love. I hope you get everything you've
wished for — and so much more — in the year ahead. There's so much I
want to say today, and somehow none of the words feel big enough. So
let me start with the simplest one: thank you.

Thank you for being exactly who you are. Thank you for caring the way
you do, and for making the world feel a little softer for everyone
around you.

I know we're far apart right now, but I hope today is full of love
and laughter, with your whole heart in it. Building this little app
was just a small gesture to make you feel a bit more special today.

Here's to the best year ahead — and to celebrating many, many more
birthdays together, in the most loving way possible.

Happiest birthday, baby.

— suhu
"""
# =========================================================================


def md(html: str):
    """Render a (possibly indented) multi-line HTML/SVG string safely.

    Streamlit's markdown parser treats any HTML block whose first line is
    indented 4+ spaces as a literal code block instead of parsing it as
    HTML — which is why raw markup could show up on screen. Dedenting
    before rendering fixes that everywhere in this app.
    """
    st.markdown(textwrap.dedent(html).strip("\n"), unsafe_allow_html=True)


st.markdown('<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">', unsafe_allow_html=True)

# ---------- Styling ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,600&family=Dancing+Script:wght@600;700&family=Poppins:wght@300;400;500;600;700&display=swap');

:root {
    --lavender-100: #faf5ff;
    --lavender-200: #f1e3fb;
    --lavender-300: #e6d1f5;
    --purple-400: #b98ee0;
    --purple-500: #9b5cc7;
    --purple-600: #7c3fa8;
    --purple-700: #5e2b83;
    --pink-300: #ffd1e3;
    --pink-400: #ff9fc4;
    --pink-500: #f2699e;
    --ink: #4a2a63;
    --ink-soft: #6d4a86;
    --white: #ffffff;
}

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 12% 8%, rgba(255, 159, 196, .30), transparent 32%),
        radial-gradient(circle at 88% 15%, rgba(185, 142, 224, .28), transparent 34%),
        radial-gradient(circle at 20% 90%, rgba(230, 209, 245, .55), transparent 38%),
        radial-gradient(circle at 90% 85%, rgba(255, 209, 227, .35), transparent 36%),
        linear-gradient(160deg, #fdf6ff 0%, #f6ebfc 35%, #f1e3fb 65%, #fdf3f8 100%);
    color: var(--ink);
}

.block-container {
    max-width: 760px;
    padding-top: .9rem;
    padding-bottom: 2.5rem;
    position: relative;
    z-index: 2;
}

/* tighten default gap between stacked widgets across the app */
div[data-testid="stVerticalBlock"] {
    gap: .45rem;
}

h1, h2, h3 {
    font-family: 'Cormorant Garamond', serif !important;
    letter-spacing: .3px;
    color: var(--purple-700) !important;
}

p, div, label, span, li {
    color: var(--ink);
}

/* ---------- floating hearts background ---------- */
.hearts-bg {
    position: fixed;
    inset: 0;
    overflow: hidden;
    pointer-events: none;
    z-index: 0;
}
.heart-float {
    position: absolute;
    bottom: -10%;
    font-size: 1.6rem;
    opacity: .55;
    animation: floatUp linear infinite;
    filter: drop-shadow(0 0 6px rgba(184, 110, 214, .25));
}
@keyframes floatUp {
    0%   { transform: translateY(0) translateX(0) rotate(0deg); opacity: 0; }
    10%  { opacity: .6; }
    50%  { transform: translateY(-55vh) translateX(20px) rotate(12deg); }
    90%  { opacity: .35; }
    100% { transform: translateY(-105vh) translateX(-15px) rotate(-10deg); opacity: 0; }
}

/* ---------- hero (page 1): 8 hanging photos + centered text ---------- */
.eyebrow {
    color: var(--pink-500);
    text-transform: uppercase;
    letter-spacing: 3px;
    font-size: .72rem;
    font-weight: 600;
}

.photo-collage {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1.35rem .7rem;
    padding: 1rem .35rem 1.3rem;
    margin-bottom: .2rem;
}
.hanging-photo {
    position: relative;
    display: flex;
    justify-content: center;
    padding-top: 18px;
}
.hanging-photo::before {
    content: "";
    position: absolute;
    top: 0;
    left: 50%;
    width: 2px;
    height: 20px;
    background: rgba(94, 43, 131, .45);
    transform: translateX(-50%);
}
.hanging-photo::after {
    content: "•";
    position: absolute;
    top: -10px;
    left: 50%;
    transform: translateX(-50%);
    color: var(--purple-700);
    font-size: 1.2rem;
    line-height: 1;
}
.hanging-photo img {
    width: clamp(68px, 16vw, 112px);
    height: clamp(68px, 16vw, 112px);
    object-fit: cover;
    border-radius: 12px;
    border: 4px solid var(--white);
    box-shadow: 0 10px 22px rgba(124, 63, 168, .26);
    display: block;
}
.hanging-photo:nth-child(4n+1) { transform: rotate(-5deg); }
.hanging-photo:nth-child(4n+2) { transform: rotate(4deg) translateY(7px); }
.hanging-photo:nth-child(4n+3) { transform: rotate(-3deg) translateY(3px); }
.hanging-photo:nth-child(4n+4) { transform: rotate(5deg) translateY(-4px); }

@media (max-width: 520px) {
    .photo-collage {
        grid-template-columns: repeat(4, 1fr);
        gap: 1.05rem .35rem;
        padding-left: 0;
        padding-right: 0;
    }
    .hanging-photo img {
        width: clamp(60px, 21vw, 88px);
        height: clamp(60px, 21vw, 88px);
    }
}

.hero-center {
    text-align: center;
    padding: .1rem 1rem .3rem;
}
.hero-center h1 {
    font-size: clamp(1.9rem, 6.4vw, 3.4rem);
    line-height: 1.1;
    margin: .4rem 0 .6rem;
    background: linear-gradient(100deg, var(--purple-600), var(--pink-500) 55%, var(--purple-500));
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
}
.hero-center .subtitle {
    max-width: 520px;
    margin: 0 auto;
    color: var(--ink-soft);
    font-size: .98rem;
    line-height: 1.7;
    text-align: center;
}

.divider-heart {
    text-align: center;
    font-size: 1.05rem;
    margin: .8rem 0;
    color: var(--pink-500);
    letter-spacing: 10px;
}

/* ---------- cards ---------- */
.card {
    background: rgba(255,255,255,.72);
    backdrop-filter: blur(6px);
    border: 1px solid rgba(185, 142, 224, .35);
    border-radius: 22px;
    padding: 1.2rem 1.35rem;
    margin: .7rem 0;
    box-shadow: 0 12px 34px rgba(124, 63, 168, .12);
    color: var(--ink);
    text-align: left;
}

.card b { color: var(--purple-600); }

.quote {
    font-family: 'Dancing Script', cursive;
    font-weight: 700;
    font-size: 1.8rem;
    line-height: 1.4;
    color: var(--purple-700);
    text-align: center;
    padding: .9rem .5rem;
}

.small {
    color: var(--ink-soft);
    font-size: .92rem;
    line-height: 1.7;
    text-align: left;
}

/* ---------- quiz page ---------- */
.quiz-q {
    font-family: 'Cormorant Garamond', serif;
    font-weight: 700;
    font-size: clamp(1.2rem, 3.8vw, 1.45rem);
    color: var(--purple-700);
    margin: .55rem 0 .2rem;
    line-height: 1.25;
    text-align: left;
}
div[data-testid="stRadio"] {
    margin-bottom: -.3rem;
}
div[data-testid="stRadio"] > div {
    background: rgba(255,255,255,.55);
    padding: .4rem .65rem;
    border-radius: 16px;
    border: 1px solid rgba(185, 142, 224, .3);
    gap: .1rem;
}
div[data-testid="stRadio"] label,
div[data-testid="stRadio"] p {
    color: var(--ink) !important;
    font-weight: 500;
    font-size: .96rem;
}

/* ---------- photo memories (left photo / right text) ---------- */
.photo-frame {
    background: var(--white);
    border-radius: 24px;
    padding: 10px;
    box-shadow: 0 16px 40px rgba(124, 63, 168, .18);
    border: 1px solid rgba(255,255,255,.9);
    position: relative;
}

[data-testid="stImage"] img {
    border-radius: 16px;
}

.mem-text-wrap {
    height: 100%;
    display: flex;
    align-items: center;
    margin-top: .6rem;
}

.mem-text-card {
    background: rgba(255,255,255,.72);
    backdrop-filter: blur(6px);
    border: 1px solid rgba(185, 142, 224, .35);
    border-radius: 20px;
    padding: 1.1rem 1.2rem;
    box-shadow: 0 12px 32px rgba(124, 63, 168, .12);
    text-align: left;
    width: 100%;
}

.mem-text-card .mem-tag {
    color: var(--pink-500);
    text-transform: uppercase;
    letter-spacing: 2px;
    font-size: .66rem;
    font-weight: 600;
}

.mem-text-card h3 {
    margin: .2rem 0 .35rem;
    font-size: clamp(1.1rem, 3.6vw, 1.3rem);
    text-align: left;
}

.mem-text-card p {
    color: var(--ink-soft);
    margin: 0;
    font-size: .92rem;
    line-height: 1.6;
    text-align: left;
}

.missing-photo {
    text-align: center;
    padding: 2.2rem 1rem;
    color: var(--purple-500);
    background: rgba(255,255,255,.6);
    border: 1px dashed var(--purple-400);
    border-radius: 20px;
    font-size: .88rem;
}

.memory-row {
    margin-bottom: 1.4rem;
}

/* ---------- "things I hope you never forget" grid ---------- */
.points-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: .6rem;
    margin: .5rem 0 .3rem;
}
.point-card {
    background: rgba(255,255,255,.72);
    backdrop-filter: blur(6px);
    border: 1px solid rgba(185, 142, 224, .35);
    border-radius: 16px;
    padding: .85rem 1rem;
    box-shadow: 0 10px 26px rgba(124, 63, 168, .1);
    display: flex;
    gap: .55rem;
    align-items: flex-start;
    text-align: left;
}
.point-card .point-num {
    font-family: 'Cormorant Garamond', serif;
    font-weight: 700;
    font-size: 1.35rem;
    color: var(--pink-500);
    line-height: 1;
    flex-shrink: 0;
}
.point-card .point-text {
    font-size: 1.02rem;
    line-height: 1.45;
    color: var(--ink);
    font-weight: 500;
    text-align: left;
}

/* ---------- love letter ---------- */
.letter-card {
    background: linear-gradient(180deg, rgba(255,255,255,.92), rgba(250, 240, 255, .85));
    border: 1px solid rgba(185, 142, 224, .4);
    border-radius: 24px;
    padding: 1.8rem 1.6rem;
    box-shadow: 0 18px 48px rgba(124, 63, 168, .16);
    position: relative;
}

.letter-card::before {
    content: "💌";
    position: absolute;
    top: -16px;
    left: 50%;
    transform: translateX(-50%);
    font-size: 1.8rem;
    background: var(--lavender-100);
    padding: 4px 12px;
    border-radius: 50%;
}

.letter-text {
    font-family: 'Cormorant Garamond', serif;
    font-style: italic;
    font-size: 1.16rem;
    line-height: 1.85;
    color: var(--ink);
    white-space: pre-line;
    text-align: left;
    padding-top: .7rem;
}

.letter-signoff {
    text-align: right;
    font-family: 'Dancing Script', cursive;
    font-size: 1.5rem;
    color: var(--purple-600);
    margin-top: .4rem;
}

/* ---------- flip card (final page) ---------- */
.flip-card {
    perspective: 1200px;
    width: 100%;
    max-width: 380px;
    margin: .8rem auto 1.2rem;
}
.flip-toggle-input { display: none; }
.flip-card-inner {
    position: relative;
    display: block;
    width: 100%;
    padding-top: 125%;
    cursor: pointer;
    transform-style: preserve-3d;
    transition: transform .9s cubic-bezier(.4,.2,.2,1);
}
.flip-toggle-input:checked + .flip-card-inner {
    transform: rotateY(180deg);
}
.flip-card-face {
    position: absolute;
    inset: 0;
    -webkit-backface-visibility: hidden;
    backface-visibility: hidden;
    border-radius: 24px;
    box-shadow: 0 16px 40px rgba(124, 63, 168, .2);
    overflow: hidden;
}
.flip-card-front {
    background: var(--white);
}
.flip-card-front img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
}
.flip-hint {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    text-align: center;
    color: var(--white);
    background: rgba(94, 43, 131, .6);
    padding: .55rem;
    font-size: .8rem;
    font-weight: 600;
    letter-spacing: .3px;
}
.flip-card-back {
    transform: rotateY(180deg);
    background: linear-gradient(160deg, rgba(255,255,255,.96), rgba(246,235,252,.94));
    padding: 1.5rem 1.3rem;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
}
.flip-card-back .eyebrow { margin-bottom: .2rem; }
.flip-card-back h1 {
    font-size: clamp(1.8rem, 7.5vw, 2.7rem);
    margin: .25rem 0;
    background: linear-gradient(100deg, var(--purple-600), var(--pink-500) 55%, var(--purple-500));
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
}
.flip-card-back p {
    font-size: .9rem;
    line-height: 1.7;
    color: var(--ink-soft);
    margin: 0;
}
.flip-card-back .quote {
    font-size: 1.25rem;
    padding: .5rem 0;
}

/* ---------- final page ---------- */
.final {
    text-align: center;
    padding: 1.4rem 1rem .8rem;
}

.final h1 {
    font-size: clamp(2.6rem, 9vw, 5rem);
    margin: .4rem 0;
    background: linear-gradient(100deg, var(--purple-600), var(--pink-500) 55%, var(--purple-500));
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
}

.final p {
    color: var(--ink-soft);
    line-height: 1.8;
    font-size: 1rem;
}

/* ---------- simple cake cutting ---------- */
.simple-cake-wrap {
    display: flex;
    justify-content: center;
    margin: 1rem auto 1.3rem;
}

.simple-cake {
    position: relative;
    width: min(320px, 86vw);
    height: 260px;
}

.cake-plate {
    position: absolute;
    left: 5%;
    right: 5%;
    bottom: 18px;
    height: 22px;
    border-radius: 50%;
    background: #f1e3fb;
    box-shadow: 0 8px 18px rgba(124,63,168,.15);
}

.cake-bottom {
    position: absolute;
    left: 14%;
    right: 14%;
    bottom: 38px;
    height: 105px;
    border-radius: 18px 18px 28px 28px;
    background: linear-gradient(180deg, #c98fe6, #a56bd1);
    box-shadow: inset 0 12px 0 rgba(255,255,255,.18);
}

.cake-top {
    position: absolute;
    left: 22%;
    right: 22%;
    bottom: 130px;
    height: 62px;
    border-radius: 16px 16px 22px 22px;
    background: linear-gradient(180deg, #ffc2dc, #ff9fc4);
}

.icing {
    position: absolute;
    left: 0;
    right: 0;
    top: -5px;
    height: 24px;
    border-radius: 50%;
    background: #fff0f6;
}

.candles {
    position: absolute;
    left: 0;
    right: 0;
    bottom: 184px;
    display: flex;
    justify-content: center;
    gap: 18px;
    font-size: 1.7rem;
}

.simple-cake.cut .cake-slice-gap {
    position: absolute;
    right: 7%;
    top: 0;
    width: 22%;
    height: 100%;
    background: #f6ebfc;
    clip-path: polygon(20% 0, 100% 10%, 78% 100%, 0 100%);
}

.cake-cut-message {
    position: absolute;
    left: 0;
    right: 0;
    bottom: -28px;
    text-align: center;
    color: var(--purple-700);
    font-weight: 700;
    font-size: 1rem;
}

/* ---------- progress ---------- */
.progress-text {
    text-align: center;
    color: var(--ink-soft);
    font-size: .72rem;
    letter-spacing: 1.5px;
    margin-bottom: .4rem;
    font-weight: 600;
}

div[data-testid="stProgress"] > div > div {
    background: linear-gradient(90deg, var(--pink-400), var(--purple-500)) !important;
}
div[data-testid="stProgress"] > div {
    background-color: var(--lavender-300) !important;
}

/* ---------- buttons ---------- */
div.stButton > button {
    width: 100%;
    border-radius: 999px;
    border: 1px solid rgba(255,255,255,.5);
    background: linear-gradient(90deg, var(--pink-500), var(--purple-600));
    color: var(--white);
    font-weight: 600;
    min-height: 2.8rem;
    box-shadow: 0 10px 26px rgba(155, 92, 199, .3);
    transition: all .15s ease;
}

div.stButton > button p {
    color: var(--white) !important;
}

div.stButton > button:hover {
    filter: brightness(1.06);
    transform: translateY(-2px);
    box-shadow: 0 14px 32px rgba(155, 92, 199, .4);
}

div.stButton > button:disabled {
    background: linear-gradient(90deg, #dcc8ea, #cbb3e0) !important;
    box-shadow: none;
    opacity: .8;
    cursor: not-allowed;
}

div.stButton > button:disabled p {
    color: rgba(255,255,255,.85) !important;
}

/* ---------- lock hint ---------- */
.lock-hint {
    text-align: center;
    color: var(--pink-500);
    font-size: .8rem;
    font-weight: 500;
    margin-top: .5rem;
    animation: pulseHint 1.8s ease-in-out infinite;
}

@keyframes pulseHint {
    0%, 100% { opacity: .65; }
    50% { opacity: 1; }
}

/* ---------- inputs / alerts / checkbox ---------- */
div[data-testid="stTextInput"] input {
    border-radius: 14px !important;
    border: 1px solid var(--purple-400) !important;
    background: rgba(255,255,255,.85) !important;
    color: var(--ink) !important;
}

div[data-testid="stCheckbox"] label p {
    color: var(--ink) !important;
    font-weight: 500;
}

div[data-testid="stCaptionContainer"] {
    color: var(--ink-soft) !important;
    text-align: center;
}

div[data-testid="stAlert"] {
    border-radius: 16px;
    background: rgba(255,255,255,.85);
    color: var(--ink);
}

.footer {
    text-align: center;
    color: var(--purple-500);
    font-size: .72rem;
    padding-top: 1.6rem;
    letter-spacing: .5px;
}

/* ---------- small-screen tightening ---------- */
@media (max-width: 480px) {
    .block-container { padding-left: .8rem; padding-right: .8rem; }
    .card { padding: 1rem 1.05rem; }
    .letter-card { padding: 1.4rem 1.05rem; }
    .letter-text { font-size: 1rem; line-height: 1.75; }
    .point-card { padding: .75rem .85rem; }
    .point-card .point-text { font-size: .96rem; }
}
</style>

<div class="hearts-bg">
    <span class="heart-float" style="left:6%;  font-size:1.4rem; color:#f2699e; animation-duration:13s; animation-delay:0s;">💗</span>
    <span class="heart-float" style="left:18%; font-size:1.1rem; color:#b98ee0; animation-duration:16s; animation-delay:2s;">💜</span>
    <span class="heart-float" style="left:30%; font-size:1.7rem; color:#ff9fc4; animation-duration:11s; animation-delay:4s;">💕</span>
    <span class="heart-float" style="left:44%; font-size:1.2rem; color:#9b5cc7; animation-duration:14s; animation-delay:1s;">💜</span>
    <span class="heart-float" style="left:58%; font-size:1.5rem; color:#f2699e; animation-duration:12s; animation-delay:5s;">💗</span>
    <span class="heart-float" style="left:70%; font-size:1.1rem; color:#b98ee0; animation-duration:17s; animation-delay:3s;">💜</span>
    <span class="heart-float" style="left:82%; font-size:1.6rem; color:#ff9fc4; animation-duration:13s; animation-delay:6s;">💕</span>
    <span class="heart-float" style="left:92%; font-size:1.2rem; color:#9b5cc7; animation-duration:15s; animation-delay:2.5s;">💜</span>
    <span class="heart-float" style="left:50%; font-size:1.3rem; color:#f2699e; animation-duration:18s; animation-delay:7s;">💗</span>
</div>
""", unsafe_allow_html=True)

# ---------- Session state ----------
if "page" not in st.session_state:
    st.session_state.page = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}

TOTAL = 9

def next_page():
    st.session_state.page = min(st.session_state.page + 1, TOTAL - 1)

def prev_page():
    st.session_state.page = max(st.session_state.page - 1, 0)

def nav(unlocked=True, lock_msg="Finish the task above to unlock this 💭"):
    st.write("")
    if st.session_state.page > 0:
        c1, c2 = st.columns(2)
        with c1:
            st.button("← Back", on_click=prev_page, key=f"back_{st.session_state.page}")
        with c2:
            if st.session_state.page < TOTAL - 1:
                if unlocked:
                    st.button("Continue →", on_click=next_page, key=f"next_{st.session_state.page}")
                else:
                    st.button("🔒 Continue →", disabled=True, key=f"next_locked_{st.session_state.page}")
        if not unlocked and st.session_state.page < TOTAL - 1:
            md(f'<div class="lock-hint">{lock_msg}</div>')
    elif st.session_state.page == 0:
        st.button("Open your birthday surprise →", on_click=next_page, key="start")

def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def find_asset(name):
    """Look for name + a known extension inside the assets folder."""
    exts = [".jpeg", ".jpg", ".png", ".JPEG", ".JPG", ".PNG"]
    for ext in exts:
        candidate = ASSETS / f"{name}{ext}"
        if candidate.exists():
            mime = "png" if ext.lower() == ".png" else "jpeg"
            return candidate, mime
    return None, None

def photo(name):
    """Display an image, using a container width that works across
    Streamlit versions, with a friendly placeholder if it's missing."""
    path = ASSETS / name
    md('<div class="photo-frame">')
    if path.exists():
        try:
            st.image(str(path), use_container_width=True)
        except TypeError:
            st.image(str(path))
    else:
        md(f'<div class="missing-photo">💜 Photo "{name}" not found in the assets folder 💜</div>')
    md('</div>')

def collage_html(names):
    """Render a hanging photo collage using exact asset filenames."""
    imgs = []
    for filename in names:
        path = ASSETS / filename

        # Also support the old name-without-extension format if needed.
        if not path.exists():
            path, mime = find_asset(filename)
        else:
            suffix = path.suffix.lower()
            mime = "png" if suffix == ".png" else "jpeg"

        if path and path.exists():
            b64 = img_to_base64(path)
            imgs.append(
                f'<div class="hanging-photo">'
                f'<img src="data:image/{mime};base64,{b64}" alt="Birthday memory">'
                f'</div>'
            )

    if not imgs:
        return ""
    return '<div class="photo-collage">' + "".join(imgs) + '</div>'

def memory_row(name, tag, title, text):
    md('<div class="memory-row">')
    col1, col2 = st.columns([1, 1])
    with col1:
        photo(name)
    with col2:
        md(f"""
        <div class="mem-text-wrap">
            <div class="mem-text-card">
                <div class="mem-tag">{tag}</div>
                <h3>{title}</h3>
                <p>{text}</p>
            </div>
        </div>
        """)
    md('</div>')

def simple_cake_html(cut=False):
    """Simple birthday cake. No knife animation; the button performs the cut."""
    if cut:
        cake = """
        <div class="simple-cake cut">
            <div class="cake-plate"></div>
            <div class="cake-bottom">
                <div class="cake-slice-gap"></div>
                <div class="icing"></div>
            </div>
            <div class="cake-top">
                <div class="icing"></div>
            </div>
            <div class="candles">
                <span>🕯️</span><span>🕯️</span><span>🕯️</span>
            </div>
            <div class="cake-cut-message">🎂 Cake cut! 🎉</div>
        </div>
        """
    else:
        cake = """
        <div class="simple-cake">
            <div class="cake-plate"></div>
            <div class="cake-bottom">
                <div class="icing"></div>
            </div>
            <div class="cake-top">
                <div class="icing"></div>
            </div>
            <div class="candles">
                <span>🕯️</span><span>🕯️</span><span>🕯️</span>
            </div>
        </div>
        """

    return f'<div class="simple-cake-wrap">{cake}</div>'

# ---------- Pages ----------
page = st.session_state.page

if page > 0:
    md(f'<div class="progress-text">YOUR BIRTHDAY JOURNEY · {page}/{TOTAL-1}</div>')
    st.progress(page / (TOTAL - 1))

if page == 0:
    md('<div class="eyebrow" style="text-align:center;">A tiny corner of the internet · made only for you</div>')
    # Page 1: all 8 hero photos are shown together as hanging photos.
    md(collage_html([
        "hero1.jpeg.jpeg",
        "hero2.jpeg.jpeg",
        "hero3.jpeg.jpeg",
        "hero4.jpeg.jpeg",
        "hero5.jpeg.jpeg",
        "hero6.jpeg.jpeg",
        "hero7.jpeg.jpeg",
        "hero8.jpeg.jpeg",
    ]))
    md("""
    <div class="hero-center">
        <h1>20th August,<br>Happiest Birthday, Bunny</h1>
        <div class="subtitle">Before you go any further, I just want you to know —
        a great deal of love went into building this, one page at a time.</div>
    </div>
    """)
    md('<div class="quote">"Celebrating you every day — but today is entirely yours. I just made a little of it about how much I adore you."</div>')
    md('<div class="divider-heart">💜 · 💗 · 💜</div>')
    st.caption("Fair warning: you can't skip ahead. Every page has a tiny task waiting for you. 😌")
    nav()

elif page == 1:
    st.markdown("## A small question, just for you")
    md('<div class="card"><div class="small">There are no wrong answers here — only the one I already know is right. 💜</div></div>')
    name = st.text_input("What does your favourite person call you?", placeholder="Type your answer here...")
    if st.button("This is definitely me 😌"):
        if name.strip():
            with st.spinner("🔍 Verifying that you are, in fact, my favourite person..."):
                time.sleep(1.1)
            st.session_state.answers["name"] = name.strip()
            st.success("Identity confirmed. And lucky for you, you're stuck with me. 💜")
        else:
            st.warning("You have to type something first — I'm waiting. 😊")
    unlocked = "name" in st.session_state.answers
    nav(unlocked, "Type your answer and tap the button above first 💭")

elif page == 2:
    st.markdown("## How well do you know us? 🎲")
    st.caption("A tiny, playful relationship quiz. No cheating — I'll know. 💗")

    md('<div class="quiz-q">1. In a dance-off with zero practice, who takes the win?</div>')
    q1 = st.radio("q1", ["Me, no contest 💃", "You, no contest 🕺", "We'd both lose spectacularly"],
                   index=None, label_visibility="collapsed", key="q1_widget")

    md('<div class="quiz-q">2. Who\'s more likely to text "you up?" at 1am?</div>')
    q2 = st.radio("q2", ["Me, guilty as charged", "You, guilty as charged", "Both of us, shamelessly"],
                   index=None, label_visibility="collapsed", key="q2_widget")

    md('<div class="quiz-q">3. Stranded on a desert island, who packs snacks and who packs snacks... for the vibes?</div>')
    q3 = st.radio("q3", ["Me — practical to a fault", "You — practical to a fault", "Neither of us survives a week"],
                   index=None, label_visibility="collapsed", key="q3_widget")

    md('<div class="quiz-q">4. Real talk — who loves the other person a little more?</div>')
    q4 = st.radio("q4", ["Me 💜", "You 💜", "Honestly, both"],
                   index=None, label_visibility="collapsed", key="q4_widget")

    if st.button("Submit my very accurate answers"):
        if None in (q1, q2, q3, q4):
            st.warning("Pick an answer for every question first — no skipping 👀")
        else:
            st.session_state.answers.update({"q1": q1, "q2": q2, "q3": q3, "q4": q4})
            st.balloons()

    if "q4" in st.session_state.answers:
        a = st.session_state.answers
        if a["q4"].startswith("You"):
            verdict = "Aww, close call — but I still say it's me. 💜"
        elif a["q4"].startswith("Me"):
            verdict = "See? I've been telling you this the whole time. 💜"
        else:
            verdict = "The most diplomatic answer in relationship history. Respect. 🫡"
        md(f"""
        <div class="card">
            <div class="small">
                According to you: <b>{a['q1']}</b> wins the dance-off, and <b>{a['q2']}</b>
                sends the risky 1am text. Noted and filed away. 📝
            </div>
            <div class="quote" style="font-size:1.25rem;">{verdict}</div>
        </div>
        """)

    unlocked = "q4" in st.session_state.answers
    nav(unlocked, "Submit your answers first, sneaky 👀")

elif page == 3:
    st.markdown("## A few of my favourite versions/memories of us")
    md('<div class="small">Some memories deserve more than just a place in the camera roll — they deserve a little home of their own.</div>')

    memory_row(
        "first_trip.jpeg",
        "Memory 01",
        "OUR FIRST TRIP",
        "You are this cute, ofc I am biased for you. ye picture meri favourite hai I never posted it "
        "becuase i wanted to post on your biwrthday. Will cherish this trip always.",
    )
    memory_row(
        "the_view.jpeg",
        "Memory 02",
        "Dates to die for",
        "I prefer looking at you the same way on each date going forward, "
        "this is the perfect view i would give on world for.",
    )
    memory_row(
        "prettiest_frame.jpeg",
        "Memory 03",
        "Scary car rides",
        "Little heart attacks is what you give when we are in this setup, "
        "no worries signing up for these with all my heart",
    )
    nav()

elif page == 4:
    st.markdown("## Things I hope you never forget")
    st.caption("No task here, just a few reminders I need you to keep. 💜")
    points = [
        "We are proud of you and love celebrating you.",
        "You don't have to have everything figured out right now — things "
        "will fall back into place gradually, so no tension babu.",
        "I hope you keep choosing the things that make you genuinely happy.",
        "I hope you chase the big dreams, even the ones that feel far away. You deserve everything.",
        "I hope you never forget how capable you truly are. You are the softest guy that i dreamt of.",
        "And on the days you do forget — I'll be here to remind you. 💜",
    ]
    cards = []
    for i, text in enumerate(points, 1):
        cards.append(f'<div class="point-card"><div class="point-num">{i:02}</div><div class="point-text">{text}</div></div>')
    md('<div class="points-grid">' + "".join(cards) + '</div>')
    nav()

elif page == 5:
    st.markdown("## Pick your poison 😏 (the fun kind)")
    st.caption("You may open only one. Choose with your heart, not your curiosity. 💗")

    choices = {
        "💌 A soft one": "I love you more than I could ever fit into a website — and believe me, I tried.",
        "🌙 A gentle tease": "You're officially one year older today ( Ab nahi hu tumse badi same same hogye ab ). "
                             "Fortunately for you, I've decided to be kind about it. 😊",
        "🌱 A future one": "One day we'll look back on this version of us, and be so proud of everything we built together.",
    }
    for label, message in choices.items():
        if st.button(label, key=f"surprise_{label}"):
            st.session_state.answers["surprise"] = label
            st.balloons()
    if "surprise" in st.session_state.answers:
        message = choices[st.session_state.answers["surprise"]]
        md(f'<div class="card"><div class="quote">{message}</div></div>')

    unlocked = "surprise" in st.session_state.answers
    nav(unlocked, "Pick a surprise above to continue 🎁")

elif page == 6:
    st.markdown("## One last thing before the letter...")
    md("""
    <div style="text-align:center;">
        <div class="subtitle">You have one important birthday duty left to perform.</div>
        <h1 style="font-family:'Cormorant Garamond',serif;background:linear-gradient(100deg,var(--purple-600),var(--pink-500) 55%,var(--purple-500));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;font-size:clamp(2.2rem,7vw,3.6rem);margin:.4rem 0;">Cut the Cake</h1>
    </div>
    """)

    cut = st.session_state.answers.get("cake", False)

    md(simple_cake_html(cut=cut))

    if not cut:
        st.caption("Your only birthday duty: cut the cake. 🎂")
        if st.button("🔪 Cut the cake 🎂"):
            st.session_state.answers["cake"] = True
            st.balloons()
            st.rerun()
    else:
        md("""
        <div class="final">
            <div style="font-size:4rem;">🎂✨💜</div>
            <h1>IT'S YOUR DAY!</h1>
            <p>Make a wish — I have a feeling I already know mine. 💜</p>
        </div>
        """)

    unlocked = cut
    nav(unlocked, "You must cut the cake first — no shortcuts 🎂")

elif page == 7:
    st.markdown("## The Letter")
    md('<div class="small">Everything else on this little site was just the build-up. This part, I mean with my whole heart.</div>')
    md(f"""
    <div class="letter-card">
        <div class="letter-text">{FINAL_LETTER.strip()}</div>
        <div class="letter-signoff">— always yours 💜</div>
    </div>
    """)
    st.write("")
    felt = st.checkbox("I felt every word of this 💜", key="felt_letter")
    nav(felt, "Take a moment, then check the box above 💭")

elif page == 8:
    st.markdown("## One last surprise")
    st.caption("Tap the card below to open it. 💜")

    img_path = ASSETS / "birthday_final.jpeg"
    if img_path.exists():
        b64 = img_to_base64(img_path)
        front_html = f'<img src="data:image/jpeg;base64,{b64}" alt="Birthday photo" />'
    else:
        front_html = '<div class="missing-photo">💜 Photo "birthday_final.jpeg" not found in the assets folder 💜</div>'

    md(f"""
    <div class="flip-card">
        <input type="checkbox" id="flipToggle" class="flip-toggle-input">
        <label for="flipToggle" class="flip-card-inner">
            <div class="flip-card-face flip-card-front">
                {front_html}
                <div class="flip-hint">Tap to open your last surprise 💜</div>
            </div>
            <div class="flip-card-face flip-card-back">
                <div class="eyebrow">The final page</div>
                <h1>HAPPY<br>BIWRTHDAY AGAIN JI</h1>
                <p>
                    Saksham —<br>
                    I love celebrating you <br>
                    Biggest biwrthday hugs and kisses to you.
                </p>
                <div class="quote">"And yes... I would choose you again."</div>
                <div style="font-size:1.8rem;">💜 💗 🎂 💗 💜</div>
            </div>
        </label>
    </div>
    """)

md('<div class="footer">Made with an unreasonable amount of love 💜</div>')
