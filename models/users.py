from db.db import sql

def create_user(first_name, last_name, email):
  sql('INSERT INTO users(first_name, last_name, email) VALUES(%s, %s, %s) RETURNING *', [first_name, last_name, email])
