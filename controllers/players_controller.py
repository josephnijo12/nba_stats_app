from flask import render_template, request, redirect
from models.players import all_players, get_player, create_player, update_player, delete_player 
from services.session_info import current_user


def index():
    players = all_players() 
    return render_template('players/index.html', players=players, current_user=current_user)

def new():
    return render_template('players/new.html')

def create():
    image_url = request.form.get('image_url')
    name = request.form.get('name')
    PPG = request.form.get('PPG')
    RPG = request.form.get('RPG')
    APG = request.form.get('APG')
    championship = request.form.get('championship')
    create_players(image_url, name, RPG, PPG, APG, championship)
    return redirect('/')

def edit(id):
    player = get_player(id)
    return render_template('players/edit.html', player=player)

def update(id):
    name = request.form.get('name')
    image_url = request.form.get('image_url')
    RPG = request.form.get('RPG')
    PPG = request.form.get('PPG')
    championship = request.form.get('championship')
    APG = request.form.get('APG')
    update_player (image_url, name, RPG, PPG, championship, APG)
    return redirect('/')

def delete(id):
    delete_player(id)
    return redirect('/')