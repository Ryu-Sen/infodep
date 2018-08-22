from django.db import models


class Kitting(models.Model):
    job_type = models.CharField(max_length=50, null=True)
    job_date = models.CharField(max_length=50, null=True)
    unit_number = models.CharField(max_length=50, null=True)
    account_name = models.CharField(max_length=30, null=True)
    user_name = models.CharField(max_length=50, null=True)
    furigana = models.CharField(max_length=50, null=True)
    note = models.CharField(max_length=300, null=True)
    status = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.account_name

    class Meta:
        db_table = 'infodep_kitting'

