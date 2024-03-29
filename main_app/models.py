from django.db import models
from django.urls import reverse

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

# Create your models here.
class Finch(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()


  def __str__(self):
    return f'{self.name} ({self.id})'
    
  def get_absolute_url(self):
    return reverse('detail', kwargs={'finch_id': self.id})

class Feeding(models.Model):
  date = models.DateField('feeding date') 
  meal = models.CharField(
    max_length=1,
	 choices=MEALS,
	 default=MEALS[0][0]
  )
  finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"
    # change the default sort
    class Meta:
     ordering = ['-date']



class Photo(models.Model):
    url = models.CharField(max_length=200)
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for finch_id: {self.finch_id} @{self.url}"