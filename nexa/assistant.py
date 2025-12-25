import datetime
import wikipedia
import webbrowser
import subprocess
import random

from nexa.voice import speak
from nexa.memory import Memory
from nexa.prompt_controller import PromptController
from config.logger import get_logger

logger = get_logger(__name__)

class NexaAssistant:
    def __init__(self, engine):
        self.engine = engine
        self.memory = Memory()
        self.role = "Tutor"
        logger.info("NexaAssistant initialized")

    def set_role(self, role):
        self.role = role
        logger.info(f"Role set to {role}")

    def is_wake_word(self, text):
        return "hi nexa" in text or "hey nexa" in text

    def handle(self, query):
        logger.info(f"Handling query: {query}")

        # Name query
        if "your name" in query:
            speak("My name is NEXA")
            logger.info("User asked for assistant's name.")
            return "My name is NEXA"

        # Time query
        if "time" in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {time}")
            logger.info("User asked for current time.")
            return f"The time is {time}"

        # How are you
        if "how are you" in query:
            speak("I am functioning at full capacity!")
            logger.info("User asked about assistant's well-being.")
            return "I am functioning at full capacity!"

        # Who made you
        if "who made you" in query or "who created you" in query:
            speak("I was created by Shafin, a brilliant mind!")
            logger.info("User asked about assistant's creator.")
            return "I was created by Shafin, a brilliant mind!"

        # Thank you
        if "thank you" in query or "thanks" in query:
            speak("It's my pleasure. Always happy to help.")
            logger.info("User expressed gratitude.")
            return "It's my pleasure. Always happy to help."

        # Open Google
        if "open google" in query:
            speak("Opening Google for you")
            webbrowser.open("https://google.com")
            logger.info("User requested to open Google.")
            return "Opening Google"

        # Calculator
        if "open calculator" in query or "calculator" in query:
            speak("Opening calculator")
            subprocess.Popen("calc.exe")
            logger.info("User requested to open Calculator.")
            return "Opening calculator"

        # Notepad
        if "open notepad" in query or "notepad" in query:
            speak("Opening Notepad")
            subprocess.Popen("notepad.exe")
            logger.info("User requested to open Notepad.")
            return "Opening Notepad"

        # Calendar
        if "open calendar" in query or "calendar" in query:
            speak("Opening Google Calendar")
            webbrowser.open("https://calendar.google.com")
            logger.info("User requested to open Calendar.")
            return "Opening Google Calendar"

        # YouTube
        if "youtube" in query:
            speak("Opening YouTube for you")
            search_query = query.replace("youtube", "").strip()
            if search_query:
                webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")
            else:
                webbrowser.open("https://www.youtube.com")
            logger.info("User requested to search on YouTube.")
            return "Opening YouTube"

        # Facebook
        if "open facebook" in query or "facebook" in query:
            speak("Opening Facebook")
            webbrowser.open("https://facebook.com")
            logger.info("User requested to open Facebook.")
            return "Opening Facebook"

        # GitHub
        if "open github" in query or "github" in query:
            speak("Opening GitHub")
            webbrowser.open("https://github.com")
            logger.info("User requested to open GitHub.")
            return "Opening GitHub"

        # LinkedIn
        if "open linkedin" in query or "linkedin" in query:
            speak("Opening LinkedIn")
            webbrowser.open("https://linkedin.com")
            logger.info("User requested to open LinkedIn.")
            return "Opening LinkedIn"

        # Joke
        if "joke" in query:
            jokes = [
                "Why don't programmers like nature? Too many bugs.",
                "I told my computer I needed a break. It said no problem, it will go to sleep.",
                "Why do Java developers wear glasses? Because they don't C sharp."
            ]
            joke = random.choice(jokes)
            speak(joke)
            logger.info("User requested a joke.")
            return joke

        # Wikipedia
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            search_query = query.replace("wikipedia", "").strip()
            try:
                results = wikipedia.summary(search_query, sentences=2)
                speak("According to Wikipedia")
                speak(results)
                logger.info("User requested information from Wikipedia.")
                return results
            except Exception as e:
                logger.error(f"Wikipedia search error: {e}")
                speak("Could not find information on Wikipedia")
                return "Could not find information on Wikipedia"

        # AI MODE (fallback for unhandled queries)
        context = ""
        prompt = PromptController(self.role).build(context, query)
        speak("Let me think")
        answer = self.engine.generate(prompt)

        self.memory.add("User", query)
        self.memory.add("NEXA", answer)

        speak(answer)
        return answer
