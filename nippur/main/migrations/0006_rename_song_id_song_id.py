# Generated by Django 5.0.1 on 2024-04-02 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_song_id_remove_song_num_alter_song_song_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='song_id',
            new_name='id',
        ),
    ]
