# Generated by Django 3.1.4 on 2021-04-09 02:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spells', '0002_spell_fantasy_universe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spell',
            old_name='comical_desc',
            new_name='comical_description',
        ),
    ]