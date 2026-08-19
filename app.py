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
# CSS
# ============================================================

st.markdown(
    """
<style>

@import url(
'https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,600&family=Dancing+Script:wght@500;600;700&family=Poppins:wght@300;400;500;600;700&display=swap'
);


/* ============================================================
   VARIABLES
   ============================================================ */

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


/* ============================================================
   GENERAL
   ============================================================ */

html,
body,
[class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {

    background:
        radial-gradient(
            circle at 8% 8%,
            rgba(255,159,196,.30),
            transparent 30%
        ),

        radial-gradient(
            circle at 92% 12%,
            rgba(185,142,224,.30),
            transparent 32%
        ),

        radial-gradient(
            circle at 12% 90%,
            rgba(230,209,245,.55),
            transparent 35%
        ),

        radial-gradient(
            circle at 90% 88%,
            rgba(255,209,227,.38),
            transparent 35%
        ),

        linear-gradient(
            160deg,
            #fdf6ff 0%,
            #f6ebfc 38%,
            #f1e3fb 68%,
            #fdf3f8 100%
        );

    color: var(--ink);

    min-height: 100vh;
}


.block-container {

    max-width: 900px;

    padding-top: 1.4rem;
    padding-bottom: 5rem;

    position: relative;
    z-index: 2;
}


div[data-testid="stVerticalBlock"] {
    gap: .6rem;
}


h1,
h2,
h3 {

    font-family:
        'Cormorant Garamond',
        serif !important;

    color:
        var(--purple-700) !important;
}


p,
div,
label,
span,
li {
    color: var(--ink);
}


/* ============================================================
   FLOATING BACKGROUND HEARTS
   ============================================================ */

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

    opacity: .55;

    animation:
        floatUp linear infinite;

    filter:
        drop-shadow(
            0 0 6px
            rgba(184,110,214,.25)
        );
}


@keyframes floatUp {

    0% {
        transform:
            translateY(0)
            translateX(0)
            rotate(0deg);

        opacity: 0;
    }

    10% {
        opacity: .6;
    }

    50% {
        transform:
            translateY(-55vh)
            translateX(20px)
            rotate(12deg);
    }

    90% {
        opacity: .35;
    }

    100% {
        transform:
            translateY(-105vh)
            translateX(-15px)
            rotate(-10deg);

        opacity: 0;
    }
}


/* ============================================================
   SCRAPBOOK FIRST PAGE
   ============================================================ */

.scrapbook {

    position: relative;

    min-height: 810px;

    padding:
        20px
        8px
        45px;

    overflow: hidden;
}


/* Clothesline */

.memory-string {

    position: absolute;

    left: 1%;
    right: 1%;

    top: 8%;

    height: 100px;

    border-top:
        3px solid
        rgba(124,63,168,.30);

    border-radius: 50%;

    transform:
        rotate(-1deg);

    z-index: 0;
}


/* Little pins */

.pin {

    position: absolute;

    width: 13px;

    height: 13px;

    border-radius: 50%;

    background:
        var(--pink-500);

    box-shadow:
        0 2px 5px
        rgba(0,0,0,.18);

    z-index: 10;
}


/* Scrapbook floating hearts */

.scrap-heart {

    position: absolute;

    font-size: 2rem;

    z-index: 3;

    animation:
        cuteFloat 3s
        ease-in-out
        infinite;
}


.sh1 {
    left: 2%;
    top: 4%;
}

.sh2 {
    right: 3%;
    top: 23%;
    animation-delay: .8s;
}

.sh3 {
    left: 7%;
    bottom: 17%;
    animation-delay: 1.4s;
}

.sh4 {
    right: 6%;
    bottom: 7%;
    animation-delay: .5s;
}

.sh5 {
    left: 46%;
    top: 4%;
    font-size: 1.4rem;
    animation-delay: 1.1s;
}


@keyframes cuteFloat {

    0%,
    100% {
        transform:
            translateY(0)
            rotate(-5deg);
    }

    50% {
        transform:
            translateY(-10px)
            rotate(6deg);
    }
}


/* ============================================================
   SCRAPBOOK PHOTOS
   ============================================================ */

.scrap-photo {

    position: absolute;

    width: 185px;

    background:
        white;

    padding:
        9px
        9px
        29px;

    border-radius: 5px;

    box-shadow:
        0 18px 38px
        rgba(94,43,131,.25);

    z-index: 5;

    transition:
        transform .3s ease,
        box-shadow .3s ease;
}


.scrap-photo:hover {

    transform:
        scale(1.08)
        rotate(0deg) !important;

    box-shadow:
        0 25px 50px
        rgba(94,43,131,.32);

    z-index: 30;
}


.scrap-photo img {

    width: 100%;

    height: 175px;

    object-fit: cover;

    display: block;

    border-radius: 3px;
}


/* Tape */

.tape {

    position: absolute;

    width: 68px;

    height: 21px;

    background:
        rgba(255,211,226,.85);

    top: -11px;

    left: 50%;

    transform:
        translateX(-50%)
        rotate(-4deg);

    box-shadow:
        0 2px 6px
        rgba(0,0,0,.10);

    z-index: 4;
}


/* Different photo positions */

.photo-a {

    left: 1%;

    top: 13%;

    transform:
        rotate(-8deg);
}


.photo-b {

    right: 1%;

    top: 15%;

    transform:
        rotate(8deg);
}


.photo-c {

    left: 5%;

    bottom: 11%;

    transform:
        rotate(7deg);
}


.photo-d {

    right: 5%;

    bottom: 9%;

    transform:
        rotate(-7deg);
}


/* Handwritten photo names */

.photo-label {

    position: absolute;

    bottom: 3px;

    left: 0;
    right: 0;

    text-align: center;

    font-family:
        'Dancing Script',
        cursive;

    font-size:
        1.15rem;

    color:
        var(--purple-600);
}


/* ============================================================
   CENTER OF SCRAPBOOK
   ============================================================ */

.scrap-center {

    position: relative;

    z-index: 15;

    width:
        min(
            570px,
            76%
        );

    margin:
        130px
        auto
        0;

    text-align: center;
}


.scrap-small {

    font-family:
        'Dancing Script',
        cursive;

    font-size:
        1.45rem;

    color:
        var(--pink-500);

    margin-bottom:
        7px;
}


.scrap-title {

    font-family:
        'Cormorant Garamond',
        serif !important;

    font-size:
        clamp(
            3.4rem,
            9vw,
            6rem
        ) !important;

    font-weight:
        700;

    line-height:
        .88;

    margin:
        0;

    background:
        linear-gradient(
            110deg,
            var(--purple-700),
            var(--pink-500),
            var(--purple-500)
        );

    -webkit-background-clip:
        text;

    background-clip:
        text;

    -webkit-text-fill-color:
        transparent;
}


.scrap-subtitle {

    font-family:
        'Dancing Script',
        cursive;

    font-size:
        clamp(
            1.5rem,
            4vw,
            2.2rem
        );

    color:
        var(--purple-600);

    margin-top:
        16px;
}


/* ============================================================
   PAPER NOTE
   ============================================================ */

.scrap-note {

    margin:
        30px
        auto;

    max-width:
        465px;

    padding:
        23px
        28px;

    background:
        #fffdf7;

    transform:
        rotate(-1.3deg);

    box-shadow:
        0 12px 28px
        rgba(94,43,131,.14);

    border-radius:
        4px;

    font-family:
        'Dancing Script',
        cursive;

    font-size:
        1.38rem;

    line-height:
        1.55;

    color:
        var(--ink);

    position:
        relative;
}


.scrap-note:before {

    content:
        "";

    position:
        absolute;

    width:
        78px;

    height:
        22px;

    background:
        rgba(255,211,226,.75);

    top:
        -11px;

    left:
        50%;

    transform:
        translateX(-50%)
        rotate(-2deg);
}


/* Sticker */

.love-sticker {

    position:
        absolute;

    bottom:
        1%;

    left:
        50%;

    transform:
        translateX(-50%)
        rotate(-3deg);

    background:
        var(--pink-300);

    padding:
        12px 24px;

    border-radius:
        50%;

    font-family:
        'Dancing Script',
        cursive;

    font-size:
        1.3rem;

    color:
        var(--purple-700);

    box-shadow:
        0 8px 20px
        rgba(242,105,158,.18);

    z-index:
        20;
}


/* ============================================================
   OTHER PAGE STYLES
   ============================================================ */

.divider-heart {

    text-align:
        center;

    font-size:
        1.1rem;

    margin:
        1.1rem 0;

    color:
        var(--pink-500);

    letter-spacing:
        10px;
}


.card {

    background:
        rgba(255,255,255,.72);

    backdrop-filter:
        blur(6px);

    border:
        1px solid
        rgba(185,142,224,.35);

    border-radius:
        24px;

    padding:
        1.5rem 1.6rem;

    margin:
        1rem 0;

    box-shadow:
        0 14px 40px
        rgba(124,63,168,.12);
}


.card b {
    color:
        var(--purple-600);
}


.quote {

    font-family:
        'Dancing Script',
        cursive;

    font-weight:
        700;

    font-size:
        2rem;

    line-height:
        1.4;

    color:
        var(--purple-700);

    text-align:
        center;

    padding:
        1.2rem .5rem;
}


.small {

    color:
        var(--ink-soft);

    font-size:
        .92rem;

    line-height:
        1.75;
}


/* ============================================================
   QUIZ
   ============================================================ */

.quiz-q {

    font-family:
        'Cormorant Garamond',
        serif;

    font-weight:
        700;

    font-size:
        clamp(
            1.3rem,
            4vw,
            1.6rem
        );

    color:
        var(--purple-700);

    margin:
        .7rem 0 .25rem;

    line-height:
        1.25;
}


div[data-testid="stRadio"] {
    margin-bottom:
        -.3rem;
}


div[data-testid="stRadio"] > div {

    background:
        rgba(255,255,255,.55);

    padding:
        .45rem .7rem;

    border-radius:
        16px;

    border:
        1px solid
        rgba(185,142,224,.3);
}


div[data-testid="stRadio"] label,
div[data-testid="stRadio"] p {

    color:
        var(--ink) !important;

    font-weight:
        500;

    font-size:
        1rem;
}


/* ============================================================
   MEMORY PAGES
   ============================================================ */

.photo-frame {

    background:
        white;

    border-radius:
        26px;

    padding:
        12px;

    box-shadow:
        0 18px 45px
        rgba(124,63,168,.18);

    border:
        1px solid
        rgba(255,255,255,.9);

    position:
        relative;
}


[data-testid="stImage"] img {
    border-radius:
        18px;
}


.mem-text-wrap {

    height:
        100%;

    display:
        flex;

    align-items:
        center;

    margin-top:
        .8rem;
}


.mem-text-card {

    background:
        rgba(255,255,255,.72);

    backdrop-filter:
        blur(6px);

    border:
        1px solid
        rgba(185,142,224,.35);

    border-radius:
        22px;

    padding:
        1.3rem 1.4rem;

    box-shadow:
        0 14px 36px
        rgba(124,63,168,.12);

    text-align:
        left;

    width:
        100%;
}


.mem-text-card .mem-tag {

    color:
        var(--pink-500);

    text-transform:
        uppercase;

    letter-spacing:
        2px;

    font-size:
        .68rem;

    font-weight:
        600;
}


.mem-text-card h3 {

    margin:
        .25rem 0 .4rem;

    font-size:
        clamp(
            1.2rem,
            4vw,
            1.45rem
        );
}


.mem-text-card p {

    color:
        var(--ink-soft);

    margin:
        0;

    font-size:
        .95rem;

    line-height:
        1.65;
}


.missing-photo {

    text-align:
        center;

    padding:
        2.5rem 1rem;

    color:
        var(--purple-500);

    background:
        rgba(255,255,255,.6);

    border:
        1px dashed
        var(--purple-400);

    border-radius:
        20px;

    font-size:
        .9rem;
}


.memory-row {
    margin-bottom:
        1.8rem;
}


/* ============================================================
   THINGS TO REMEMBER
   ============================================================ */

.points-grid {

    display:
        grid;

    grid-template-columns:
        repeat(
            auto-fit,
            minmax(
                260px,
                1fr
            )
        );

    gap:
        .7rem;

    margin:
        .6rem 0 .4rem;
}


.point-card {

    background:
        rgba(255,255,255,.72);

    backdrop-filter:
        blur(6px);

    border:
        1px solid
        rgba(185,142,224,.35);

    border-radius:
        18px;

    padding:
        1rem 1.1rem;

    box-shadow:
        0 10px 28px
        rgba(124,63,168,.1);

    display:
        flex;

    gap:
        .6rem;

    align-items:
        flex-start;
}


.point-card .point-num {

    font-family:
        'Cormorant Garamond',
        serif;

    font-weight:
        700;

    font-size:
        1.5rem;

    color:
        var(--pink-500);

    line-height:
        1;

    flex-shrink:
        0;
}


.point-card .point-text {

    font-size:
        1.08rem;

    line-height:
        1.5;

    color:
        var(--ink);

    font-weight:
        500;
}


/* ============================================================
   LOVE LETTER
   ============================================================ */

.letter-card {

    background:
        linear-gradient(
            180deg,
            rgba(255,255,255,.92),
            rgba(250,240,255,.85)
        );

    border:
        1px solid
        rgba(185,142,224,.4);

    border-radius:
        26px;

    padding:
        2rem 1.8rem;

    box-shadow:
        0 20px 55px
        rgba(124,63,168,.16);

    position:
        relative;
}


.letter-card::before {

    content:
        "💌";

    position:
        absolute;

    top:
        -18px;

    left:
        50%;

    transform:
        translateX(-50%);

    font-size:
        2rem;

    background:
        var(--lavender-100);

    padding:
        4px 12px;

    border-radius:
        50%;
}


.letter-text {

    font-family:
        'Cormorant Garamond',
        serif;

    font-style:
        italic;

    font-size:
        1.28rem;

    line-height:
        2;

    color:
        var(--ink);

    white-space:
        pre-line;

    text-align:
        left;

    padding-top:
        .8rem;
}


.letter-signoff {

    text-align:
        right;

    font-family:
        'Dancing Script',
        cursive;

    font-size:
        1.6rem;

    color:
        var(--purple-600);

    margin-top:
        .5rem;
}


/* ============================================================
   CAKE — CSS ONLY
   No SVG = no SVG animation errors
   ============================================================ */

.cake-stage {

    position:
        relative;

    min-height:
        350px;

    display:
        flex;

    flex-direction:
        column;

    justify-content:
        center;

    align-items:
        center;

    margin:
        10px auto 20px;

    overflow:
        visible;
}


.cake {

    width:
        340px;

    height:
        315px;

    position:
        relative;

    margin:
        auto;
}


/* Cake plate */

.cake::after {

    content:
        "";

    position:
        absolute;

    width:
        285px;

    height:
        30px;

    left:
        28px;

    bottom:
        15px;

    background:
        #f1e3fb;

    border-radius:
        50%;

    box-shadow:
        0 10px 15px
        rgba(94,43,131,.15);
}


/* Main cake */

.cake-body {

    position:
        absolute;

    width:
        230px;

    height:
        125px;

    left:
        55px;

    top:
        125px;

    background:
        linear-gradient(
            to bottom,
            #c98fe6,
            #a56bd1
        );

    border-radius:
        18px 18px 28px 28px;

    box-shadow:
        0 18px 30px
        rgba(94,43,131,.22);

    overflow:
        hidden;

    z-index:
        3;
}


/* Frosting */

.frosting {

    position:
        absolute;

    left:
        -5px;

    right:
        -5px;

    top:
        -5px;

    height:
        40px;

    background:
        #ffd8e8;

    border-radius:
        20px 20px 50% 50%;

    z-index:
        4;
}


.frosting::after {

    content:
        "♡  ♡  ♡  ♡  ♡";

    position:
        absolute;

    width:
        100%;

    text-align:
        center;

    top:
        8px;

    color:
        #b35bc9;

    font-size:
        16px;
}


/* Cake cream layers */

.cake-layer {

    position:
        absolute;

    left:
        15px;

    right:
        15px;

    height:
        20px;

    border-radius:
        50%;

    z-index:
        2;
}


.cake-layer.cream {

    background:
        #fff6ee;

    top:
        48px;
}


.cake-layer.pink {

    background:
        #f7c9da;

    top:
        72px;
}


.cake-layer.cream:last-child {

    top:
        96px;
}


/* ============================================================
   CANDLES
   ============================================================ */

.candles {

    position:
        absolute;

    top:
        55px;

    left:
        80px;

    width:
        180px;

    display:
        flex;

    justify-content:
        space-between;

    z-index:
        8;
}


.candle {

    width:
        10px;

    height:
        65px;

    border-radius:
        5px;

    background:
        linear-gradient(
            to right,
            #7c3fa8,
            #c88de7
        );

    position:
        relative;

    box-shadow:
        0 4px 8px
        rgba(94,43,131,.2);
}


.candle span {

    position:
        absolute;

    top:
        -32px;

    left:
        50%;

    transform:
        translateX(-50%);

    font-size:
        20px;

    animation:
        flame 1s
        ease-in-out
        infinite;
}


.candle:nth-child(2) span {
    animation-delay:
        .2s;
}

.candle:nth-child(3) span {
    animation-delay:
        .4s;
}

.candle:nth-child(4) span {
    animation-delay:
        .1s;
}

.candle:nth-child(5) span {
    animation-delay:
        .3s;
}


@keyframes flame {

    0%,
    100% {

        transform:
            translateX(-50%)
            scale(1);

    }

    50% {

        transform:
            translateX(-50%)
            scale(1.2);

    }
}


/* ============================================================
   CAKE DECORATIONS
   ============================================================ */

.cake-decor {

    position:
        absolute;

    bottom:
        48px;

    width:
        100%;

    text-align:
        center;

    font-size:
        20px;

    z-index:
        10;
}


/* ============================================================
   KNIFE
   ============================================================ */

.knife {

    position:
        absolute;

    top:
        10px;

    right:
        -15px;

    font-size:
        65px;

    transform:
        rotate(-35deg);

    transform-origin:
        bottom left;

    animation:
        knifeWaiting
        2s
        ease-in-out
        infinite;

    z-index:
        15;
}


@keyframes knifeWaiting {

    0%,
    100% {

        transform:
            rotate(-35deg)
            translateY(0);

    }

    50% {

        transform:
            rotate(-42deg)
            translateY(8px);

    }
}


/* ============================================================
   CUTTING ANIMATION
   ============================================================ */

.cut .knife {

    animation:
        cutCake
        1.1s
        ease-in-out
        forwards;
}


@keyframes cutCake {

    0% {

        transform:
            rotate(-35deg)
            translateY(-10px);

    }

    35% {

        transform:
            rotate(-35deg)
            translateY(105px);

    }

    55% {

        transform:
            rotate(-25deg)
            translateY(110px);

    }

    100% {

        transform:
            rotate(-35deg)
            translateY(-10px);

    }
}


/* Slice */

.slice-left {

    position:
        absolute;

    width:
        95px;

    height:
        105px;

    left:
        25px;

    top:
        135px;

    background:
        linear-gradient(
            to bottom,
            #c98fe6,
            #a56bd1
        );

    border-radius:
        15px;

    opacity:
        0;

    z-index:
        12;
}


.cut .slice-left {

    animation:
        sliceMove
        1.2s
        ease
        forwards;
}


@keyframes sliceMove {

    0% {

        opacity:
            1;

        transform:
            translate(0,0)
            rotate(0deg);

    }

    60% {

        opacity:
            1;

    }

    100% {

        opacity:
            0;

        transform:
            translate(-105px,55px)
            rotate(-22deg);

    }
}


/* Cake success message */

.cake-message {

    font-family:
        'Dancing Script',
        cursive;

    font-size:
        2.2rem;

    color:
        var(--purple-600);

    margin-top:
        -5px;

    animation:
        messagePop
        .7s
        ease
        forwards;
}


@keyframes messagePop {

    from {

        opacity:
            0;

        transform:
            scale(.7);

    }

    to {

        opacity:
            1;

        transform:
            scale(1);

    }
}


/* ============================================================
   FINAL PAGE
   ============================================================ */

.final {

    text-align:
        center;

    padding:
        1.8rem 1rem 1rem;
}


.final h1 {

    font-size:
        clamp(
            3rem,
            10vw,
            6rem
        );

    margin:
        .5rem 0;

    background:
        linear-gradient(
            100deg,
            var(--purple-600),
            var(--pink-500) 55%,
            var(--purple-500)
        );

    -webkit-background-clip:
        text;

    background-clip:
        text;

    -webkit-text-fill-color:
        transparent;
}


.final p {

    color:
        var(--ink-soft);

    line-height:
        1.85;

    font-size:
        1.02rem;
}


/* ============================================================
   PROGRESS
   ============================================================ */

.progress-text {

    text-align:
        center;

    color:
        var(--ink-soft);

    font-size:
        .74rem;

    letter-spacing:
        1.5px;

    margin-bottom:
        .5rem;

    font-weight:
        600;
}


div[data-testid="stProgress"] > div > div {

    background:
        linear-gradient(
            90deg,
            var(--pink-400),
            var(--purple-500)
        ) !important;
}


div[data-testid="stProgress"] > div {

    background-color:
        var(--lavender-300) !important;
}


/* ============================================================
   BUTTONS
   ============================================================ */

div.stButton > button {

    width:
        100%;

    border-radius:
        999px;

    border:
        1px solid
        rgba(255,255,255,.5);

    background:
        linear-gradient(
            90deg,
            var(--pink-500),
            var(--purple-600)
        );

    color:
        var(--white);

    font-weight:
        600;

    min-height:
        3rem;

    box-shadow:
        0 10px 28px
        rgba(155,92,199,.3);

    transition:
        all .15s ease;
}


div.stButton > button p {

    color:
        var(--white) !important;
}


div.stButton > button:hover {

    filter:
        brightness(1.06);

    transform:
        translateY(-2px);

    box-shadow:
        0 14px 34px
        rgba(155,92,199,.4);
}


div.stButton > button:disabled {

    background:
        linear-gradient(
            90deg,
            #dcc8ea,
            #cbb3e0
        ) !important;

    box-shadow:
        none;

    opacity:
        .8;
}


div.stButton > button:disabled p {

    color:
        rgba(255,255,255,.85) !important;
}


/* ============================================================
   INPUTS
   ============================================================ */

div[data-testid="stTextInput"] input {

    border-radius:
        14px !important;

    border:
        1px solid
        var(--purple-400) !important;

    background:
        rgba(255,255,255,.85) !important;

    color:
        var(--ink) !important;
}


div[data-testid="stCheckbox"] label p {

    color:
        var(--ink) !important;

    font-weight:
        500;
}


div[data-testid="stCaptionContainer"] {

    color:
        var(--ink-soft) !important;

    text-align:
        center;
}


/* ============================================================
   LOCK HINT
   ============================================================ */

.lock-hint {

    text-align:
        center;

    color:
        var(--pink-500);

    font-size:
        .82rem;

    font-weight:
        500;

    margin-top:
        .6rem;

    animation:
        pulseHint
        1.8s
        ease-in-out
        infinite;
}


@keyframes pulseHint {

    0%,
    100% {
        opacity:
            .65;
    }

    50% {
        opacity:
            1;
    }
}


/* ============================================================
   FLIP CARD
   ============================================================ */

.flip-card {

    perspective:
        1200px;

    width:
        100%;

    max-width:
        420px;

    margin:
        1rem auto 1.5rem;
}


.flip-toggle-input {
    display:
        none;
}


.flip-card-inner {

    position:
        relative;

    display:
        block;

    width:
        100%;

    padding-top:
        125%;

    cursor:
        pointer;

    transform-style:
        preserve-3d;

    transition:
        transform .9s
        cubic-bezier(.4,.2,.2,1);
}


.flip-toggle-input:checked
+ .flip-card-inner {

    transform:
        rotateY(180deg);
}


.flip-card-face {

    position:
        absolute;

    inset:
        0;

    backface-visibility:
        hidden;

    border-radius:
        26px;

    box-shadow:
        0 18px 45px
        rgba(124,63,168,.2);

    overflow:
        hidden;
}


.flip-card-front {

    background:
        var(--white);
}


.flip-card-front img {

    width:
        100%;

    height:
        100%;

    object-fit:
        cover;

    display:
        block;
}


.flip-hint {

    position:
        absolute;

    bottom:
        0;

    left:
        0;

    right:
        0;

    text-align:
        center;

    color:
        var(--white);

    background:
        rgba(94,43,131,.6);

    padding:
        .6rem;

    font-size:
        .82rem;

    font-weight:
        600;
}


.flip-card-back {

    transform:
        rotateY(180deg);

    background:
        linear-gradient(
            160deg,
            rgba(255,255,255,.96),
            rgba(246,235,252,.94)
        );

    padding:
        1.7rem 1.4rem;

    display:
        flex;

    flex-direction:
        column;

    justify-content:
        center;

    align-items:
        center;

    text-align:
        center;
}


.flip-card-back .eyebrow {

    color:
        var(--pink-500);

    text-transform:
        uppercase;

    letter-spacing:
        3px;

    font-size:
        .72rem;
}


.flip-card-back h1 {

    font-size:
        clamp(
            2rem,
            8vw,
            3rem
        );

    margin:
        .3rem 0;

    background:
        linear-gradient(
            100deg,
            var(--purple-600),
            var(--pink-500) 55%,
            var(--purple-500)
        );

    -webkit-background-clip:
        text;

    background-clip:
        text;

    -webkit-text-fill-color:
        transparent;
}


.flip-card-back p {

    font-size:
        .92rem;

    line-height:
        1.75;

    color:
        var(--ink-soft);

    margin:
        0;
}


.flip-card-back .quote {

    font-size:
        1.35rem;

    padding:
        .6rem 0;
}


/* ============================================================
   FOOTER
   ============================================================ */

.footer {

    text-align:
        center;

    color:
        var(--purple-500);

    font-size:
        .75rem;

    padding-top:
        2.2rem;

    letter-spacing:
        .5px;
}


/* ============================================================
   MOBILE
   ============================================================ */

@media (max-width: 700px) {

    .scrapbook {
        min-height:
            850px;
    }

    .scrap-photo {

        width:
            125px;

        padding:
            6px 6px 21px;
    }

    .scrap-photo img {

        height:
            120px;
    }

    .photo-a {

        left:
            0;

        top:
            5%;
    }

    .photo-b {

        right:
            0;

        top:
            8%;
    }

    .photo-c {

        left:
            0;

        bottom:
            9%;
    }

    .photo-d {

        right:
            0;

        bottom:
            8%;
    }

    .scrap-center {

        width:
            84%;

        margin-top:
            150px;
    }

    .scrap-title {

        font-size:
            clamp(
                3rem,
                15vw,
                5rem
            ) !important;
    }

    .scrap-note {

        font-size:
            1.15rem;

        padding:
            18px;
    }

    .cake {

        transform:
            scale(.86);

        transform-origin:
            center top;
    }

    .cake-stage {

        min-height:
            315px;
    }
}


@media (max-width: 480px) {

    .block-container {

        padding-left:
            .9rem;

        padding-right:
            .9rem;
    }

    .card {

        padding:
            1.1rem
            1.15rem;
    }

    .letter-card {

        padding:
            1.6rem
            1.2rem;
    }

    .letter-text {

        font-size:
            1.05rem;

        line-height:
            1.85;
    }

    .point-card {

        padding:
            .85rem
            .9rem;
    }

    .point-card .point-text {

        font-size:
            1rem;
    }
}

</style>


<!-- ============================================================
     FLOATING BACKGROUND
     ============================================================ -->

<div class="hearts-bg">

    <span
        class="heart-float"
        style="
            left:6%;
            font-size:1.4rem;
            animation-duration:13s;
            animation-delay:0s;
        "
    >💗</span>

    <span
        class="heart-float"
        style="
            left:18%;
            font-size:1.1rem;
            animation-duration:16s;
            animation-delay:2s;
        "
    >💜</span>

    <span
        class="heart-float"
        style="
            left:30%;
            font-size:1.7rem;
            animation-duration:11s;
            animation-delay:4s;
        "
    >💕</span>

    <span
        class="heart-float"
        style="
            left:44%;
            font-size:1.2rem;
            animation-duration:14s;
            animation-delay:1s;
        "
    >💜</span>

    <span
        class="heart-float"
        style="
            left:58%;
            font-size:1.5rem;
            animation-duration:12s;
            animation-delay:5s;
        "
    >💗</span>

    <span
        class="heart-float"
        style="
            left:70%;
            font-size:1.1rem;
            animation-duration:17s;
            animation-delay:3s;
        "
    >💜</span>

    <span
        class="heart-float"
        style="
            left:82%;
            font-size:1.6rem;
            animation-duration:13s;
            animation-delay:6s;
        "
    >💕</span>

    <span
        class="heart-float"
        style="
            left:92%;
            font-size:1.2rem;
            animation-duration:15s;
            animation-delay:2.5s;
        "
    >💜</span>

    <span
        class="heart-float"
        style="
            left:50%;
            font-size:1.3rem;
            animation-duration:18s;
            animation-delay:7s;
        "
    >💗</span>

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
                        key=f"next_locked_{st.session_state.page}",
                    )

        if (
            not unlocked
            and
            st.session_state.page < TOTAL - 1
        ):

            st.markdown(
                f"""
                <div class="lock-hint">
                    {lock_msg}
                </div>
                """,
                unsafe_allow_html=True,
            )

    else:

        st.button(
            "Open your birthday surprise →",
            on_click=next_page,
            key="start",
        )


# ============================================================
# IMAGE HELPERS
# ============================================================

def img_to_base64(path):

    with open(path, "rb") as f:

        return base64.b64encode(
            f.read()
        ).decode()


def photo(name):

    path = ASSETS / name

    st.markdown(
        '<div class="photo-frame">',
        unsafe_allow_html=True,
    )

    if path.exists():

        try:

            st.image(
                str(path),
                use_container_width=True,
            )

        except TypeError:

            st.image(str(path))

    else:

        st.markdown(
            f"""
            <div class="missing-photo">
                💜 Photo "{name}" not found
                in the assets folder 💜
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        '</div>',
        unsafe_allow_html=True,
    )


def memory_row(
    name,
    tag,
    title,
    text,
):

    st.markdown(
        '<div class="memory-row">',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(
        [1, 1]
    )

    with col1:

        photo(name)

    with col2:

        st.markdown(
            f"""
            <div class="mem-text-wrap">

                <div class="mem-text-card">

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
        '</div>',
        unsafe_allow_html=True,
    )


# ============================================================
# CSS CAKE
# ============================================================

def cake_html(cutting=False):

    if not cutting:

        return """
        <div class="cake-stage">

            <div class="cake">

                <div class="cake-body">

                    <div class="frosting"></div>

                    <div class="cake-layer cream"></div>

                    <div class="cake-layer pink"></div>

                    <div class="cake-layer cream"></div>

                </div>


                <div class="candles">

                    <div class="candle">
                        <span>🔥</span>
                    </div>

                    <div class="candle">
                        <span>🔥</span>
                    </div>

                    <div class="candle">
                        <span>🔥</span>
                    </div>

                    <div class="candle">
                        <span>🔥</span>
                    </div>

                    <div class="candle">
                        <span>🔥</span>
                    </div>

                </div>


                <div class="knife">
                    🔪
                </div>


                <div class="cake-decor">
                    💜 💗 💜
                </div>

            </div>

        </div>
        """

    return """
    <div class="cake-stage cut">

        <div class="cake">

            <div class="cake-body">

                <div class="frosting"></div>

                <div class="cake-layer cream"></div>

                <div class="cake-layer pink"></div>

                <div class="cake-layer cream"></div>

            </div>


            <div class="slice-left">

                <div class="frosting"></div>

            </div>


            <div class="candles">

                <div class="candle">
                    <span>🔥</span>
                </div>

                <div class="candle">
                    <span>🔥</span>
                </div>

                <div class="candle">
                    <span>🔥</span>
                </div>

                <div class="candle">
                    <span>🔥</span>
                </div>

                <div class="candle">
                    <span>🔥</span>
                </div>

            </div>


            <div class="knife">
                🔪
            </div>


            <div class="cake-decor">
                💜 💗 💜
            </div>

        </div>


        <div class="cake-message">
            🎂✨ YOU DID IT ✨🎂
        </div>

    </div>
    """


# ============================================================
# CURRENT PAGE
# ============================================================

page = st.session_state.page


if page > 0:

    st.markdown(
        f"""
        <div class="progress-text">
            YOUR BIRTHDAY JOURNEY ·
            {page}/{TOTAL - 1}
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.progress(
        page / (TOTAL - 1)
    )


# ============================================================
# PAGE 0 — CRAZY CUTE SCRAPBOOK
# ============================================================

if page == 0:

    def scrapbook_photo(
        filename,
        position,
        label,
        rotation,
    ):

        path = ASSETS / filename

        if not path.exists():
            return ""

        b64 = img_to_base64(path)

        return f"""
        <div
            class="scrap-photo {position}"
            style="transform:rotate({rotation});"
        >

            <div class="tape"></div>

            <img
                src="data:image/jpeg;base64,{b64}"
            >

            <div class="photo-label">
                {label}
            </div>

        </div>
        """


    # ========================================================
    # YOUR EXISTING PHOTOS
    # ========================================================

    photo_data = [

        (
            "first_trip.jpeg",
            "photo-a",
            "my favourite one",
            "-8deg",
        ),

        (
            "the_view.jpeg",
            "photo-b",
            "this view ♡",
            "8deg",
        ),

        (
            "prettiest_frame.jpeg",
            "photo-c",
            "prettiest frame",
            "7deg",
        ),

        (
            "birthday_final.jpeg",
            "photo-d",
            "birthday boy ♡",
            "-7deg",
        ),

    ]


    photos_html = ""

    for (
        filename,
        position,
        label,
        rotation,
    ) in photo_data:

        photos_html += scrapbook_photo(
            filename,
            position,
            label,
            rotation,
        )


    st.markdown(
        f"""
        <div class="scrapbook">


            <!-- STRING -->

            <div class="memory-string"></div>


            <!-- HEARTS -->

            <div class="scrap-heart sh1">
                💗
            </div>

            <div class="scrap-heart sh2">
                💜
            </div>

            <div class="scrap-heart sh3">
                💕
            </div>

            <div class="scrap-heart sh4">
                💗
            </div>

            <div class="scrap-heart sh5">
                ✨
            </div>


            <!-- PICTURES -->

            {photos_html}


            <!-- CENTER -->

            <div class="scrap-center">

                <div class="scrap-small">
                    ✨ a tiny corner of the internet ✨
                </div>


                <h1 class="scrap-title">

                    HAPPY<br>
                    BIRTHDAY<br>
                    BUNNY

                </h1>


                <div class="scrap-subtitle">

                    20th August ♡

                </div>


                <div class="scrap-note">

                    Before you go any further, I just want
                    you to know —

                    <br><br>

                    a great deal of love went into building
                    this, one page at a time. 🥹

                    <br><br>

                    This tiny little world is just for you. 💜

                </div>


                <div
                    style="
                        font-size:2rem;
                        letter-spacing:10px;
                        margin-top:15px;
                    "
                >
                    💜 💗 💜
                </div>

            </div>


            <div class="love-sticker">

                made with an unreasonable
                amount of love ♡

            </div>


        </div>
        """,
        unsafe_allow_html=True,
    )


    st.markdown(
        '<div class="divider-heart">💜 · 💗 · 💜</div>',
        unsafe_allow_html=True,
    )


    st.caption(
        "Fair warning: you can't skip ahead. "
        "Every page has a tiny task waiting for you. 😌"
    )


    nav()


# ============================================================
# PAGE 1 — NAME
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
        "This is definitely me 😌"
    ):

        if name.strip():

            with st.spinner(
                "🔍 Verifying that you are, "
                "in fact, my favourite person..."
            ):

                time.sleep(1.1)


            st.session_state.answers[
                "name"
            ] = name.strip()


            st.success(
                "Identity confirmed. "
                "And lucky for you, you're stuck with me. 💜"
            )

        else:

            st.warning(
                "You have to type something first — "
                "I'm waiting. 😊"
            )


    unlocked = (
        "name"
        in st.session_state.answers
    )


    nav(
        unlocked,
        "Type your answer and tap the button above first 💭",
    )


# ============================================================
# PAGE 2 — QUIZ
# ============================================================

elif page == 2:

    st.markdown(
        "## How well do you know us? 🎲"
    )

    st.caption(
        "A tiny, playful relationship quiz. "
        "No cheating — I'll know. 💗"
    )


    st.markdown(
        """
        <div class="quiz-q">
            1. In a dance-off with zero practice,
            who takes the win?
        </div>
        """,
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
        """
        <div class="quiz-q">
            2. Who's more likely to text
            "you up?" at 1am?
        </div>
        """,
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
        """
        <div class="quiz-q">
            3. Stranded on a desert island,
            who packs snacks and who packs
            snacks... for the vibes?
        </div>
        """,
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
        """
        <div class="quiz-q">
            4. Real talk — who loves the other
            person a little more?
        </div>
        """,
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


    if st.button(
        "Submit my very accurate answers"
    ):

        if None in (
            q1,
            q2,
            q3,
            q4,
        ):

            st.warning(
                "Pick an answer for every question "
                "first — no skipping 👀"
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
                "Aww, close call — "
                "but I still say it's me. 💜"
            )

        elif a["q4"].startswith("Me"):

            verdict = (
                "See? I've been telling you "
                "this the whole time. 💜"
            )

        else:

            verdict = (
                "The most diplomatic answer "
                "in relationship history. Respect. 🫡"
            )


        st.markdown(
            f"""
            <div class="card">

                <div class="small">

                    According to you:
                    <b>{a['q1']}</b>
                    wins the dance-off, and
                    <b>{a['q2']}</b>
                    sends the risky 1am text.
                    Noted and filed away. 📝

                </div>

                <div
                    class="quote"
                    style="font-size:1.3rem;"
                >
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


    nav(
        unlocked,
        "Submit your answers first, sneaky 👀",
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

            Some memories deserve more than just a
            place in the camera roll — they deserve
            a little home of their own.

        </div>
        """,
        unsafe_allow_html=True,
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
# PAGE 4 — THINGS TO REMEMBER
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


    cards_html = (
        '<div class="points-grid">'
    )


    for i, text in enumerate(
        points,
        1,
    ):

        cards_html += f"""

        <div class="point-card">

            <div class="point-num">
                {i:02}
            </div>

            <div class="point-text">
                {text}
            </div>

        </div>

        """


    cards_html += (
        "</div>"
    )


    st.markdown(
        cards_html,
        unsafe_allow_html=True,
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
        "You may open only one. "
        "Choose with your heart, not your curiosity. 💗"
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

        message = choices[
            st.session_state.answers[
                "surprise"
            ]
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


    unlocked = (
        "surprise"
        in st.session_state.answers
    )


    nav(
        unlocked,
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
        <div
            style="
                text-align:center;
                padding:10px 0;
            "
        >

            <div class="subtitle">

                You have one important birthday
                duty left to perform.

            </div>

            <h1
                style="
                    font-family:'Cormorant Garamond',serif;
                    text-align:center;

                    background:
                        linear-gradient(
                            100deg,
                            var(--purple-600),
                            var(--pink-500) 55%,
                            var(--purple-500)
                        );

                    -webkit-background-clip:text;
                    background-clip:text;

                    -webkit-text-fill-color:transparent;

                    font-size:
                        clamp(
                            2.8rem,
                            8vw,
                            4.5rem
                        );

                    margin:
                        .5rem 0;
                "
            >
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


    st.markdown(
        cake_html(cutting=cut),
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

            st.rerun()


    else:

        st.balloons()


        st.markdown(
            """
            <div class="final">

                <div style="font-size:4.5rem;">
                    🎂✨💜
                </div>

                <h1>
                    IT'S YOUR DAY!
                </h1>

                <p>
                    Make a wish — I have a feeling
                    I already know mine. 💜
                </p>

            </div>
            """,
            unsafe_allow_html=True,
        )


    unlocked = cut


    nav(
        unlocked,
        "You must cut the cake first — no shortcuts 🎂",
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

            Everything else on this little site was just
            the build-up. This part, I mean with my whole heart.

        </div>
        """,
        unsafe_allow_html=True,
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
# PAGE 8 — FINAL SURPRISE
# ============================================================

elif page == 8:

    st.markdown(
        "## One last surprise"
    )


    st.caption(
        "Tap the card below to open it. 💜"
    )


    img_path = (
        ASSETS /
        "birthday_final.jpeg"
    )


    if img_path.exists():

        b64 = img_to_base64(
            img_path
        )

        front_html = f"""
        <img
            src="data:image/jpeg;base64,{b64}"
            alt="Birthday photo"
        />
        """

    else:

        front_html = """
        <div class="missing-photo">

            💜 Photo
            "birthday_final.jpeg"
            not found in the assets folder 💜

        </div>
        """


    st.markdown(
        f"""
        <div class="flip-card">

            <input
                type="checkbox"
                id="flipToggle"
                class="flip-toggle-input"
            >


            <label
                for="flipToggle"
                class="flip-card-inner"
            >


                <div
                    class="flip-card-face
                           flip-card-front"
                >

                    {front_html}

                    <div class="flip-hint">

                        Tap to open your last surprise 💜

                    </div>

                </div>


                <div
                    class="flip-card-face
                           flip-card-back"
                >

                    <div class="eyebrow">

                        The final page

                    </div>


                    <h1>

                        HAPPY<br>
                        BIWRTHDAY AGAIN JI

                    </h1>


                    <p>

                        Saksham —<br>

                        I love celebrating you <br>

                        Biggest biwrthday hugs and kisses
                        to you.

                    </p>


                    <div class="quote">

                        "And yes... I would choose you again."

                    </div>


                    <div style="font-size:2rem;">

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
