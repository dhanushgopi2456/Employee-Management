from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    def _str_(self):
        return f"{self.name} {self.location}"

class Role(models.Model):
    name = models.CharField(max_length=255)
    def _str_(self):
        return self.namep[dgh]

class Employee(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    salary = models.IntegerField(null=True)
    bonus = models.IntegerField(null=True)
    phonenum = models.IntegerField(null=True)
    hiredate = models.DateField(null=True,blank=True)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    def _str_(self):
        return f"{self.firstname} {self.lastname} {self.salary} {self.bonus} {self.phonenum} {self.hiredate} {self.dept} {self.role}"

# Create your models here.
