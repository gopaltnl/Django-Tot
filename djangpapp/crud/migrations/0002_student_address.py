# Generated by Django 3.1.4 on 2020-12-11 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.TextField(null=True),
        ),
    ]
