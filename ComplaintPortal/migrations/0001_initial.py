# Generated by Django 4.1 on 2022-08-27 16:16

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
                ('cid', models.CharField(max_length=30)),
                ('typeOfIssue', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('avail_start', models.DateTimeField()),
                ('avail_end', models.DateTimeField()),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Officer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empid', models.CharField(max_length=9)),
                ('name', models.CharField(max_length=30)),
                ('phnnum', models.CharField(max_length=10)),
                ('rank', models.IntegerField()),
                ('officeRoom', models.IntegerField()),
                ('wing', models.CharField(max_length=1)),
                ('hostel', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=9)),
                ('name', models.CharField(max_length=30)),
                ('phnNum', models.CharField(max_length=10)),
                ('room', models.IntegerField()),
                ('wing', models.CharField(max_length=1)),
                ('hostel', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]