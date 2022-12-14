from django.db import models


# Create your models here.
class EnglishSchemeModel(models.Model):
    EDU_TYPES = (
        (3, 'Graduate'),
        (2, 'Under Graduate'),
        (1, 'Schooling'),
        (0, 'Not Applicable'),
    )

    name = models.CharField(max_length=500, null=False, blank=False)
    desc = models.TextField(null=True, blank=True)
    income_limit = models.TextField(null=True, blank=True)
    interest_rate = models.TextField(null=True, blank=True)
    # extra_data = models.TextField(null=True, blank=True)
    caste = models.CharField(max_length=255, null=True, blank=True)
    religion = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    min_age = models.IntegerField(null=True, blank=True)
    max_age = models.IntegerField(null=True, blank=True)
    min_inc = models.IntegerField(null=True, blank=True)
    max_inc = models.IntegerField(null=True, blank=True)
    educational_qualifications = models.IntegerField(choices=EDU_TYPES, null=True, blank=True)
    occupation = models.CharField(max_length=255, null=True, blank=True)
    disability = models.CharField(max_length=255, null=True, blank=True)
    tags = models.TextField(null=True, blank=True)


# class EnglishTagModel(models.Model):
#     name = models.CharField(max_length=255)
#     scheme = models.ManyToManyField(EnglishSchemeModel)

# class GujTagModel(models.Model):
#     name = models.CharField(max_length=255)
#     scheme = models.ManyToManyField(EnglishSchemeModel)


class GujSchemeModel(models.Model):
    name = models.CharField(max_length=500, null=False, blank=False)
    desc = models.TextField(null=True, blank=True)
    income = models.TextField(null=True, blank=True)
    interest_rate = models.TextField(null=True, blank=True)
    # extra_data = models.TextField(null=True, blank=True)
    caste = models.CharField(max_length=255, null=True, blank=True)
    religion = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    min_age = models.IntegerField(null=True, blank=True)
    max_age = models.IntegerField(null=True, blank=True)
    min_inc = models.IntegerField(null=True, blank=True)
    max_inc = models.IntegerField(null=True, blank=True)
    education = models.CharField(max_length=255, null=True, blank=True)
    occupation = models.CharField(max_length=255, null=True, blank=True)
    disability = models.CharField(max_length=255, null=True, blank=True)
    tags = models.TextField(null=True, blank=True)
