# Generated by Django 2.1.3 on 2018-11-12 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Password',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(default=0)),
                ('website', models.CharField(default='', max_length=100)),
                ('name', models.CharField(default='', max_length=100)),
                ('passwordGenerator', models.CharField(default='', max_length=100)),
            ],
        ),
    ]