# Generated by Django 3.1.4 on 2020-12-11 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('empid', models.IntegerField(primary_key=True, serialize=False)),
                ('empname', models.CharField(max_length=30)),
                ('empsal', models.IntegerField()),
                ('empdept', models.EmailField(max_length=30)),
            ],
        ),
    ]