from flask_restful import Resource, reqparse
from models.player import PlayerModel
from factory import Factory

players = [
  {
    'player_id': '1',
    'name': 'Neymar',
    'position': 'ponta-direita',
    'team': 'Paris Saint-Germain',
    'shirt': 10,
    'height': 1.80,
    'weight': 68,
    'gols': 1342,
    'stars': 4.7
  },
  {
    'player_id': '2',
    'name': 'Cristiano Ronaldo',
    'position': 'central',
    'team': 'Manchster United',
    'shirt': 7,
    'height': 1.92,
    'weight': 83,
    'gols': 1981,
    'stars': 4.9
  },
  {
    'player_id': '3',
    'name': 'Lionel Messi',
    'position': 'ponta-esquerda',
    'team': 'Paris Saint-Germain',
    'shirt': 30,
    'height': 1.67,
    'weight': 65,
    'gols': 1231,
    'stars': 4.2
  },
]

class Players(Resource):
  def get(self): 
    players = Factory().select("SELECT * FROM test;") 
    return {'Players': players}

class Player(Resource):
  arguments = reqparse.RequestParser()
  arguments.add_argument('name')
  arguments.add_argument('position')
  arguments.add_argument('team')
  arguments.add_argument('shirt')
  arguments.add_argument('height')
  arguments.add_argument('weight')
  arguments.add_argument('gols')
  arguments.add_argument('stars')

  def find_player(player_id):
    for player in players:
      if player['player_id'] == player_id:
        return player
    return None

  def get(self, player_id):
    player = Player.find_player(player_id)
    if player:
      return player
    return {'message': 'Player not found'}, 404

  def post(self, player_id):

    dates = Player.arguments.parse_args()
    player_object = PlayerModel(player_id, **dates)
    new_player = player_object.json()
    players.append(new_player)
    return new_player, 200

  def put(self, player_id):

    dates = Player.arguments.parse_args()
    player_object = PlayerModel(player_id, **dates)
    new_player = player_object.json()
    player = Player.find_player(player_id)
    if player:
      player.update(new_player)
      return new_player, 200
    players.append(new_player)
    return new_player, 201

  def delete(self, player_id):
    global players
    players = [player for player in players if player['player_id'] != player_id]
    return {'message': 'Player deleted'}
