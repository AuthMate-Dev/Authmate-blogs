# Generated by Django 4.2.17 on 2025-01-02 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timeStamp',
            field=models.DateTimeField(blank=True, db_index=True),
        ),
    ]
