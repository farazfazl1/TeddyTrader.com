from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField


class TeddyBear(models.Model):
    # State Choices
    state_choices = [
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    ]

    feature_choices = [
        ('moveable arms', 'Moveable arms'),
        ('moveable legs', 'Moveable legs'),
        ('button eyes', 'Button eyes'),
        ('embroidered eyes', 'Embroidered eyes'),
        ('satin bow', 'Satin bow'),
        ('growler', 'Growler'),
        ('jingle bell', 'Jingle bell'),
        ('ribbon', 'Ribbon'),
        ('heart-shaped nose', 'Heart-shaped nose'),
        ('paw pads', 'Paw pads'),
        ('bean filling', 'Bean filling'),
        ('jointed', 'Jointed'),
    ]

    color_choices = (
        ('brown', 'Brown'),
        ('black', 'Black'),
        ('white', 'White'),
        ('golden', 'Golden'),
        ('cream', 'Cream'),
        ('beige', 'Beige'),
        ('red', 'Red'),
        ('green', 'Green'),
        ('blue', 'Blue'),
        ('pink', 'Pink'),
        ('purple', 'Purple'),
        ('gray', 'Gray'),
    )

    size_choices = [
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    ]

    material_choices = [
        ('cotton', 'Cotton'),
        ('wool', 'Wool'),
        ('plush', 'Plush'),
        ('synthetic', 'Synthetic'),
    ]

    brand_choices = [
        ('Aristobear', 'Aristobear'),
        ('Regency Bears', 'Regency Bears'),
        ('Aurelia Bears', 'Aurelia Bears'),
        ('Evermore Bears', 'Evermore Bears'),
        ('Ambrosia Bears', 'Ambrosia Bears'),
        ('Luminous Bears', 'Luminous Bears'),
        ('Celestine Bears', 'Celestine Bears'),
        ('Nimbus Bears', 'Nimbus Bears'),
        ('Lavender Lane Bears', 'Lavender Lane Bears'),
        ('Verdant Valley Bears', 'Verdant Valley Bears'),
        ('Crimson Peak Bears', 'Crimson Peak Bears'),
        ('Belle Époque Bears', 'Belle Époque Bears'),
    ]

    condition_choices = [
        ('new', 'New'),
        ('like new', 'Like New'),
        ('excellent', 'Excellent'),
        ('good', 'Good'),
        ('fair', 'Fair')
    ]

    tag_choices = [
        ('For Sale', 'For Sale'),
        ('For Rent', 'For Rent'),
        ('New Arrival', 'New Arrival'),
        ('Limited Edition', 'Limited Edition'),
    ]

    year_choice = []
    for r in range(1902, (datetime.now().year+1)):
        year_choice.append((r, r))

    # Basic Teddy Bear Details
    name = models.CharField(max_length=255, blank=False)
    brand = models.CharField(
        max_length=255, choices=brand_choices, blank=False)
    # allows users to pick year instead of typing it on their own
    year = models.IntegerField(('year'), choices=year_choice, blank=False)
    state = models.CharField(max_length=50, choices=state_choices, blank=False)
    city = models.CharField(max_length=50, blank=False)
    condition = models.CharField(
        max_length=50, choices=condition_choices, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    description = RichTextField(blank=False)
    tag = models.CharField(
        max_length=50, choices=tag_choices, blank=False, null=True)

    # Teddy Bear Photos
    bear_photo = models.ImageField(
        upload_to='photos/%Y/%m/%d', blank=False)
    bear_photo_1 = models.ImageField(
        upload_to='photos/%Y/%m/%d', blank=True)
    bear_photo_2 = models.ImageField(
        upload_to='photos/%Y/%m/%d', blank=True)
    bear_photo_3 = models.ImageField(
        upload_to='photos/%Y/%m/%d', blank=True)
    bear_photo_4 = models.ImageField(
        upload_to='photos/%Y/%m/%d', blank=True)

    # Additional Details
    color = models.CharField(max_length=20, choices=color_choices, blank=False)
    size = models.CharField(max_length=20, choices=size_choices, blank=False)
    material = models.CharField(
        max_length=20, choices=material_choices, blank=False)
    features = MultiSelectField(
        max_length=255, choices=feature_choices, blank=False)
    recommended_age = models.CharField(max_length=50, blank=False)
    # to be feautred or not in page
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:  # order based on id number
        ordering = ['id']

    def __str__(self):
        return f"{self.name} ({self.year} {self.brand})"
