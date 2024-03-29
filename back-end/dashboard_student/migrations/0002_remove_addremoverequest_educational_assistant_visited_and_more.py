# Generated by Django 5.0.2 on 2024-03-29 17:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addremoverequest',
            name='educational_assistant_visited',
        ),
        migrations.RemoveField(
            model_name='addremoverequest',
            name='semester',
        ),
        migrations.RemoveField(
            model_name='addremoverequest',
            name='status',
        ),
        migrations.RemoveField(
            model_name='addremoverequest',
            name='student',
        ),
        migrations.RemoveField(
            model_name='addremoverequest',
            name='teacher_visited',
        ),
        migrations.RemoveField(
            model_name='emergencyremovalrequest',
            name='educational_assistant_visited',
        ),
        migrations.RemoveField(
            model_name='emergencyremovalrequest',
            name='status',
        ),
        migrations.RemoveField(
            model_name='emergencyremovalrequest',
            name='teacher_visited',
        ),
        migrations.RemoveField(
            model_name='employmenteducationrequest',
            name='educational_assistant_visited',
        ),
        migrations.RemoveField(
            model_name='employmenteducationrequest',
            name='semester',
        ),
        migrations.RemoveField(
            model_name='employmenteducationrequest',
            name='status',
        ),
        migrations.RemoveField(
            model_name='employmenteducationrequest',
            name='teacher_visited',
        ),
        migrations.RemoveField(
            model_name='enrollmentrequest',
            name='educational_assistant_visited',
        ),
        migrations.RemoveField(
            model_name='enrollmentrequest',
            name='status',
        ),
        migrations.RemoveField(
            model_name='enrollmentrequest',
            name='teacher_visited',
        ),
        migrations.RemoveField(
            model_name='revisionrequest',
            name='educational_assistant_visited',
        ),
        migrations.RemoveField(
            model_name='revisionrequest',
            name='status',
        ),
        migrations.RemoveField(
            model_name='revisionrequest',
            name='teacher_visited',
        ),
        migrations.RemoveField(
            model_name='semesterregistrationrequest',
            name='educational_assistant_visited',
        ),
        migrations.RemoveField(
            model_name='semesterregistrationrequest',
            name='explanation',
        ),
        migrations.RemoveField(
            model_name='semesterregistrationrequest',
            name='status',
        ),
        migrations.RemoveField(
            model_name='semesterregistrationrequest',
            name='teacher_visited',
        ),
        migrations.RemoveField(
            model_name='studentdeletesemesterrequest',
            name='educational_assistant_visited',
        ),
        migrations.RemoveField(
            model_name='studentdeletesemesterrequest',
            name='result',
        ),
        migrations.RemoveField(
            model_name='studentdeletesemesterrequest',
            name='semester',
        ),
        migrations.RemoveField(
            model_name='studentdeletesemesterrequest',
            name='status',
        ),
        migrations.RemoveField(
            model_name='studentdeletesemesterrequest',
            name='student',
        ),
        migrations.RemoveField(
            model_name='studentdeletesemesterrequest',
            name='teacher_visited',
        ),
        migrations.RemoveField(
            model_name='unitselectionrequest',
            name='educational_assistant_visited',
        ),
        migrations.RemoveField(
            model_name='unitselectionrequest',
            name='semester',
        ),
        migrations.RemoveField(
            model_name='unitselectionrequest',
            name='status',
        ),
        migrations.RemoveField(
            model_name='unitselectionrequest',
            name='student',
        ),
        migrations.RemoveField(
            model_name='unitselectionrequest',
            name='teacher_visited',
        ),
        migrations.AddField(
            model_name='addremoverequest',
            name='approval_status',
            field=models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('R', 'Rejected')], default='P', max_length=1),
        ),
        migrations.AddField(
            model_name='addremoverequest',
            name='semester_registration_request',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='dashboard_student.semesterregistrationrequest'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emergencyremovalrequest',
            name='approval_status',
            field=models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('R', 'Rejected')], default='P', max_length=1),
        ),
        migrations.AddField(
            model_name='employmenteducationrequest',
            name='approval_status',
            field=models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('R', 'Rejected')], default='P', max_length=1),
        ),
        migrations.AddField(
            model_name='revisionrequest',
            name='approval_status',
            field=models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('R', 'Rejected')], default='P', max_length=1),
        ),
        migrations.AddField(
            model_name='semesterregistrationrequest',
            name='approval_status',
            field=models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('R', 'Rejected')], default='P', max_length=1),
        ),
        migrations.AddField(
            model_name='studentdeletesemesterrequest',
            name='educational_assistant_approval_status',
            field=models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('R', 'Rejected')], default='P', max_length=1),
        ),
        migrations.AddField(
            model_name='studentdeletesemesterrequest',
            name='semester_registration_request',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='dashboard_student.semesterregistrationrequest'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentdeletesemesterrequest',
            name='teacher_approval_status',
            field=models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('R', 'Rejected')], default='P', max_length=1),
        ),
        migrations.AddField(
            model_name='unitselectionrequest',
            name='approval_status',
            field=models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('R', 'Rejected')], default='P', max_length=1),
        ),
        migrations.AddField(
            model_name='unitselectionrequest',
            name='semester_registration_request',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='dashboard_student.semesterregistrationrequest'),
            preserve_default=False,
        ),
    ]
