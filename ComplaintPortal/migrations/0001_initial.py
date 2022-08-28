# Generated by Django 4.1 on 2022-08-28 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=9)),
                ('date', models.DateTimeField()),
                ('typeOfIssue', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('avail_start', models.DateTimeField()),
                ('avail_end', models.DateTimeField()),
                ('status', models.CharField(max_length=10)),
                ('officerName', models.CharField(max_length=30)),
                ('officerRank', models.IntegerField()),
            ],
        ),
    ]
