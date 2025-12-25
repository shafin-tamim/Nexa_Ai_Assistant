import streamlit as st
from config.settings import Settings
from nexa.gemini_engine import GeminiEngine
from nexa.assistant import NexaAssistant
from nexa.voice import take_command, greet
from config.logger import get_logger

logger = get_logger(__name__)

st.set_page_config(
    page_title="NEXA AI Assistant",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        text-align: center;
        padding: 20px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
        color: white;
        margin-bottom: 20px;
    }
    .role-card {
        padding: 15px;
        border-radius: 8px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        margin: 10px 0;
        color: white;
        border: 2px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .chat-container {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        border-radius: 12px;
        padding: 20px;
        margin: 15px 0;
        min-height: 400px;
        max-height: 600px;
        overflow-y: auto;
    }
    .chat-message {
        padding: 12px 15px;
        border-radius: 8px;
        margin: 10px 0;
        word-wrap: break-word;
        color: #333;
        font-size: 14px;
    }
    .user-msg {
        background-color: #e3f2fd;
        border-left: 4px solid #667eea;
        margin-left: 20px;
        color: #1565c0;
    }
    .assistant-msg {
        background-color: #f3e5f5;
        border-left: 4px solid #764ba2;
        margin-right: 20px;
        color: #6a1b9a;
    }
    </style>
""", unsafe_allow_html=True)

logger.info("Application started")

# Initialize
settings = Settings()
engine = GeminiEngine(settings.load_api_key())
assistant = NexaAssistant(engine)

# Sidebar Configuration
with st.sidebar:
    st.markdown("### ⚙️ Settings")
    
    # Role Selection
    st.markdown("#### 👤 Select Your Role")
    role = st.radio(
        "Choose AI Role:",
        ["Tutor", "Coding Assistant", "Career Mentor"],
        index=0,
        label_visibility="collapsed"
    )
    assistant.set_role(role)
    
    st.markdown(f"**Current Role:** {role}")
    
    st.divider()
    
    # Chat Management
    st.markdown("#### 💬 Chat Management")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🆕 New Chat", use_container_width=True):
            st.session_state.messages = []
            assistant.memory.clear()
            st.success("Chat cleared!")
    with col2:
        if st.button("🔄 Reset", use_container_width=True):
            st.session_state.clear()
    
    st.divider()
    
    # Information
    st.markdown("#### ℹ️ About NEXA")
    st.info(
        "🧠 **NEXA** - Your Advanced AI Assistant\n\n"
        "• Real-time conversation\n"
        "• Voice command support\n"
        "• Multiple role modes\n"
        "• Persistent memory"
    )

# Main Content Area
st.markdown(
    '<div class="main-header"><h1>🧠 NEXA – Advanced AI Assistant</h1><p>Your intelligent companion for learning, coding, and career guidance</p></div>',
    unsafe_allow_html=True
)

# Greeting
if "greeted" not in st.session_state:
    greet()
    st.session_state.greeted = True

# Initialize messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Role Info Card
st.markdown(f"""
    <div class="role-card">
    <b>📋 Active Mode:</b> {role}<br>
    <small>Tap the 🎙️ button to speak or type your message below</small>
    </div>
""", unsafe_allow_html=True)

# Chat Display Area
st.markdown("### 💭 Conversation")

# Center container for messages
col_left, col_center, col_right = st.columns([1, 3, 1])

with col_center:
    if st.session_state.messages:
        for idx, msg in enumerate(st.session_state.messages):
            if msg["role"] == "user":
                st.markdown(f"""
                    <div style="
                        background-color: #e3f2fd;
                        border-left: 4px solid #667eea;
                        padding: 12px 15px;
                        border-radius: 8px;
                        margin: 10px 0;
                        color: #1565c0;
                        font-size: 14px;
                    ">
                    <b>👤 You:</b><br>{msg["content"]}
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                    <div style="
                        background-color: #f3e5f5;
                        border-left: 4px solid #764ba2;
                        padding: 12px 15px;
                        border-radius: 8px;
                        margin: 10px 0;
                        color: #6a1b9a;
                        font-size: 14px;
                    ">
                    <b>🧠 NEXA:</b><br>{msg["content"]}
                    </div>
                """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div style="
                text-align: center;
                color: #999;
                padding: 60px 20px;
                font-size: 16px;
            ">
                <p style="font-size: 32px; margin: 0;">👋</p>
                <p><b>Welcome to NEXA!</b></p>
                <p>Start a conversation by typing a message or clicking 🎙️ to speak.</p>
            </div>
        """, unsafe_allow_html=True)

# Input Section
st.markdown("### 📤 Send Message")

with st.form(key="message_form", clear_on_submit=True):
    user_text = st.text_input(
        "Your message",
        placeholder="Type your message here...",
        label_visibility="collapsed",
        key="message_input"
    )
    
    col1, col2 = st.columns(2)
    with col1:
        send_button = st.form_submit_button("📨 Send", use_container_width=True)
    with col2:
        speak_button = st.form_submit_button("🎙️ Speak", use_container_width=True)
    
    if send_button and user_text:
        st.session_state.messages.append({"role": "user", "content": user_text})
        with st.spinner("🤔 NEXA is thinking..."):
            response = assistant.handle(user_text)
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()

# Handle speak button outside form
if speak_button:
    with st.spinner("🎤 Listening... (speak clearly)"):
        voice_text = take_command()
    
    if voice_text:
        if assistant.is_wake_word(voice_text):
            query = voice_text.replace("hi nexa", "").strip()
            if query:
                st.session_state.messages.append({"role": "user", "content": query})
                with st.spinner("🤔 Processing your voice command..."):
                    response = assistant.handle(query)
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.rerun()
            else:
                st.warning("⚠️ Please say a command after **'Hi NEXA'**")
        else:
            st.info("ℹ️ Start with **'Hi NEXA'** to activate voice commands")
    else:
        st.error("❌ No speech detected. Check microphone and try again.")
    
    logger.info("Voice command processed")

# Footer
st.divider()
st.markdown(
    "<div style='text-align: center; color: gray; font-size: 12px;'>"
    "🤖 NEXA AI Assistant v1.0 | Powered by Gemini AI</div>",
    unsafe_allow_html=True
)