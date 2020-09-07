# Generated by Django 3.1.1 on 2020-09-07 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='djangoClasses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(blank=True, default='', max_length=60)),
                ('Course_Number', models.IntegerField(blank=True, default=0, max_length=5000)),
                ('Instructor_Number', models.CharField(blank=True, default=0, max_length=60)),
                ('Duration', models.FloatField(blank=True, default=None)),
            ],
        ),
    ]
