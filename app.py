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

ASSETS = Path(__file__).parent / "assets"


# ============================================================
# YOUR LETTER — UNCHANGED
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
# ASSET HELPERS
# ============================================================

def find_image(name):
    """
    Finds image regardless of .jpg/.jpeg/.png capitalization.
    """
    possible = [
        name,
        f"{name}.jpg",
        f"{name}.jpeg",
        f"{name}.png",
        f"{name}.JPG",
        f"{name}.JPEG",
        f"{name}.PNG",
    ]

    for item in possible:
        path = ASSETS / item
        if path.exists():
            return path

    return None


def image_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def show_image(name, height=None):
    path = find_image(name)

    if not path:
        st.markdown(
            f"""
            <div class="missing-photo">
                💜 Photo "{name}" not found 💜
            </div>
            """,
            unsafe_allow_html=True,
        )
        return

    if height:
        st.image(str(path), width="stretch")
    else:
        st.image(str(path), width="stretch")


# ============================================================
# CSS
# ============================================================

st.markdown(
    """
<style>

@import url(
'https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,600&family=Dancing+Script:wght@500;600;700&family=Poppins:wght@300;400;500;600;700&display=swap'
);

:root {
    --purple-dark: #5b2c6f;
    --purple: #8e55b8;
    --purple-light: #c99be8;
    --pink: #f47da8;
    --pink-light: #ffd5e4;
    --cream: #fffafc;
    --ink: #4b3157;
}

html,
body,
[data-testid="stAppViewContainer"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(255, 183, 211, .42),
            transparent 25%
        ),
        radial-gradient(
            circle at 90% 10%,
            rgba(205, 160, 235, .38),
            transparent 28%
        ),
        radial-gradient(
            circle at 15% 85%,
            rgba(235, 204, 250, .55),
            transparent 30%
        ),
        radial-gradient(
            circle at 90% 85%,
            rgba(255, 215, 230, .45),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #fff8fd,
            #f7eafb,
            #fff5f8
        );

    min-height: 100vh;
}

.block-container {
    max-width: 920px;
    padding-top: 1.2rem;
    padding-bottom: 5rem;
}

h1,
h2,
h3 {
    font-family: 'Cormorant Garamond', serif !important;
    color: var(--purple-dark) !important;
}

p,
span,
label,
div {
    color: var(--ink);
}


/* ============================================================
   FLOATING HEARTS
   ============================================================ */

.heart-layer {
    position: fixed;
    inset: 0;
    pointer-events: none;
    overflow: hidden;
    z-index: 0;
}

.float-heart {
    position: absolute;
    bottom: -50px;
    animation-name: floatHeart;
    animation-timing-function: linear;
    animation-iteration-count: infinite;
    opacity: .7;
}

@keyframes floatHeart {

    0% {
        transform:
            translateY(0)
            rotate(0deg);
        opacity: 0;
    }

    10% {
        opacity: .75;
    }

    50% {
        transform:
            translateY(-50vh)
            translateX(25px)
            rotate(15deg);
    }

    90% {
        opacity: .35;
    }

    100% {
        transform:
            translateY(-110vh)
            translateX(-20px)
            rotate(-15deg);
        opacity: 0;
    }
}


/* ============================================================
   FIRST PAGE — SCRAPBOOK
   ============================================================ */

.scrapbook {
    position: relative;
    min-height: 720px;
    padding: 20px 10px 40px;
    overflow: hidden;
}


/* hanging strings */

.string {
    position: absolute;
    top: -20px;
    width: 2px;
    height: 145px;
    background: rgba(91,44,111,.35);
    transform-origin: top center;
    z-index: 1;
}

.string.one {
    left: 8%;
    transform: rotate(-7deg);
}

.string.two {
    left: 28%;
    height: 110px;
    transform: rotate(5deg);
}

.string.three {
    right: 28%;
    height: 125px;
    transform: rotate(-4deg);
}

.string.four {
    right: 8%;
    height: 150px;
    transform: rotate(7deg);
}


/* centre text */

.scrap-center {
    position: relative;
    z-index: 5;

    width: min(90%, 600px);
    margin: 145px auto 80px;

    padding: 35px 30px;

    background:
        rgba(255,255,255,.76);

    border:
        1px solid rgba(255,255,255,.9);

    border-radius: 30px;

    box-shadow:
        0 25px 70px rgba(91,44,111,.15);

    text-align: center;

    transform: rotate(-1deg);
}

.scrap-eyebrow {
    font-size: .72rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--pink) !important;
    font-weight: 600;
}

.scrap-center h1 {
    font-family: 'Dancing Script', cursive !important;
    font-size: clamp(3rem, 9vw, 5.5rem);
    line-height: 1.05;
    margin: 15px 0 20px;

    background:
        linear-gradient(
            90deg,
            #6c3a8b,
            #f06f9e,
            #8e55b8
        );

    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
}

.scrap-subtitle {
    font-size: 1rem;
    line-height: 1.8;
    color: #70567c !important;
}


/* ============================================================
   POLAROIDS
   ============================================================ */

.polaroid {
    position: absolute;

    background: white;

    padding: 10px 10px 30px;

    width: 185px;

    box-shadow:
        0 15px 35px rgba(91,44,111,.23);

    border-radius: 3px;

    z-index: 4;

    transition:
        transform .25s ease,
        box-shadow .25s ease;
}

.polaroid:hover {
    transform:
        rotate(0deg)
        scale(1.06) !important;

    box-shadow:
        0 25px 50px rgba(91,44,111,.3);

    z-index: 10;
}

.polaroid img {
    width: 100%;
    height: 155px;
    object-fit: cover;
}

.polaroid-caption {
    font-family: 'Dancing Script', cursive;
    font-size: 1.1rem;
    text-align: center;
    margin-top: 7px;
    color: var(--purple-dark) !important;
}

.photo-a {
    top: 15px;
    left: 3%;
    transform: rotate(-8deg);
}

.photo-b {
    top: 25px;
    right: 4%;
    transform: rotate(8deg);
}

.photo-c {
    bottom: 35px;
    left: 5%;
    transform: rotate(7deg);
}

.photo-d {
    bottom: 25px;
    right: 4%;
    transform: rotate(-7deg);
}


/* little tape */

.tape {
    position: absolute;
    width: 65px;
    height: 20px;
    background: rgba(255,224,150,.65);
    top: -10px;
    left: 50%;
    transform: translateX(-50%) rotate(-2deg);
}


/* tiny notes */

.note {
    position: absolute;
    z-index: 3;

    background: #fff6b8;

    padding: 15px 18px;

    font-family: 'Dancing Script', cursive;
    font-size: 1.15rem;

    box-shadow:
        0 10px 25px rgba(91,44,111,.14);
}

.note-one {
    left: 14%;
    top: 230px;
    transform: rotate(-6deg);
}

.note-two {
    right: 12%;
    top: 245px;
    transform: rotate(7deg);
}

.note-three {
    left: 38%;
    bottom: 15px;
    transform: rotate(-3deg);
}


/* ============================================================
   GENERAL CARDS
   ============================================================ */

.card {
    background: rgba(255,255,255,.78);

    border:
        1px solid rgba(201,155,232,.35);

    border-radius: 25px;

    padding: 1.5rem;

    margin: 1rem 0;

    box-shadow:
        0 15px 40px rgba(91,44,111,.12);
}

.quote {
    font-family: 'Dancing Script', cursive;
    font-size: 2rem;
    line-height: 1.4;
    color: var(--purple-dark) !important;
    text-align: center;
}

.small {
    color: #70567c !important;
    font-size: .92rem;
    line-height: 1.8;
}


/* ============================================================
   MEMORY PHOTOS
   ============================================================ */

.memory-card {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 25px;

    align-items: center;

    margin: 35px 0;
}

.memory-photo {
    background: white;
    padding: 12px;

    box-shadow:
        0 18px 45px rgba(91,44,111,.18);

    border-radius: 18px;
}

.memory-text {
    background: rgba(255,255,255,.75);
    padding: 25px;
    border-radius: 22px;

    box-shadow:
        0 12px 35px rgba(91,44,111,.1);
}

.memory-tag {
    text-transform: uppercase;
    letter-spacing: 2px;
    font-size: .68rem;
    color: var(--pink) !important;
    font-weight: 600;
}

.memory-text h3 {
    margin: 5px 0 10px;
}

.memory-text p {
    color: #70567c !important;
    line-height: 1.7;
}


/* ============================================================
   POINTS
   ============================================================ */

.points {
    display: grid;
    grid-template-columns:
        repeat(auto-fit,minmax(250px,1fr));

    gap: 12px;
}

.point {
    background: rgba(255,255,255,.78);

    border-radius: 20px;

    padding: 18px;

    display: flex;
    gap: 12px;

    box-shadow:
        0 10px 25px rgba(91,44,111,.09);
}

.point-number {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.6rem;
    font-weight: 700;
    color: var(--pink) !important;
}


/* ============================================================
   LETTER
   ============================================================ */

.letter {
    background:
        linear-gradient(
            180deg,
            rgba(255,255,255,.96),
            rgba(250,240,255,.92)
        );

    border-radius: 28px;

    padding: 35px 28px;

    box-shadow:
        0 20px 60px rgba(91,44,111,.16);

    border:
        1px solid rgba(201,155,232,.4);
}

.letter-text {
    white-space: pre-line;

    font-family: 'Cormorant Garamond', serif;

    font-size: 1.35rem;

    line-height: 1.9;

    font-style: italic;

    color: var(--ink) !important;
}

.signoff {
    text-align: right;

    font-family: 'Dancing Script', cursive;

    font-size: 1.7rem;

    color: var(--purple) !important;
}


/* ============================================================
   CAKE
   ============================================================ */

.cake {
    text-align: center;
    margin: 35px auto;
}

.cake-body {
    position: relative;

    width: 280px;
    height: 180px;

    margin: auto;
}

.cake-bottom {
    position: absolute;

    bottom: 0;
    left: 0;

    width: 280px;
    height: 100px;

    border-radius:
        20px 20px 25px 25px;

    background:
        linear-gradient(
            #c58be0,
            #8e55b8
        );

    box-shadow:
        0 15px 30px rgba(91,44,111,.2);
}

.cake-top {
    position: absolute;

    bottom: 80px;
    left: 35px;

    width: 210px;
    height: 70px;

    border-radius:
        18px 18px 12px 12px;

    background:
        linear-gradient(
            #ffd1e3,
            #ff9fc4
        );
}

.candle {
    position: absolute;

    bottom: 145px;

    width: 7px;
    height: 35px;

    background: var(--purple);

    border-radius: 5px;
}

.candle.one {
    left: 90px;
}

.candle.two {
    left: 135px;
}

.candle.three {
    left: 180px;
}

.flame {
    position: absolute;

    bottom: 177px;

    font-size: 25px;

    animation:
        flicker .8s infinite alternate;
}

.flame.one {
    left: 82px;
}

.flame.two {
    left: 127px;
}

.flame.three {
    left: 172px;
}

@keyframes flicker {
    from {
        transform: scale(.85) rotate(-3deg);
    }

    to {
        transform: scale(1.1) rotate(3deg);
    }
}

.cut-message {
    text-align: center;

    padding: 25px;

    background: rgba(255,255,255,.8);

    border-radius: 25px;

    box-shadow:
        0 15px 40px rgba(91,44,111,.12);
}


/* ============================================================
   FINAL
   ============================================================ */

.final-page {
    text-align: center;
    padding: 40px 10px;
}

.final-page h1 {
    font-family: 'Dancing Script', cursive !important;
    font-size: clamp(3rem,10vw,6rem);
}

.final-hearts {
    font-size: 3rem;
    margin: 20px;
}


/* ============================================================
   BUTTONS
   ============================================================ */

.stButton > button {
    width: 100%;

    border: none;

    border-radius: 999px;

    min-height: 3rem;

    background:
        linear-gradient(
            90deg,
            #f2699e,
            #8e55b8
        );

    color: white !important;

    font-weight: 600;

    box-shadow:
        0 10px 25px rgba(142,85,184,.25);
}

.stButton > button p {
    color: white !important;
}


/* ============================================================
   INPUTS
   ============================================================ */

input {
    border-radius: 15px !important;
}


/* ============================================================
   FOOTER
   ============================================================ */

.footer {
    text-align: center;

    padding: 40px 0 10px;

    color: var(--purple) !important;

    font-size: .75rem;
}


/* ============================================================
   MOBILE
   ============================================================ */

@media(max-width:700px) {

    .scrapbook {
        min-height: 900px;
    }

    .polaroid {
        width: 125px;
        padding: 7px 7px 20px;
    }

    .polaroid img {
        height: 105px;
    }

    .photo-a {
        left: 1%;
    }

    .photo-b {
        right: 1%;
    }

    .photo-c {
        left: 2%;
        bottom: 80px;
    }

    .photo-d {
        right: 2%;
        bottom: 70px;
    }

    .note {
        font-size: .9rem;
        padding: 10px;
    }

    .note-one {
        left: 5%;
        top: 200px;
    }

    .note-two {
        right: 5%;
        top: 205px;
    }

    .note-three {
        left: 35%;
        bottom: 25px;
    }

    .scrap-center {
        margin-top: 190px;
        margin-bottom: 130px;
        padding: 30px 18px;
    }

    .memory-card {
        grid-template-columns: 1fr;
    }

}

</style>
""",
    unsafe_allow_html=True,
)


# ============================================================
# FLOATING HEART HTML
# IMPORTANT:
# THIS IS INSIDE st.markdown SO IT WILL NOT SHOW AS TEXT
# ============================================================

st.markdown(
    """
<div class="heart-layer">

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
# NAVIGATION
# ============================================================

def nav(unlocked=True, message="Finish the task above to unlock this 💭"):

    st.write("")

    if st.session_state.page == 0:

        st.button(
            "Open your birthday surprise →",
            on_click=next_page,
            key="start_button",
        )

    else:

        c1, c2 = st.columns(2)

        with c1:

            st.button(
                "← Back",
                on_click=prev_page,
                key=f"back_{st.session_state.page}",
            )

        with c2:

            if st.session_state.page < TOTAL - 1:

                if unlocked:

                    st.button(
                        "Continue →",
                        on_click=next_page,
                        key=f"next_{st.session_state.page}",
                    )

                else:

                    st.button(
                        "🔒 Continue →",
                        disabled=True,
                        key=f"locked_{st.session_state.page}",
                    )

        if not unlocked:

            st.markdown(
                f"""
                <div style="
                    text-align:center;
                    color:#f2699e;
                    font-size:.8rem;
                    margin-top:8px;
                ">
                    {message}
                </div>
                """,
                unsafe_allow_html=True,
            )


# ============================================================
# PAGE 0
# ============================================================

page = st.session_state.page


if page == 0:

    st.markdown(
        """
<div class="scrapbook">

    <div class="string one"></div>
    <div class="string two"></div>
    <div class="string three"></div>
    <div class="string four"></div>


    <!-- PHOTO A -->

    <div class="polaroid photo-a">

        <div class="tape"></div>

        <img src="data:image/jpeg;base64,PHOTO_A">

        <div class="polaroid-caption">
            my favourite 🥹
        </div>

    </div>


    <!-- PHOTO B -->

    <div class="polaroid photo-b">

        <div class="tape"></div>

        <img src="data:image/jpeg;base64,PHOTO_B">

        <div class="polaroid-caption">
            this view 💜
        </div>

    </div>


    <!-- PHOTO C -->

    <div class="polaroid photo-c">

        <div class="tape"></div>

        <img src="data:image/jpeg;base64,PHOTO_C">

        <div class="polaroid-caption">
            prettiest frame ✨
        </div>

    </div>


    <!-- PHOTO D -->

    <div class="polaroid photo-d">

        <div class="tape"></div>

        <img src="data:image/jpeg;base64,PHOTO_D">

        <div class="polaroid-caption">
            you. always. 💗
        </div>

    </div>


    <div class="note note-one">
        mai iske liye baised hu 💜
    </div>

    <div class="note note-two">
        I want this view always ✨
    </div>

    <div class="note note-three">
        prettiest frame 🥹
    </div>


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
""".replace(
            "PHOTO_A",
            image_base64(find_image("first_trip.jpeg"))
            if find_image("first_trip.jpeg")
            else "",
        )
        .replace(
            "PHOTO_B",
            image_base64(find_image("the_view.jpeg"))
            if find_image("the_view.jpeg")
            else "",
        )
        .replace(
            "PHOTO_C",
            image_base64(find_image("prettiest_frame.jpeg"))
            if find_image("prettiest_frame.jpeg")
            else "",
        )
        .replace(
            "PHOTO_D",
            image_base64(find_image("birthday_final.jpeg"))
            if find_image("birthday_final.jpeg")
            else "",
        ),
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="quote">
            "Celebrating you every day —
            but today is entirely yours."
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.caption(
        "Fair warning: you can't skip ahead. "
        "Every page has a tiny task waiting for you. 😌"
    )

    nav()


# ============================================================
# PAGE 1
# ============================================================

elif page == 1:

    st.markdown("## A small question, just for you")

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

    if st.button("This is definitely me 😌"):

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
        "Type your answer and tap the button above first 💭",
    )


# ============================================================
# PAGE 2
# ============================================================

elif page == 2:

    st.markdown("## How well do you know us? 🎲")

    st.caption(
        "A tiny, playful relationship quiz. No cheating — I'll know. 💗"
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
    )

    if st.button("Submit my very accurate answers"):

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
                    According to you: <b>{a["q1"]}</b>
                    wins the dance-off, and <b>{a["q2"]}</b>
                    sends the risky 1am text.
                    Noted and filed away. 📝
                </div>

                <div class="quote">
                    {verdict}
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    nav(
        "q4" in st.session_state.answers,
        "Submit your answers first, sneaky 👀",
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
            Some memories deserve more than just a place
            in the camera roll — they deserve a little home
            of their own.
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

        c1, c2 = st.columns(2)

        with c1:

            path = find_image(image)

            if path:

                st.markdown(
                    '<div class="memory-photo">',
                    unsafe_allow_html=True,
                )

                st.image(str(path), width="stretch")

                st.markdown(
                    '</div>',
                    unsafe_allow_html=True,
                )

        with c2:

            st.markdown(
                f"""
                <div class="memory-text">

                    <div class="memory-tag">
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
                unsafe_allow_html=True,
            )

        st.write("")

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

        "I hope you chase the big dreams, even the ones that feel far away. "
        "You deserve everything.",

        "I hope you never forget how capable you truly are. "
        "You are the softest guy that i dreamt of.",

        "And on the days you do forget — I'll be here to remind you. 💜",

    ]

    html = '<div class="points">'

    for i, text in enumerate(points, 1):

        html += f"""
        <div class="point">

            <div class="point-number">
                {i:02}
            </div>

            <div>
                {text}
            </div>

        </div>
        """

    html += "</div>"

    st.markdown(
        html,
        unsafe_allow_html=True,
    )

    nav()


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
            "I love you more than I could ever fit into a website — "
            "and believe me, I tried.",

        "🌙 A gentle tease":
            "You're officially one year older today ( Ab nahi hu tumse badi same same hogye ab ). "
            "Fortunately for you, I've decided to be kind about it. 😊",

        "🌱 A future one":
            "One day we'll look back on this version of us, "
            "and be so proud of everything we built together.",

    }

    for label, message in choices.items():

        if st.button(
            label,
            key=f"choice_{label}",
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
            unsafe_allow_html=True,
        )

    nav(
        "surprise" in st.session_state.answers,
        "Pick a surprise above to continue 🎁",
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
        <div style="text-align:center;">

            <div class="small">
                You have one important birthday duty left to perform.
            </div>

            <h1>
                Cut the Cake
            </h1>

        </div>
        """,
        unsafe_allow_html=True,
    )

    cut = st.session_state.answers.get(
        "cake",
        False,
    )

    if not cut:

        st.markdown(
            """
            <div class="cake">

                <div class="cake-body">

                    <div class="cake-bottom"></div>

                    <div class="cake-top"></div>

                    <div class="candle one"></div>
                    <div class="candle two"></div>
                    <div class="candle three"></div>

                    <div class="flame one">🔥</div>
                    <div class="flame two">🔥</div>
                    <div class="flame three">🔥</div>

                </div>

                <div class="quote">
                    Make a wish first 🎂
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

        st.caption(
            "Fun fact: virtual cake has zero calories. Cut freely. 🍰"
        )

        if st.button(
            "🔪 Cut the cake 🎂",
            key="cut_cake",
        ):

            st.session_state.answers["cake"] = True

            st.balloons()

            st.rerun()

    else:

        st.markdown(
            """
            <div class="cake">

                <div style="font-size:5rem;">
                    🎂🔪✨
                </div>

            </div>

            <div class="cut-message">

                <div style="font-size:3rem;">
                    🎂✨💜
                </div>

                <h1>
                    IT'S YOUR DAY!
                </h1>

                <p>
                    Cake successfully cut.
                </p>

                <div class="quote">
                    Make a wish —
                    I have a feeling I already know mine. 💜
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    nav(
        cut,
        "You must cut the cake first — no shortcuts 🎂",
    )


# ============================================================
# PAGE 7 — LETTER
# ============================================================

elif page == 7:

    st.markdown("## The Letter")

    st.markdown(
        """
        <div class="small">
            Everything else on this little site was just the build-up.
            This part, I mean with my whole heart.
        </div>
        """,
        unsafe_allow_html=True,
    )

    safe_letter = (
        FINAL_LETTER
        .strip()
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )

    st.markdown(
        f"""
        <div class="letter">

            <div class="letter-text">
                {safe_letter}
            </div>

            <div class="signoff">
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

    nav(
        felt,
        "Take a moment, then check the box above 💭",
    )


# ============================================================
# PAGE 8 — FINAL PHOTO
# ============================================================

elif page == 8:

    st.markdown(
        "## One last surprise"
    )

    st.caption(
        "You made it all the way here. 💜"
    )

    final_image = find_image(
        "birthday_final.jpeg"
    )

    if final_image:

        st.markdown(
            """
            <div style="
                background:white;
                padding:12px;
                border-radius:25px;
                box-shadow:
                    0 20px 60px rgba(91,44,111,.2);
            ">
            """,
            unsafe_allow_html=True,
        )

        st.image(
            str(final_image),
            width="stretch",
        )

        st.markdown(
            """
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div class="final-page">

            <div class="final-hearts">
                💜 💗 🎂 💗 💜
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
