from flask import Blueprint
from controllers.players_controller import index, new, create, edit, update, delete

players_routes = Blueprint('players_routes', __name__)


players_routes.route(''),(index)
players_routes.route(',/new')(new)
players_routes.route('', methods=['POST'])(create)
players_routes.route('/<id>/edit')(edit)
players_routes.route('/<id>', methods=["POST"])(update)
players_routes.route('/<id>/delete', methods=["POST"])(delete)