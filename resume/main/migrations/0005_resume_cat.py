# Generated by Django 5.0 on 2024-01-02 10:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.categories'),
        ),
    ]
