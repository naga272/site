# Generated by Django 4.2.2 on 2023-07-04 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RiceviRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('cognome', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('contenuto', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'contattami',
                'verbose_name_plural': 'contattami',
            },
        ),
    ]