from django import forms


class FilesForm(forms.Form):
    CHOICES = [('choice1', 'Phone number and date view'),
               ('choice2', 'Domain based view')]


    way = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),
                            label='How do you want to view the data?')
    file1 = forms.FileField(widget=forms.ClearableFileInput, label='Select a file',
        help_text='Please select a text (.txt) file')
