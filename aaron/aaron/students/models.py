from django.db import models

# Create your models here.
class Studentdetails(models.Model):
    registerno = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    fathername = models.CharField(max_length=100)
    dob = models.CharField(max_length=10)
    phonenumber = models.CharField(max_length=10)
    mail = models.CharField(max_length=100)

class Payment(models.Model):
    registerno = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    billdate = models.CharField(max_length=20)
    reciptno = models.CharField(max_length=20)
    course = models.CharField(max_length=100)
    feesamount = models.CharField(max_length=100)
    paytype = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

class Certificate(models.Model):
    registerno = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    feesamount = models.CharField(max_length=100)

class Exam(models.Model):
    registerno = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    feesamount = models.CharField(max_length=100)
    paytype = models.CharField(max_length=100)


class meta:
    db_table ="students_member"
