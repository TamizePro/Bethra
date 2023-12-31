# Generated by Django 4.2.3 on 2023-07-17 18:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('messagerie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='destinataire',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='recu_par', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='expediteur',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='envoye_par', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
