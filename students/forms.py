from django import forms 
from .models import Student, Company, PlacementActivity 

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student 
        fields = "__all__"

class StudentReadOnlyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['readonly'] = True
    class Meta:
        model = Student 
        fields = '__all__'

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company 
        fields = '__all__'

class PlacementActivityForm(forms.ModelForm):
    class Meta:
        model = PlacementActivity
        fields = '__all__'