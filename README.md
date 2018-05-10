[![GitHub license](https://img.shields.io/github/license/YuoMamoru/mdc-for-django.svg)](https://github.com/YuoMamoru/mdc-for-django/blob/master/LICENSE)

# MDC for Django

MDC for Django provides a helper to use [Material Companent for the Web](https://www.material.io/develop/web/)
with Django application.

MDC for Django includes following components:

* Custom widgets for using on django form
* Custom tags
* Stylesheets

## Installation

First, create your django application.

```bash
$ python -m django-admin startproject your-project-name
```

Then add MDC for Django to your application

```bash
$ cd your-project-name
$ git clone https://github.com/YuoMamoru/mdc-for-django.git mdc
```

## Usage of widgets on form

Just use `mdc.forms` instead of `django.forms`.

```python
from mdc import forms

class CustomForm(forms.Form):
    field1 = forms.CharField(
        max_length=127,
        required=False,
        widget=forms.TextInput,
    )
```

> Note: Please replace the `mdc` part in accordance with your cloned directory name.
