import time
import base64
import streamlit as st
from pathlib import Path

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="For My Birthday Boy 💜",
    page_icon="💜",
    layout="centered",
    initial_sidebar_state="collapsed",
)

ASSETS = Path(__file__).parent / "assets"


# ============================================================
# YOUR LETTER — GRAMMAR KEPT EXACTLY AS YOU WROTE IT
# ============================================================

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


# ============================================================
# CSS
# ============================================================

st.markdown(
    """
<style>

@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,600&family=Dancing+Script:wght@600;700&family=Poppins:wght@300;400;500;600;700&display=swap');


/* ==========================================================
   GLOBAL
   ========================================================== */

:root {
    --purple: #7c3fa8;
    --purple-dark: #5e2b83;
    --purple-light: #c9a6e6;
    --pink: #f2699e;
    --pink-light: #ffd1e3;
    --lavender: #f3e5fa;
    --cream: #fffaf5;
    --ink: #4a2a63;
    --soft: #76558d;
}

html,
body,
[class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    min-height: 100vh;

    background:
        radial-gradient(circle at 5% 10%, rgba(255, 184, 210, .40), transparent 25%),
        radial-gradient(circle at 95% 15%, rgba(198, 161, 231, .38), transparent 27%),
        radial-gradient(circle at 10% 90%, rgba(228, 202, 244, .55), transparent 30%),
        radial-gradient(circle at 90% 90%, rgba(255, 210, 227, .40), transparent 30%),
        linear-gradient(
            135deg,
            #fff8fc 0%,
            #f7edfc 35%,
            #f3e6fa 65%,
            #fff3f8 100%
        );
}

.block-container {
    max-width: 1000px;
    padding-top: 1.2rem;
    padding-bottom: 5rem;
    position: relative;
    z-index: 5;
}

div[data-testid="stVerticalBlock"] {
    gap: .55rem;
}

h1,
h2,
h3 {
    font-family: 'Cormorant Garamond', serif !important;
    color: var(--purple-dark) !important;
}

p,
div,
span,
label,
li {
    color: var(--ink);
}


/* ==========================================================
   FLOATING HEARTS
   ========================================================== */

.hearts-bg {
    position: fixed;
    inset: 0;
    overflow: hidden;
    pointer-events: none;
    z-index: 0;
}

.float-heart {
    position: absolute;
    bottom: -50px;
    animation: floatHeart linear infinite;
    opacity: .55;
}

@keyframes floatHeart {

    0% {
        transform: translateY(0) rotate(0deg);
        opacity: 0;
    }

    10% {
        opacity: .55;
    }

    50% {
        transform: translateY(-50vh) translateX(25px) rotate(15deg);
    }

    90% {
        opacity: .30;
    }

    100% {
        transform: translateY(-110vh) translateX(-20px) rotate(-15deg);
        opacity: 0;
    }
}


/* ==========================================================
   PROGRESS
   ========================================================== */

.progress-text {
    text-align: center;
    color: var(--soft);
    font-size: .72rem;
    letter-spacing: 2px;
    margin-bottom: .5rem;
    font-weight: 600;
}

div[data-testid="stProgress"] > div > div {
    background: linear-gradient(
        90deg,
        var(--pink),
        var(--purple)
    ) !important;
}

div[data-testid="stProgress"] > div {
    background-color: #e7d5f1 !important;
}


/* ==========================================================
   BUTTONS
   ========================================================== */

div.stButton > button {
    width: 100%;
    min-height: 3rem;

    border: none !important;
    border-radius: 999px;

    background: linear-gradient(
        90deg,
        var(--pink),
        var(--purple)
    ) !important;

    color: white !important;

    font-weight: 600;

    box-shadow:
        0 10px 25px rgba(124, 63, 168, .25);

    transition: .2s ease;
}

div.stButton > button p {
    color: white !important;
}

div.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow:
        0 14px 32px rgba(124, 63, 168, .35);
}


/* ==========================================================
   FIRST PAGE — SCRAPBOOK
   ========================================================== */

.scrapbook {
    position: relative;
    min-height: 760px;
    margin-top: .5rem;
    padding: 25px 10px 60px;
}


/* hanging strings */

.string {
    position: absolute;
    width: 2px;
    background: rgba(94, 43, 131, .25);
    transform-origin: top;
}

.string.one {
    height: 100px;
    left: 15%;
    top: 0;
    transform: rotate(-4deg);
}

.string.two {
    height: 130px;
    right: 16%;
    top: 0;
    transform: rotate(5deg);
}

.string.three {
    height: 95px;
    left: 72%;
    top: 180px;
    transform: rotate(-3deg);
}

.string.four {
    height: 80px;
    left: 24%;
    top: 420px;
    transform: rotate(4deg);
}


/* little clips */

.clip {
    position: absolute;
    width: 30px;
    height: 10px;
    border-radius: 5px;
    background: #d5a7dc;
    box-shadow: 0 2px 5px rgba(0,0,0,.12);
    z-index: 4;
}


/* photo */

.polaroid {
    position: absolute;
    background: white;
    padding: 10px 10px 32px;
    box-shadow:
        0 15px 30px rgba(75, 38, 96, .20);
    border-radius: 3px;
    width: 215px;
}

.polaroid img {
    width: 100%;
    height: 220px;
    object-fit: cover;
    display: block;
}

.polaroid .caption {
    position: absolute;
    bottom: 7px;
    left: 0;
    right: 0;

    text-align: center;

    font-family: 'Dancing Script', cursive;
    font-size: 17px;
    color: var(--purple-dark);
}


/* different photo positions */

.photo-a {
    left: 2%;
    top: 35px;
    transform: rotate(-8deg);
}

.photo-b {
    right: 2%;
    top: 70px;
    transform: rotate(8deg);
}

.photo-c {
    left: 8%;
    top: 405px;
    transform: rotate(6deg);
}

.photo-d {
    right: 7%;
    top: 440px;
    transform: rotate(-6deg);
}


/* tape */

.tape {
    position: absolute;
    width: 72px;
    height: 22px;
    background: rgba(255, 211, 226, .75);
    top: -10px;
    left: 50%;
    transform: translateX(-50%) rotate(-3deg);
}


/* center text */

.scrap-center {
    position: absolute;
    left: 50%;
    top: 195px;

    transform: translateX(-50%);

    width: 46%;
    min-width: 300px;

    text-align: center;

    z-index: 10;
}

.scrap-eyebrow {
    font-size: .7rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--pink);
    font-weight: 600;
}

.scrap-center h1 {
    font-family: 'Dancing Script', cursive !important;

    font-size: clamp(3rem, 7vw, 5.2rem);

    line-height: .95;

    margin: 12px 0;

    background: linear-gradient(
        100deg,
        var(--purple),
        var(--pink),
        var(--purple)
    );

    -webkit-background-clip: text;
    background-clip: text;

    -webkit-text-fill-color: transparent;
}

.scrap-subtitle {
    background: rgba(255,255,255,.72);

    border: 1px solid rgba(185,142,224,.30);

    border-radius: 25px;

    padding: 18px 20px;

    box-shadow:
        0 12px 30px rgba(124,63,168,.10);

    font-size: .95rem;
    line-height: 1.8;
}


/* tiny notes */

.note {
    position: absolute;

    background: #fff6a8;

    padding: 13px 17px;

    width: 165px;

    font-family: 'Dancing Script', cursive;

    font-size: 18px;

    color: #704c2b;

    box-shadow:
        0 8px 18px rgba(80,60,20,.15);
}

.note-a {
    top: 300px;
    left: 1%;
    transform: rotate(-8deg);
}

.note-b {
    top: 345px;
    right: 0%;
    transform: rotate(7deg);
    background: #ead8ff;
    color: var(--purple-dark);
}

.note-c {
    bottom: 15px;
    left: 50%;
    transform: translateX(-50%) rotate(-2deg);
    background: #ffddea;
    color: #874362;
}


/* mobile */

@media(max-width: 700px) {

    .scrapbook {
        min-height: auto;
        display: flex;
        flex-direction: column;
        align-items: center;
        padding-bottom: 20px;
    }

    .string,
    .clip,
    .note {
        display: none;
    }

    .scrap-center {
        position: relative;
        left: auto;
        top: auto;
        transform: none;

        width: 100%;
        min-width: auto;

        order: 1;

        margin-bottom: 25px;
    }

    .polaroid {
        position: relative;

        left: auto;
        right: auto;
        top: auto;

        width: 75%;

        margin: -5px auto 25px;
    }

    .photo-a {
        order: 2;
        transform: rotate(-5deg);
    }

    .photo-b {
        order: 3;
        transform: rotate(5deg);
    }

    .photo-c {
        order: 4;
        transform: rotate(4deg);
    }

    .photo-d {
        order: 5;
        transform: rotate(-5deg);
    }

    .polaroid img {
        height: 270px;
    }
}


/* ==========================================================
   CARDS
   ========================================================== */

.card {
    background: rgba(255,255,255,.75);

    backdrop-filter: blur(8px);

    border: 1px solid rgba(185,142,224,.35);

    border-radius: 24px;

    padding: 1.5rem;

    margin: 1rem 0;

    box-shadow:
        0 14px 40px rgba(124,63,168,.12);
}

.small {
    color: var(--soft);
    font-size: .92rem;
    line-height: 1.75;
}

.quote {
    font-family: 'Dancing Script', cursive;

    font-weight: 700;

    font-size: 2rem;

    line-height: 1.4;

    color: var(--purple-dark);

    text-align: center;

    padding: 1rem;
}


/* ==========================================================
   MEMORY PHOTOS
   ========================================================== */

.photo-frame {
    background: white;

    border-radius: 24px;

    padding: 10px;

    box-shadow:
        0 18px 40px rgba(124,63,168,.18);
}

[data-testid="stImage"] img {
    border-radius: 18px;
}

.memory-row {
    margin: 2rem 0;
}

.mem-card {
    background: rgba(255,255,255,.75);

    border-radius: 22px;

    padding: 1.4rem;

    box-shadow:
        0 14px 35px rgba(124,63,168,.10);
}

.mem-tag {
    color: var(--pink);

    font-size: .68rem;

    letter-spacing: 2px;

    text-transform: uppercase;
}

.mem-card h3 {
    margin: .3rem 0 .5rem;

    font-size: 1.5rem;
}

.mem-card p {
    color: var(--soft);

    line-height: 1.7;
}


/* ==========================================================
   POINT CARDS
   ========================================================== */

.points-grid {
    display: grid;

    grid-template-columns:
        repeat(auto-fit, minmax(260px, 1fr));

    gap: 12px;
}

.point-card {
    background: rgba(255,255,255,.75);

    border: 1px solid rgba(185,142,224,.3);

    border-radius: 18px;

    padding: 17px;

    display: flex;

    gap: 12px;

    box-shadow:
        0 10px 25px rgba(124,63,168,.08);
}

.point-num {
    font-family: 'Cormorant Garamond', serif;

    font-size: 1.5rem;

    color: var(--pink);

    font-weight: 700;
}

.point-text {
    font-size: 1rem;

    line-height: 1.5;

    font-weight: 500;
}


/* ==========================================================
   LETTER
   ========================================================== */

.letter-card {
    background:
        linear-gradient(
            180deg,
            rgba(255,255,255,.96),
            rgba(250,240,255,.9)
        );

    border: 1px solid rgba(185,142,224,.4);

    border-radius: 28px;

    padding: 2rem 1.8rem;

    box-shadow:
        0 20px 55px rgba(124,63,168,.16);

    position: relative;
}

.letter-card::before {
    content: "💌";

    position: absolute;

    top: -20px;

    left: 50%;

    transform: translateX(-50%);

    font-size: 2rem;

    background: #fff8ff;

    padding: 5px 12px;

    border-radius: 50%;
}

.letter-text {
    font-family: 'Cormorant Garamond', serif;

    font-style: italic;

    font-size: 1.28rem;

    line-height: 2;

    white-space: pre-line;

    color: var(--ink);

    padding-top: 15px;
}

.letter-signoff {
    text-align: right;

    font-family: 'Dancing Script', cursive;

    font-size: 1.6rem;

    color: var(--purple);
}


/* ==========================================================
   CAKE — SIMPLE HTML/CSS, NO SVG
   ========================================================== */

.cake-area {
    position: relative;

    width: 350px;
    height: 360px;

    margin: 20px auto;
}

.cake {
    position: absolute;

    left: 50%;
    bottom: 25px;

    transform: translateX(-50%);

    width: 270px;
    height: 180px;
}

.cake-bottom {
    position: absolute;

    bottom: 0;
    left: 0;

    width: 270px;
    height: 105px;

    background: linear-gradient(
        #c58ce1,
        #9558bd
    );

    border-radius: 15px 15px 25px 25px;

    box-shadow:
        inset 0 -12px 0 rgba(80,30,100,.10),
        0 12px 20px rgba(90,50,110,.20);
}

.cake-middle {
    position: absolute;

    bottom: 75px;
    left: 35px;

    width: 200px;
    height: 70px;

    background: linear-gradient(
        #ffbfd9,
        #ff8fb9
    );

    border-radius: 15px;

    box-shadow:
        0 8px 12px rgba(100,50,100,.12);
}

.cream {
    position: absolute;

    bottom: 70px;

    left: 35px;

    width: 200px;

    height: 25px;

    background: #fff5fa;

    border-radius: 50%;
}

.cake-cream-bottom {
    position: absolute;

    bottom: 92px;

    left: 0;

    width: 270px;

    height: 30px;

    background: #fff4fa;

    border-radius: 50%;
}

.candle {
    position: absolute;

    bottom: 140px;

    width: 9px;
    height: 45px;

    background: #8c55b4;

    border-radius: 4px;
}

.candle.c1 { left: 80px; }
.candle.c2 { left: 130px; }
.candle.c3 { left: 180px; }

.flame {
    position: absolute;

    width: 14px;
    height: 22px;

    background: radial-gradient(
        circle at 50% 70%,
        #fff6a0,
        #ff9f43 60%,
        #f2699e
    );

    border-radius: 60% 40% 60% 40%;

    top: -21px;
    left: -2px;

    animation: flame 1s infinite alternate;
}

@keyframes flame {

    from {
        transform: scale(.9) rotate(-3deg);
    }

    to {
        transform: scale(1.12) rotate(3deg);
    }
}


/* knife */

.knife {
    position: absolute;

    top: 45px;
    left: 230px;

    width: 130px;
    height: 18px;

    transform: rotate(-35deg);

    transition:
        transform 1s cubic-bezier(.4,0,.2,1);

    z-index: 5;
}

.knife-handle {
    position: absolute;

    right: 0;

    width: 45px;
    height: 24px;

    border-radius: 8px;

    background: var(--purple-dark);
}

.knife-blade {
    position: absolute;

    left: 0;

    top: 3px;

    width: 95px;
    height: 12px;

    background: linear-gradient(
        #ffffff,
        #dcd8e2
    );

    border-radius: 4px 0 0 4px;

    border: 1px solid #c9c3d2;
}

.cutting .knife {
    animation: cutCake 1.4s forwards;
}

@keyframes cutCake {

    0% {
        transform:
            translate(50px,-60px)
            rotate(-45deg);
    }

    35% {
        transform:
            translate(10px,35px)
            rotate(-45deg);
    }

    60% {
        transform:
            translate(-20px,115px)
            rotate(-45deg);
    }

    100% {
        transform:
            translate(-15px,105px)
            rotate(-35deg);
    }
}


/* slice */

.slice {
    position: absolute;

    bottom: 25px;
    right: 5px;

    width: 65px;
    height: 70px;

    opacity: 0;

    transform: translate(0,0) rotate(0deg);

    z-index: 10;
}

.slice .slice-purple {
    position: absolute;

    bottom: 0;

    width: 65px;
    height: 55px;

    background: #a96bd0;

    clip-path: polygon(
        0 0,
        100% 35%,
        100% 100%,
        25% 100%
    );
}

.slice .slice-cream {
    position: absolute;

    top: 8px;

    left: 4px;

    width: 58px;
    height: 13px;

    background: #fff5fa;

    transform: rotate(15deg);

    border-radius: 50%;
}

.cutting .slice {
    animation: sliceMove 1s 1s forwards;
}

@keyframes sliceMove {

    from {
        opacity: 0;
        transform:
            translate(0,0)
            rotate(0);
    }

    to {
        opacity: 1;
        transform:
            translate(65px,20px)
            rotate(18deg);
    }
}

.cake-message {
    text-align: center;

    font-family: 'Dancing Script', cursive;

    font-size: 2rem;

    color: var(--purple-dark);

    animation: appear .8s ease;
}

@keyframes appear {

    from {
        opacity: 0;
        transform: translateY(10px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}


/* ==========================================================
   FINAL FLIP CARD
   ========================================================== */

.flip-card {
    perspective: 1000px;

    width: 100%;

    max-width: 420px;

    margin: 30px auto;
}

.flip-input {
    display: none;
}

.flip-inner {
    position: relative;

    width: 100%;

    padding-top: 125%;

    transition:
        transform .8s;

    transform-style: preserve-3d;

    cursor: pointer;
}

.flip-input:checked + .flip-inner {
    transform: rotateY(180deg);
}

.flip-face {
    position: absolute;

    inset: 0;

    border-radius: 25px;

    overflow: hidden;

    backface-visibility: hidden;

    box-shadow:
        0 18px 45px rgba(124,63,168,.2);
}

.flip-front {
    background: white;
}

.flip-front img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.flip-hint {
    position: absolute;

    bottom: 0;
    left: 0;
    right: 0;

    padding: 14px;

    text-align: center;

    background: rgba(94,43,131,.65);

    color: white !important;

    font-weight: 600;
}

.flip-back {
    transform: rotateY(180deg);

    background:
        linear-gradient(
            160deg,
            #fff,
            #f5e7fc
        );

    display: flex;

    flex-direction: column;

    justify-content: center;

    align-items: center;

    text-align: center;

    padding: 30px;
}

.flip-back h1 {
    font-family: 'Dancing Script', cursive !important;

    font-size: 3rem;

    line-height: 1;

    color: var(--purple) !important;
}

.flip-back p {
    line-height: 1.8;

    color: var(--soft);
}


/* ==========================================================
   INPUT / CHECKBOX
   ========================================================== */

div[data-testid="stTextInput"] input {

    border-radius: 14px !important;

    border:
        1px solid var(--purple-light) !important;

    background:
        rgba(255,255,255,.9) !important;

    color: var(--ink) !important;
}

div[data-testid="stCheckbox"] label p {
    color: var(--ink) !important;
}


/* ==========================================================
   FOOTER
   ========================================================== */

.footer {
    text-align: center;

    color: var(--purple);

    font-size: .75rem;

    padding-top: 35px;

    letter-spacing: .5px;
}

</style>


<!-- FLOATING HEARTS -->

<div class="hearts-bg">

    <span class="float-heart"
          style="left:5%;font-size:20px;animation-duration:14s;animation-delay:0s;">
        💗
    </span>

    <span class="float-heart"
          style="left:17%;font-size:16px;animation-duration:17s;animation-delay:2s;">
        💜
    </span>

    <span class="float-heart"
          style="left:31%;font-size:23px;animation-duration:12s;animation-delay:4s;">
        💕
    </span>

    <span class="float-heart"
          style="left:47%;font-size:18px;animation-duration:15s;animation-delay:1s;">
        💜
    </span>

    <span class="float-heart"
          style="left:61%;font-size:22px;animation-duration:13s;animation-delay:5s;">
        💗
    </span>

    <span class="float-heart"
          style="left:76%;font-size:17px;animation-duration:18s;animation-delay:3s;">
        💜
    </span>

    <span class="float-heart"
          style="left:90%;font-size:23px;animation-duration:14s;animation-delay:6s;">
        💕
    </span>

</div>
""",
    unsafe_allow_html=True,
)


# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = 0

if "answers" not in st.session_state:
    st.session_state.answers = {}


TOTAL = 9


def next_page():
    st.session_state.page = min(
        st.session_state.page + 1,
        TOTAL - 1
    )


def prev_page():
    st.session_state.page = max(
        st.session_state.page - 1,
        0
    )


def nav(
    unlocked=True,
    lock_msg="Finish the task above to unlock this 💭"
):

    st.write("")

    if st.session_state.page > 0:

        c1, c2 = st.columns(2)

        with c1:
            st.button(
                "← Back",
                on_click=prev_page,
                key=f"back_{st.session_state.page}"
            )

        with c2:

            if st.session_state.page < TOTAL - 1:

                if unlocked:

                    st.button(
                        "Continue →",
                        on_click=next_page,
                        key=f"next_{st.session_state.page}"
                    )

                else:

                    st.button(
                        "🔒 Continue →",
                        disabled=True,
                        key=f"locked_{st.session_state.page}"
                    )

        if not unlocked:

            st.markdown(
                f"""
                <div style="
                    text-align:center;
                    color:#f2699e;
                    font-size:.82rem;
                    margin-top:8px;
                ">
                    {lock_msg}
                </div>
                """,
                unsafe_allow_html=True
            )

    else:

        st.button(
            "Open your birthday surprise →",
            on_click=next_page,
            key="start"
        )


# ============================================================
# IMAGE HELPERS
# ============================================================

def find_image(names):

    extensions = [
        ".jpeg",
        ".jpg",
        ".png",
        ".JPG",
        ".JPEG",
        ".PNG"
    ]

    for name in names:

        path = ASSETS / name

        if path.exists():
            return path

        for ext in extensions:

            candidate = ASSETS / f"{name}{ext}"

            if candidate.exists():
                return candidate

    return None


def img_to_base64(path):

    with open(path, "rb") as f:

        return base64.b64encode(
            f.read()
        ).decode()


def photo(name):

    path = find_image([name])

    if path:

        st.image(
            str(path),
            use_container_width=True
        )

    else:

        st.markdown(
            f"""
            <div style="
                background:#fff;
                padding:40px;
                border-radius:20px;
                text-align:center;
                color:#9b5cc7;
            ">
                💜 Photo "{name}" not found
            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# MEMORY ROW
# ============================================================

def memory_row(
    image_name,
    tag,
    title,
    text
):

    col1, col2 = st.columns(
        [1, 1],
        gap="large"
    )

    with col1:

        st.markdown(
            '<div class="photo-frame">',
            unsafe_allow_html=True
        )

        photo(image_name)

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            f"""
            <div class="mem-card">

                <div class="mem-tag">
                    {tag}
                </div>

                <h3>
                    {title}
                </h3>

                <p>
                    {text}
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")


# ============================================================
# PAGE
# ============================================================

page = st.session_state.page


# ============================================================
# PROGRESS
# ============================================================

if page > 0:

    st.markdown(
        f"""
        <div class="progress-text">
            YOUR BIRTHDAY JOURNEY · {page}/{TOTAL-1}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.progress(
        page / (TOTAL - 1)
    )


# ============================================================
# PAGE 0 — CRAZY CUTE SCRAPBOOK
# ============================================================

if page == 0:

    # Find the photos you already have
    photos = [
        (
            ["first_trip.jpeg", "first_trip"],
            "our first trip"
        ),
        (
            ["the_view.jpeg", "the_view"],
            "this view always"
        ),
        (
            ["prettiest_frame.jpeg", "prettiest_frame"],
            "prettiest frame"
        ),
        (
            ["birthday_final.jpeg", "birthday_final"],
            "my birthday boy"
        ),
    ]

    html = """
    <div class="scrapbook">

        <div class="string one"></div>
        <div class="string two"></div>
        <div class="string three"></div>
        <div class="string four"></div>

        <div class="scrap-center">

            <div class="scrap-eyebrow">
                made with an unreasonable amount of love
            </div>

            <h1>
                Happiest Birthday,<br>
                Bunny 💜
            </h1>

            <div class="scrap-subtitle">
                20th August ✨
                <br><br>
                Before you go any further, I just want you to know —
                a great deal of love went into building this,
                one page at a time.
            </div>

        </div>
    """

    positions = [
        "photo-a",
        "photo-b",
        "photo-c",
        "photo-d",
    ]

    for i, ((names, caption), position) in enumerate(
        zip(photos, positions)
    ):

        path = find_image(names)

        if path:

            ext = path.suffix.lower()

            mime = (
                "png"
                if ext == ".png"
                else "jpeg"
            )

            b64 = img_to_base64(path)

            html += f"""
            <div class="polaroid {position}">

                <div class="tape"></div>

                <img
                    src="data:image/{mime};base64,{b64}"
                >

                <div class="caption">
                    {caption} 💜
                </div>

            </div>
            """

    html += """

        <div class="note note-a">
            Mai iske liye biased hu 💜
        </div>

        <div class="note note-b">
            I want this view always ✨
        </div>

        <div class="note note-c">
            my favourite boy. always.
        </div>

    </div>
    """

    st.markdown(
        html,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="quote">
            "Celebrating you every day —
            but today is entirely yours."
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="
            text-align:center;
            color:#76558d;
            font-size:.85rem;
            margin:15px 0 5px;
        ">
            Fair warning: you can't skip ahead.
            Every page has a tiny task waiting for you. 😌
        </div>
        """,
        unsafe_allow_html=True
    )

    nav()


# ============================================================
# PAGE 1
# ============================================================

elif page == 1:

    st.markdown(
        "## A small question, just for you"
    )

    st.markdown(
        """
        <div class="card">
            <div class="small">
                There are no wrong answers here —
                only the one I already know is right. 💜
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    name = st.text_input(
        "What does your favourite person call you?",
        placeholder="Type your answer here..."
    )

    if st.button(
        "This is definitely me 😌"
    ):

        if name.strip():

            with st.spinner(
                "🔍 Verifying that you are, in fact, my favourite person..."
            ):

                time.sleep(1)

            st.session_state.answers["name"] = name.strip()

            st.success(
                "Identity confirmed. And lucky for you, you're stuck with me. 💜"
            )

        else:

            st.warning(
                "You have to type something first — I'm waiting. 😊"
            )

    nav(
        "name" in st.session_state.answers,
        "Type your answer and tap the button above first 💭"
    )


# ============================================================
# PAGE 2 — QUIZ
# ============================================================

elif page == 2:

    st.markdown(
        "## How well do you know us? 🎲"
    )

    st.caption(
        "A tiny, playful relationship quiz. No cheating — I'll know. 💗"
    )

    st.markdown(
        """
        <div class="quiz-q">
            1. In a dance-off with zero practice, who takes the win?
        </div>
        """,
        unsafe_allow_html=True
    )

    q1 = st.radio(
        "q1",
        [
            "Me, no contest 💃",
            "You, no contest 🕺",
            "We'd both lose spectacularly"
        ],
        index=None,
        label_visibility="collapsed",
        key="q1_widget"
    )

    st.markdown(
        """
        <div class="quiz-q">
            2. Who's more likely to text "you up?" at 1am?
        </div>
        """,
        unsafe_allow_html=True
    )

    q2 = st.radio(
        "q2",
        [
            "Me, guilty as charged",
            "You, guilty as charged",
            "Both of us, shamelessly"
        ],
        index=None,
        label_visibility="collapsed",
        key="q2_widget"
    )

    st.markdown(
        """
        <div class="quiz-q">
            3. Stranded on a desert island, who packs snacks
            and who packs snacks... for the vibes?
        </div>
        """,
        unsafe_allow_html=True
    )

    q3 = st.radio(
        "q3",
        [
            "Me — practical to a fault",
            "You — practical to a fault",
            "Neither of us survives a week"
        ],
        index=None,
        label_visibility="collapsed",
        key="q3_widget"
    )

    st.markdown(
        """
        <div class="quiz-q">
            4. Real talk — who loves the other person a little more?
        </div>
        """,
        unsafe_allow_html=True
    )

    q4 = st.radio(
        "q4",
        [
            "Me 💜",
            "You 💜",
            "Honestly, both"
        ],
        index=None,
        label_visibility="collapsed",
        key="q4_widget"
    )

    if st.button(
        "Submit my very accurate answers"
    ):

        if None in (q1, q2, q3, q4):

            st.warning(
                "Pick an answer for every question first — no skipping 👀"
            )

        else:

            st.session_state.answers.update(
                {
                    "q1": q1,
                    "q2": q2,
                    "q3": q3,
                    "q4": q4
                }
            )

            st.balloons()

    if "q4" in st.session_state.answers:

        a = st.session_state.answers

        if a["q4"].startswith("You"):

            verdict = (
                "Aww, close call — but I still say it's me. 💜"
            )

        elif a["q4"].startswith("Me"):

            verdict = (
                "See? I've been telling you this the whole time. 💜"
            )

        else:

            verdict = (
                "The most diplomatic answer in relationship history. Respect. 🫡"
            )

        st.markdown(
            f"""
            <div class="card">

                <div class="small">
                    According to you:
                    <b>{a['q1']}</b>
                    wins the dance-off,
                    and <b>{a['q2']}</b>
                    sends the risky 1am text.
                    Noted and filed away. 📝
                </div>

                <div class="quote"
                     style="font-size:1.3rem;">
                    {verdict}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    nav(
        "q4" in st.session_state.answers,
        "Submit your answers first, sneaky 👀"
    )


# ============================================================
# PAGE 3 — MEMORIES
# ============================================================

elif page == 3:

    st.markdown(
        "## A few of my favourite versions/memories of us"
    )

    st.markdown(
        """
        <div class="small">
            Some memories deserve more than just a place
            in the camera roll — they deserve a little home
            of their own.
        </div>
        """,
        unsafe_allow_html=True
    )

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


# ============================================================
# PAGE 4
# ============================================================

elif page == 4:

    st.markdown(
        "## Things I hope you never forget"
    )

    st.caption(
        "No task here, just a few reminders I need you to keep. 💜"
    )

    points = [

        "We are proud of you and love celebrating you.",

        "You don't have to have everything figured out right now — things "
        "will fall back into place gradually, so no tension babu.",

        "I hope you keep choosing the things that make you genuinely happy.",

        "I hope you chase the big dreams, even the ones that feel far away. You deserve everything.",

        "I hope you never forget how capable you truly are. You are the softest guy that i dreamt of.",

        "And on the days you do forget — I'll be here to remind you. 💜",
    ]

    html = '<div class="points-grid">'

    for i, text in enumerate(points, 1):

        html += f"""
        <div class="point-card">

            <div class="point-num">
                {i:02}
            </div>

            <div class="point-text">
                {text}
            </div>

        </div>
        """

    html += "</div>"

    st.markdown(
        html,
        unsafe_allow_html=True
    )

    nav()


# ============================================================
# PAGE 5 — SURPRISE
# ============================================================

elif page == 5:

    st.markdown(
        "## Pick your poison 😏 (the fun kind)"
    )

    st.caption(
        "You may open only one. Choose with your heart, not your curiosity. 💗"
    )

    choices = {

        "💌 A soft one":
            "I love you more than I could ever fit into a website — and believe me, I tried.",

        "🌙 A gentle tease":
            "You're officially one year older today ( Ab nahi hu tumse badi same same hogye ab ). "
            "Fortunately for you, I've decided to be kind about it. 😊",

        "🌱 A future one":
            "One day we'll look back at this version of us, and be so proud of everything we built together.",
    }

    for label, message in choices.items():

        if st.button(
            label,
            key=f"surprise_{label}"
        ):

            st.session_state.answers["surprise"] = label

            st.balloons()

    if "surprise" in st.session_state.answers:

        message = choices[
            st.session_state.answers["surprise"]
        ]

        st.markdown(
            f"""
            <div class="card">

                <div class="quote">
                    {message}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    nav(
        "surprise" in st.session_state.answers,
        "Pick a surprise above to continue 🎁"
    )


# ============================================================
# PAGE 6 — CAKE
# ============================================================

elif page == 6:

    st.markdown(
        "## One last thing before the letter..."
    )

    st.markdown(
        """
        <div style="
            text-align:center;
            margin-top:5px;
        ">

            <div style="
                font-family:'Dancing Script',cursive;
                font-size:clamp(3rem,8vw,5rem);
                color:#7c3fa8;
                line-height:1;
            ">
                Cut the Cake
            </div>

            <div style="
                color:#76558d;
                margin-top:8px;
            ">
                You have one important birthday duty left to perform.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    cut = st.session_state.answers.get(
        "cake",
        False
    )

    # IMPORTANT:
    # Everything below is HTML/CSS.
    # No SVG. No JavaScript. No fragile animation.

    cake_class = "cake-area cutting" if cut else "cake-area"

    st.markdown(
        f"""
        <div class="{cake_class}">

            <div class="cake">

                <div class="cake-bottom"></div>

                <div class="cake-cream-bottom"></div>

                <div class="cake-middle"></div>

                <div class="cream"></div>

                <div class="candle c1">
                    <div class="flame"></div>
                </div>

                <div class="candle c2">
                    <div class="flame"></div>
                </div>

                <div class="candle c3">
                    <div class="flame"></div>
                </div>

            </div>


            <div class="knife">

                <div class="knife-blade"></div>

                <div class="knife-handle"></div>

            </div>


            <div class="slice">

                <div class="slice-purple"></div>

                <div class="slice-cream"></div>

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    if not cut:

        st.markdown(
            """
            <div style="
                text-align:center;
                color:#76558d;
                margin-top:-5px;
            ">
                Fun fact: virtual cake has zero calories.
                Cut freely. 🍰
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "🔪 Cut the cake 🎂",
            key="cut_cake"
        ):

            st.session_state.answers["cake"] = True

            st.rerun()

    else:

        st.balloons()

        st.markdown(
            """
            <div class="cake-message">
                🎂✨ You did it! ✨🎂
            </div>

            <div style="
                text-align:center;
                color:#76558d;
                margin-top:5px;
            ">
                Make a wish — I have a feeling I already know mine. 💜
            </div>
            """,
            unsafe_allow_html=True
        )

    nav(
        cut,
        "You must cut the cake first — no shortcuts 🎂"
    )


# ============================================================
# PAGE 7 — LETTER
# ============================================================

elif page == 7:

    st.markdown(
        "## The Letter"
    )

    st.markdown(
        """
        <div class="small">
            Everything else on this little site was just the build-up.
            This part, I mean with my whole heart.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="letter-card">

            <div class="letter-text">
                {FINAL_LETTER.strip()}
            </div>

            <div class="letter-signoff">
                — always yours 💜
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    felt = st.checkbox(
        "I felt every word of this 💜",
        key="felt_letter"
    )

    nav(
        felt,
        "Take a moment, then check the box above 💭"
    )


# ============================================================
# PAGE 8 — FINAL SURPRISE
# ============================================================

elif page == 8:

    st.markdown(
        "## One last surprise"
    )

    st.caption(
        "Tap the card below to open it. 💜"
    )

    img_path = find_image(
        ["birthday_final.jpeg", "birthday_final"]
    )

    if img_path:

        ext = img_path.suffix.lower()

        mime = (
            "png"
            if ext == ".png"
            else "jpeg"
        )

        b64 = img_to_base64(
            img_path
        )

        front = f"""
        <img
            src="data:image/{mime};base64,{b64}"
            alt="Birthday photo"
        >
        """

    else:

        front = """
        <div style="
            height:100%;
            display:flex;
            align-items:center;
            justify-content:center;
            background:#fff;
            color:#9b5cc7;
        ">
            💜 Photo not found
        </div>
        """

    st.markdown(
        f"""
        <div class="flip-card">

            <input
                type="checkbox"
                id="flipToggle"
                class="flip-input"
            >

            <label
                for="flipToggle"
                class="flip-inner"
            >

                <div class="flip-face flip-front">

                    {front}

                    <div class="flip-hint">
                        Tap to open your last surprise 💜
                    </div>

                </div>


                <div class="flip-face flip-back">

                    <div style="
                        font-size:.7rem;
                        letter-spacing:3px;
                        color:#f2699e;
                        text-transform:uppercase;
                    ">
                        The final page
                    </div>

                    <h1>
                        HAPPY<br>
                        BIWRTHDAY AGAIN JI
                    </h1>

                    <p>
                        Saksham —<br>
                        I love celebrating you <br>
                        Biggest biwrthday hugs and kisses to you.
                    </p>

                    <div class="quote"
                         style="font-size:1.4rem;">
                        "And yes... I would choose you again."
                    </div>

                    <div style="
                        font-size:2rem;
                        margin-top:10px;
                    ">
                        💜 💗 🎂 💗 💜
                    </div>

                </div>

            </label>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        Made with an unreasonable amount of love 💜
    </div>
    """,
    unsafe_allow_html=True
)
