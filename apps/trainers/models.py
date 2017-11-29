from django.db import models
from django.contrib import admin


class Pokemon(models.Model):
	number = models.CharField(default='', max_length=50)
	name = models.CharField(max_length=50, default='')
	type_i = models.CharField(max_length=50, default='')
	type_ii = models.CharField(max_length=50, default='')
	ability_i = models.CharField(max_length=50, default='')
	ability_ii = models.CharField(max_length=50, default='')
	hidden_ability = models.CharField(max_length=50, default='')
	battle_sprite = models.URLField(default='')

	def __str__(self):
		return '{}. {}'. format(self, number, self.name)


class TrainerClass(models.Model):
	title = models.CharField(max_length=255)
	battle_sprite = models.URLField()
	overworld_sprite = models.URLField()

	def __str__(self):
		return self.title


class Trainer(models.Model):
	trainer_class = models.ForeignKey(TrainerClass, related_name='trainers')
	name = models.CharField(max_length=50)
	pokemon = models.ManyToManyField(Pokemon, related_name='trainers')

	def __str__(self):
		return '{} {}'.format(self.trainer_class.title, self.name)


class DoubleBattleClass(models.Model):
	title = models.CharField(max_length=255)
	battle_sprite = models.URLField()
	overworld_sprite = models.URLField()
	trainers = models.ManyToManyField(TrainerClass, related_name='double_battles')
