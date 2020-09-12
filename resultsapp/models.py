from django.db import models


class Halticket(models.Model):
    id= models.CharField(max_length=150, null=False, blank=True,primary_key=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'hallticket'


class Student(models.Model):
    htno = models.OneToOneField(Halticket, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=True, blank=True)
    group=models.CharField(max_length=150,null=True,blank=True)
    status_choices=(('Pass','Pass'),('Fail','Fail'))
    status=models.CharField(max_length=10,choices=status_choices,default='Pass')
    grade_choices=(('Outstanding','Outstanding'),('Average','Average'),('Good','Good'))
    grade=models.CharField(max_length=20,null=True,blank=True,choices=grade_choices,default='Outstanding')

    class Meta:
        db_table='student'


    def __str__(self):
        return self.name
