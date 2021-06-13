from django.shortcuts import render, get_object_or_404, redirect
from .models import Spell
from random import randint, random
import random

# Create your views here.

def quiz(request, spell_id=None):
    '''Save the users recent selection to a list and keep record of
    the seletions class type and points'''

    spells = Spell.objects.all().filter(is_included=True)
    previous_selections = request.session.get('previous_selections', [])
    if spell_id != None:
        if len(previous_selections) > 0 and previous_selections[-1] == spell_id:
            return redirect('reset')
        user_selection = get_object_or_404(Spell, id=spell_id)
        previous_selections.append(user_selection.id)
        print(previous_selections)                                           
        request.session['previous_selections'] = previous_selections

        class_scores = request.session.get('class_scores', {})
        for each_class in user_selection.class_type.all():
            class_scores[each_class.name] = class_scores.get(each_class.name, 0) + user_selection.points
            request.session['class_scores'] = class_scores  

        '''Check if any class_type has exceeded the point limit'''
        for c in class_scores:
            print(c,class_scores[c])
            if class_scores[c] >= 20:
                result_message = "You're ready to discover your class type!"
                class_type = c
                context = {
                    'result_message': result_message,
                    'class_type': class_type,
                }
                return render(request, 'spells/quiz.html', context)


    '''Pull 2 random spells if there are less selections 
    made than spells available'''
    if len(previous_selections) <= len(spells)-2:
        random_spells_list = []
        while len(random_spells_list) < 2:
            random_spell = random.choice(spells)
            if random_spell.id not in previous_selections:
                if random_spell not in random_spells_list:
                    random_spells_list.append(random_spell)
    else:
        no_result = "You finished the quiz and still don't have a destiny?!"
        return render(request, 'spells/quiz.html', {'no_result':no_result})

    context = {
        'random_spells_list': random_spells_list,
    }
    return render(request, 'spells/quiz.html', context)



def reset(request):
    '''Resets the session and removes existing quiz selections'''
    request.session.clear() 
    return redirect('quiz')


def result(request, class_type):
    '''This renders the result page html with relevant class details'''
    content_url = "https://www.dndbeyond.com/classes/"+class_type
    return render(request, 'spells/result.html',  {'class_type': class_type,'content_url': content_url})


