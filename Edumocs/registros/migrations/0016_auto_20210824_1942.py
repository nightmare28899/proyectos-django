# Generated by Django 3.2.5 on 2021-08-25 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0015_carrito_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='descripcion',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='lecciones',
            field=models.TextField(null=True),
        ),
    ]
