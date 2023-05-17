from db.db import sql

def all_players():
    return sql('SELECT * FROM players')

def create_player(image_url, name, ppg, rpg, apg, championship):
    sql('INSERT INTO players(image_url, name, ppg, rpg, apg, championship) VALUES(%s, %s, %s, %s, %s, %s) RETURNING *', [image_url, name, ppg, rpg, apg, championship])

def get_player(id):
    players = sql("SELECT * FROM players WHERE id = %s", [id])
    return players[0]

def update_player(image_url, name, ppg, rpg, apg, championship, id):
    sql('UPDATE players SET image_url=%s, name=%s, ppg=%s, rpg=%s, apg=%s, championship=%s WHERE id=%s RETURNING *', [image_url, name, ppg, rpg, apg, championship, id])

def add_comment_player(id, comment):
    sql('INSERT INTO comment(player_id, comment) VALUES(%s, %s) RETURNING *', [id, comment])

def get_comments(player_id):
    comments = sql("SELECT * FROM comment WHERE player_id = %s", [player_id])
    return comments


def delete_player(id):
    sql('DELETE FROM players WHERE id=%s RETURNING *', [id])

def get_all_comments():
    comments = sql("SELECT * FROM comment")
    return comments
