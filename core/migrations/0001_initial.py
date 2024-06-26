# Generated by Django 4.2.6 on 2024-05-30 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=300)),
                ('date', models.DateField()),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('income', models.IntegerField(default=0)),
                ('month', models.CharField(default='05-2024', max_length=30, primary_key=True, serialize=False)),
            ],
        ),
    ]
