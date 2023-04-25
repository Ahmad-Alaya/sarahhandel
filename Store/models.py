from django.db import models

# Create your models here.
from django.db import models


# Klasse Waschmaschine
class Waschmaschine(models.Model):
    FASSUNG_CHOICES = [
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
        ("10", "10"),
        ("mehr", "mehr"),

    ]
    name = models.CharField(max_length=50, )
    fassung = models.CharField(max_length=20, choices=FASSUNG_CHOICES)
    model = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=200, null=True, blank=True)
    artikel_nr = models.CharField(max_length=200, null=True, blank=True)
    bestellungsnummer = models.IntegerField(null=True, blank=True)
    einkaufsdatum = models.DateField(null=True, blank=True)
    preis = models.FloatField(null=True, blank=True)
    energie = models.CharField(max_length=10, null=True, blank=True)
    other = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        if self.preis:
            return f"{self.name} : {self.fassung}: {self.model} :{self.preis}"
        else:
            return f"{self.name} : {self.fassung}: {self.model}"


# Klasse Spuelmaschine
class Spuelmaschine(models.Model):
    BREITE_CHOICESE = [
        ("45 cm", "45 cm"),
        ("60 cm", "60 cm")
    ]
    ART_CHOICES = [
        ("Vollintegriert", "Vollintegriert"),
        ("Teilintegriert", "Teilintegriert"),
        ("Standgerät", "Standgerät"),
        ("Unterbau", "Unterbau")

    ]
    name = models.CharField(max_length=50)
    breite = models.CharField(max_length=100, choices=BREITE_CHOICESE)
    art = models.CharField(max_length=100, choices=ART_CHOICES)
    model = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=200, null=True, blank=True)
    artikel_nr = models.CharField(max_length=200, null=True, blank=True)
    bestellungsnummer = models.IntegerField(null=True, blank=True)
    einkaufsdatum = models.DateField(null=True, blank=True)
    preis = models.FloatField(null=True, blank=True)
    energie = models.CharField(max_length=10, null=True, blank=True)
    other = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        if self.preis:
            return f"{self.name} : {self.breite} : {self.art} : {self.model} : {self.preis}"
        else:
            return f"{self.name} : {self.breite} : {self.art} : {self.model}"


# Klasse EinbauBackofen
class Backofen(models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=200, null=True, blank=True)
    artikel_nr = models.CharField(max_length=200, null=True, blank=True)
    bestellungsnummer = models.IntegerField(null=True, blank=True)
    einkaufsdatum = models.DateField(null=True, blank=True)
    preis = models.FloatField(null=True, blank=True)
    energie = models.CharField(max_length=10, null=True, blank=True)
    other = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        if self.preis:
            return f"{self.name} : {self.model} : {self.preis}"
        else:
            return f"{self.name} : {self.model}"


# Klasse BackofenHerd
class BackofenHerd(models.Model):
    JANEIN_CHOICES = [
        ("Ja", "Ja"),
        ("Nein", "Nein"),
        ("Nicht sicher", "Nicht sicher"),
    ]
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    iduktion = models.CharField(max_length=100, choices=JANEIN_CHOICES,)
    serial_number = models.CharField(max_length=200, null=True, blank=True)
    artikel_nr = models.CharField(max_length=200, null=True, blank=True)
    bestellungsnummer = models.IntegerField(null=True, blank=True)
    einkaufsdatum = models.DateField(null=True, blank=True)
    preis = models.FloatField(null=True, blank=True)
    energie = models.CharField(max_length=10, null=True, blank=True)
    other = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        if self.preis:
            return f"{self.name} : {self.model}"
        else:
            return f"{self.name} : {self.model} : {self.preis}"


# Klasse Kuehlschrank
class Kuehlschrank(models.Model):
    TYPE_CHOICES = [
        ("Kombi", "Kombi"),
        ("Nur Kuehlen", "Nur Kuehlen"),
        ("Nur Gefrier", "Nur Gefrier"),
        ("Mini Kühlschrank mit Gefrierfach", "Mini Kühlschrank mit Gefrierfach"),
        ("Mini Kühlschrank ohne Gefrierfach", "Mini Kühlschrank ohne Gefrierfach"),
        ("Mini nur Gefrier", "Mini nur Gefrier"),
        ("Side-By-Side", "Side-By-Side"),
    ]
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    type = models.CharField(max_length=200, choices=TYPE_CHOICES)
    serial_number = models.CharField(max_length=200, null=True, blank=True)
    artikel_nr = models.CharField(max_length=200, null=True, blank=True)
    bestellungsnummer = models.IntegerField(null=True, blank=True)
    einkaufsdatum = models.DateField(null=True, blank=True)
    preis = models.FloatField(null=True, blank=True)
    energie = models.CharField(max_length=10, null=True, blank=True)
    other = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        if self.preis:
            return f"{self.name} : {self.type} : {self.model} : {self.preis}"
        else:
            return f"{self.name} : {self.type} : {self.model}"


# Klasse Verkaufen
class Verkaufen(models.Model):
    SORT_CHOICES = (
        ('Waschmaschine', 'Waschmaschine'),
        ('Spuelmaschine', 'Spuelmaschine'),
        ('EinbauBackofen', 'EinbauBackofen'),
        ('BackofenHerd', 'BackofenHerd'),
        ('Kuehlschrank', 'Kuehlschrank'),
    )

    sort = models.CharField(max_length=20, choices=SORT_CHOICES)
    product = models.ManyToManyField('Waschmaschine', blank=True)
