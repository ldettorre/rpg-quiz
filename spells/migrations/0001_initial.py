# Generated by Django 3.1.4 on 2021-04-09 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('class_type', models.CharField(max_length=100)),
                ('level', models.IntegerField()),
                ('points', models.IntegerField()),
                ('comical_desc', models.TextField()),
            ],
        ),
    ]
