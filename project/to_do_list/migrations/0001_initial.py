# Generated by Django 4.0.2 on 2022-02-24 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('priority', models.CharField(choices=[('low', 'Low'), ('med', 'Medium'), ('hi', 'High')], default='med', max_length=3)),
            ],
        ),
    ]