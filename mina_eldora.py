import json
import os
import tloe100
import random
import math
BIOMAS = {
    "seca": {
        "minerios": {"carvao": 0.6, "ferro": 0.3, "ouro": 0.1},
        "saturacao": 0.7
    },
    "umida": {
        "minerios": {"carvao": 0.4, "ferro": 0.4, "ouro": 0.2},
        "saturacao": 0.6
    },
    "vulcanica": {
        "minerios": {"ferro": 0.4, "ouro": 0.4, "obsidiana": 0.2, "diamante":0.2, "rubi":0.1,},
        "saturacao": 0.5
    }
}

class mina_eldora:
	def __init__(self):
		self.camada = 0
		self.bioma = None
	def escolher_bioma(z):
		if z < 2:
			return "seca"
		elif z < 5:
			return "umida"
		else:
			return "vulcanica"
	def distancia_spawn(x, y):
		return math.sqrt(x*x + y*y)

