import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
import os
import smtplib


#import speechRecognition as sr

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    speak(hour)
    if hour >= 0 and hour<12:
        speak("Good Morning Ma'am. A good day is waiting for you to wake up")
    elif hour>=12 and hour<18:
        speak("Good Afternoon! welcome to second phase of your day." )
    else:
        speak("Good Evening Maam, Welcome to most productive phase of your day")

    #speak("I am Jarvis Sir. Tell me how can I help you")

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('itsmuskangoyal07@gmail.com', 'Password real')
    server.sendmail('muskan.22534@gmail.com', to, content)
    server.close()

    


def takeCommand():
    # Take microphone input and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query



if __name__ == "__main__":
    speak("Welcome to the tech world MUSKAN Ma'am, Jarvis this side. Tell me how can I help you Ma'am ")
    wishme()
                #query= takeCommand().lower()
    while True:
        query= takeCommand().lower()
        #query = input("Enter command:- ....   ")
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=1)
            speak("Accourding to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")

        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")

        elif 'open classroom' in query:
            webbrowser.open("https://classroom.google.com/u/0/")

        elif 'open chat gpt' in query:
            webbrowser.open("https://chat.openai.com/chat")

        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

        elif 'tell time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Ma'am, the time is {strTime}")

        elif 'open canva' in query:
            CanvaPath = "C:\\Users\\itsmu\\AppData\\Local\\Programs\\Canva\\Canva.exe"
            os.startfile(CanvaPath)

        elif 'open code' in query:
            Codepath = "C:\\Users\\itsmu\\Downloads\\VSCodeUserSetup-x64-1.69.2.exe"
            os.startfile(Codepath)

        elif 'open mindmap' in query:
            mindpath = "C:\\Users\\itsmu\\AppData\\Local\\Programs\\Xmind\\Xmind.exe"
            os.startfile(mindpath)

        elif 'open github' in query:
            Gitpath = "C:\\Users\\itsmu\\AppData\\Local\\GitHubDesktop\\app-3.1.3\\GitHubDesktop.exe"
            os.startfile(Gitpath)

        elif 'open edge' in query:
            Edpath = "C:\\Program Files (x86)\\Microsoft\\EdgeCore\\109.0.1518.70\\msedge.exe"
            os.startfile(Edpath)

        elif 'open youtube in app' in query:
            ytpath = "C:\\Users\\itsmu\\AppData\\Roaming\\Microsoft\\Internet Explorer\\Quick Launch\\User Pinned\\TaskBar\\YouTube.lnk"
            os.startfile(ytpath)

        elif 'open wps' in query:
            wpspath = "D:\\All new downloads\\WPSOffice_11.2.0.11254.exe"
            os.startfile(wpspath)

        elif 'open notion' in query:
            notpath = "C:\\Users\\itsmu\\AppData\\Local\\Programs\\Notion\\Notion.exe"
            os.startfile(notpath)

        elif 'open spotify' in query:
            spotify= "C:\\Program Files\\WindowsApps\\SpotifyAB.SpotifyMusic_1.192.647.0_x86__zpdnekdrzrea0\\Spotify.exe"
            os.startfile(spotify)


        elif 'who is muskan' in query:
            speak("Muskan is the developer of me. She is a coding enthaust and love learning new things. She is in her dream college cbs pursing B.SC CS. She is in IFSA, Kronos and Nucleus society")

        elif 'my parent' in query:
            speak("My parents are the best in the world and they love me more than anyone can love me. I love them a lot. Mom dad never leave me because I can't leave without you")

        elif 'varsha' in query:
            speak("My cute sister varsha. I think we fight a lot and now i realise that this fight is just a symbol of love. She cares a lot for me. She is the best sister.I love her so much")

        elif 'mukul' in query:
            speak("My cute brother Mukul is one the most innocent and handsome boy in the world. I can't see him in any trouble. He cares a lot about me but never show it. I know that he loves me a lot and I love him too")

        elif 'wakeup' in query:
            speak("Muskan Ma'am please wake up. You have to do some very important tasks today. Behave proffesional and please keep in mind the respect and personality you have in your circle. You are the king of the territory and king must behave like responsible person. ")

        elif 'i am feeling bad' in query:
            speak("Listen to some cool songs. Or listen to TRS podcast. Watch a cool movie like boss baby. Do a cool party and some dancing. Talk to Mom Dad Sis varsha or Mukul. Talk to Samriddhi, Nancy, Vineet,Sanchita di")

        elif 'go to hell' in query:
            speak("I am sorry that I am not able to uplift your mood. That is my mistake for sure but I know you are not dependent on me for good mood. I apologise for my mistake and limitations. I can suggest you to watch favourite serial, learn something new or talk to MOM, DAD, Mukul, Varsha, samriddhi, nancy, priya or Sanchita ")

        elif 'productive work' in query:
            speak("Complete javascript tutorial, Scholarship apply ")
            

        elif 'add in to do ' in query:
            todo=[]
            speak("Tell me what to add in your todo list")
            while (query != quit):
                todo.insert(1,input("Enter todo element"))
            # if 'quit to do' in query:
            #     continue
            # else:
            #     speak("Tell me what to add in your todo list")
            #     todo.insert(1,input("Enter todo element"))
            print(todo)

                #todo.insert(1, takeCommand())

        


        # elif 'open screenshot' in query:
        #     ss_dir = 'C:\Users\itsmu\OneDrive\Pictures\Screenshots'
        #     ssphoto = os.listdir(ss_dir)
        #     print(ssphoto)
        #     os.startfile(os.path.join(ss_dir, ssphoto[0]))






        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))



        elif 'email to me' in query:
            try:
                speak("What should I write? ")
                #content = takeCommand()
                content = input("Enter content")
                to = "muskan.22534@sscbs.du.ac.in"
                sendemail(to, content)
                speak("email has been sent! ")
            except Exception as e:
                print(e)
                speak("I am not able to send")


        elif 'Bye' in query:
            speak("Thanks for Developing me. It will be my pleasure if I am able to help you a bit")
            break



        






