from flask_restful import Resource, reqparse

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
    return {'Players': players}

class Player(Resource):
  def get(self, player_id):
    for player in players:
      if player['player_id'] == player_id:
        return player
    return {'message': 'Player not found'}, 404

  def post(self, player_id):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('player_id')
    argumentos.add_argument('name')
    argumentos.add_argument('position')
    argumentos.add_argument('team')
    argumentos.add_argument('shirt')
    argumentos.add_argument('height')
    argumentos.add_argument('weight')
    argumentos.add_argument('gols')
    argumentos.add_argument('stars')

    dados = argumentos.parse_args()

    new_player = {
      'player_id': player_id,
      'name': dados['name'],
      'position': dados['position'],
      'team': dados['team'],
      'shirt': dados['shirt'],
      'height': dados['height'],
      'weight': dados['weight'],
      'gols': dados['gols'],
      'stars': dados['stars']
    }

    players.append(new_player)
    return new_player, 200

  def post(self, id):
    pass

  def delete(self, id):
    pass
