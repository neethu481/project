from django import forms
from .models import products


class productForm(forms.ModelForm):

    class Meta:
        model = products
        fields = ('fullname','code','position')
        labels = {'fullname':'Full Name',
                  'code':' Code'
                  }

    def __init__(self, *args, **kwargs):
        super(productForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['code'].required = False