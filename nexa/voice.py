import speech_recognition as sr
import pyttsx3
import datetime
from config.logger import get_logger

logger = get_logger(__name__)

def speak(text):
    """Convert text to speech (Streamlit-safe)."""
    try:
        logger.info(f"Speaking: {text}")

        # ✅ FIX: engine initialized INSIDE function
        engine = pyttsx3.init()
        engine.setProperty("rate", 170)

        engine.say(text)
        engine.runAndWait()
        engine.stop()

    except Exception as e:
        logger.error(f"Error in speak(): {type(e).__name__}: {str(e)}")

def take_command():
    """Listen to user voice command and return recognized text."""
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 3000
    recognizer.dynamic_energy_threshold = True
    recognizer.pause_threshold = 1

    try:
        with sr.Microphone() as source:
            logger.info("Listening for command...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(
                source,
                timeout=15,
                phrase_time_limit=15
            )

        logger.info("Recognizing command...")
        query = recognizer.recognize_google(audio, language="en-in")
        logger.info(f"Command recognized: {query}")
        return query.lower()

    except sr.UnknownValueError:
        logger.warning("Speech not understood")
        speak("Say that again please")
        return "none"

    except sr.RequestError as e:
        logger.error(f"Speech recognition service error: {e}")
        speak("Speech service is not available")
        return "none"

    except Exception as e:
        logger.error(f"Unexpected error: {type(e).__name__}: {str(e)}")
        return "none"

def wish_me():
    """Greet the user based on the time of day."""
    hour = datetime.datetime.now().hour
    logger.info("Greeting user")

    if 0 <= hour < 12:
        speak("Good Morning! Shafin")
    elif 12 <= hour < 18:
        speak("Good Afternoon! Shafin")
    else:
        speak("Good Evening! Shafin")
        
    speak("I am NEXA. How may I assist you today?")

def greet():
    """Alias for backward compatibility."""
    wish_me()
