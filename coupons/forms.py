from django import forms


class CouponApplyForm(forms.Form):
    Код = forms.CharField()
