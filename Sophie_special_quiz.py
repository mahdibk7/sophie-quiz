# Sophie Special Quiz 💖 (Streamlit Version)

import streamlit as st

st.set_page_config(page_title="Sophie’s Special Quiz 💘", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
        .main {
            background-color: #fff5f8;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
        }
        h1, h3 {
            text-align: center;
            color: #d63384;
        }
        .stButton>button {
            background-color: #ff91af;
            color: white;
            border: none;
            border-radius: 10px;
            padding: 0.5rem 1.5rem;
            font-size: 1rem;
            margin: 0.25rem auto;
            display: block;
        }
        .stButton>button:hover {
            background-color: #ff5e95;
        }
        .result {
            font-size: 1.2rem;
            color: #6f42c1;
            text-align: center;
            margin-top: 1rem;
        }
        .score-box {
            background-color: #ffe3ed;
            padding: 1rem;
            border-radius: 10px;
            margin-top: 1rem;
            text-align: center;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Image at top
st.image("sophie.png", use_column_width=True)

st.markdown("<div class='main'>", unsafe_allow_html=True)

st.title("Sophie’s Special Quiz 💘")
st.markdown("### How well do you know me? 😏")

# Questions and answers
questions = [
    {"question": "What’s my favourite food?", "options": ["Pizza", "Burger", "Couscous", "Sushi"], "answer": "Pizza"},
    {"question": "Where did we first meet?", "options": ["Mosque", "Library", "Muzz", "Park"], "answer": "Muzz"},
    {"question": "What’s my favourite colour?", "options": ["Blue", "Red and Yellow", "Green", "Black"], "answer": "Red and Yellow"},
    {"question": "Which city would I love to visit together?", "options": ["Paris", "Marrakech", "Algiers", "Istanbul"], "answer": "Algiers"},
    {"question": "A car I want to buy?", "options": ["BMW 3 Series", "Toyota Corolla", "Mercedes A-Class", "Audi A1"], "answer": "Mercedes A-Class"},
    {"question": "What’s my dream job?", "options": ["Vet", "Chef", "Footballer", "Photographer"], "answer": "Footballer"},
    {"question": "What’s my favourite sport?", "options": ["Football", "Boxing", "Basketball", "Tennis"], "answer": "Football"},
    {"question": "Which game do I enjoy the most?", "options": ["Call of Duty", "FIFA", "Fortnite", "Assassin's Creed"], "answer": "FIFA"},
    {"question": "What’s my go-to snack?", "options": ["Popcorn", "Chocolate", "Hazelnuts", "Chips"], "answer": "Chocolate"},
    {"question": "What language do I want to improve?", "options": ["French", "Arabic", "Italian", "Spanish"], "answer": "Italian"},
]

if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.q_index = 0

if st.session_state.q_index < len(questions):
    q = questions[st.session_state.q_index]
    st.markdown(f"#### {q['question']}")
    for option in q["options"]:
        if st.button(option):
            if option == q["answer"]:
                st.session_state.score += 1
            st.session_state.q_index += 1
            st.experimental_rerun()
else:
    st.markdown("---")
    st.markdown(f"<div class='score-box'>You scored {st.session_state.score} out of {len(questions)}</div>", unsafe_allow_html=True)

    if st.session_state.score == len(questions):
        st.markdown("<div class='result'>💘 You know me so well! MashaAllah 💘</div>", unsafe_allow_html=True)
    elif st.session_state.score >= 7:
        st.markdown("<div class='result'>😊 Great job! You really know me!</div>", unsafe_allow_html=True)
    elif st.session_state.score >= 4:
        st.markdown("<div class='result'>😅 Not bad! But there's room for improvement!</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='result'>😂 We need to talk! Just kidding. Love you anyway ❤️</div>", unsafe_allow_html=True)

    if st.button("Play Again 💫"):
        st.session_state.score = 0
        st.session_state.q_index = 0
        st.experimental_rerun()

st.markdown("</div>", unsafe_allow_html=True)
