import streamlit as st
import random
import time

# ❄️ ونٹر ایفیکٹ کے لیے CSS
snow_effect = """
    <style>
    @keyframes snow {
        from {transform: translateY(0px);}
        to {transform: translateY(100vh);}
    }
    .snowflake {
        position: fixed;
        top: -10px;
        color: white;
        user-select: none;
        font-size: 32px;
        animation: snow 5s linear infinite;
    }
    </style>
"""

# ❤️ دلوں کے لیے CSS ایفیکٹ
hearts_effect = """
    <style>
    @keyframes hearts {
        from {transform: translateY(0px);}
        to {transform: translateY(100vh);}
    }
    .heart {
        position: fixed;
        top: -10px;
        color: red;
        user-select: none;
        font-size: 32px;
        animation: hearts 5s linear infinite;
    }
    </style>
"""

# 🔲 بیک گراؤنڈ امیج شامل کریں (صحیح طریقے سے)
bg_image = """
    <style>
    .stApp {
        background: url('https://media.istockphoto.com/id/900009520/photo/valentines-day-blurred-hearts-background.jpg?s=612x612&w=0&k=20&c=QgAl2uWzM0w5aEHkrlCXv3LdMqUg6EtPaWjoo13dZME=') no-repeat center center fixed;
        background-size: cover;
    }
    </style>
"""
st.markdown(bg_image, unsafe_allow_html=True)

# ایپ کا ٹائٹل
st.title("💌 Message for You My Bestu")

# لفافے کی تصویر
closed_envelope = "👉✉️"
open_envelope = "💌"

# میسج کو پہلے چھپائیں
if "opened" not in st.session_state:
    st.session_state.opened = False

# لفافہ کھولنے کا بٹن (بڑا کیا اور ایموجیز شامل کیے)
button_text = "💖💌 CLICK TO OPEN THE ENVELOPE 💌💖" if not st.session_state.opened else "📜 Scroll Down 📜"
if st.button(button_text, key="open_btn", help="Surprise Inside!", use_container_width=True):
    st.session_state.opened = True
    time.sleep(1)  # تھوڑا سا ڈرامائی وقفہ

# لفافے کی حالت دکھائیں
if not st.session_state.opened:
    st.markdown(f"<h1 style='text-align: center; margin-bottom: 0px;'>{closed_envelope}</h1>", unsafe_allow_html=True)
else:
    st.markdown(snow_effect, unsafe_allow_html=True)  # ❄️ برفباری کا ایفیکٹ شامل کریں
    
    # ❄️ اسکرین پر برف، دل، غبارے اور پارٹی پاپرز کے ایموجیز دکھانے کے لیے
    for i in range(20):
        x_pos = random.randint(0, 100)  # تصادفی X پوزیشن
        emoji = random.choice(["❄️", "❤️", "💫", "🎉","😊","💕"])  # تصادفی ایموجیز
        st.markdown(f"<div class='snowflake' style='left:{x_pos}%;'>{emoji}</div>", unsafe_allow_html=True)
    
    # کھلا لفافہ دکھائیں
    st.markdown(f"<h1 style='text-align: center; margin-bottom: 0px;'>{open_envelope}</h1>", unsafe_allow_html=True)
    
    # پیغام دکھائیں (بہت بڑا سائز کیا)
    st.markdown(
        """
        <div style='text-align: center; font-size: 60px; color: #e63946; font-weight: bold; margin-top: -20px;'>
            🎈🎉 Aap bohat ache hain, aap meri duniya ka sabse khoobsurat hissa hain. Munu, aap meri khushi, mera sukoon, aur meri har muskurahat ki wajah hain. Aapki har baat dil ko sukoon deti hai, aur aapka har ek lafz meri duniya roshan kar deta hai. Aap sirf ek naam nahi, ek ehsaas hain jo har waqt dil ke kareeb rehta hai. ❤️🎉🎈
        </div>
        """,
        unsafe_allow_html=True
    )

    # ❤️ دلوں والا دوسرا سیکشن
    time.sleep(2)  # تھوڑا سا وقفہ کہ دل بعد میں آئیں
    st.markdown(hearts_effect, unsafe_allow_html=True)  # ❤️ دلوں کا ایفیکٹ شامل کریں
    for i in range(20):
        x_pos = random.randint(0, 100)  # تصادفی X پوزیشن
        emoji = random.choice(["❤️", "🥰", "🎉","💞","❣️","💝"])  # تصادفی ایموجیز
        st.markdown(f"<div class='heart' style='left:{x_pos}%;'>{emoji}</div>", unsafe_allow_html=True)
    
    st.markdown(
        """
        <div style='text-align: center; font-size: 60px; color: #ff1493; font-weight: bold; margin-top: -20px;'>
            💞✨ Love You So Much, Munu! 💞✨
        </div>
        """,
        unsafe_allow_html=True
    )
