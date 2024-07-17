from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class userdetails(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.IntegerField()
    roll_no = models.IntegerField()
    register_id = models.CharField(max_length=10)
    college_name=models.CharField(max_length=40)
    department=models.CharField(max_length=40)

class LibraryBookDetail(models.Model):
    book_name=models.CharField(max_length=20)
    book_img=models.ImageField(upload_to='image/')
    auther=models.CharField(max_length=20)
    book_id=models.CharField(max_length=10)
    description=models.CharField(max_length=100)
    available_copies=models.IntegerField()
    def __str__(self):
        return self.book_name


class BookRequest(models.Model):
    user=models.ForeignKey(userdetails,on_delete=models.CASCADE)
    book=models.ForeignKey(LibraryBookDetail,on_delete=models.CASCADE)
    request_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"request by {self.user.user.username} for {self.book.book_name}"


class AcceptedBooks(models.Model):
    details=models.ForeignKey(BookRequest,on_delete=models.CASCADE)
    accepted_date=models.DateTimeField(auto_now_add=True)
    return_date=models.DateTimeField()
    fine=models.IntegerField(default=0)

    def __str__(self):
        return f"Accepted request by {self.details.user.user.username} for {self.details.book.book_name}"


class AcceptedBooksNewModel(models.Model):
    book_name=models.CharField(max_length=20)
    auther=models.CharField(max_length=20)
    request_date=models.DateTimeField(auto_now_add=True)
    userd=models.ForeignKey(userdetails,on_delete=models.CASCADE)
    accepted_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField()
    fine = models.IntegerField(default=0)

    def __str__(self):
        return f"Accepted request by {self.userd.user.username} for {self.book_name}"




class usermodel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone=models.IntegerField()
    age=models.IntegerField()
    job=models.CharField(max_length=40)
    higher_qualification=models.CharField(max_length=50)


