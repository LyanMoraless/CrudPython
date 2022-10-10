class PlayerModel:
  def __init__(self, player_id, name, position, team, shirt, height, weight, gols, stars):
    self.player_id = player_id
    self.name = name
    self.position = position
    self.team = team
    self.shirt = shirt
    self.height = height
    self.weight = weight
    self.gols = gols
    self.stars = stars

  def json(self):
    return{
      'player_id': self.player_id,
      'name': self.name,
      'position': self.position,
      'team': self.team,
      'shirt': self.shirt,
      'height': self.height,
      'weight': self.weight,
      'gols': self.gols,
      'stars': self.stars,
    }