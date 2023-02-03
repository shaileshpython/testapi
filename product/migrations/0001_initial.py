# Generated by Django 4.1.6 on 2023-02-03 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrderDate', models.DateField()),
                ('Region', models.CharField(max_length=50)),
                ('City', models.CharField(max_length=100)),
                ('Category', models.CharField(max_length=50)),
                ('Product', models.CharField(max_length=50)),
                ('Quantity', models.IntegerField()),
                ('UnitPrice', models.FloatField()),
            ],
        ),
    ]