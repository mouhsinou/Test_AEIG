# Generated by Django 5.1.1 on 2024-09-19 11:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sim', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permissiontache',
            name='utilisateur',
        ),
        migrations.RemoveField(
            model_name='task',
            name='créateur',
        ),
        migrations.RemoveField(
            model_name='task',
            name='utilisateur_assigné',
        ),
        migrations.CreateModel(
            name='AutorisationTache',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ajouter', models.BooleanField(default=False)),
                ('modifier', models.BooleanField(default=False)),
                ('supprimer', models.BooleanField(default=False)),
                ('marquer_termine', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tache',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date_debut', models.DateTimeField(auto_now_add=True)),
                ('date_fin', models.DateTimeField(blank=True, null=True)),
                ('termine', models.BooleanField(default=False)),
                ('utilisateurs', models.ManyToManyField(related_name='taches', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='GroupeTache',
        ),
        migrations.DeleteModel(
            name='PermissionTache',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
