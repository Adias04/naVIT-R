import speech_recognition as sr
import pygame
import os

# function to convert text to speech
def speak(text):
    pygame.mixer.init()
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

# function to convert speech to text
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Speak now...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except:
        print("Sorry, could not recognize your voice.")
        return ""

# main program loop
while True:
    speak("What would you like to search for? Enter 1 for University Prediction or 2 for Faculty Room Information.")
    choice = listen().lower()
    
    if "1" in choice:
        import University_prediction
        University_prediction.get_university_ratings_voice()
    elif "2" in choice:
        import faculty_details_getter
        faculty_details_getter.get_faculty_details_voice()
    else:
        speak("Sorry, I didn't understand what you said. Please try again.")

    speak("Do you want to search for something else?")
    choice = listen().lower()
    if "no" in choice:
        speak("Thank you for using our service.")
        break


    
        
       












