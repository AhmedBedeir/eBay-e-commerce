from pyexpat import model
from tkinter.ttk import Style
from django import forms
from .models import Listings
from auctions import models


class newListing(forms.ModelForm):
  class Meta:
        model = Listings
        fields = ['title', 'description', 'startingBid', 'photo', 'category', 'active']

class itemBids(forms.Form):
  getPrice = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={
        'class' : 'form-control',
        'placeholder': "Bid",
        'style' : 'width: 300px; margin-bottom: 10px;',
    }))
