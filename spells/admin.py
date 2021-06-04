from django.contrib import admin
from .models import Spell, ClassType
# Register your models here.


class ClassTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


class SpellAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'points', 'is_included')
    list_editable = ('is_included',)


admin.site.register(Spell, SpellAdmin)
admin.site.register(ClassType, ClassTypeAdmin)