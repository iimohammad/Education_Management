# Generated by Django 4.2 on 2024-04-11 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_initial'),
        ('dashboard_student', '0002_remove_studentdeletesemesterrequest_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unitselectionrequest',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.student'),
        ),
    ]
