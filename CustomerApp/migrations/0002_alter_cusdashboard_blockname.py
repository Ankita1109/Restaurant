# Generated by Django 3.2.8 on 2023-02-24 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cusdashboard',
            name='blockname',
            field=models.CharField(choices=[('IceCreamCorner', 'IceCream Corner'), ('ChocolateCorner', 'Chocolate Corner')], max_length=300),
        ),
    ]