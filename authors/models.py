from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(
        max_length=40,
        validators=[
            MinLengthValidator(4),
            RegexValidator(
                r'^[a-zA-Z]+$',
                message='Your name must contain letters only!'
            )
        ]
    )
    last_name = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(2),
            RegexValidator(
                r'^[a-zA-Z]+$',
                message='Your name must contain letters only!'
            )
        ]
    )
    passcode = models.CharField(
        max_length=6,
        validators=[
            RegexValidator(
                r'^[0-9]{6}$',
                message='Your passcode must be exactly 6 digits!'
            )
        ],
        help_text='Your passcode must be a combination of 6 digits'
    )
    pets_number = models.PositiveSmallIntegerField()
    info = models.TextField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)


