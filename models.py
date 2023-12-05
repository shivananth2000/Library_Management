from django.db import models

# Create your models here.
class Book_management(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    ISBM = models.IntegerField()
    availability_status = models.CharField(max_length=20)
    def __str__(self):
        return f'{self.ISBM}'

class Patron_management(models.Model):
    name = models.CharField(max_length=50)
    contact_num = models.IntegerField()
    Membership = models.CharField(max_length=20)
    def __str__(self):
        return f'{self.name}'

class Borrowing(models.Model):
    ISBN = models.ForeignKey(Book_management,on_delete=models.CASCADE)
    name = models.ForeignKey(Patron_management,on_delete=models.CASCADE)
    Borrowing_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return f'{self.name}=>{self.Borrowing_date}=>{self.return_date}'