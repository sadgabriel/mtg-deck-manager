# Generated by Django 4.1 on 2023-12-02 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mtg', '0005_remove_deck_user_key_delete_contains_delete_deck'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deckname', models.CharField(max_length=50, unique=True)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mtg.user', to_field='username')),
            ],
            options={
                'db_table': 'deck',
            },
        ),
    ]
