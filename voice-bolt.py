import speech_recognition as sr
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to the user's command
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for your command...")
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
            return None
        except sr.RequestError:
            print("Sorry, I couldn't connect to the speech recognition service.")
            return None

# Main loop for the bot
def main():
    speak("Hello, I am your voice assistant.")
    
    while True:
        command = listen()
        
        if command:
            command = command.lower()
            if "hello" in command:
                speak("Hi there! How can I assist you?")
            elif "exit" in command or "quit" in command:
                speak("Goodbye!")
                break
            else:
                speak("Sorry, I did not understand that. Please try again.")

if __name__ == "__main__":
    main()
