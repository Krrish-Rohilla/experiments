import time
import os


def start_os():
    # Clear screen and show a fake boot-up sequence
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Initializing hardware...")
    time.sleep(1)
    print("Loading kernel...")
    time.sleep(1)
    print("Welcome to MyPythonOS v1.0!\n")

    # Main OS loop (the shell)
    while True:
        # Get user input like a real terminal
        command = input("MyOS> ").strip().lower()

        if command == "help":
            print("Available commands:")
            print("  hello  - Greets you")
            print("  time   - Shows the current time")
            print("  clear  - Clears the screen")
            print("  exit   - Shuts down the OS")
        elif command == "hello":
            print("Hello there! Thanks for using my custom OS.")
        elif command == "time":
            current_time = time.strftime("%H:%M:%S")
            print(f"Current System Time: {current_time}")
        elif command == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')
        elif command == "exit":
            print("Shutting down... Goodbye!")
            break
        else:
            print(f"Unknown command: '{command}'. Type 'help' for a list of commands.")


if __name__ == "__main__":
    start_os()