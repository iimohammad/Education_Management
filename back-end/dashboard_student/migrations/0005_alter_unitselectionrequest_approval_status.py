# Generated by Django 4.2 on 2024-04-10 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_student', '0004_remove_emergencyremovalrequest_educational_assistant_explanation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unitselectionrequest',
            name='approval_status',
            field=models.CharField(choices=[('A', 'Registered'), ('R', 'Reserved'), ('C', 'NeedChange'), ('P', 'Approved'), ('D', 'DeletedSemester')], max_length=1),
        ),
    ]
