from django.db import models


# Create your models here.
class UserModel(models.Model):
    username = models.CharField(max_length=50)
    bio = models.CharField( max_length=50)
    profile = models.ImageField( upload_to='images/profiles/', blank=True)
    date_of_birth = models.DateField(null=False, blank=False)
    phone_number = models.IntegerField(max_length=10, blank=False)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class TodoModel(models.Model):
    username = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    bio = models.CharField( max_length=50)
    title = models.CharField( max_length=50)
    completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=False)
    due_date = models.DateField( null=True, blank=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField( max_length=50)

    def __str__(self):
        return self.name



class Comment(models.Model):
    username = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    todo = models.ForeignKey(TodoModel, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField( auto_now_add=False)
    phone_number = models.IntegerField(max_length=20, blank=False)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.text


class TagModel(models.Model):
    name = models.CharField( max_length=50)

    def __str__(self):
        return self.name

