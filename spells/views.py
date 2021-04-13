from django.shortcuts import render, get_object_or_404, redirect
from .models import Spell
from random import randint, random
import random

# Create your views here.

def index(request, spell_id=None):
    '''Check if a spell has been selected'''
    prev_selection = None
    if spell_id != None:
        prev_selection = get_object_or_404(Spell, id=spell_id)
        # print(prev_selection.class_type, prev_selection.points)

        '''The name for our record of submissions is 'total' '''
        total = request.session.get('total', {})

        '''We update the class total by the number of points the user selection carries'''
        total[prev_selection.class_type] = total.get(prev_selection.class_type, 0) + prev_selection.points

        request.session['total'] = total

        ''' Check if any class_type has exceeded the point limit'''
        for t in total:
            if total[t] >= 25:
                # return redirect('result')
                result_message = "Congratulations! You're ready to discover your class type."
                class_type = t
                context = {
                    'result_message': result_message,
                    'class_type':class_type,
                }
                return render(request, 'spells/index.html', context)

        
    '''Generate two random spells for the user to choose from'''
    randomspells = []
    while len(randomspells) < 2:
        random_selection = random.choice(Spell.objects.all())
        if random_selection != prev_selection:
            if random_selection not in randomspells:
                randomspells.append(random_selection)
    context = {
        'randomspells': randomspells,
        'prev_selection': prev_selection,
    }
    
    return render(request, 'spells/index.html', context)



def reset(request):
    '''Resets the session and removes existing quiz selections'''
    total = request.session
    total.clear()
    return redirect('index')


def result(request, class_type):
    '''This renders the result page html with relevant class details'''
    context = {
        'class_type': class_type,
    }
    return render(request, 'spells/result.html', context)