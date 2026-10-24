import shutil
class Post:
    def __init__(self, id, creator, title, views = 0, likes = 0, dislikes = 0):
        self.id = id
        self.creator = creator
        self.title = title
        self.views = views
        self.likes = likes
        self.dislikes = dislikes

    def __str__(self):
        # Get current terminal width (default to 80 columns if it fails or runs in a non-terminal environment)
        terminal_width = shutil.get_terminal_size((80, 24)).columns

        left_side = f"[{self.id}] @{self.creator}: '{self.title}'"
        right_side = f"Views: {self.views} | Likes: {self.likes} | Dislikes: {self.dislikes} | Score: {self.calculate_engagement()}"

        padding_length = terminal_width - len(left_side) - len(right_side)
        if padding_length < 3: padding_length = 3

        return left_side + (" " * padding_length) + right_side

    def calculate_engagement(self):
        score = self.views + (self.likes * 5) - (self.dislikes * 3)
        return max(0, score)  # Ensures score doesn't drop below zero
