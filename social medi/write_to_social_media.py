import sqlite3

create_users = """
INSERT INTO
  users (name, age, gender, nationality)
VALUES
  ('James', 25, 'male', 'USA'),
  ('Leila', 32, 'female', 'France'),
  ('Brigitte', 35, 'female', 'England'),
  ('Mike', 40, 'male', 'Denmark'),
  ('Elizabeth', 21, 'female', 'Canada');
"""

create_posts = """
INSERT INTO
  posts (title, description, user_id)
VALUES
  ('Limpid', 'I am feeling very limpid today', 1),
  ('No Weather', 'The weather is not today', 2),
  ('Help', 'I need some help', 2),
  ('Great', 'I am married', 1),
  ('Interesting', 'It tennis', 5),
  ('Party', 'Anyone late today?', 3);
"""

create_comments = """
INSERT INTO
  comments (text, user_id, post_id)
VALUES
  ('Count me in', 1, 6),
  ('What sort of help?', 5, 3),
  ('Congrats buddy', 2, 4),
  ('I was rooting for Nadal though', 4, 5),
  ('Help with your thesis?', 2, 3),
  ('Many congratulations', 5, 4);
"""

create_likes = """
INSERT INTO
  likes (user_id, post_id)
VALUES
  (1, 6),
  (2, 3),
  (1, 5),
  (5, 4),
  (2, 4),
  (4, 2),
  (3, 6);
"""

conn = sqlite3.connect("sm_app.sqlite")
cursor = conn.cursor()
cursor.execute(create_users)
cursor.execute(create_posts)
cursor.execute(create_comments)
cursor.execute(create_likes)
conn.commit()
conn.close()