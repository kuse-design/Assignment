menu =("""
      print(" main_memu")
      print(" 1 phonebook")
      print(" 2 Messages")
      print(" 3 Chat")
      print(" 4 Call register")
      print(" 5 Tones")
      print(" 6 Settings")
      print(" 7 Call divert")
      print(" 8 Games")
      print(" 9 Calculator")
      print(" 10 Reminders")
      print(" 11 Clock")
      print(" 12 profiles")
      print(" 13 SIM service")
      print(" 0 Exit")
      print("................................")
   """) 
menu = input("Enter any number from 1 - 13 : ")
match menu:

    case "1": 
        print("phonebook")
        print(" 1 Search")
        print(" 2 Service Nos.")
        print(" 3 Add name")
        print(" 4 Erase")
        print(" 5 Edit")
        print(" 6 Assign tone")
        print(" 7 Send b'card'")
        print(" 8 Options")
        print(" 9 Speed dials")
        print(" 10 Voice tags")
        Options = input("Enter any number 8 for more : ")
        match(Options):

            case "8":
                print(" 1 Type")
                print(" 2 Memory status")
    
    case "2":
        print("Messages")
        print(" 1 Write messages")
        print(" 2 Inbox")
        print(" 3 Outbox")
        print(" 4 Picture messages")
        print(" 5 Templates")
        print(" 6 Smileys")
        print(" 7 Message settings")
        print(" 8 Info service")
        print(" 9 Voice mailbox number")
        print(" 10 Service command editor")
        Message_settings = input("Enter any number 7 for more : ")
        match(Message_settings):

            case "7":
                print(" 1 Set")
                print(" 2 Common")
                Set = input("Enter any number 1 for more : ")
                match(Set):

                    case "1":
                        print(" 1 Message centre number")
                        print(" 2 Message sent as")
                        print(" 3 Message validity")
                    case "2":
                        print(" 1 Delivery report")
                        print(" 2 Reply via same centre")
                        print(" 3 Character support")

    case "3":
        print("Chat")

    case "4":
        print("Call register")
        print(" 1 Missed calls")
        print(" 2 Receive calls")
        print(" 3 Dialed number")
        print(" 4 Erase recent call lists")
        print(" 5 Show call duration")
        print(" 6 Show call costs")
        print(" 7 Call cost settings")
        print(" 8 Prepaid credit")
        call_register = input("Enter any number 5,6,7 for more : ")
        match(call_register):

            case "5":
                print(" 1 Last call duration")
                print(" 2 All calls duration")
                print(" 3 Received calls duration")
                print(" 4 Dialled calls duration")
                print(" 5 Clear timers")
            case "6":
                print(" 1 Last call cost")
                print(" 2 All calls cost")
                print(" 3 Clear counters")
            case "7":
                print(" 1 Call cost limit")
                print(" 2 Show costs in")

    case "5":
        print(" Tones ")
        print(" 1 Ringing tone")
        print(" 2 Ringing volume")
        print(" 3 Incoming call alert")
        print(" 4 Composer")
        print(" 5 Message alert tone")
        print(" 6 Keypad tones")
        print(" 7 Warning and game tones")
        print(" 8 Vibrating alert")
        print(" 9 Screen saver")

    case "6":
        print(" Settings")
        print(" 1 Call settings")
        print(" 2 Phone settings")
        print(" 3 Security settings")
        print(" 4 Restore factory settings")
        Settings = input("Enter any number 1,2,3 for more : ")
        match(Settings):
        
            case "1":
                print(" 1 Automatic redial")
                print(" 2 Speed dialling")
                print(" 3 Call waiting options")
                print(" 4 Own number sending")
                print(" 5 Phone line in use")
                print(" 6 Automatic answer")
            case "2":
                print(" 1 Language")
                print(" 2 Cell info display")
                print(" 3 Welcome note")
                print(" 4 Network selection")
                print(" 5 Light")
                print(" 6 Confirm SIM service actions")
            case "3":
                print(" 1 PIN code request")
                print(" 2 Call barring service")
                print(" 3 Fixed dialling")
                print(" 4 Closed user group")
                print(" 5 Phone security")
                print(" 6 Change access codes")
            case "4":
                print(" Restore factory settings")

    case "7":
        print("Call divert")

    case "8":
        print("Games")

    case "9":
        print("Calculator")

    case "10":
        print("Remainders")

    case "11":
        print(" 1 Alarm clock")
        print(" 2 Clock settings")
        print(" 3 Date setting")
        print(" 4 Stopwatch")
        print(" 5 Countdown timer")
        print(" 6 Auto update of date and time")

    case "12":
        print("Profiles")

    case "13":
        print("SIM services")
        
                
































































        
