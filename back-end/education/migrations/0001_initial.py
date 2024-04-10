# Generated by Django 4.2 on 2024-04-10 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=40)),
                ('course_code', models.PositiveSmallIntegerField(unique=True)),
                ('credit_num', models.PositiveSmallIntegerField()),
                ('course_type', models.CharField(choices=[('L', 'Laboratory'), ('R', 'Research'), ('I', 'Internship'), ('A', 'Activity '), ('G', 'General'), ('B', 'Basic')], max_length=1)),
                ('availablity', models.CharField(choices=[('A', 'Available'), ('D', 'Deleted')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('saturday', 'Saturday'), ('sunday', 'Sunday'), ('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday')], max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=40, unique=True)),
                ('department_code', models.PositiveSmallIntegerField(unique=True)),
                ('year_established', models.DateField()),
                ('department_location', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('start_semester', models.DateField()),
                ('end_semester', models.DateField()),
                ('semester_type', models.CharField(choices=[('F', 'Fall'), ('W', 'Winter'), ('S', 'Summer')], default='F', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='SemesterCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_time_start', models.TimeField()),
                ('class_time_end', models.TimeField()),
                ('exam_datetime', models.DateTimeField(blank=True, null=True)),
                ('exam_location', models.CharField(blank=True, max_length=100, null=True)),
                ('course_capacity', models.PositiveSmallIntegerField()),
                ('corse_reserve_capasity', models.PositiveSmallIntegerField(default=0)),
                ('class_days', models.ManyToManyField(to='education.day')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.course')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.teacher')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.semester')),
            ],
        ),
        migrations.CreateModel(
            name='SemesterUnitSelection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_selection_start', models.DateField()),
                ('unit_selection_end', models.DateField()),
                ('semester', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='unit_selection', to='education.semester')),
            ],
        ),
        migrations.CreateModel(
            name='SemesterExam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_start', models.DateField()),
                ('exam_end', models.DateField()),
                ('semester', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='exams', to='education.semester')),
            ],
        ),
        migrations.CreateModel(
            name='SemesterEmergency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emergency_remove_start', models.DateField()),
                ('emergency_remove_end', models.DateField()),
                ('semester', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='emergency', to='education.semester')),
            ],
        ),
        migrations.CreateModel(
            name='SemesterClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classes_start', models.DateField()),
                ('classes_end', models.DateField()),
                ('semester', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='education.semester')),
            ],
        ),
        migrations.CreateModel(
            name='SemesterAddRemove',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addremove_start', models.DateField()),
                ('addremove_end', models.DateField()),
                ('semester', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='addremove', to='education.semester')),
            ],
        ),
        migrations.CreateModel(
            name='Requisite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requisites', to='education.course')),
                ('requisite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='required_with', to='education.course')),
            ],
        ),
        migrations.CreateModel(
            name='Prerequisite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prerequisites', to='education.course')),
                ('prerequisite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='required_by', to='education.course')),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major_name', models.CharField(max_length=30)),
                ('major_code', models.PositiveSmallIntegerField(unique=True)),
                ('number_of_credits', models.PositiveIntegerField()),
                ('level', models.CharField(choices=[('B', 'Bachelor'), ('M', 'Master'), ('P', 'PhD')], default='B', max_length=1)),
                ('education_group', models.CharField(max_length=30)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='education.department')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='education.department'),
        ),
        migrations.AddField(
            model_name='course',
            name='major',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='education.major'),
        ),
        migrations.CreateModel(
            name='StudentCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('F', 'FinalRegistered'), ('R', 'Registered'), ('P', 'Pending'), ('W', 'Withdrawn'), ('D', 'Deleted')], default='R', max_length=1)),
                ('score', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('semester_course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='education.semestercourse')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.student')),
            ],
            options={
                'unique_together': {('student', 'semester_course')},
            },
        ),
    ]
