from Engine import Engine
import time

def main():
    engine = Engine()

    print("===============================")
    print("     WELCOME TO PROJECT AVA    ")
    print("===============================")

    while True:
        print("\n--- SM MENU ---")
        print("1. Publish New Post")
        print("2. View Feed (Sorted by Score)")
        print("3. Interact with Post (Like/Dislike/View)")
        print("4. Delete Post")
        print("5. Exit")

        choice = input("Enter your choice: ").strip().lower()
        if choice.isdigit():
            choice = int(choice)

        if choice == 1:
            post_id = input("Enter Post ID (e.g., v1): ").strip()
            creator = input("Enter Creator Handle: ").strip()
            title = input("Enter Video/Post Title: ").strip()

            success: bool = engine.add_post(post_id, creator, title)
            if success:
                print("-> Post published successfully!")
            else:
                print("-> Error: Post ID already exists!")

        elif choice == 2:
            feed = engine.get_sorted_feed()
            if not feed:
                print("-> No posts available yet.")
            else:
                print("\n--- TRENDING FEED ---")
                for post in feed:
                    print(post)  # Automatically calls __str__ method!

        elif choice == 3:
            post_id = input("Enter Post ID to interact with: ").strip()
            print("Actions available: view, like, dislike")
            action = input("Enter action: ").strip().lower()

            result = engine.interact(post_id, action)

            success, message = result
            print(f"-> {message}")
            if success:
                print("-> action done successfully!")

        elif choice == 4:
            post_id = input("Enter Post ID to delete!: ").strip()
            success = engine.remove_post(post_id)
            if success:
                print("-> Post deleted successfully!")
            else:
                print("-> Error: Post ID does not exist!")

        elif choice == 5 or choice == "exit":
            engine.save_data()
            print("Exiting... SM shutting down!")
            time.sleep(1)
            print("Thank you for your time!")
            break

        else:
            time.sleep(1)
            print("-> Error: Invalid choice!")

if __name__ == "__main__":
    main()
