# Project Ava 

A lightweight, terminal-based social media simulation engine built from scratch in Python. Ava models core social media dynamics—including post creation, engagement tracking, score-based sorting algorithms, and disk persistence—entirely through an optimized command-line interface.

## Key Features
* **Modular Architecture:** Clean separation of concerns across Data Models (`Post.py`), Business Logic/State Management (`Engine.py`), Disk Persistence (`Storage.py`), and UI Control (`main.py`).
* **Optimized $O(1)$ Lookups:** Utilizes Python hash-map dictionaries (`{id: post}`) instead of list-scanning arrays for instantaneous post retrieval, interaction, and deletion.
* **Custom Disk Serialization:** Built-in plain-text CSV data persistence layer mapping raw text records back to live object instances without external database dependencies.
* **Dynamic Terminal Rendering:** Leverages Python's standard `shutil` library to dynamically detect terminal width and push real-time engagement metrics to the far right edge of the window.
* **Algorithmic Engagement Scoring:** Automatically calculates dynamic ranking scores based on views, weighted likes, and dislike penalties with a zero-floor threshold.

---

## 📂 Project Structure
```text
Ava_sm/
│
├── data/
│   └── posts.csv       # Flat-file database for persistent storage
├── Engine.py           # Core business logic and dictionary state manager
├── Post.py             # Data blueprint and engagement score calculator
├── Storage.py          # CSV read/write serialization layer
└── main.py             # Terminal menu loop and user interface controller