"""Field classes for *Material Components for the Web*.

This module defines classes, and the widgets of the class are modified into
the widgets using MDC.

See also:
    https://docs.djangoproject.com/en/1.11/ref/forms/fields/
"""

from django.forms import fields
from django.forms.fields import (
    Field,
    DateField, TimeField, DateTimeField, DurationField,
    RegexField, FileField, ImageField, URLField,
    NullBooleanField, MultipleChoiceField,
    ComboField, MultiValueField,
    SplitDateTimeField, GenericIPAddressField, FilePathField,
    SlugField, TypedChoiceField, TypedMultipleChoiceField, UUIDField,
)

from mdc.forms import widgets

__all__ = (
    'Field', 'CharField', 'IntegerField',
    'DateField', 'TimeField', 'DateTimeField', 'DurationField',
    'RegexField', 'EmailField', 'FileField', 'ImageField', 'URLField',
    'BooleanField', 'NullBooleanField', 'ChoiceField', 'MultipleChoiceField',
    'ComboField', 'MultiValueField', 'FloatField', 'DecimalField',
    'SplitDateTimeField', 'GenericIPAddressField', 'FilePathField',
    'SlugField', 'TypedChoiceField', 'TypedMultipleChoiceField', 'UUIDField',
)


class LabelFieldMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if hasattr(self.widget, 'label'):
            self.widget.label = self.label


class SliderFieldMixin:
    def widget_attrs(self, widget):
        attrs = super().widget_attrs(widget)
        if isinstance(widget, widgets.Slider):
            attrs['role'] = 'slider'
            if 'tabindex' not in widget.attrs:
                attrs['tabindex'] = 0
            if self.label is not None:
                attrs['aria-label'] = self.label
            if self.min_value is not None:
                attrs['aria-valuemin'] = self.min_value
            if self.max_value is not None:
                attrs['aria-valuemax'] = self.max_value
        return attrs

    def update_widgets(self):
        if isinstance(self.widget, widgets.Slider):
            self.widget.attrs['aria-valuemin'] = self.min_value
            self.widget.attrs['aria-valuemax'] = self.max_value


class CharField(LabelFieldMixin, fields.CharField):
    widget = widgets.TextInput


class IntegerField(SliderFieldMixin, LabelFieldMixin, fields.IntegerField):
    widget = widgets.NumberInput


class EmailField(LabelFieldMixin, fields.EmailField):
    widget = widgets.EmailInput


class ChoiceField(LabelFieldMixin, fields.ChoiceField):
    widget = widgets.Select


class BooleanField(LabelFieldMixin, fields.BooleanField):
    widget = widgets.CheckboxInput


class FloatField(SliderFieldMixin, LabelFieldMixin, fields.FloatField):
    widget = widgets.NumberInput


class DecimalField(SliderFieldMixin, LabelFieldMixin, fields.DecimalField):
    widget = widgets.NumberInput
