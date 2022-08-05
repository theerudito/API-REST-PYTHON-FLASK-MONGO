# CREATE THE CLASS
class Characters:
  def __init__(self, name, age, clan, pic):
    self.name = name
    self.age = age
    self.clan = clan
    self.pic = pic

  # CREATE COLLECTION
  def DBCollection(self):
    return {
      'name': self.name,
      'age': self.age,
      'clan': self.clan,
      "pic": self.pic
    }  