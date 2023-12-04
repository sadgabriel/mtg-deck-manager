# Generated by Django 4.1 on 2023-11-30 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cost', models.CharField(max_length=10)),
                ('type', models.CharField(max_length=50)),
                ('text', models.CharField(max_length=200)),
                ('power', models.IntegerField()),
                ('toughness', models.IntegerField()),
            ],
            options={
                'db_table': 'card',
            },
        ),
    ]
