import os
from Post import Post

Data_file = "data/posts.csv"

def save_posts(posts):
    """Saves all posts from the engine dictionary into a CSV file."""

    os.makedirs(os.path.dirname(Data_file), exist_ok=True)
    with open(Data_file, "w", encoding="utf-8") as f:
        for post in posts.values():
            # ID, Creator, Title, Views, Likes, Dislikes
            line = f"{post.id},{post.creator},{post.title},{post.views},{post.likes},{post.dislikes}\n"
            f.write(line)

def load_posts():
    """Loads all posts from the engine dictionary into a CSV file."""
    posts = {}

    if not os.path.exists(Data_file):
        return posts

    with open(Data_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            parts = line.split(",")
            if len(parts) == 6:
                post_id, creator, title, views, likes, dislikes = parts
                # Reconstruct the Post object with its saved metrics
                post = Post(post_id, creator, title, int(views), int(likes), int(dislikes))
                posts[post_id] = post

    return posts