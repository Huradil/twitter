# Generated by Django 4.2 on 2023-05-11 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_reaction_unique_together_replyreaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reaction',
            name='tweet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reactions', to='posts.tweet'),
        ),
    ]