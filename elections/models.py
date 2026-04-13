# Create your models here.
from django.db import models

class PollingUnit(models.Model):
    uniqueid = models.IntegerField(primary_key=True)
    polling_unit_id = models.IntegerField()
    ward_id = models.IntegerField()
    lga_id = models.IntegerField()

    class Meta:
        db_table = 'polling_unit'
        managed = False


class LGA(models.Model):
    uniqueid = models.IntegerField(primary_key=True)
    lga_id = models.IntegerField()
    lga_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'lga'
        managed = False


class AnnouncedPUResult(models.Model):
    result_id = models.IntegerField(primary_key=True)
    polling_unit_uniqueid = models.IntegerField()
    party_abbreviation = models.CharField(max_length=10)
    party_score = models.IntegerField()

    class Meta:
        db_table = 'announced_pu_results'
        managed = False


class Party(models.Model):
    id = models.IntegerField(primary_key=True)
    partyid = models.CharField(max_length=10)
    partyname = models.CharField(max_length=50)

    class Meta:
        db_table = 'party'
        managed = False