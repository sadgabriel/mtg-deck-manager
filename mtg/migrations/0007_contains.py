# Generated by Django 4.1 on 2023-12-02 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mtg', '0006_alter_card_name_alter_user_username_deck'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contains',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mtg.card', to_field='name')),
                ('deckname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mtg.deck', to_field='deckname')),
            ],
            options={
                'db_table': 'contains',
            },
        ),
    ]
