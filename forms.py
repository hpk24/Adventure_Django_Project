from myapp1.models import bookingData,packages, packagebookingData
from django import forms
from django.forms.widgets import TextInput


# class PlaceholderTextInput(TextInput):
#         def __init__(self, attrs=None, placeholder=None):
#                 super().__init__(attrs)
#                 self.attrs.update({'placeholder': placeholder})
#
#         def get_context(self, name, value, attrs):
#                 context = super().get_context(name, value, attrs)
#                 context['widget']['label'] = ''
#                 return context


class BookingForm(forms.ModelForm):

        def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.label_suffix = ''
                for visible in self.visible_fields():
                        visible.field.widget.attrs['class'] = 'single-input'
                        visible.field.widget.attrs['placeholder'] = visible.field.label

        AvailbleCapacity = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
        Price = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
        TotalPrice = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
        class Meta:
                model=bookingData
                fields =['user','aid','AvailbleCapacity','Price','People','TotalPrice','day','time','Comments']

class PacakgesForm(forms.ModelForm):

        def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.label_suffix = ''
                for visible in self.visible_fields():
                        visible.field.widget.attrs['class'] = 'single-input'
                        visible.field.widget.attrs['placeholder'] = visible.field.label

        # AvailbleCapacity = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
        # Price = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
        # TotalPrice = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
        class Meta:
                model= packages
                fields =['package_name','package_activities','description','price','capacity', 'day']

class BookPacakgesForm(forms.ModelForm):

        def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.label_suffix = ''
                for visible in self.visible_fields():
                        visible.field.widget.attrs['class'] = 'single-input'
                        visible.field.widget.attrs['placeholder'] = visible.field.label

        AvailbleCapacity = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
        Price = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
        TotalPrice = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
        class Meta:
                model= packagebookingData
                fields =['user','pid','People','AvailbleCapacity','Price','day','Comments','TotalPrice']