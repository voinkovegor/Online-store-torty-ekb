# Generated by Django 4.1.7 on 2023-03-14 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_category_options_alter_product_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name'], 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.RemoveIndex(
            model_name='category',
            name='shop_catego_name_289c7e_idx',
        ),
        migrations.RemoveIndex(
            model_name='product',
            name='shop_produc_id_f21274_idx',
        ),
        migrations.RemoveIndex(
            model_name='product',
            name='shop_produc_name_a2070e_idx',
        ),
        migrations.RemoveIndex(
            model_name='product',
            name='shop_produc_created_ef211c_idx',
        ),
    ]