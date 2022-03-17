from django import forms
from project.apps.profiles.models import User

class UserModelForm(forms.ModelForm):
    last_login = forms.DateTimeField(disabled=True)
    date_joined = forms.DateTimeField(disabled=True)
    is_active = forms.BooleanField(disabled=True)
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            # "usertype",
            "is_active",
            "last_login",
            "date_joined"
        ]
        labels = {
            # "paymentdate": "Payment Date",
        }
        widgets = {
            # "usertype": Select()
        }
        help_texts = {
            #"invfrom": _("Who is the invoice from?"),
        }
        error_messages = {
            # "invnumber": {'required': _('Don\'t forget to enter the invoice number')}
        }
