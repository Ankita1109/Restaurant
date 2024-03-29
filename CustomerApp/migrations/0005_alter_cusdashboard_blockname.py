# Generated by Django 3.2.8 on 2023-02-24 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerApp', '0004_alter_cusdashboard_blockname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cusdashboard',
            name='blockname',
            field=models.CharField(choices=[('IceCreamCorner', 'IceCream Corner'), ('ChocolateCorner', 'Chocolate Corner'), ('SweetCorner', 'Sweet Corner'), ('MocktailCorner', 'Mocktail Corner'), ('CocktailCorner', 'Cocktail Corner'), ('VodkaCorner', 'Vodka Corner'), ('BeerCorner', 'Beer Corner'), ('colddrinkCorner', 'Cold Drink Corner'), ('WineCorner', 'Wine Corner'), ('AllDrinksCorner', 'All Drinks Corner')], max_length=300, unique=True),
        ),
    ]
