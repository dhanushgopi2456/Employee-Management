# Generated by Django 5.1.1 on 2024-09-28 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='bonus',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='hiredate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phonenum',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.IntegerField(null=True),
        ),
    ]
