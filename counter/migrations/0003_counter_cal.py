# Generated by Django 5.0.1 on 2024-02-16 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0002_rename_daily_counter_rename_item_counter_query'),
    ]

    operations = [
        migrations.AddField(
            model_name='counter',
            name='cal',
            field=models.IntegerField(default=0),
        ),
    ]