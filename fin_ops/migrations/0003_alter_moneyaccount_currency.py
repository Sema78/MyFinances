# Generated by Django 4.1.1 on 2022-12-07 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fin_ops', '0002_alter_currencytype_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moneyaccount',
            name='currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fin_ops.currencytype'),
        ),
    ]
