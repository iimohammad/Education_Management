# Generated by Django 4.2 on 2024-04-11 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_initial'),
        ('dashboard_student', '0004_alter_unitselectionrequest_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unitselectionrequest',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.student'),
        ),
    ]
