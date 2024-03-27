# Generated by Django 4.2 on 2024-03-27 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0003_alter_semesteraddremove_semester_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semesterclass',
            name='semester',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='education.semester'),
        ),
    ]