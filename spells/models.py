from django.db import models


class ClassType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Spell(models.Model):
    ABILITY_CHOICES =[("Spell", "Spell"), ("Feature", "Feature")]
    name = models.CharField(max_length=100)
    class_type = models.ManyToManyField(ClassType)
    level = models.IntegerField()
    points = models.IntegerField()
    description = models.TextField()
    fantasy_universe = models.CharField(max_length=100, default = "Example: D&D")
    ability_type = models.CharField(max_length=100, blank=True, choices = ABILITY_CHOICES)
    is_included = models.BooleanField(default=False)
    


    def get_classes(self):
        ''' Below pulls the name from a ManyToMany model in order to show it in django's list display'''
        return "\n".join([c.name for c in self.class_type.all()])

    def __str__(self):
        return self.name
    
