# Generated by Django 4.2 on 2024-03-27 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_rename_course_studentcourse_semester_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semesteraddremove',
            name='semester',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='addremove', to='education.semester'),
        ),
        migrations.AlterField(
            model_name='semesterclass',
            name='semester',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='unit_class', to='education.semester'),
        ),
        migrations.AlterField(
            model_name='semesteremergency',
            name='semester',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='emergency', to='education.semester'),
        ),
        migrations.AlterField(
            model_name='semesterexam',
            name='semester',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='exam', to='education.semester'),
        ),
        migrations.AlterField(
            model_name='semesterunitselection',
            name='semester',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='unit_selection', to='education.semester'),
        ),
    ]