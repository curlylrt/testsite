from django import forms

class OrderForm(forms.Form):
    
    timeLimit = forms.DecimalField(min_value=1, max_value=24)
   
    METHOD_CHOICES = (
        ("DRIVING", "DRIVING"),
        ("BICYCLING", "BICYCLING"),
        ("TRANSIT", "TRANSIT"),
        ("WALKING", "WALKING"),
    ) 
    method = forms.ChoiceField(choices=METHOD_CHOICES)
