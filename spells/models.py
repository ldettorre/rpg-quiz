from django.db import models


class ClassType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Spell(models.Model):
    name = models.CharField(max_length=100)
    class_type = models.ManyToManyField(ClassType)
    level = models.IntegerField()
    points = models.IntegerField()
    comical_description = models.TextField()
    fantasy_universe = models.CharField(max_length=100, default = "Example: D&D")
    
    def __str__(self):
        return self.name