from django.shortcuts import render, get_object_or_404
from .models import Spell
from random import randint

# Create your views here.

def index(request):
    count = Spell.objects.count()
    randomspells = []
    while len(randomspells) < 2:
        x = randint(1, count)
        random_selection = get_object_or_404(Spell, id=x)
        if random_selection not in randomspells:
            randomspells.append(random_selection)
    context = {
        'randomspells': randomspells
    }
    
    return render(request, 'spells/index.html', context)