# Generated by Django 4.1.4 on 2022-12-27 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_elev'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=45)),
                ('prenom', models.CharField(max_length=45)),
                ('tel', models.CharField(max_length=45)),
                ('adresse', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
            ],
        ),
    ]
