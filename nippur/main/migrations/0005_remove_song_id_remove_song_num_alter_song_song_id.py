# Generated by Django 5.0.1 on 2024-04-02 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_song_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='id',
        ),
        migrations.RemoveField(
            model_name='song',
            name='num',
        ),
        migrations.AlterField(
            model_name='song',
            name='song_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]