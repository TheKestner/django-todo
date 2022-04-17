from django.db import models
from django.contrib.auth.models import User

# Model for Todos Table
class Todo(models.Model):
    label = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    due_date = models.DateTimeField('date due')
    status = models.BooleanField(True, False)
    HIGH = 'H'
    MED = 'M'
    LOW = 'L'
    PRIORITY_CHOICES = [
        (HIGH , 'High'),
        (MED, 'Medium'),
        (LOW, 'Low'),
    ]
    priority = models.CharField(
        max_length=200,
        choices=PRIORITY_CHOICES,
        default=MED,
    )
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.label

    def __str__(self):
        return self.description


#Model for Events Table
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField()
    event_time = models.DurationField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def __str__(self):
        return self.description


#Model for Category table
class Category(models.Model):
    title = models.CharField(max_length=200)
    RED = 'RD'
    BLUE = 'BL'
    GREEN = 'GN'
    BLACK = 'BK'
    WHITE = 'WT'
    COLOR_CHOICES = [
        (RED , 'Red'),
        (BLUE, 'Blue'),
        (GREEN, 'Green'),
        (BLACK, 'Black'),
        (WHITE, 'White'),
    ]
    color = models.CharField(
        max_length=200,
        choices=COLOR_CHOICES,
        default=WHITE,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
     verbose_name_plural = 'Categories'
     
    def __str__(self):
        return self.title