# Generated by Django 3.2.13 on 2022-06-08 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banco', '0006_alter_agencia_tipo1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agencia',
            name='tipo1',
            field=models.CharField(blank=True, choices=[('f', 'Fixo'), ('c', 'Celular')], max_length=1, null=True),
        ),
    ]
