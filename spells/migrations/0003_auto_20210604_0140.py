# Generated by Django 3.1.4 on 2021-06-04 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spells', '0002_spell_ability_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spell',
            old_name='comical_description',
            new_name='description',
        ),
        migrations.AddField(
            model_name='spell',
            name='is_included',
            field=models.BooleanField(default=False),
        ),
    ]