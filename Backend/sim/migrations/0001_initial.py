# Generated by Django 5.1.1 on 2024-09-19 10:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PermissionTache',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peut_créer', models.BooleanField(default=False)),
                ('peut_modifier', models.BooleanField(default=False)),
                ('peut_supprimer', models.BooleanField(default=False)),
                ('peut_changer_statut', models.BooleanField(default=False)),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GroupeTache',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
                ('permissions', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sim.permissiontache')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date_limite', models.DateField()),
                ('statut', models.BooleanField(default=False)),
                ('créateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taches_créées', to=settings.AUTH_USER_MODEL)),
                ('utilisateur_assigné', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taches_assignées', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
