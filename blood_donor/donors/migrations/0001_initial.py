# Generated by Django 5.0.3 on 2024-03-27 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('blood_group', models.CharField(max_length=5)),
                ('last_donation', models.DateField()),
                ('address', models.TextField()),
            ],
        ),
    ]
