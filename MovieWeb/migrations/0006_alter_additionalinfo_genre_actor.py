# Generated by Django 4.0.3 on 2022-03-25 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieWeb', '0005_alter_additionalinfo_genre_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalinfo',
            name='genre',
            field=models.PositiveSmallIntegerField(choices=[(4, 'Drama'), (3, 'Sci-Fi'), (1, 'Horror'), (2, 'Comedy'), (0, 'Other')], default=0),
        ),
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('surname', models.CharField(max_length=32)),
                ('films', models.ManyToManyField(to='MovieWeb.film')),
            ],
        ),
    ]
