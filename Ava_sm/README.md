# Project Ava 

A lightweight social media simulation engine built from scratch in Python. Ava models core social media dynamics—including post creation, engagement tracking, score-based sorting algorithms, and database persistence—with a modern desktop graphical user interface.

## Key Features
* **Modular Architecture:** Clean separation of concerns across Data Models (`Post.py`), Business Logic/State Management (`Engine.py`), Relational Database Persistence (`Storage.py`), and UI Control (`main.py`).
* **Relational Database Persistence:** Built-in MySQL data persistence layer mapping live object instances to tables with automatic synchronization and deletion handling.
* **Interactive Desktop GUI:** Built using Python's native Tkinter framework featuring a scrollable trending feed table, form validation, and real-time engagement controls.
* **Algorithmic Engagement Scoring:** Automatically calculates dynamic ranking scores based on views, weighted likes, and dislike penalties with a zero-floor threshold.
* **Optimized $O(1)$ Lookups:** Utilizes Python hash-map dictionaries (`{id: post}`) instead of list-scanning arrays for instantaneous post retrieval, interaction, and deletion.

---

## 📂 Project Structure
```text
Ava_sm/
│
├── Engine.py           # Core business logic and dictionary state manager
├── Post.py             # Data blueprint and engagement score calculator
├── Storage.py          # MySQL database read/write persistence layer
└── main.py             # Tkinter desktop graphical user interface controller