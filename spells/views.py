from django.shortcuts import render, get_object_or_404, redirect
from .models import Spell
from random import randint, random
import random

# Create your views here.

def index(request, spell_id=None):
    '''Check if a spell has been selected'''
    prev_selection = None
    previous_selections = []
    if spell_id != None:
        prev_selection = get_object_or_404(Spell, id=spell_id)
        # print(prev_selection.class_type, prev_selection.points)
        previous_selections = request.session.get('previous_selections', [])
        previous_selections.append(prev_selection.id)                                                    
        print(previous_selections)

        '''We create a previous selections list to avoid duplicates'''
        request.session['previous_selections'] = previous_selections
        # print(previous_selections)

        '''The name for our record of submissions is 'total' '''
        total = request.session.get('total', {})

        '''We update the class total by the number of points the user selection carries'''
        total[prev_selection.class_type] = total.get(prev_selection.class_type, 0) + prev_selection.points

        request.session['total'] = total

        ''' Check if any class_type has exceeded the point limit'''
        for t in total:
            if total[t] >= 20:
                result_message = "Congratulations! You're ready to discover your class type."
                class_type = t
                context = {
                    'result_message': result_message,
                    'class_type':class_type,
                }
                return render(request, 'spells/index.html', context)

    '''Check if there are enough spells left to generate 2 at random'''
    if len(previous_selections) <= len(Spell.objects.all())-2:

        '''Generate said random spells'''
        randomspells = []
        while len(randomspells) < 2:
            random_selection = random.choice(Spell.objects.all())
            print(random_selection.id)
            if random_selection.id not in previous_selections:
                if random_selection not in randomspells:
                    randomspells.append(random_selection)
    else:
        error_message = "You finished the quiz and still don't have a destiny?!"
        context = {
                    'error_message': error_message,
                }
        return render(request, 'spells/index.html', context)



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