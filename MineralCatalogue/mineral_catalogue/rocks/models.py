from django.db import models

# Create your models here.

class Mineral(models.Model):
    '''
        THE MINERAL MODEL TAKES IN CHARACTERS, BUT IF THE FIELD IS LEFT EMPTY,
        BLANK=TRUE ALLOWS IT TO BE EMPTY.
    '''

    name = models.CharField(max_length=128, blank=True)
    image_filename = models.CharField(max_length=255, blank=True)
    image_caption = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=128, blank=True)
    formula = models.CharField(max_length=255, blank=True)
    strunz_classification = models.CharField(max_length=255, blank=True)
    color = models.CharField(max_length=255, blank=True)
    crystal_system = models.CharField(max_length=255, blank=True)
    unit_cell = models.CharField(max_length=255, blank=True)
    crystal_symmetry = models.CharField(max_length=255, blank=True)
    cleavage = models.CharField(max_length=255, blank=True)
    mohs_scale_hardness = models.CharField(max_length=255, blank=True)
    luster = models.CharField(max_length=255, blank=True)
    streak = models.CharField(max_length=255, blank=True)
    diaphaneity = models.CharField(max_length=255, blank=True)
    optical_properties = models.CharField(max_length=255, blank=True)
    refractive_index = models.CharField(max_length=255, blank=True)
    crystal_habit = models.CharField(max_length=255, blank=True)
    specific_gravity = models.CharField(max_length=255, blank=True)

