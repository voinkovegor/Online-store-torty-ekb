# Generated by Django 4.1.7 on 2023-03-24 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_dekor_remove_topping_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='choice',
            field=models.BooleanField(default=False, verbose_name='Конструктор'),
        ),
        migrations.AddField(
            model_name='product',
            name='standart_weight',
            field=models.CharField(default='1', max_length=2),
        ),
    ]