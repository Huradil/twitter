# Generated by Django 4.2 on 2023-05-16 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_replyreaction_reply'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweet',
            options={'verbose_name': 'Твит', 'verbose_name_plural': 'Твиты'},
        ),
    ]
