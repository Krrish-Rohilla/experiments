import tkinter as tk
from tkinter import ttk, messagebox
from Engine import Engine

class AvaGUI:
    def __init__(self, root):
        self.root = root
        self.engine = Engine()
        self.root.title("AvaGUI - Version 2")
        self.root.geometry("750x550")
        self.root.minsize(650, 500)

        # Style
        style = ttk.Style()
        style.theme_use("clam")

        # --- TOP FRAME: CREATE POST ---
        create_frame = ttk.LabelFrame(self.root, text="Publish New Post", padding=15)
        create_frame.pack(fill="x", padx=15, pady=10)

        ttk.Label(create_frame, text="Post ID").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.id_entry = ttk.Entry(create_frame, width=12)
        self.id_entry.grid(row=0, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(create_frame, text="Creator Handle").grid(row=0, column=2, sticky="w", padx=5, pady=5)
        self.creator_entry = ttk.Entry(create_frame, width=18)
        self.creator_entry.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(create_frame, text="Post Title").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.title_entry = ttk.Entry(create_frame, width=35)
        self.title_entry.grid(row=1, column=1, columnspan=3, sticky="w", padx=5, pady=5)

        publish_btn = ttk.Button(create_frame, text="Publish Post", command=self.publish_post)
        publish_btn.grid(row=1, column=4, padx=10, pady=5)

        # --- CENTER FRAME: TRENDING FEED TABLE ---
        feed_frame = ttk.LabelFrame(self.root, text="Trending Feed", padding=10)
        feed_frame.pack(fill="both", expand=True, padx=15, pady=5)

        # Treeview
        columns = ("id", "creator", "title", "view", "likes", "dislikes", "score")
        self.tree = ttk.Treeview(feed_frame, columns=columns, show="headings", selectmode="browse")

        self.tree.heading("id", text="ID")
        self.tree.heading("creator", text="Creator")
        self.tree.heading("title", text="Post Title")
        self.tree.heading("view", text="View")
        self.tree.heading("likes", text="Likes")
        self.tree.heading("dislikes", text="Dislikes")
        self.tree.heading("score", text="Score")

        self.tree.column("id", width=60, anchor="center")
        self.tree.column("creator", width=110, anchor="w")
        self.tree.column("title", width=240, anchor="w")
        self.tree.column("view", width=60, anchor="center")
        self.tree.column("likes", width=60, anchor="center")
        self.tree.column("dislikes", width=60, anchor="center")
        self.tree.column("score", width=70, anchor="center")

        scrollbar = ttk.Scrollbar(feed_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)  # <--- Link tree to scrollbar

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # --- BOTTOM FRAME: INTERACTION & CONTROLS ---
        control_frame = ttk.Frame(root, padding=10)
        control_frame.pack(fill="x", padx=15, pady=5)

        ttk.Button(control_frame, text="👍 Like", command=lambda: self.interact_post("like")).pack(side="left", padx=5)
        ttk.Button(control_frame, text="👎 Dislike", command=lambda: self.interact_post("dislike")).pack(side="left", padx=5)
        ttk.Button(control_frame, text="👁️ View", command=lambda: self.interact_post("view")).pack(side="left", padx=5)

        ttk.Button(control_frame, text="🗑️ Delete Selected", command=self.delete_post).pack(side="right", padx=5)
        ttk.Button(control_frame, text="🔄 Refresh", command=self.refresh_feed).pack(side="left", padx=5)

        # Handle window close event
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.refresh_feed()

    def refresh_feed(self):
        # Clear existing rows
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Fetch sorted feed from Engine
        feed = self.engine.get_sorted_feed()
        for post in feed:
            self.tree.insert("", "end", values=(
                post.id,
                f"@{post.creator}",
                post.title,
                post.views,
                post.likes,
                post.dislikes,
                post.calculate_engagement()
            ))

    def publish_post(self):
        post_id = self.id_entry.get().strip()
        creator = self.creator_entry.get().strip()
        title = self.title_entry.get().strip()

        if not post_id or not creator or not title:
            messagebox.showerror("Error", "Please fill all fields")
            return

        success = self.engine.add_post(post_id, creator, title)
        if success:
            self.id_entry.delete(0, tk.END)
            self.creator_entry.delete(0, tk.END)
            self.title_entry.delete(0, tk.END)
            self.refresh_feed()
        else:
            messagebox.showerror("Error", f"Post ID {post_id} already exists!")

    def interact_post(self, action):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Required", "Please select a post!")
            return

        item = self.tree.item(selected_item)
        post_id = item["values"][0]

        success, message = self.engine.interact(post_id, action)
        if success: self.refresh_feed()
        else: messagebox.showerror("Error", message)

    def delete_post(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Required", "Please select a post to delete!")
            return

        item = self.tree.item(selected_item)
        post_id = item["values"][0]

        if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete {post_id}?"):
            success = self.engine.remove_post(post_id)
            if success: self.refresh_feed()
            else: messagebox.showerror("Error", "Post could not be deleted.")

    def on_closing(self):
        # Save state to MySQL database on exit
        self.engine.save_data()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AvaGUI(root)
    root.mainloop()
