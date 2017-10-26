from django import forms


class MailForm(forms.Form):
    from_mail = forms.EmailField(
        error_messages={'required': "'From' field is required"})
    to_mail = forms.EmailField(
        error_messages={'required': "'To' field is required"})
    subject_mail = forms.CharField(max_length=100, error_messages={
                                   'required': "'Subject' field is required"})
    content_mail = forms.CharField(widget=forms.Textarea(attrs={'cols': 54, 'rows': 10}),
                                   error_messages={'required': "'Content' field is required"})
