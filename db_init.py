from pymongo import MongoClient
c = MongoClient("mongodb://localhost:27017")
db = c.MonPy

p = [
    {"nom": "Guerrier", "ATK": 15, "DEF": 10, "PV": 100},
    {"nom": "Mage", "ATK": 20, "DEF": 5, "PV": 80},
    {"nom": "Archer", "ATK": 18, "DEF": 7, "PV": 90},
    {"nom": "Voleur", "ATK": 22, "DEF": 8, "PV": 85},
    {"nom": "Paladin", "ATK": 14, "DEF": 12, "PV": 110},
    {"nom": "Sorcier", "ATK": 25, "DEF": 3, "PV": 70},
    {"nom": "Chevalier", "ATK": 17, "DEF": 15, "PV": 120},
    {"nom": "Moine", "ATK": 19, "DEF": 9, "PV": 95},
    {"nom": "Berserker", "ATK": 23, "DEF": 6, "PV": 105},
    {"nom": "Chasseur", "ATK": 16, "DEF": 11, "PV": 100}
]

e = [
    {"nom": "Gobelin", "ATK": 10, "DEF": 5, "PV": 50},
    {"nom": "Orc", "ATK": 20, "DEF": 8, "PV": 120},
    {"nom": "Dragon", "ATK": 35, "DEF": 20, "PV": 300},
    {"nom": "Zombie", "ATK": 12, "DEF": 6, "PV": 70},
    {"nom": "Troll", "ATK": 25, "DEF": 15, "PV": 200},
    {"nom": "Spectre", "ATK": 18, "DEF": 10, "PV": 100},
    {"nom": "Golem", "ATK": 30, "DEF": 25, "PV": 250},
    {"nom": "Vampire", "ATK": 22, "DEF": 12, "PV": 150},
    {"nom": "Loup-garou", "ATK": 28, "DEF": 18, "PV": 180},
    {"nom": "Squelette", "ATK": 15, "DEF": 7, "PV": 90}
]

s = [{"pseudo" : "OB", "points" : 99}]

prso = db.personnages_db.insert_many(p)
ennm = db.ennemis_db.insert_many(e)
sc = db.scoreboards_db.insert_many(s)

db.close