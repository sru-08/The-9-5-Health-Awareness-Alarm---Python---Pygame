from pygame import mixer  # pygame is used for building small games; mixer for playing audio files
import time

def musicplay(music, volume):
    """Play a music file at the specified volume and await stop commands."""
    mixer.init()
    mixer.music.load(music)
    mixer.music.set_volume(volume)
    mixer.music.play()
    while True:
        a = input("Enter 'yes' to stop the music or 'q' to exit the program: ").lower()
        if a == 'yes':
            mixer.music.stop()
            return False
        elif a == 'q':
            mixer.music.stop()
            return True
        print("Invalid input! Try again.")

def logs(msg, filename):
    """Log a specified message with a timestamp to a log file."""
    with open(f"{filename}.txt", "a") as file:
        file.write(f"{msg} at {time.ctime()}\n")
    print("Log saved!")

def disp(log):
    """Display the content of a log file if it exists."""
    try:
        with open(f"{log}.txt", 'r') as file:
            print(f"\nYour {log}:")
            print(file.read())
    except FileNotFoundError:
        print(f"\nSorry, {log} does not exist.")

while True:
    user = input('(Press "q" to exit)\nEnter your name: ')
    if user.lower() == 'q':
        print("\nThanks for using :)")
        break

    while True:
        print(f"\nWELCOME {user}\nWhat would you like to do?")
        try:
            menu_choice = int(input('\n1. Start the Alarm\n2. View Logs\n3. Exit\nEnter your choice: '))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if menu_choice == 1:
            current_hour = int(time.strftime('%H'))
            if 9 <= current_hour <= 23:
                try:
                    drink_interval = float(input("Water reminder interval (minutes): ")) * 60
                    eye_interval = float(input("Eye relaxation interval (minutes): ")) * 60
                    stretch_interval = float(input("Stretching interval (minutes): ")) * 60
                    volume = float(input("Alarm volume (0.0 to 1.0): "))
                except ValueError:
                    print("Invalid input, please enter numbers only.")
                    continue

                print("\nYou can continue with your work now...")

                last_drink = last_eye = last_stretch = time.time()

                while True:
                    current_hour = int(time.strftime('%H'))
                    if current_hour > 23 or current_hour < 9:
                        print("Office time over!!")
                        break

                    if time.time() - last_drink >= drink_interval:
                        print(f"Time for a water break, {user} (250ml)!")
                        if musicplay('alarm.mp3', volume):
                            break
                        logs("Took a water break", f"{user}_drinking_log")
                        last_drink = time.time()

                    if time.time() - last_eye >= eye_interval:
                        print(f"Take a break to relax your eyes, {user}.")
                        if musicplay('alarm.mp3', volume):
                            break
                        logs("Relaxed eyes", f"{user}_eye_log")
                        last_eye = time.time()

                    if time.time() - last_stretch >= stretch_interval:
                        print(f"Take a 5-minute stretch break, {user}.")
                        if musicplay('alarm.mp3', volume):
                            break
                        logs("Took a stretch break", f"{user}_stretch_log")
                        last_stretch = time.time()

            else:
                print('It is not your office time.')

        elif menu_choice == 2:
            while True:
                print("\nAvailable Logs:")
                try:
                    log_choice = int(input('1. Drinking Log\n2. Eye Log\n3. Stretch Log\n4. Back\nEnter your choice: '))
                except ValueError:
                    print("Please enter a valid number.")
                    continue

                if log_choice == 1:
                    disp(f"{user}_drinking_log")
                elif log_choice == 2:
                    disp(f"{user}_eye_log")
                elif log_choice == 3:
                    disp(f"{user}_stretch_log")
                elif log_choice == 4:
                    break
                else:
                    print("Invalid choice, please try again.")

        elif menu_choice == 3:
            print("\nSee you soon! :)")
            break

        else:
            print("Invalid choice! Please select from the menu.")
