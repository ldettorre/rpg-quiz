from django.shortcuts import render
from .models import Spell

# Create your views here.

def index(request):
    spells = Spell.objects.all()
    context = {
        'spells': spells,
    }
    return render(request, 'spells/index.html', context)