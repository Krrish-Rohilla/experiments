import mysql.connector
from Post import Post

def get_connection():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "kr",
        database = "data_ava"
    )

def save_posts(posts: dict):
    connection = get_connection()
    cursor = connection.cursor()

    if posts:
        format_strings = ','.join(['%s'] * len(posts))
        cursor.execute(f"DELETE FROM posts WHERE id NOT IN ({format_strings})", tuple(posts.keys()))
    else:
        cursor.execute("DELETE FROM posts")

    # Insert or update each post
    for post in posts.values():
        query = """
                    INSERT INTO posts (id, creator, title, views, likes, dislikes) 
                    VALUES (%s, %s, %s, %s, %s, %s)
                    ON DUPLICATE KEY UPDATE 
                        creator=VALUES(creator), 
                        title=VALUES(title), 
                        views=VALUES(views), 
                        likes=VALUES(likes), 
                        dislikes=VALUES(dislikes)
                """
        cursor.execute(query, (post.id, post.creator, post.title, post.views, post.likes, post.dislikes))

    connection.commit()
    cursor.close()
    connection.close()

def load_posts():
    posts: dict = {}
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS posts (
                id VARCHAR(50) PRIMARY KEY,
                creator VARCHAR(100),
                title VARCHAR(255),
                views INT,
                likes INT,
                dislikes INT
            )
        """)

    cursor.execute("Select id, creator, title, views, likes, dislikes FROM posts")
    rows = cursor.fetchall()

    for row in rows:
        post_id, creator, title, views, likes, dislikes = row
        posts[post_id] = Post(post_id, creator, title, views, likes, dislikes)

    cursor.close()
    connection.close()
    return posts
