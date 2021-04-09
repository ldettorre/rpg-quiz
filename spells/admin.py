from django.contrib import admin
from .models import Spell
# Register your models here.

class SpellAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'class_type', 'points')


admin.site.register(Spell, SpellAdmin)