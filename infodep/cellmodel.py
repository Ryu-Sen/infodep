from django.db import models

class Cellphone(models.Model):
    phone_number = models.CharField(max_length=30, null=True)
    brand = models.CharField(max_length=50, null=True)
    password_protection = models.CharField(max_length=50, null=True)
    presentability = models.CharField(max_length=50, null=True)
    main_body = models.BinaryField(default=False)
    box = models.BinaryField(default=False)
    notes = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.phone_number

    class Meta:
        db_table = 'infodep_cellphone'