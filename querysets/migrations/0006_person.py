# Generated by Django 4.0.1 on 2022-02-16 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('querysets', '0005_city_goo_dong'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('shirt_size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=2)),
            ],
        ),
    ]
