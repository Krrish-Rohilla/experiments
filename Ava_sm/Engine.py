import Post as Model
from Storage import *

class Engine:
    def __init__(self):
        self.posts = load_posts()

    def save_data(self):
        """Triggers writing the current memory state to disk."""
        save_posts(self.posts)

    def add_post(self, id, creator, title):
        if id in self.posts:
            return False

        self.posts[id] = Model.Post(id, creator, title)
        return True

    def remove_post(self, id):
        if id in self.posts:
            self.posts.pop(id)
            return True
        return False

    def interact(self, id, action):
        if id not in self.posts:
            return False, "Post not found!"

        if action == "view":
            self.posts[id].views += 1
        elif action == "like":
            self.posts[id].likes += 1
        elif action == "dislike":
            self.posts[id].dislikes += 1
        else:
            return False, "Invalid action!"

        return True, f"Successfully updated post {id}!"

    def get_sorted_feed(self):
        """Returns all posts sorted by highest engagement score."""
        # Convert dictionary values to a list, then sort by engagement
        return sorted(self.posts.values(), key=lambda p: p.calculate_engagement(), reverse=True)
