# Generated by Django 2.0.9 on 2018-12-21 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dracoin', '0003_auto_20181221_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='posts',
            field=models.ManyToManyField(blank=True, related_name='tags', to='dracoin.Article'),
        ),
    ]
