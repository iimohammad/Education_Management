# Generated by Django 4.2 on 2024-03-25 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prerequisite',
            name='course',
        ),
        migrations.RemoveField(
            model_name='prerequisite',
            name='prerequisite',
        ),
        migrations.RemoveField(
            model_name='department',
            name='number_of_students',
        ),
        migrations.AddField(
            model_name='course',
            name='corequisite',
            field=models.ManyToManyField(to='education.course'),
        ),
        migrations.AddField(
            model_name='course',
            name='prerequisite',
            field=models.ManyToManyField(to='education.course'),
        ),
        migrations.DeleteModel(
            name='Corequisite',
        ),
        migrations.DeleteModel(
            name='Prerequisite',
        ),
    ]