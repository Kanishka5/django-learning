from __future__ import unicode_literals

from django.db import models

class Cell(models.Model):
    cell_name=models.CharField(max_length=100)
    cell_head=models.CharField(max_length=100)
    cell_logo=models.CharField(max_length=500)

def __str__(self):
    return self.cell_name

class Member(models.Model):
    cell = models.ForeignKey(Cell, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    post=models.CharField(max_length=100)

def __str__(self):
    return self.name
