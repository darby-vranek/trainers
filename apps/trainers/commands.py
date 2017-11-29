from .models import *
from .pokedex import x
from collections import namedtuple


trainers_tuple = namedtuple('trainers_tuple', 'name pokemon')


def parse_file():
	entries = x.split('\n')
	for i in range(1, len(entries)):
		columns = entries[i].split(',')
		url = 'https://img.pokemondb.net/sprites/black-white/anim/normal/{}.gif'.format(columns[2].lower())
		Pokemon.objects.create(
			number=columns[1],
			name=columns[2],
			type_i=columns[10],
			type_ii=columns[11],
			ability_i =columns[12],
			ability_ii=columns[13],
			hidden_ability=columns[14],
			battle_sprite=url
		)


def pokefind(name):
	return Pokemon.objects.get(name=name)



def add_trainers(trainer_class, trainers):
	for trainer in trainers:
		t = Trainer.objects.create(
			trainer_class=trainer_class,
			name=trainer.name
		)
		t.save()
		for pokemon in trainer.pokemon:
			t.pokemon.add(pokefind(pokemon))
			t.save()


def new_double(title, t1, t2, battle):
	trainer1 = TrainerClass.objects.get(title=t1)
	trainer2 = TrainerClass.objects.get(title=t2)
	double = DoubleBattleClass.objects.create(title=title, battle_sprite=battle, overworld_sprite='')
	double.trainers.add(trainer1)
	double.trainers.add(trainer2)
