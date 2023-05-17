from flask import Blueprint
from controllers.players_controller import index, new, create, edit, update, add_comment, delete, comment, display_comments

players_routes = Blueprint('players_routes', __name__)


players_routes.route('')(index)
players_routes.route('/new')(new)
players_routes.route('', methods=['POST'])(create)
players_routes.route('/<id>/edit')(edit)
players_routes.route('/<id>', methods=["POST"])(update)
players_routes.route('/<id>/comment')(comment)
players_routes.route('/<id>/comment', methods=["POST"])(add_comment)
players_routes.route('/comments')(display_comments)
players_routes.route('/<id>/delete', methods=["POST"])(delete)
