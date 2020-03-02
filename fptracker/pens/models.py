from django.db import models
from django.forms import ModelForm
from django.forms.widgets import TextInput

# Create your models here.
class Ink(models.Model):
    brand_name = models.CharField(max_length=100)
    color = models.CharField(max_length=7)
    color_name = models.CharField(max_length=100)
    rating = models.IntegerField()

    def __str__(self):
        return self.brand_name + " " + self.color_name + " " + "(" + str(self.rating) + ")"

class Pen(models.Model):
    brand_name = models.CharField (max_length=100)
    model_name = models.CharField (max_length=100)
    color = models.CharField(max_length=7)
    date_purchased = models.DateField()
    current_ink = models.ForeignKey(Ink, on_delete=models.SET_NULL, null=True, blank= True)

    NIB_SIZES = (
    ('B', 'Broad'),
    ('M', 'Medium'),
    ('F', 'Fine'),
    ('EF', 'Extra Fine')
    )

    nib_size = models.CharField(
        max_length=2,
        choices=NIB_SIZES
    )

    def __str__(self):
        return self.color + ' ' + self.brand_name + ' ' + self.model_name

class PenForm(ModelForm):
    class Meta:
        model = Pen
        fields = "__all__"
        widgets = {
            'color': TextInput(attrs={'type':'color'})
        }

class InkForm(ModelForm):
    class Meta:
        model = Ink
        fields = "__all__"
        widgets = {
            'color':TextInput(attrs={'type':'color'})
        }
