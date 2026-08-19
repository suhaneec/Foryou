
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="For My Birthday Boy ❤️",
    page_icon="🎂",
    layout="centered",
    initial_sidebar_state="collapsed",
)

ASSETS = Path(__file__).parent / "assets"

# ---------- Styling ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Poppins:wght@400;500;600&display=swap');

.stApp {
    background:
        radial-gradient(circle at 15% 10%, rgba(255, 105, 180, .14), transparent 30%),
        radial-gradient(circle at 85% 20%, rgba(255, 180, 200, .10), transparent 28%),
        linear-gradient(135deg, #10070d 0%, #1c0b16 48%, #090509 100%);
    color: #fff;
}

.block-container {
    max-width: 850px;
    padding-top: 2.2rem;
    padding-bottom: 4rem;
}

h1, h2, h3 {
    font-family: 'Cormorant Garamond', serif !important;
    letter-spacing: .5px;
}

p, div, label, button {
    font-family: 'Poppins', sans-serif;
}

.hero {
    text-align: center;
    padding: 2.5rem 1rem 1.5rem;
}

.eyebrow {
    color: #f5a6c6;
    text-transform: uppercase;
    letter-spacing: 4px;
    font-size: .72rem;
    font-weight: 600;
}

.hero h1 {
    font-size: clamp(3rem, 9vw, 6rem);
    line-height: .9;
    margin: .5rem 0 1rem;
}

.subtitle {
    color: #e8cdd8;
    font-size: 1rem;
    line-height: 1.8;
}

.card {
    background: rgba(255,255,255,.055);
    border: 1px solid rgba(255,255,255,.12);
    border-radius: 24px;
    padding: 1.4rem;
    margin: 1rem 0;
    box-shadow: 0 18px 60px rgba(0,0,0,.22);
}

.quote {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.75rem;
    line-height: 1.35;
    color: #ffe3ed;
    text-align: center;
    padding: 1.5rem .5rem;
}

.small {
    color: #cdb5c0;
    font-size: .85rem;
    line-height: 1.7;
}

.mem-caption {
    text-align: center;
    padding: .8rem .2rem 1.2rem;
}

.mem-caption h3 {
    margin: .2rem 0;
    font-size: 1.7rem;
}

.mem-caption p {
    color: #d9c0cb;
    margin: 0;
}

.final {
    text-align: center;
    padding: 2rem 1rem 1rem;
}

.final h1 {
    font-size: clamp(3.5rem, 11vw, 7rem);
    margin: .5rem 0;
}

.final p {
    color: #f0dce4;
    line-height: 1.8;
}

.progress-text {
    text-align: center;
    color: #bfa9b3;
    font-size: .75rem;
    letter-spacing: 1px;
    margin-bottom: .5rem;
}

div.stButton > button {
    width: 100%;
    border-radius: 999px;
    border: 1px solid rgba(255,255,255,.18);
    background: linear-gradient(90deg, #d84b83, #a72d68);
    color: white;
    font-weight: 600;
    min-height: 3rem;
    box-shadow: 0 8px 25px rgba(200,55,120,.2);
}

div.stButton > button:hover {
    border-color: #ffc1d8;
    transform: translateY(-1px);
}

[data-testid="stImage"] img {
    border-radius: 22px;
}

div[data-testid="stRadio"] label {
    color: #f6e7ed !important;
}

.footer {
    text-align:center;
    color:#8f7883;
    font-size:.72rem;
    padding-top:2rem;
}
</style>
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

def nav():
    if st.session_state.page > 0:
        c1, c2 = st.columns(2)
        with c1:
            st.button("← Back", on_click=prev_page, key=f"back_{st.session_state.page}")
        with c2:
            if st.session_state.page < TOTAL - 1:
                st.button("Continue →", on_click=next_page, key=f"next_{st.session_state.page}")
    elif st.session_state.page == 0:
        st.button("Open your birthday surprise →", on_click=next_page, key="start")

def photo(name, width="stretch"):
    path = ASSETS / name
    if path.exists():
        st.image(str(path), width=width)

# ---------- Pages ----------
page = st.session_state.page

if page > 0:
    st.markdown(f'<div class="progress-text">YOUR BIRTHDAY JOURNEY · {page}/{TOTAL-1}</div>', unsafe_allow_html=True)
    st.progress(page / (TOTAL - 1))

if page == 0:
    st.markdown("""
    <div class="hero">
        <div class="eyebrow">A tiny corner of the internet · made just for you</div>
        <h1>Happy Birthday,<br>Birthday Boy ❤️</h1>
        <div class="subtitle">
            Before you scroll any further...<br>
            just know that someone has put an unreasonable amount of love into this.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('<div class="quote">“Tonight is yours. But I may have secretly made it about us too.”</div>', unsafe_allow_html=True)
    nav()

elif page == 1:
    st.markdown("## 🔐 Okay birthday boy… prove it's you")
    st.markdown('<div class="card"><div class="small">There are no wrong answers. Except the ones that are wrong. Those are definitely wrong. 😂</div></div>', unsafe_allow_html=True)
    name = st.text_input("What does your favourite person call you?", placeholder="Your answer...")
    if st.button("I am definitely him 😌"):
        if name.strip():
            st.session_state.answers["name"] = name.strip()
            st.success("Identity confirmed. Unfortunately, you're stuck with me. ❤️")
        else:
            st.warning("You have to type something first 😂")
    nav()

elif page == 2:
    st.markdown("## 🧠 How well do you know us?")
    st.caption("Tiny relationship exam. No cheating. I know where you live. 😂")

    q1 = st.radio("Who is more dramatic?", ["Me", "You", "We are equally dramatic"], key="q1")
    q2 = st.radio("Who is more likely to say “I'm fine” while absolutely NOT being fine?", ["Me", "You", "Both of us"], key="q2")
    q3 = st.radio("Who loves the other person more?", ["Me ❤️", "You ❤️", "Obviously both"], key="q3")

    if st.button("Submit my extremely accurate answers"):
        st.session_state.answers.update({"q1": q1, "q2": q2, "q3": q3})
        st.balloons()
        st.success("Answers received. The relationship department will review your application. 😂❤️")
    nav()

elif page == 3:
    st.markdown("## 📸 A few of my favourite versions of us")
    st.markdown('<div class="small">Some memories deserve more than a camera roll. They deserve their own little place here.</div>', unsafe_allow_html=True)

    photo("first_trip.jpeg")
    st.markdown("""
    <div class="mem-caption">
        <h3>Our first trip 🧳</h3>
        <p>I'm biased, but this is still my favourite picture of you.</p>
    </div>
    """, unsafe_allow_html=True)

    photo("the_view.jpeg")
    st.markdown("""
    <div class="mem-caption">
        <h3>The view 🌙</h3>
        <p>I want this view always.</p>
    </div>
    """, unsafe_allow_html=True)

    photo("prettiest_frame.jpeg")
    st.markdown("""
    <div class="mem-caption">
        <h3>Prettiest frame 🤍</h3>
        <p>Some pictures are pretty. Some just feel like us.</p>
    </div>
    """, unsafe_allow_html=True)
    nav()

elif page == 4:
    st.markdown("## ❤️ Things I hope you never forget")
    points = [
        "You are allowed to be proud of how far you've come.",
        "You don't have to have everything figured out right now.",
        "I hope you keep choosing the things that make you genuinely happy.",
        "I hope you chase the big dreams, even when they look scary.",
        "I hope you never forget how capable you are.",
        "And on the days when you forget... I'll remind you. 🫶",
    ]
    for i, text in enumerate(points, 1):
        st.markdown(f'<div class="card"><b>{i:02}</b> &nbsp; {text}</div>', unsafe_allow_html=True)
    nav()

elif page == 5:
    st.markdown("## 💌 A little love letter")
    st.markdown("""
    <div class="card">
    <div class="quote">
    I don't know what the future is going to look like.<br>
    But I know one thing I want in it — <b>you.</b>
    </div>
    <p>
    I want the ordinary days with you. The random drives, the stupid jokes,
    the arguments over absolutely nothing, the food runs, the trips we haven't
    planned yet, the pictures we'll take, and all the little moments that
    nobody else will understand the way we do.
    </p>
    <p>
    I hope this year gives you everything you've been working for.
    And I hope, somewhere between all the big achievements, you remember
    to stop and enjoy the life you're building.
    </p>
    <p>
    Happy birthday to my favourite person. ❤️
    </p>
    </div>
    """, unsafe_allow_html=True)
    nav()

elif page == 6:
    st.markdown("## 🎁 Pick a little surprise")
    st.caption("You can only open one. Choose wisely. Or don't. 😌")

    choices = {
        "💌 A soft one": "I love you more than I can fit into a website. And yes, I tried.",
        "😂 A dangerous one": "You are officially one year older. Unfortunately, I still have evidence of all your embarrassing moments.",
        "🌱 A future one": "One day we'll look back at this version of us and be ridiculously proud of everything we built.",
    }
    for label, message in choices.items():
        if st.button(label, key=f"surprise_{label}"):
            st.session_state.answers["surprise"] = label
            st.markdown(f'<div class="card"><div class="quote">{message}</div></div>', unsafe_allow_html=True)
            st.balloons()
    nav()

elif page == 7:
    st.markdown("## 🎂 One last thing...")
    st.markdown('<div class="hero"><div class="subtitle">Before the final surprise, you have an important birthday duty.</div><h1>Cut the cake.</h1></div>', unsafe_allow_html=True)
    cake = st.button("🔪 CUT THE CAKE 🎂", key="cake")
    if cake:
        st.balloons()
        st.markdown("""
        <div class="final">
            <div style="font-size:5rem;">🎂✨🎉</div>
            <h1>IT'S YOUR DAY!</h1>
            <p>Make a wish. I already know mine. ❤️</p>
        </div>
        """, unsafe_allow_html=True)
        st.session_state.answers["cake"] = True
    nav()

elif page == 8:
    photo("birthday_final.jpeg")
    st.markdown("""
    <div class="final">
        <div class="eyebrow">The final page</div>
        <h1>HAPPY<br>BIRTHDAY ❤️</h1>
        <p>
            To my favourite human,<br>
            may this year be kinder, bigger, crazier, happier<br>
            and full of everything you deserve.
        </p>
        <div class="quote">“And yes… I would choose you again.”</div>
        <div style="font-size:2rem;">🫶 ✨ 🎂 ❤️ ✨ 🫶</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="footer">Made with an unreasonable amount of love ❤️</div>', unsafe_allow_html=True)
