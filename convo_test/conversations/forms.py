from django import forms


class FilesForm(forms.Form):
    text1 = forms.CharField()
    file1 = forms.FileField(widget=forms.ClearableFileInput, label='Select a file',
        help_text='Please select a text file')
