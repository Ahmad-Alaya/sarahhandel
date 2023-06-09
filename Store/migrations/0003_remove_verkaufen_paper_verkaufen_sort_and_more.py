# Generated by Django 4.2 on 2023-04-10 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0002_backofenherd_serial_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='verkaufen',
            name='paper',
        ),
        migrations.AddField(
            model_name='verkaufen',
            name='sort',
            field=models.CharField(choices=[('Waschmaschine', 'Waschmaschine'), ('Spuelmaschine', 'Spuelmaschine'), ('EinbauBackofen', 'EinbauBackofen'), ('BackofenHerd', 'BackofenHerd'), ('Kuehlschrank', 'Kuehlschrank')], default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='verkaufen',
            name='product',
        ),
        migrations.AddField(
            model_name='verkaufen',
            name='product',
            field=models.ManyToManyField(blank=True, to='Store.waschmaschine'),
        ),
    ]
