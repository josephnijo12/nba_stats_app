from flask import render_template, request, redirect
from models.players import all_players, get_player, create_player, update_player, delete_player, add_comment_player, get_comments, get_all_comments
from services.session_info import current_user


def index():
    players = all_players()
    return render_template('players/index.html', players=players, current_user=current_user)


def new():
    return render_template('players/new.html')


def create():
    image_url = request.form.get('image_url')
    name = request.form.get('name')
    ppg = request.form.get('ppg')
    rpg = request.form.get('rpg')
    apg = request.form.get('apg')
    championship = request.form.get('championship')
    create_player(image_url, name, ppg, rpg, apg, championship)
    return redirect('/')


def edit(id):
    player = get_player(id)
    return render_template('players/edit.html', player=player)


def update(id):
    image_url = request.form.get('image_url')
    name = request.form.get('name')
    ppg = request.form.get('ppg')
    rpg = request.form.get('rpg')
    apg = request.form.get('apg')
    championship = request.form.get('championship')
    update_player(image_url, name, ppg, rpg, apg, championship, id)
    return redirect('/')


def comment(id):
    player = get_player(id)
    comments = get_comments(id)
    return render_template('players/comment.html', player=player, comments=comments)


def add_comment(id):
    comment = request.form.get('comment', '')
    add_comment_player(id, comment)
    return redirect('/')


def delete(id):
    delete_player(id)
    return redirect('/')

def display_comments():
    all_comments = get_all_comments()

    player_comment_map = {}

    for item in all_comments:
        player_id = item['player_id']
        comment = item['comment']
        player_name = get_player(player_id)['name']

        if str(player_name) not in player_comment_map:
            player_comment_map[str(player_name)] = []
        
        player_comment_map[str(player_name)].append(comment)
    return render_template('players/comments_list.html',player_comment_map=player_comment_map)