import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import random
import requests as req
import subprocess


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice) 
            command = command.lower()
        if "friday" in command:              
            command = command.replace("friday", "")
            print(command)
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    command = ""  # Assign an empty string to command if there's an error
    return command

def run_friday():
    command = take_command()
    print(command)
    if "hi" in command:
        current_datetime= datetime.datetime.now()
        hour=current_datetime.hour
        if(hour >= 6) and (hour < 12): 
            print("good morning, my name is friday, and I am a dedicated personal assistant with a years of experience in providing top-notch administrative support. I am here to make your life easier, handling tasks efficiently and allowing you to focus on what matters most")
            talk("Hello, my name is friday, and I am a dedicated personal assistant with a years of experience in providing top-notch administrative support. I am here to make your life easier, handling tasks efficiently and allowing you to focus on what matters most.")
        elif(hour >= 12) and (hour < 16) :
            print("good afternoon, I am friday,your tech-savvy personal assistant. With a passion for staying on the cutting edge of technology, I can help you streamline your digital life, from managing your calendar and emails to setting up smart home systems.")
            talk("good afternoon,I am friday, your tech-savvy personal assistant. With a passion for staying on the cutting edge of technology, I can help you streamline your digital life, from managing your calendar and emails to setting up smart home systems.")
        else:
            print("good evening, I'm friday, your organizational wizard. Whether it's coordinating your schedule, tracking important deadlines, or creating streamlined processes, I'm here to ensure your life runs smoothly and efficiently.")
            talk("good evening, I'm friday, your organizational wizard. Whether it's coordinating your schedule, tracking important deadlines, or creating streamlined processes, I'm here to ensure your life runs smoothly and efficiently.")
    
  #play song in the youtube  
    elif"play" in command:
        song = command.replace("playing","")
        talk("playing"+song)
        pywhatkit.playonyt(song)
  
  #show current time 
    elif 'time' in command:        
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk("current time is"+time)
   
  # show the ip address of the location  
    elif "location ip" in command:
        url: str="https://checkip.amazonaws.com"
        request=req.get(url)
        ip: str=request.text
        print("IP:",ip)
        talk(ip)
    
  #show result in the wikipedia  
    elif 'who is' in command:
        person = command.replace("who is","")
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    
    elif 'tell about' in command:
        person = command.replace("who is","")
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    
    elif 'tell me about' in command:
        person = command.replace("who is","")
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)        
    
   #chat with the ai assitence
    elif "date" in command:
        random_number=random.randint(1, 5)
        if random_number==1:    
            talk("sorry, i have a headache")
        elif random_number==2:
            talk( "I'm really sorry, but I've come down with something and I don't want to risk getting you sick. Can we reschedule our date?")
        elif random_number==3:
            talk("I had an unexpected work commitment come up that I can't get out of. I wish I could make it, but I'll have to raincheck.")
        elif random_number==4:
            talk("I hate to do this, but there's been a family emergency that I need to attend to immediately. Can we plan for another time?")
        else:
            talk( "I completely forgot that I already had plans for tonight that I can't change. I'm really sorry for the mix-up. Can we plan for another day?")
   
    # asking joke to ai assitence  
    elif "joke" in command:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())
    
    #tell todays date
    elif "today" in command:
        current_date = datetime.date.today()
        print(current_date)
        talk(current_date)
   
    #flip a coin
    elif "coin" in command:
        random_number = random.randint(0,1)
        if random_number==0:
            print("heads")
            talk("heads")
        else:
            print("tails")
            talk("tails")
    
    elif "search" in command:
        search = command.replace("searching","")
        talk("searching"+search)
        pywhatkit.search(search)
    
    elif "reminder" in command:
       # Extract the reminder message from the command
       reminder_message = command.replace("reminder", "").strip()
       
       # Set the reminder time (you can customize the time logic)
       reminder_time = (datetime.datetime.now()).strftime('%I:%M %p')
       
       # Print and speak the reminder message and time
       print(f"Reminder: {reminder_message} at {reminder_time}")
       talk(f"Reminder: {reminder_message} at {reminder_time}")

   
    # opens the notepad  
    elif "notepad" in command:
        application_name = "notepad.exe"  # Example: Opening Notepad on Windows

        try:
            # Use subprocess to open the application
            subprocess.Popen([application_name])
        except FileNotFoundError:
            print(f"Error: {application_name} not found or not in the system PATH.")        
        talk("opening"+application_name)    
     
    else:
        print("please say it again")
        talk("please say it again")
        
while True:
    run_friday()
