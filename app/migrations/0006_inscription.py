# Generated by Django 4.1.4 on 2022-12-27 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_classe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(max_length=45)),
                ('anneescolaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.anneescolaire')),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.classe')),
                ('elev', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.elev')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.parent')),
            ],
        ),
    ]
