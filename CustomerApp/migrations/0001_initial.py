# Generated by Django 3.2.8 on 2023-02-24 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BeveragesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Brand', models.CharField(default='Local', max_length=200)),
                ('DrinkName', models.CharField(max_length=200)),
                ('DrinkType', models.CharField(max_length=200)),
                ('DrinkCost', models.CharField(max_length=200)),
                ('DrinkImage', models.FileField(max_length=600, upload_to='Beverages/')),
            ],
        ),
        migrations.CreateModel(
            name='Chinese_Snacks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=300)),
                ('ItemCost', models.CharField(max_length=100)),
                ('ItemImage', models.FileField(default='None', max_length=600, upload_to='Chinese_Snacks/')),
                ('Check', models.CharField(default='snacks', max_length=100)),
                ('CreatedDate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CusDashboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blockname', models.CharField(max_length=300)),
                ('BannerOfdata', models.CharField(max_length=300)),
                ('dishName', models.CharField(default='none', max_length=300)),
                ('DishCost', models.CharField(default='0', max_length=100)),
                ('BannerImage', models.FileField(max_length=600, upload_to='DashboardBanner/')),
            ],
        ),
        migrations.CreateModel(
            name='MenuCategories',
            fields=[
                ('Caregories', models.CharField(max_length=300, primary_key=True, serialize=False)),
                ('CreatedDate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='RiceChapati',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(default='enter', max_length=300)),
                ('ItemCost', models.CharField(default='0', max_length=100)),
                ('ItemImage', models.FileField(default='None', max_length=600, upload_to='Mainmenu/RiceChapati/')),
                ('Check', models.CharField(default='rice', max_length=100)),
                ('CreatedDate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SweetCornerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DessertType', models.CharField(max_length=200)),
                ('DessertName', models.CharField(max_length=200)),
                ('DessertCost', models.CharField(max_length=200)),
                ('DessertImage', models.FileField(max_length=600, upload_to='Dessert/')),
            ],
        ),
        migrations.CreateModel(
            name='Starter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StarterName', models.CharField(max_length=300)),
                ('Startercost', models.CharField(max_length=300)),
                ('starterIamge', models.FileField(default='None', max_length=600, upload_to='Mainmenu/Starter/')),
                ('Check', models.CharField(default='veg', max_length=100)),
                ('Starter', models.DateTimeField(auto_now=True)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CustomerApp.menucategories')),
            ],
        ),
        migrations.CreateModel(
            name='Main_CourceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MaincourceName', models.CharField(max_length=300)),
                ('MaincourceCost', models.CharField(max_length=300)),
                ('MaincourceIamge', models.FileField(max_length=600, upload_to='Mainmenu/MainCource/')),
                ('Check', models.CharField(default='veg', max_length=100)),
                ('Maincource', models.DateTimeField(auto_now=True)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CustomerApp.menucategories')),
            ],
        ),
    ]