# Generated by Django 3.2.4 on 2021-08-23 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0010_alter_cursos_duracion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='email',
        ),
        migrations.AddField(
            model_name='usuario',
            name='username',
            field=models.TextField(null=True),
        ),
    ]
