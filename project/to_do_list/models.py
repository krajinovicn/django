from django.db import models


class ToDo(models.Model):
    title = models.CharField(max_length=30)
    LOW = "low"
    MEDIUM = "med"
    HIGH = "hi"
    PRIORITY_CHOICES = [
        (LOW, "Low"),
        (MEDIUM, "Medium"),
        (HIGH, "High")
    ]
    priority = models.CharField(
        max_length=3, choices=PRIORITY_CHOICES, default=MEDIUM,)
