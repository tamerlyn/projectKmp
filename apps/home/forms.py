from django import forms

class Search(forms.Form):
    text = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "class": "form-control",
                "id": "search-text",
                "disabled": "true"
            }
        )
    )

    search = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Звук не включен, поиск невозможен",
                "class": "form-control",
                "id": "search-phrase",
                "disabled": "true"
            }
        )
    )