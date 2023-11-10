from django.db import models
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
)


# Create your models here.
class Student(models.Model):
    s_roll = models.CharField(max_length=20, primary_key=True)
    s_fname = models.CharField(max_length=20)
    s_lname = models.CharField(max_length=20)
    s_branch = models.CharField(max_length=10)
    s_section = models.CharField(max_length=5)
    s_year = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(4)],
    )

    def __str__(self) -> str:
        return f"{self.s_fname} {self.s_lname} - {self.s_roll} - {self.s_branch}({self.s_year}{self.s_section})"
