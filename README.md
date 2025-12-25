# 🧠 NEXA - Advanced AI Assistant

An intelligent voice-enabled AI assistant built with Python, Streamlit, and Google's Gemini API. NEXA can understand voice commands, provide real-time responses, open applications, search the web, and assist with various tasks through a beautiful web interface.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

## ✨ Features

### 🎙️ Voice Interaction
- **Voice Recognition**: Listen and respond to voice commands using Google Speech Recognition
- **Text-to-Speech**: Natural speech output with adjustable speed and tone using pyttsx3
- **Wake Word Detection**: Activate voice mode with "Hi NEXA" or "Hey NEXA"

### 🤖 AI Capabilities
- **AI-Powered Responses**: Intelligent answers powered by Google's Gemini 2.5 Flash model
- **Multiple Roles**: Switch between Tutor, Coding Assistant, and Career Mentor modes
- **Context-Aware**: Remembers conversation history for better responses
- **Real-time Streaming**: Get instant responses with beautiful UI updates

### 💾 Memory Management
- **Persistent Memory**: Keeps track of conversation history
- **Session Management**: Clear chat history or start new conversations
- **Context Building**: Uses previous messages for informed responses

### 🌐 Web Integration
- **Open Websites**: Google, YouTube, Facebook, GitHub, LinkedIn
- **YouTube Search**: Search and open YouTube videos directly
- **Google Calendar**: Quick access to Google Calendar
- **Web Navigation**: Easy browser automation

### 🛠️ System Control
- **Launch Applications**: Open Calculator, Notepad, and more
- **System Commands**: Control Windows applications (calc.exe, notepad.exe)
- **Cross-Platform**: Works on Windows, Linux, and macOS

### 📚 Information Services
- **Wikipedia Search**: Quick access to Wikipedia summaries
- **Current Time**: Get current time with voice response
- **Joke Telling**: Random jokes for entertainment
- **Casual Conversation**: Natural responses to greetings and questions

### 🎨 Beautiful UI
- **Modern Streamlit Interface**: Gradient styling with smooth animations
- **Chat History Display**: Beautiful message formatting
- **Responsive Design**: Works on desktop and tablet
- **Sidebar Controls**: Easy role switching and chat management

## 📋 Prerequisites

- **Python**: 3.8 or higher
- **Microphone**: For voice input
- **Speakers**: For audio output
- **Google Gemini API Key**: Free tier available at [Google AI Studio](https://makersuite.google.com/app/apikey)
- **Internet Connection**: Required for speech recognition and API calls

## 🚀 Installation

### Option 1: Using Conda (Recommended) ⭐

#### 1. Install Conda
Download and install [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/) or [Anaconda](https://www.anaconda.com/download)

#### 2. Clone the Repository
```bash
git clone https://github.com/yourusername/Nexa_Ai_Assistant.git
cd Nexa_Ai_Assistant
```

#### 3. Run Setup Script

**On Windows:**
```bash
conda create -n env name python=3.10 -y

```

#### 4. Setup Environment Variables
Create a `.env` file in the project root:
```env
GOOGLE_API_KEY="your_api_key_here"
```

Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

#### 5. Activate Environment & Run
```bash
conda activate env name
streamlit run app.py
```

# Install dependencies
pip install -r requirements.txt

# Create .env file
echo GOOGLE_API_KEY="your_api_key_here" > .env

# Run application
streamlit run app.py
```

## 📁 Project Structure

```
Nexa_Ai_Assistant/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── .env                            # Environment variables (API keys)
├── .gitignore                      # Git ignore rules
├── README.md                       # This file
├── LICENSE                         # MIT License
├── config/
│   ├── __init__.py
│   ├── logger.py                   # Logging configuration
│   └── settings.py                 # Application settings
├── nexa/
│   ├── __init__.py
│   ├── voice.py                    # Voice recognition & TTS
│   ├── assistant.py                # Main assistant logic
│   ├── gemini_engine.py            # Gemini API integration
│   ├── memory.py                   # Conversation memory
│   └── prompt_controller.py        # Prompt building
├── logs/
│   └── nexa.log                    # Application logs
└── research.ipynb                  # Testing & research notebook
```

## 🎯 Usage Guide

### 📝 Text Input
1. Open the app in your browser (usually `http://localhost:8501`)
2. Type your message in the input field at the bottom
3. Click **📨 Send** to get a response
4. Chat history appears in the conversation area above

### 🎤 Voice Commands
1. Click **🎙️ Speak** button
2. Say your command clearly
3. Start with **"Hi NEXA"** to activate voice mode
4. Example: *"Hi NEXA, what time is it?"*


## 📝 Logging

All activities are logged to `logs/nexa.log`:
- Voice recognition events
- API calls and responses
- User commands and assistant actions
- Error messages and exceptions


## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/YourFeature`
3. Commit changes: `git commit -m 'Add YourFeature'`
4. Push to branch: `git push origin feature/YourFeature`
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Google Gemini AI** - For powerful language model capabilities
- **Streamlit** - For beautiful web framework
- **SpeechRecognition** - For voice input capabilities
- **pyttsx3** - For text-to-speech synthesis
- **Wikipedia API** - For knowledge integration

## 📧 Contact & Support

- **Author**: Shafin Tamim
- **Email**: [your-email@example.com]
- **GitHub**: [github.com/your-username]
- **Issues**: [Report bugs here](https://github.com/yourusername/Nexa_Ai_Assistant/issues)

## 🗺️ Roadmap

- [ ] Multi-language support
- [ ] Email integration
- [ ] Calendar event creation
- [ ] Weather forecasts
- [ ] News summaries
- [ ] Custom voice profiles
- [ ] Mobile app
- [ ] Cloud deployment
- [ ] Database integration for persistent memory
- [ ] Advanced NLP features

## 🎓 Learning Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Google Gemini API Docs](https://ai.google.dev/docs)
- [Speech Recognition Library](https://github.com/Uberi/speech_recognition)
- [pyttsx3 Documentation](https://pyttsx3.readthedocs.io/)

## 💡 Tips & Tricks

1. **Faster Setup**: Use the automated `setup_conda.bat` (Windows) or `setup_conda.sh` (Linux/Mac)
2. **Custom Environment**: Use `python create_env.py custom-name` for custom names
3. **Voice Accuracy**: Speak clearly and reduce background noise
4. **API Optimization**: Cache responses for repeated queries
5. **Multiple Roles**: Switch roles for different use cases

---

**Made with ❤️ by Shafin Tamim**

⭐ **If you find this project helpful, please star it on GitHub!**

🚀 **Get Started Today**: `streamlit run app.py`