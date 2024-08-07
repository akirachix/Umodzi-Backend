# Generated by Django 5.0.6 on 2024-07-07 18:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0001_initial'),
        ('users', '0002_remove_users_id_alter_users_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.users'),
        ),
    ]
