# Generated by Django 4.2 on 2023-04-24 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0003_remove_verkaufen_paper_verkaufen_sort_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Backofen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=100)),
                ('serial_number', models.CharField(blank=True, max_length=200, null=True)),
                ('artikel_nr', models.CharField(blank=True, max_length=200, null=True)),
                ('bestellungsnummer', models.IntegerField(blank=True, null=True)),
                ('einkaufsdatum', models.DateField(blank=True, null=True)),
                ('preis', models.FloatField(blank=True, null=True)),
                ('energie', models.CharField(blank=True, max_length=10, null=True)),
                ('other', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='EinbauBackofen',
        ),
        migrations.AddField(
            model_name='backofenherd',
            name='artikel_nr',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='backofenherd',
            name='bestellungsnummer',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='backofenherd',
            name='einkaufsdatum',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='backofenherd',
            name='energie',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='backofenherd',
            name='iduktion',
            field=models.CharField(blank=True, choices=[('Ja', 'Ja'), ('Nein', 'Nein'), ('Nicht sicher', 'Nicht sicher')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='backofenherd',
            name='preis',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='kuehlschrank',
            name='artikel_nr',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='kuehlschrank',
            name='bestellungsnummer',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='kuehlschrank',
            name='einkaufsdatum',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='kuehlschrank',
            name='energie',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='kuehlschrank',
            name='preis',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='kuehlschrank',
            name='type',
            field=models.CharField(choices=[('Kombi', 'Kombi'), ('Nur Kuehlen', 'Nur Kuehlen'), ('Nur Gefrier', 'Nur Gefrier'), ('Mini Kühlschrank mit Gefrierfach', 'Mini Kühlschrank mit Gefrierfach'), ('Mini Kühlschrank ohne Gefrierfach', 'Mini Kühlschrank ohne Gefrierfach'), ('Mini nur Gefrier', 'Mini nur Gefrier'), ('Side-By-Side', 'Side-By-Side')], default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spuelmaschine',
            name='art',
            field=models.CharField(choices=[('Vollintegriert', 'Vollintegriert'), ('Teilintegriert', 'Teilintegriert'), ('Standgerät', 'Standgerät'), ('Unterbau', 'Unterbau')], default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spuelmaschine',
            name='artikel_nr',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='spuelmaschine',
            name='bestellungsnummer',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='spuelmaschine',
            name='breite',
            field=models.CharField(choices=[('45 cm', '45 cm'), ('60 cm', '60 cm')], default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spuelmaschine',
            name='einkaufsdatum',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='spuelmaschine',
            name='energie',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='spuelmaschine',
            name='preis',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='waschmaschine',
            name='artikel_nr',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='waschmaschine',
            name='bestellungsnummer',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='waschmaschine',
            name='einkaufsdatum',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='waschmaschine',
            name='energie',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='waschmaschine',
            name='fassung',
            field=models.CharField(choices=[('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('mehr', 'mehr')], default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='waschmaschine',
            name='preis',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='backofenherd',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='kuehlschrank',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='spuelmaschine',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='waschmaschine',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]