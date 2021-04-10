from django.shortcuts import render, get_object_or_404
from .models import Spell
from random import randint, random
import random

# Create your views here.

def index(request, spell_id=None):
    prev_selection = None
    if spell_id != None:
        prev_selection = get_object_or_404(Spell, id=spell_id)
    randomspells = []
  
    while len(randomspells) < 2:
        random_selection = random.choice(Spell.objects.all())
        print(random_selection)
        # random_selection = get_object_or_404(Spell, id=x)
        if random_selection not in randomspells:
            if random_selection != prev_selection:
                randomspells.append(random_selection)
    context = {
        'randomspells': randomspells,
        'prev_selection': prev_selection,
    }
    
    return render(request, 'spells/index.html', context)

