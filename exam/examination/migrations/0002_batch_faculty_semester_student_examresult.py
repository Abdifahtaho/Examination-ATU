# Generated by Django 5.1 on 2024-08-14 19:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examination', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('courses', models.ManyToManyField(related_name='semesters', to='examination.course')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.TextField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('student_id', models.CharField(max_length=20, unique=True)),
                ('enrollment_year', models.IntegerField()),
                ('batches', models.ManyToManyField(related_name='students', to='examination.batch')),
                ('faculty', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='examination.faculty')),
            ],
        ),
        migrations.CreateModel(
            name='ExamResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.DecimalField(decimal_places=2, max_digits=5)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examination.course')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examination.semester')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exam_results', to='examination.student')),
            ],
        ),
    ]
