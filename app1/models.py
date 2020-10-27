from django.db import models

class login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    def __str__(self):
        return self.username

class signup(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone = models.IntegerField()
    password = models.CharField(max_length=30)
    pic = models.ImageField(upload_to='profile',default='default.jpg')

    #def __str__(self):
    #    return self.fname

    @staticmethod
    def getdata_username(email):
        return signup.objects.get(email=email)
