from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# 1- this is our first model, this is how we create models, we derived class TodoList that inherits models.Model, that models from django.db then use Model class from models

# 2 - then we need mention those fields that are applicable for the particular model, here for todo we have task column, status column with the datatype & their length

# 3 - then we need to follow migrations that we follow while start of the django, that is the two commands, see the django_ref_pad for more clarififcation
# 1 - python manage.py makemigrations - this will help us to convert our queries - create our migrations for the particular model, it will create a migrations file for this class TodoList inside the migratrions folder
# 2 - python manage.py migrate - this will help us to actually apply the queries - this will apply our migration queries
# 3 - whenever we change any columns, add columns, alter datatypes, we need run above 2 commands to apply changes

# 4 - after run these two commands there nothing going to change we just create migrations for our TodoList class and apply the migration queries, finally to see changes we need register them in admin.py file - this file is register all the models that we are created

# IMPORTANT thing its not a mandatory, its jus your wish if you need showcase your model in admin panel then you need to register them otherwise if you want to hide them, hide means not a important one no need to display,

# 5 - next how we register ?
# 1 - you need import your model in admin.py, then
# 2 - regsiter usgin - admin.site.register(pass the model name)

# 6 - all done, now you may able see your TodoList model and able to add todolists and one thing to remember after created todo's it always appearing in object type, why becuase our model TodoList is class, every element we are going to register will going to store as a objects, to rectify that use __str__ special function to get the string

# need to look up the django model field types
# https://docs.djangoproject.com/en/4.2/ref/models/fields/#model-field-types


class TodoList(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    # this foreign key function takes three arguments 1 - which model to use foreign key, 2 - on_delete attribute to delete all the records of a user if that specific user get deleted for this purpose we use on_delete attribute to this, 3 - default attribute for the default value here we pass None to this
    task = models.CharField(
        max_length=300
    )  # CharField are datatype that are pre-definedly available under the django models, max_length is a argument for the CharField
    status = models.BooleanField(
        default=False
    )  # BooleanField are datatype that are pre-definedly available under the django models

    def __str__(self):
        done = (
            "Done" if self.status else "Yet to be done"
        )  # ternary opertor in python, if true then the lefthandside as result else the else block
        return "{0} - {1}".format(self.task, done)
