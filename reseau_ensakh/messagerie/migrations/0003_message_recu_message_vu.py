# Generated by Django 4.2.3 on 2023-07-18 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messagerie', '0002_message_destinataire_message_expediteur'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='recu',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='message',
            name='vu',
            field=models.BooleanField(default=False),
        ),
    ]
