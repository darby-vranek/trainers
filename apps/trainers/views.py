from django.shortcuts import render, HttpResponse
from .models import *

def index(request):
	return render(request, 'trainers/index.html', context={'trainers': TrainerClass.objects.all() })


def doubles(request):
	return render(request, 'trainers/doubles.html', context={'doubles':DoubleBattleClass.objects.all() })


def show_trainer(request, id):
	return render(request, 'trainers/trainer.html', context={'trainer_class': TrainerClass.objects.get(id=id) })
