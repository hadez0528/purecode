# Generated by Django 4.2.6 on 2023-10-21 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_userinfo_followers_alter_userinfo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='followers',
            field=models.ManyToManyField(related_name='following', to='user.userinfo'),
        ),
    ]