from django.db import models

# Create your models here.

class ToDoItem(models.Model):
    title=models.CharField(max_length=200)
    created_date=models.DateTimeField(auto_num_add=True)
    user=models.CharField(max_length=200)
    options=(
        ("completed","completed"),
        ("pending","pending"),
        ("inprogress","inprogress")
    )
    status=models.CharField(max_length=200,choices=options,default="pending")


