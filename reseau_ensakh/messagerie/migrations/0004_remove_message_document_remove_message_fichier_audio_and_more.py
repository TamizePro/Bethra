# Generated by Django 4.2.3 on 2023-07-18 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messagerie', '0003_message_recu_message_vu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='document',
        ),
        migrations.RemoveField(
            model_name='message',
            name='fichier_audio',
        ),
        migrations.RemoveField(
            model_name='message',
            name='image',
        ),
        migrations.RemoveField(
            model_name='message',
            name='video',
        ),
        migrations.AddField(
            model_name='message',
            name='fichier',
            field=models.FileField(blank=True, null=True, upload_to='fichiers/messsagerie/'),
        ),
    ]