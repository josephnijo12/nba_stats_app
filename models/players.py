from db.db import sql

def all_players():
    return sql('SELECT * FROM players')

def create_player(name, PPG, RPG, APG, championships, image_url):
    sql('INSERT INTO players(name, PPG, RPG, APG, championships, image_url) VALUES(%s, %s, %s, %s, %s, %s) RETURNING *', [name, PPG, RPG, APG, championships, image_url])

def get_player(id):
    players = sql("SELECT * FROM players WHERE id = %s", [id])
    return players[0]

def update_player(name, PPG, RPG, APG, championships, image_url):
    sql('UPDATE players SET name=%s, image_url=%s, PPG=%s, RPG=%s, APG=%s, championships=%s WHERE id=%s RETURNING *', [name, PPG, RPG, APG, championships, image_url, id])

def delete_player (id):
    sql('DELETE FROM player WHERE id=%s RETURNING *', [id])