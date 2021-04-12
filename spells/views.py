from django.shortcuts import render, get_object_or_404, redirect
from .models import Spell
from random import randint, random
import random

# Create your views here.

def index(request, spell_id=None):
    '''Generate two random spells for the user to choose from'''
    prev_selection = None
    if spell_id != None:
        prev_selection = get_object_or_404(Spell, id=spell_id)
        print(prev_selection.class_type, prev_selection.points)

        '''We called our record of submissions 'total' '''
        total = request.session.get('total', {})

        '''We update the class total by the number of points the user selection carries'''
        total[prev_selection.class_type] = total.get(prev_selection.class_type, 0) + prev_selection.points

        request.session['total'] = total
        print(total)
        

    randomspells = []
    while len(randomspells) < 2:
        random_selection = random.choice(Spell.objects.all())
        print(random_selection)
        if random_selection != prev_selection:
            if random_selection not in randomspells:
                randomspells.append(random_selection)
    context = {
        'randomspells': randomspells,
        'prev_selection': prev_selection,
    }
    
    return render(request, 'spells/index.html', context)


