import speech_recognition as sr
import pyttsx3

# initialize the text-to-speech engine
engine = pyttsx3.init()

# function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# function to convert speech to text
def listen():
    r = sr.Recognizer()
    r.energy_threshold = 1000 # adjust as necessary
    with sr.Microphone() as source:
        print("Speak now...")
        audio = r.listen(source, phrase_time_limit=10) # adjust as necessary
    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except:
        print("Sorry, could not recognize your voice.")
        return ""

# main program loop
while True:
    speak("What would you like to search for? Say 'University Prediction' or 'Faculty Room Information'.")
    choice = listen().lower()
    
    if "university prediction" in choice:
        import University_prediction
        University_prediction.admission_service()
    elif "faculty room information" in choice:
        import faculty_details_getter
        faculty_details_getter.run()
    else:
        speak("Sorry, I didn't understand what you said. Please try again.")
        continue

    speak("Do you want to search for something else?")
    choice = listen().lower()
    if "no" in choice:
        speak("Thank you for using our service.")
        exit()


    
        
       












