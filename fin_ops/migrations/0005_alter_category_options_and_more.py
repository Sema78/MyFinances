# Generated by Django 4.1.1 on 2022-12-09 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fin_ops', '0004_category_rename_annotation_finoperation_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='finoperation',
            name='op_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fin_ops.category'),
        ),
    ]
