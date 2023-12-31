# Generated by Django 4.2.3 on 2023-07-14 15:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.TextField(max_length=20)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/publications')),
                ('video', models.FileField(blank=True, null=True, upload_to='video/publications')),
                ('date_heure_de_creation', models.DateTimeField()),
                ('utilisateur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texte', models.TextField(max_length=50)),
                ('date_heure_de_creation', models.DateTimeField()),
                ('publication', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='publications.publication')),
            ],
        ),
    ]
