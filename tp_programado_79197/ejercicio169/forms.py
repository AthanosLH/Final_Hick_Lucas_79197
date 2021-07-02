from django import forms
from crispy_forms.helper import FormHelper


class ParametersForm(forms.Form):
    t0 = forms.IntegerField(label='t0', initial=1947, min_value=0)
    P0 = forms.IntegerField(label='P0', initial=34, min_value=0)
    t1 = forms.IntegerField(label='t1', initial=1952, min_value=0)
    P1 = forms.IntegerField(label='P1', initial=48, min_value=0)
    t2 = forms.IntegerField(label='t2', initial=1957, min_value=0)
    P2 = forms.IntegerField(label='P2', initial=64, min_value=0)
    T = forms.IntegerField(label='T', initial=2021, min_value=0)

    def __init__(self, *args, **kwargs):
        super(ParametersForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.form_show_labels = False
        self.helper.form_tag = False