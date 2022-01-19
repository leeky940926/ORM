# Generated by Django 4.0.1 on 2022-01-19 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('querysets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='email',
            field=models.OneToOneField(db_column='email', on_delete=django.db.models.deletion.CASCADE, to='querysets.user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
    ]
