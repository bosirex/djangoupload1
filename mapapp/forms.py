from django import forms
from django.forms import ModelForm
from .models import Incidents
class IncidentReportForm(ModelForm):
    TYPE_INCIDENT_CHOICES = (
        ('', '-----'),  # This provides an empty option for user to select by default
        ('Medical', 'Medical'),
        ('security', 'Security'),
        ('spills', 'Spills'),
        ('other', 'other'),
    )

    type_incident = forms.ChoiceField(choices=TYPE_INCIDENT_CHOICES,
                                      widget=forms.Select(attrs={'class': 'form-control'}))
    STATE_CHOICES = (
        ('', 'Select a state'),  # Default empty selection
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
        ('GU', 'Guam'),
        ('VI', 'Virgin Islands')
    )

    state = forms.ChoiceField(choices=STATE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Incidents
        fields =  ('incident_number','first_name','last_name','seating','type_incident','latitude','longitude','unit_responding','transport','additional_resources','age','gender','injury','address','city','state','contacts','zipcode',)

        widgets ={
            'incident_number':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'seating':forms.TextInput(attrs={'class':'form-control'}),
            'latitude':forms.TextInput(attrs={'class':'form-control'}),
            'longitude':forms.TextInput(attrs={'class':'form-control'}),
            'unit_responding':forms.TextInput(attrs={'class':'form-control'}),
            'transport':forms.TextInput(attrs={'class':'form-control'}),
            'additional_resources':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            'gender':forms.TextInput(attrs={'class':'form-control'}),
            'injury':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'state':forms.TextInput(attrs={'class':'form-control'}),
            'contacts':forms.TextInput(attrs={'class':'form-control'}),
            'zipcode':forms.TextInput(attrs={'class':'form-control'}),

        }

