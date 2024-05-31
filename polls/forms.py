from django import forms

class TwitterForm(forms.Form):
    text = forms.CharField(label='Tweet Text', max_length=30)
    location = forms.CharField(label='Location Detail',max_length=100)
    check_image = forms.BooleanField(required=False, initial=False, label='Tweet Image')
    docfile = forms.FileField(required=False, label='Select a file', help_text='max. 5 megabytes')
    
   

    def clean(self):
        cleaned_data = super(TwitterForm, self).clean()
        text = cleaned_data.get('text')
        location = cleaned_data.get('location')
        check_image = cleaned_data.get('check_image')
        if not text and not location and not check_image:
            raise forms.ValidationError('You have to write something!')
