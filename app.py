import time
import base64
from pathlib import Path

import streamlit as st


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="For My Birthday Boy 💜",
    page_icon="💜",
    layout="centered",
    initial_sidebar_state="collapsed",
)


# ============================================================
# PATHS
# ============================================================

BASE_DIR = Path(__file__).parent
ASSETS = BASE_DIR / "assets"


# ============================================================
# YOUR LETTER
# DO NOT CHANGE YOUR WORDING
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


# ============================================================
# IMAGE HELPERS
# ============================================================

def find_image(filename):
    """
    Finds an image regardless of common extension/case.
    """

    exact = ASSETS / filename

    if exact.exists():
        return exact

    stem = Path(filename).stem

    possible = [
        ".jpeg",
        ".jpg",
        ".png",
        ".JPG",
        ".JPEG",
        ".PNG",
    ]

    for ext in possible:
        candidate = ASSETS / f"{stem}{ext}"
        if candidate.exists():
            return candidate

    return None


def image_base64(path):
    with open(path, "rb") as file:
        return base64.b64encode(file.read()).decode()


def show_photo(filename, width="100%"):
    """
    Safe Streamlit image display.
    """

    path = find_image(filename)

    if path:
        st.image(
            str(path),
            use_container_width=True
        )
    else:
        st.warning(
            f'Photo "{filename}" not found in assets.'
        )


# ============================================================
# GLOBAL CSS
# ============================================================

st.markdown(
    """
<style>

@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,600&family=Dancing+Script:wght@600;700&family=Poppins:wght@300;400;500;600;700&display=swap');


/* =========================================================
   GLOBAL
========================================================= */

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    min-height: 100vh;

    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(255, 159, 196, .30),
            transparent 28%
        ),
        radial-gradient(
            circle at 90% 10%,
            rgba(185, 142, 224, .30),
            transparent 30%
        ),
        radial-gradient(
            circle at 15% 90%,
            rgba(230, 209, 245, .55),
            transparent 35%
        ),
        radial-gradient(
            circle at 90% 85%,
            rgba(255, 209, 227, .40),
            transparent 35%
        ),
        linear-gradient(
            150deg,
            #fff9ff 0%,
            #f8edfc 45%,
            #f3e5fa 75%,
            #fff4f8 100%
        );

    color: #4a2a63;
}


.block-container {
    max-width: 1050px;
    padding-top: 1rem;
    padding-bottom: 4rem;
}


/* =========================================================
   TYPOGRAPHY
========================================================= */

h1,
h2,
h3 {
    font-family: 'Cormorant Garamond', serif !important;
    color: #5e2b83 !important;
}

p,
div,
span,
label,
li {
    color: #4a2a63;
}


/* =========================================================
   FLOATING HEARTS
========================================================= */

.heart {
    position: fixed;
    bottom: -50px;
    pointer-events: none;
    z-index: 1;

    animation-name: floatHeart;
    animation-timing-function: linear;
    animation-iteration-count: infinite;

    opacity: .55;
}

@keyframes floatHeart {

    0% {
        transform:
            translateY(0)
            rotate(0deg);
        opacity: 0;
    }

    10% {
        opacity: .65;
    }

    50% {
        transform:
            translateY(-50vh)
            translateX(25px)
            rotate(12deg);
    }

    100% {
        transform:
            translateY(-115vh)
            translateX(-20px)
            rotate(-12deg);
        opacity: 0;
    }
}


/* =========================================================
   PAGE PROGRESS
========================================================= */

.progress-text {
    text-align: center;
    color: #7c3fa8;
    font-size: .72rem;
    letter-spacing: 2px;
    font-weight: 600;
    margin-bottom: .4rem;
}


/* =========================================================
   BUTTONS
========================================================= */

div.stButton > button {
    width: 100%;
    min-height: 3rem;

    border-radius: 999px;

    border: none;

    background:
        linear-gradient(
            90deg,
            #f2699e,
            #9b5cc7
        );

    color: white;

    font-weight: 600;

    box-shadow:
        0 10px 28px
        rgba(155, 92, 199, .28);

    transition: all .18s ease;
}

div.stButton > button p {
    color: white !important;
}

div.stButton > button:hover {
    transform: translateY(-2px);

    box-shadow:
        0 14px 35px
        rgba(155, 92, 199, .38);
}


/* =========================================================
   GENERAL CARD
========================================================= */

.card {
    background:
        rgba(255, 255, 255, .72);

    backdrop-filter: blur(8px);

    border:
        1px solid
        rgba(185, 142, 224, .35);

    border-radius: 24px;

    padding: 1.5rem;

    margin: 1rem 0;

    box-shadow:
        0 14px 40px
        rgba(124, 63, 168, .12);
}

.small {
    color: #6d4a86;
    font-size: .92rem;
    line-height: 1.75;
}

.quote {
    font-family: 'Dancing Script', cursive;

    font-size: 2rem;

    line-height: 1.4;

    text-align: center;

    color: #5e2b83;

    padding: 1rem;
}


/* =========================================================
   FIRST PAGE — SCRAPBOOK
========================================================= */

.scrapbook {
    position: relative;

    min-height: 690px;

    margin-top: .5rem;

    overflow: hidden;

    border-radius: 34px;

    background:
        linear-gradient(
            135deg,
            rgba(255,255,255,.78),
            rgba(250,239,255,.55)
        );

    border:
        1px solid
        rgba(185,142,224,.28);

    box-shadow:
        0 25px 70px
        rgba(124,63,168,.15);
}


/* little paper texture */

.scrapbook::before {
    content: "";

    position: absolute;

    inset: 0;

    opacity: .20;

    background-image:
        radial-gradient(
            rgba(124,63,168,.13) 1px,
            transparent 1px
        );

    background-size: 18px 18px;

    pointer-events: none;
}


/* =========================================================
   SCRAPBOOK CENTER
========================================================= */

.scrap-center {
    position: absolute;

    left: 50%;
    top: 50%;

    transform:
        translate(-50%, -50%);

    width: 43%;

    min-width: 290px;

    text-align: center;

    z-index: 5;

    padding: 2.2rem 1.5rem;

    border-radius: 28px;

    background:
        rgba(255,255,255,.88);

    border:
        2px solid
        rgba(255,255,255,.95);

    box-shadow:
        0 20px 55px
        rgba(124,63,168,.17);

    backdrop-filter: blur(8px);
}

.scrap-eyebrow {
    color: #f2699e;

    text-transform: uppercase;

    letter-spacing: 2px;

    font-size: .67rem;

    font-weight: 600;

    margin-bottom: .7rem;
}

.scrap-center h1 {
    font-family:
        'Dancing Script',
        cursive !important;

    font-size:
        clamp(2.5rem, 5vw, 4.6rem);

    line-height: 1.05;

    margin: .2rem 0 1rem;

    background:
        linear-gradient(
            100deg,
            #7c3fa8,
            #f2699e,
            #9b5cc7
        );

    -webkit-background-clip: text;
    background-clip: text;

    -webkit-text-fill-color: transparent;
}

.scrap-subtitle {
    color: #6d4a86;

    font-size: .92rem;

    line-height: 1.7;
}


/* =========================================================
   HANGING PHOTOS
========================================================= */

.hanging-photo {
    position: absolute;

    width: 145px;

    padding: 9px 9px 15px;

    background: white;

    border-radius: 3px;

    box-shadow:
        0 12px 30px
        rgba(83,44,105,.22);

    z-index: 3;

    transition:
        transform .3s ease,
        box-shadow .3s ease;
}

.hanging-photo:hover {
    transform:
        rotate(0deg)
        scale(1.08) !important;

    z-index: 20;

    box-shadow:
        0 20px 40px
        rgba(83,44,105,.28);
}

.hanging-photo img {
    width: 100%;
    height: 145px;

    object-fit: cover;

    display: block;

    border-radius: 2px;
}

.photo-caption {
    font-family:
        'Dancing Script',
        cursive;

    color: #7c3fa8;

    text-align: center;

    font-size: .85rem;

    margin-top: 7px;
}


/* strings */

.photo-string {
    position: absolute;

    width: 2px;

    background:
        linear-gradient(
            to bottom,
            rgba(124,63,168,.35),
            rgba(242,105,158,.20)
        );

    height: 125px;

    transform-origin: top;

    z-index: 2;
}

.string-1 {
    left: 11%;
    top: 0;
    transform: rotate(-3deg);
}

.string-2 {
    left: 31%;
    top: 0;
    height: 115px;
    transform: rotate(4deg);
}

.string-3 {
    right: 31%;
    top: 0;
    height: 115px;
    transform: rotate(-4deg);
}

.string-4 {
    right: 11%;
    top: 0;
    transform: rotate(3deg);
}


/* photo positions */

.photo-1 {
    left: 5%;
    top: 9%;
    transform: rotate(-7deg);
}

.photo-2 {
    left: 23%;
    top: 5%;
    transform: rotate(6deg);
}

.photo-3 {
    right: 23%;
    top: 6%;
    transform: rotate(-5deg);
}

.photo-4 {
    right: 5%;
    top: 11%;
    transform: rotate(8deg);
}

.photo-5 {
    left: 6%;
    bottom: 9%;
    transform: rotate(6deg);
}

.photo-6 {
    left: 24%;
    bottom: 4%;
    transform: rotate(-5deg);
}

.photo-7 {
    right: 24%;
    bottom: 5%;
    transform: rotate(5deg);
}

.photo-8 {
    right: 5%;
    bottom: 10%;
    transform: rotate(-7deg);
}


/* decorative stickers */

.sticker {
    position: absolute;

    z-index: 6;

    font-size: 1.8rem;

    filter:
        drop-shadow(
            0 5px 8px
            rgba(124,63,168,.15)
        );
}

.sticker-1 {
    top: 39%;
    left: 12%;
    transform: rotate(-12deg);
}

.sticker-2 {
    top: 42%;
    right: 12%;
    transform: rotate(14deg);
}

.sticker-3 {
    bottom: 34%;
    left: 43%;
    transform: rotate(-8deg);
}


/* mobile */

@media (max-width: 700px) {

    .scrapbook {
        min-height: 850px;
    }

    .scrap-center {
        width: 70%;
        min-width: 0;

        top: 50%;

        padding: 1.5rem 1rem;
    }

    .hanging-photo {
        width: 105px;
    }

    .hanging-photo img {
        height: 105px;
    }

    .photo-1 {
        left: 2%;
        top: 5%;
    }

    .photo-2 {
        left: 27%;
        top: 2%;
    }

    .photo-3 {
        right: 27%;
        top: 2%;
    }

    .photo-4 {
        right: 2%;
        top: 5%;
    }

    .photo-5 {
        left: 2%;
        bottom: 4%;
    }

    .photo-6 {
        left: 27%;
        bottom: 1%;
    }

    .photo-7 {
        right: 27%;
        bottom: 1%;
    }

    .photo-8 {
        right: 2%;
        bottom: 4%;
    }

    .photo-string {
        height: 80px;
    }
}


/* =========================================================
   MEMORY PHOTOS
========================================================= */

.photo-frame {
    background: white;

    padding: 11px;

    border-radius: 24px;

    box-shadow:
        0 18px 45px
        rgba(124,63,168,.18);
}

.photo-frame img {
    border-radius: 17px;
}


/* =========================================================
   MEMORY CARDS
========================================================= */

.memory-row {
    margin-bottom: 1.8rem;
}

.mem-card {
    height: 100%;

    min-height: 220px;

    display: flex;

    align-items: center;

    background:
        rgba(255,255,255,.74);

    border:
        1px solid
        rgba(185,142,224,.35);

    border-radius: 24px;

    padding: 1.4rem;

    box-shadow:
        0 14px 36px
        rgba(124,63,168,.12);
}

.mem-tag {
    color: #f2699e;

    text-transform: uppercase;

    letter-spacing: 2px;

    font-size: .68rem;

    font-weight: 600;
}

.mem-card h3 {
    margin: .3rem 0 .5rem;

    font-size: 1.5rem;
}

.mem-card p {
    color: #6d4a86;

    line-height: 1.7;

    font-size: .94rem;
}


/* =========================================================
   POINTS
========================================================= */

.points-grid {
    display: grid;

    grid-template-columns:
        repeat(
            auto-fit,
            minmax(260px, 1fr)
        );

    gap: .8rem;
}

.point-card {
    display: flex;

    gap: .7rem;

    align-items: flex-start;

    background:
        rgba(255,255,255,.72);

    border:
        1px solid
        rgba(185,142,224,.35);

    border-radius: 19px;

    padding: 1rem;

    box-shadow:
        0 10px 28px
        rgba(124,63,168,.10);
}

.point-num {
    font-family:
        'Cormorant Garamond',
        serif;

    font-weight: 700;

    font-size: 1.5rem;

    color: #f2699e;
}

.point-text {
    font-size: 1.03rem;

    line-height: 1.5;

    font-weight: 500;
}


/* =========================================================
   LETTER
========================================================= */

.letter-card {
    background:
        linear-gradient(
            180deg,
            rgba(255,255,255,.94),
            rgba(250,240,255,.88)
        );

    border:
        1px solid
        rgba(185,142,224,.4);

    border-radius: 27px;

    padding: 2rem 1.7rem;

    box-shadow:
        0 20px 55px
        rgba(124,63,168,.16);

    position: relative;
}

.letter-text {
    font-family:
        'Cormorant Garamond',
        serif;

    font-style: italic;

    font-size: 1.28rem;

    line-height: 2;

    color: #4a2a63;

    white-space: pre-line;

    padding-top: .7rem;
}

.letter-signoff {
    text-align: right;

    font-family:
        'Dancing Script',
        cursive;

    font-size: 1.6rem;

    color: #7c3fa8;
}


/* =========================================================
   CAKE
========================================================= */

.cake-container {
    text-align: center;

    margin: 2rem auto;
}

.cake {
    position: relative;

    width: 290px;

    height: 260px;

    margin: auto;
}

.cake-shadow {
    position: absolute;

    bottom: 15px;

    left: 20px;

    width: 250px;

    height: 28px;

    background:
        rgba(124,63,168,.12);

    border-radius: 50%;
}


/* bottom cake */

.cake-bottom {
    position: absolute;

    left: 25px;

    bottom: 38px;

    width: 240px;

    height: 105px;

    border-radius:
        15px
        15px
        24px
        24px;

    background:
        linear-gradient(
            180deg,
            #c98fe6,
            #9b5cc7
        );

    box-shadow:
        0 14px 25px
        rgba(124,63,168,.22);

    transition:
        transform .8s ease;
}


/* top cake */

.cake-top {
    position: absolute;

    left: 55px;

    bottom: 125px;

    width: 180px;

    height: 75px;

    border-radius:
        15px
        15px
        18px
        18px;

    background:
        linear-gradient(
            180deg,
            #ffd0e2,
            #ff9fc4
        );

    box-shadow:
        0 8px 18px
        rgba(242,105,158,.20);
}


/* frosting */

.frosting {
    position: absolute;

    left: 55px;

    bottom: 173px;

    width: 180px;

    height: 25px;

    border-radius: 50%;

    background: #fff7fb;
}


/* candles */

.candles {
    position: absolute;

    left: 78px;

    bottom: 194px;

    width: 135px;

    display: flex;

    justify-content:
        space-between;
}

.candle {
    position: relative;

    width: 9px;

    height: 40px;

    border-radius: 5px;

    background:
        linear-gradient(
            90deg,
            #7c3fa8,
            #b98ee0
        );
}

.flame {
    position: absolute;

    left: -3px;

    top: -17px;

    font-size: 17px;

    animation:
        flicker 1s
        ease-in-out
        infinite;
}

@keyframes flicker {

    0%, 100% {
        transform: scale(1);
    }

    50% {
        transform:
            scale(1.18)
            rotate(3deg);
    }
}


/* knife */

.knife {
    position: absolute;

    width: 130px;

    height: 16px;

    background: #e4e0ea;

    border-radius: 7px;

    top: 20px;

    right: -20px;

    transform:
        rotate(-35deg);

    transform-origin:
        left center;

    box-shadow:
        0 4px 8px
        rgba(0,0,0,.12);

    transition:
        top .8s ease,
        right .8s ease,
        transform .8s ease;
}

.knife::before {
    content: "";

    position: absolute;

    left: -35px;

    top: -5px;

    width: 45px;

    height: 26px;

    border-radius: 8px;

    background: #5e2b83;
}

.cake-cut .knife {
    top: 115px;

    right: 70px;

    transform:
        rotate(90deg);
}

.cake-cut .cake-bottom {
    transform:
        translateX(-6px);
}


/* =========================================================
   FINAL FLIP CARD
========================================================= */

.flip-wrapper {
    perspective: 1000px;

    width: 100%;

    max-width: 420px;

    margin: 2rem auto;
}

.flip-checkbox {
    display: none;
}

.flip-inner {
    position: relative;

    width: 100%;

    padding-top: 125%;

    transition:
        transform .8s ease;

    transform-style:
        preserve-3d;

    cursor: pointer;
}

.flip-checkbox:checked
+ .flip-inner {
    transform:
        rotateY(180deg);
}

.flip-face {
    position: absolute;

    inset: 0;

    border-radius: 27px;

    overflow: hidden;

    backface-visibility: hidden;

    box-shadow:
        0 20px 50px
        rgba(124,63,168,.20);
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

    padding: .8rem;

    text-align: center;

    color: white;

    background:
        rgba(94,43,131,.65);

    font-weight: 600;
}

.flip-back {
    transform:
        rotateY(180deg);

    background:
        linear-gradient(
            160deg,
            #fff,
            #f6ebfc
        );

    display: flex;

    flex-direction: column;

    justify-content: center;

    align-items: center;

    text-align: center;

    padding: 1.5rem;
}

.flip-back h1 {
    font-family:
        'Dancing Script',
        cursive !important;

    font-size:
        clamp(2rem, 7vw, 3.5rem);

    line-height: 1;

    background:
        linear-gradient(
            100deg,
            #7c3fa8,
            #f2699e
        );

    -webkit-background-clip: text;

    -webkit-text-fill-color:
        transparent;
}

.flip-back p {
    color: #6d4a86;

    line-height: 1.8;
}


/* =========================================================
   FOOTER
========================================================= */

.footer {
    text-align: center;

    color: #9b5cc7;

    font-size: .75rem;

    padding-top: 2.5rem;

    letter-spacing: .5px;
}


/* =========================================================
   MOBILE
========================================================= */

@media (max-width: 480px) {

    .block-container {
        padding-left: .8rem;
        padding-right: .8rem;
    }

    .letter-card {
        padding: 1.4rem 1rem;
    }

    .letter-text {
        font-size: 1.08rem;
    }

    .cake {
        transform: scale(.85);
        margin-left: -10%;
        margin-right: -10%;
    }
}

</style>
""",
    unsafe_allow_html=True,
)


# ============================================================
# FLOATING HEARTS
# ============================================================

st.markdown(
    """
<div class="heart"
     style="left:5%;font-size:20px;animation-duration:14s;animation-delay:0s;">
    💗
</div>

<div class="heart"
     style="left:17%;font-size:16px;animation-duration:17s;animation-delay:2s;">
    💜
</div>

<div class="heart"
     style="left:31%;font-size:23px;animation-duration:12s;animation-delay:4s;">
    💕
</div>

<div class="heart"
     style="left:47%;font-size:18px;animation-duration:15s;animation-delay:1s;">
    💜
</div>

<div class="heart"
     style="left:61%;font-size:22px;animation-duration:13s;animation-delay:5s;">
    💗
</div>

<div class="heart"
     style="left:76%;font-size:17px;animation-duration:18s;animation-delay:3s;">
    💜
</div>

<div class="heart"
     style="left:90%;font-size:23px;animation-duration:14s;animation-delay:6s;">
    💕
</div>
""",
    unsafe_allow_html=True,
)


# ============================================================
# NAVIGATION
# ============================================================

def navigation(unlocked=True, message="Finish the task above to unlock this 💭"):

    st.write("")

    current = st.session_state.page

    if current == 0:

        st.button(
            "Open your birthday surprise →",
            on_click=next_page,
            key="start_button",
        )

        return

    col1, col2 = st.columns(2)

    with col1:
        st.button(
            "← Back",
            on_click=prev_page,
            key=f"back_{current}",
        )

    with col2:

        if current < TOTAL - 1:

            if unlocked:

                st.button(
                    "Continue →",
                    on_click=next_page,
                    key=f"next_{current}",
                )

            else:

                st.button(
                    "🔒 Continue →",
                    disabled=True,
                    key=f"locked_{current}",
                )

    if not unlocked:

        st.markdown(
            f"""
            <div style="
                text-align:center;
                color:#f2699e;
                font-size:.82rem;
                margin-top:.5rem;
            ">
                {message}
            </div>
            """,
            unsafe_allow_html=True,
        )


# ============================================================
# HERO PHOTO
# ============================================================

def hero_photo(filename, css_class, caption=""):

    path = find_image(filename)

    if not path:
        return f"""
        <div class="hanging-photo {css_class}">
            <div style="
                height:145px;
                display:flex;
                align-items:center;
                justify-content:center;
                text-align:center;
                background:#faf5ff;
                color:#7c3fa8;
                font-size:.7rem;
            ">
                Photo missing
            </div>
        </div>
        """

    b64 = image_base64(path)

    extension = path.suffix.lower()

    mime = "png" if extension == ".png" else "jpeg"

    return f"""
    <div class="hanging-photo {css_class}">
        <img
            src="data:image/{mime};base64,{b64}"
            alt="memory"
        >
        <div class="photo-caption">
            {caption}
        </div>
    </div>
    """


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
            YOUR BIRTHDAY JOURNEY · {page}/{TOTAL - 1}
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.progress(
        page / (TOTAL - 1)
    )


# ============================================================
# PAGE 0
# ============================================================

if page == 0:

    photos_html = ""

    photos_html += hero_photo(
        "hero_1.jpeg",
        "photo-1",
        "💜"
    )

    photos_html += hero_photo(
        "hero_2.jpeg",
        "photo-2",
        "my favourite"
    )

    photos_html += hero_photo(
        "hero_3.jpeg",
        "photo-3",
        "💕"
    )

    photos_html += hero_photo(
        "hero_4.jpeg",
        "photo-4",
        "us"
    )

    photos_html += hero_photo(
        "hero_5.jpeg",
        "photo-5",
        "always"
    )

    photos_html += hero_photo(
        "hero_6.jpeg",
        "photo-6",
        "pretty boy"
    )

    photos_html += hero_photo(
        "hero_7.jpeg",
        "photo-7",
        "✨"
    )

    photos_html += hero_photo(
        "hero_8.jpeg",
        "photo-8",
        "💗"
    )

    st.markdown(
        f"""
        <div class="scrapbook">

            <div class="photo-string string-1"></div>
            <div class="photo-string string-2"></div>
            <div class="photo-string string-3"></div>
            <div class="photo-string string-4"></div>

            {photos_html}

            <div class="sticker sticker-1">💜</div>
            <div class="sticker sticker-2">💗</div>
            <div class="sticker sticker-3">✨</div>

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

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="quote">
            "Celebrating you every day — but today is entirely yours.
            I just made a little of it about how much I adore you."
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style="
            text-align:center;
            color:#f2699e;
            font-size:1.1rem;
            letter-spacing:8px;
            margin:1rem 0;
        ">
            💜 · 💗 · 💜
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.caption(
        "Fair warning: you can't skip ahead. Every page has a tiny task waiting for you. 😌"
    )

    navigation()


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
        unsafe_allow_html=True,
    )

    name = st.text_input(
        "What does your favourite person call you?",
        placeholder="Type your answer here...",
    )

    if st.button(
        "This is definitely me 😌",
        key="identity_button",
    ):

        if name.strip():

            with st.spinner(
                "🔍 Verifying that you are, in fact, my favourite person..."
            ):

                time.sleep(1.1)

            st.session_state.answers["name"] = name.strip()

            st.success(
                "Identity confirmed. And lucky for you, you're stuck with me. 💜"
            )

        else:

            st.warning(
                "You have to type something first — I'm waiting. 😊"
            )

    unlocked = (
        "name"
        in st.session_state.answers
    )

    navigation(
        unlocked,
        "Type your answer and tap the button above first 💭"
    )


# ============================================================
# PAGE 2
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
        <div class="card">
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="quiz-q">1. In a dance-off with zero practice, who takes the win?</div>',
        unsafe_allow_html=True,
    )

    q1 = st.radio(
        "q1",
        [
            "Me, no contest 💃",
            "You, no contest 🕺",
            "We'd both lose spectacularly",
        ],
        index=None,
        label_visibility="collapsed",
        key="q1_widget",
    )

    st.markdown(
        '<div class="quiz-q">2. Who\'s more likely to text "you up?" at 1am?</div>',
        unsafe_allow_html=True,
    )

    q2 = st.radio(
        "q2",
        [
            "Me, guilty as charged",
            "You, guilty as charged",
            "Both of us, shamelessly",
        ],
        index=None,
        label_visibility="collapsed",
        key="q2_widget",
    )

    st.markdown(
        '<div class="quiz-q">3. Stranded on a desert island, who packs snacks and who packs snacks... for the vibes?</div>',
        unsafe_allow_html=True,
    )

    q3 = st.radio(
        "q3",
        [
            "Me — practical to a fault",
            "You — practical to a fault",
            "Neither of us survives a week",
        ],
        index=None,
        label_visibility="collapsed",
        key="q3_widget",
    )

    st.markdown(
        '<div class="quiz-q">4. Real talk — who loves the other person a little more?</div>',
        unsafe_allow_html=True,
    )

    q4 = st.radio(
        "q4",
        [
            "Me 💜",
            "You 💜",
            "Honestly, both",
        ],
        index=None,
        label_visibility="collapsed",
        key="q4_widget",
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True,
    )

    if st.button(
        "Submit my very accurate answers",
        key="quiz_submit",
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
                    "q4": q4,
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
                    <b>{a["q1"]}</b>
                    wins the dance-off, and
                    <b>{a["q2"]}</b>
                    sends the risky 1am text.
                    Noted and filed away. 📝

                </div>

                <div class="quote"
                     style="font-size:1.3rem;">

                    {verdict}

                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    unlocked = (
        "q4"
        in st.session_state.answers
    )

    navigation(
        unlocked,
        "Submit your answers first, sneaky 👀"
    )


# ============================================================
# PAGE 3
# ============================================================

elif page == 3:

    st.markdown(
        "## A few of my favourite versions/memories of us"
    )

    st.markdown(
        """
        <div class="small">
            Some memories deserve more than just a place in the
            camera roll — they deserve a little home of their own.
        </div>
        """,
        unsafe_allow_html=True,
    )

    memories = [

        (
            "first_trip.jpeg",
            "Memory 01",
            "OUR FIRST TRIP",
            "You are this cute, ofc I am biased for you. ye picture meri favourite hai I never posted it "
            "becuase i wanted to post on your biwrthday. Will cherish this trip always.",
        ),

        (
            "the_view.jpeg",
            "Memory 02",
            "Dates to die for",
            "I prefer looking at you the same way on each date going forward, "
            "this is the perfect view i would give on world for.",
        ),

        (
            "prettiest_frame.jpeg",
            "Memory 03",
            "Scary car rides",
            "Little heart attacks is what you give when we are in this setup, "
            "no worries signing up for these with all my heart",
        ),
    ]

    for image, tag, title, text in memories:

        st.markdown(
            '<div class="memory-row">',
            unsafe_allow_html=True,
        )

        col1, col2 = st.columns(
            [1, 1],
            gap="large",
        )

        with col1:

            st.markdown(
                '<div class="photo-frame">',
                unsafe_allow_html=True,
            )

            show_photo(image)

            st.markdown(
                "</div>",
                unsafe_allow_html=True,
            )

        with col2:

            st.markdown(
                f"""
                <div class="mem-card">

                    <div>

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

                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown(
            "</div>",
            unsafe_allow_html=True,
        )

    navigation()


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

    cards = '<div class="points-grid">'

    for i, text in enumerate(points, 1):

        cards += f"""
        <div class="point-card">

            <div class="point-num">
                {i:02}
            </div>

            <div class="point-text">
                {text}
            </div>

        </div>
        """

    cards += "</div>"

    st.markdown(
        cards,
        unsafe_allow_html=True,
    )

    navigation()


# ============================================================
# PAGE 5
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
            key=f"surprise_{label}",
        ):

            st.session_state.answers[
                "surprise"
            ] = label

            st.balloons()

    if "surprise" in st.session_state.answers:

        selected = st.session_state.answers[
            "surprise"
        ]

        st.markdown(
            f"""
            <div class="card">

                <div class="quote">
                    {choices[selected]}
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    unlocked = (
        "surprise"
        in st.session_state.answers
    )

    navigation(
        unlocked,
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
            margin:1rem 0 2rem;
        ">

            <div style="
                color:#6d4a86;
                font-size:1rem;
            ">
                You have one important birthday duty left to perform.
            </div>

            <div style="
                font-family:'Dancing Script',cursive;
                font-size:4rem;
                line-height:1.1;
                background:linear-gradient(
                    100deg,
                    #7c3fa8,
                    #f2699e,
                    #9b5cc7
                );
                -webkit-background-clip:text;
                -webkit-text-fill-color:transparent;
            ">
                Cut the Cake
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    cut = st.session_state.answers.get(
        "cake",
        False,
    )

    cake_class = (
        "cake-container cake-cut"
        if cut
        else "cake-container"
    )

    st.markdown(
        f"""
        <div class="{cake_class}">

            <div class="cake">

                <div class="cake-shadow"></div>

                <div class="cake-bottom"></div>

                <div class="cake-top"></div>

                <div class="frosting"></div>

                <div class="candles">

                    <div class="candle">
                        <div class="flame">🔥</div>
                    </div>

                    <div class="candle">
                        <div class="flame">🔥</div>
                    </div>

                    <div class="candle">
                        <div class="flame">🔥</div>
                    </div>

                    <div class="candle">
                        <div class="flame">🔥</div>
                    </div>

                    <div class="candle">
                        <div class="flame">🔥</div>
                    </div>

                </div>

                <div class="knife"></div>

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    if not cut:

        st.caption(
            "Fun fact: virtual cake has zero calories. Cut freely. 🍰"
        )

        if st.button(
            "🔪 Cut the cake 🎂",
            key="cut_cake_button",
        ):

            st.session_state.answers[
                "cake"
            ] = True

            st.balloons()

            st.rerun()

    else:

        st.markdown(
            """
            <div style="
                text-align:center;
                margin:1rem 0 1.5rem;
            ">

                <div style="
                    font-size:4rem;
                ">
                    🎂✨💜
                </div>

                <div style="
                    font-family:'Dancing Script',cursive;
                    font-size:4rem;
                    color:#7c3fa8;
                ">
                    IT'S YOUR DAY!
                </div>

                <div style="
                    color:#6d4a86;
                    font-size:1rem;
                ">
                    Make a wish — I have a feeling I already know mine. 💜
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    navigation(
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
        unsafe_allow_html=True,
    )

    safe_letter = FINAL_LETTER.strip()

    st.markdown(
        f"""
        <div class="letter-card">

            <div style="
                text-align:center;
                font-size:2rem;
                margin-bottom:.5rem;
            ">
                💌
            </div>

            <div class="letter-text">
                {safe_letter}
            </div>

            <div class="letter-signoff">
                — always yours 💜
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    felt = st.checkbox(
        "I felt every word of this 💜",
        key="felt_letter",
    )

    navigation(
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

    final_photo = find_image(
        "birthday_final.jpeg"
    )

    if final_photo:

        b64 = image_base64(
            final_photo
        )

        extension = final_photo.suffix.lower()

        mime = (
            "png"
            if extension == ".png"
            else "jpeg"
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
            background:#faf5ff;
            color:#7c3fa8;
        ">
            💜 Photo "birthday_final.jpeg"
            not found 💜
        </div>
        """

    st.markdown(
        f"""
        <div class="flip-wrapper">

            <input
                type="checkbox"
                id="birthdayFlip"
                class="flip-checkbox"
            >

            <label
                for="birthdayFlip"
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
                        color:#f2699e;
                        text-transform:uppercase;
                        letter-spacing:2px;
                        font-size:.7rem;
                        font-weight:600;
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

                    <div class="quote">
                        "And yes... I would choose you again."
                    </div>

                    <div style="
                        font-size:2rem;
                    ">
                        💜 💗 🎂 💗 💜
                    </div>

                </div>

            </label>

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
        Made with an unreasonable amount of love 💜
    </div>
    """,
    unsafe_allow_html=True,
)
