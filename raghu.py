import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import pywhatkit
import pyjokes

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

listener = sr.Recognizer()

talk('Hi, I am Raghu. Your ATM assistant. How can I help you?')
print('Hi, I am Raghu. Your ATM assistant. How can I help you?')

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            order = listener.recognize_google(voice)
            order = order.lower()
            if 'raghu' in order:
                order = order.replace('raghu', '')
                print(order)
    except:
        pass
    return order

def run_raghu():
    command = take_command()
    print(command)

    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing ' + song)
        pywhatkit.playonyt(song)

    if 'time' in command or 'date' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'what is' in command:
        person = command.replace('what is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'what are' in command:
        person = command.replace('what are', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'relationship' in command:
        talk('Sorry, not interested')
    elif 'how are you' in command:
        talk('I am good, thank you')
    elif 'are you single' in command:
        talk('Yes, do you have anyone in mind?')
    elif 'are you a real person' in command:
        talk('Yes, more authentic than you are')
    elif 'are you married' in command:
        talk('No, I am single')
    elif 'are you there' in command:
        talk('I am always here for you')
    elif 'is' in command:
        talk('I dont know, you tell me')
    elif 'tell me about' in command:
        person = command.replace('tell me about', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'where are you from' in command:
        talk('I am from Chennai, India')
    elif 'where did you come from' in command:
        talk("I am from Chennai, India")
    elif 'who are you' in command:
        talk("I am a figment of my master's imagination, designed for you, and I will always be at your service")
    elif 'you' in command:
        talk("I am a figment of my master's imagination, designed for you, and I will always be at your service")
    elif 'what happens' in command:
        person = command.replace('what happens', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'how does' in command:
        person = command.replace('how does', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'how' in command:
        person = command.replace('how', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'bad guy' in command:
        talk('You are a bad guy')
    elif any(keyword in command for keyword in
             ['banking', 'transactions', 'deposit', 'withdraw', 'account', 'cash', 'balance', 'money']):
        talk('Please tap the ATM card above the keypad...')

        class Account:
            def __init__(self, balance=0):
                self.balance = balance

            def balance_status(self):
                self.balance = 50000
                return self.balance

        account01 = Account()
        count = 1

        talk('Connected to the bank server.')
        talk('Please enter your PIN')
        talk('The keypad is in the following order: Row 1 is 1, 2, 3. Row 2 is 4, 5, 6. Row 3 is 7, 8, 9, 0.')
        print('Please enter your PIN')
        id = int(input("\nEnter ATM PIN: "))

        while (id < 1000 or id > 9999) and count < 3:
            talk('Wrong PIN. Please re-enter')
            id = int(input("\nWrong PIN. Please Re-enter: "))
            count += 1

        if (count < 2):
            talk("Press 1 to View Balance, press 2 to Withdraw, press 3 for Deposit, press 4 for Exit")
            print("Press 1 to View Balance, press 2 to Withdraw, press 3 for Deposit, press 4 for Exit")
            talk('Please enter the number to confirm')
            selection = int(input("\nPlease Select An Option: "))

            if selection == 1:
                talk('Your account balance is displayed on the screen')
                print("Account Balance: ", account01.balance_status())
                talk("Thank you for banking with us! Good day.")

            elif selection == 2:
                talk('Enter the amount to withdraw')
                amt = float(input("\nEnter amount to withdraw: "))
                if amt < account01.balance_status():
                    amt = account01.balance_status() - amt
                talk('Your new updated balance is displayed on the screen')
                print("\nNew Updated Balance: " + str(amt))
                talk("Withdrawal Successful")
                talk("Thank you for banking with us! Good day.")
            else:
                talk("Sorry, you don't have enough balance to make this transaction")
                print("Account balance: ", str(account01.balance_status()))
                talk("Please make a deposit.")
        elif selection == 3:
            talk('Enter the amount to make the deposit')
            amt = float(input("\nEnter amount to deposit: "))
            amt = amt + account01.balance_status()
            talk('Your new balance is updated and displayed on the screen')
            print("\nNew Updated Balance: " + str(amt))
            talk("Thank you for banking with us! Good day.")
        elif selection == 4:
            talk("Your transaction is complete.")
            talk("Thank you for banking with us! Good day.")
        else:
            talk("Invalid input")

    else:
        talk("Please say the command again")

while True:
    run_raghu()
