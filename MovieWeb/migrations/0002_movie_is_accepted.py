# Generated by Django 4.0.3 on 2022-04-03 18:24
from django.core.exceptions import ObjectDoesNotExist
from django.db import migrations, models
from .data.categories import categories


def add_categories(apps, schema_editor):
    model = apps.get_model('MovieWeb', 'Category')
    for category in categories:
        new_category = model.objects.create(name=category["name"], description=category["description"])
        new_category.save()


def revert(apps, schema_editor):
    model = apps.get_model('MovieWeb', 'Category')
    for category in categories:
        try:
            category_to_delete = model.object.get(name=category["name"], description=category["description"])
            category_to_delete.delete()
        except model.DoesNotExist:
            continue


class Migration(migrations.Migration):

    dependencies = [
        ('MovieWeb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='is_accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.RunPython(add_categories, revert)
    ]
