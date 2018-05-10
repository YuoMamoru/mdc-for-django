"""Wdget classes for *Material Components for the Web*.

This module defines classes that render HTML using *Material Components for
the Web*.

See also:
    https://docs.djangoproject.com/en/1.11/ref/forms/widgets/
"""

from django.conf import settings
from django.contrib.auth.password_validation import (
    get_password_validators, MinimumLengthValidator, NumericPasswordValidator,
)
from django.forms import widgets
from django.forms.widgets import (
    Media, MediaDefiningClass, Widget,
    HiddenInput,
    MultipleHiddenInput, FileInput, ClearableFileInput,
    DateInput, DateTimeInput, TimeInput,
    NullBooleanSelect, SelectMultiple,
    CheckboxSelectMultiple, MultiWidget, SplitDateTimeWidget,
    SplitHiddenDateTimeWidget, SelectDateWidget,
)
from django.utils.translation import ugettext as _, ungettext

__all__ = (
    'Media', 'MediaDefiningClass', 'Widget', 'TextInput', 'NumberInput',
    'EmailInput', 'URLInput', 'PasswordInput', 'HiddenInput',
    'MultipleHiddenInput', 'FileInput', 'ClearableFileInput', 'Textarea',
    'DateInput', 'DateTimeInput', 'TimeInput', 'CheckboxInput', 'Select',
    'NullBooleanSelect', 'SelectMultiple', 'RadioSelect',
    'CheckboxSelectMultiple', 'MultiWidget', 'SplitDateTimeWidget',
    'SplitHiddenDateTimeWidget', 'SelectDateWidget', 'Slider',
)


class MDCWidgetMixin:
    """Mixin to widgets using *Material Component for Web*."""

    mdc_class = None

    def __init__(self, *args, label=None, auto_init=True, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = label
        self.auto_init = auto_init

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        if self.mdc_class:
            if 'class' in context['widget']['attrs']:
                context['widget']['attrs']['class'] += ' ' + self.mdc_class
            else:
                context['widget']['attrs']['class'] = self.mdc_class
        context['widget']['label'] = self.label or ''
        context['widget']['auto_init'] = self.auto_init
        return context


class MDCTextMixin(MDCWidgetMixin):
    """Mixin to widgets text-input components."""

    template_name = 'mdc/forms/widgets/text.html'
    mdc_class = 'mdc-text-field__input'

    def __init__(self, *args, hint=None, persistent=False, valid_msg=False,
                 dense=False, **kwargs):
        super().__init__(*args, **kwargs)
        self.hint = hint
        self.persistent = persistent
        self.valid_msg = valid_msg
        self.dense = dense

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['hint'] = self.hint or ''
        context['persistent'] = self.persistent
        context['valid_msg'] = self.valid_msg
        context['dense'] = self.dense
        return context


class TextInput(MDCTextMixin, widgets.TextInput):
    """Text input widget compatible with Material Components for the Web.

    args:
        attrs (:obj:`dict`, optional): A dictionary containing HTML
            attributes to be set on the rendered widget.
        label (:obj:`str`, optional): Words displayed on a form.
        auto_init (:obj:`bool`, optional): If spacify `True`, You can use
            automatical instantiation of components by *mdc-auto-init*.
            If you want to instantiate components manually, specify `False`.
            Default to `True`.
        hint (:obj:`str`, optional): Words displayed as hint.
        persistent (:obj:`bool`, optional): Specifying `True` a hint is
            dipslayed persistently, specifying `False` the hint is
            displayed when the component has focus. Default to `False`.
        valid_msg (:obj:`bool`, optional): Specifying `True` a hint is
            dipslayed only when validations fails. Default to `False`.
        dense (:obj:`bool`, optional): Specifying `True` the component
            dipslayed densely. Default to `False`.
    """


class NumberInput(MDCTextMixin, widgets.NumberInput):
    """Number input widget compatible with Material Components for the Web.

    args:
        attrs (:obj:`dict`, optional): A dictionary containing HTML
            attributes to be set on the rendered widget.
        label (:obj:`str`, optional): Words displayed on a form.
        auto_init (:obj:`bool`, optional): If spacify `True`, You can use
            automatical instantiation of components by *mdc-auto-init*.
            If you want to instantiate components manually, specify `False`.
            Default to `True`.
        hint (:obj:`str`, optional): Words displayed as hint.
        persistent (:obj:`bool`, optional): Specifying `True` a hint is
            dipslayed persistently, specifying `False` the hint is
            displayed when the component has focus. Default to `False`.
        valid_msg (:obj:`bool`, optional): Specifying `True` a hint is
            dipslayed only when validations fails. Default to `False`.
        dense (:obj:`bool`, optional): Specifying `True` the component
            dipslayed densely. Default to `False`.
    """


class EmailInput(MDCTextMixin, widgets.EmailInput):
    """Email input widget compatible with Material Components for the Web.

    args:
        attrs (:obj:`dict`, optional): A dictionary containing HTML
            attributes to be set on the rendered widget.
        label (:obj:`str`, optional): Words displayed on a form.
        auto_init (:obj:`bool`, optional): If spacify `True`, You can use
            automatical instantiation of components by *mdc-auto-init*.
            If you want to instantiate components manually, specify `False`.
            Default to `True`.
        hint (:obj:`str`, optional): Words displayed as hint.
        persistent (:obj:`bool`, optional): Specifying `True` a hint is
            dipslayed persistently, specifying `False` the hint is
            displayed when the component has focus. Default to `False`.
        valid_msg (:obj:`bool`, optional): Specifying `True` a hint is
            dipslayed only when validations fails. Default to `False`.
        dense (:obj:`bool`, optional): Specifying `True` the component
            dipslayed densely. Default to `False`.
    """


class URLInput(MDCTextMixin, widgets.URLInput):
    """URL input widget compatible with Material Components for the Web.

    args:
        attrs (:obj:`dict`, optional): A dictionary containing HTML
            attributes to be set on the rendered widget.
        label (:obj:`str`, optional): Words displayed on a form.
        auto_init (:obj:`bool`, optional): If spacify `True`, You can use
            automatical instantiation of components by *mdc-auto-init*.
            If you want to instantiate components manually, specify `False`.
            Default to `True`.
        hint (:obj:`str`, optional): Words displayed as hint.
        persistent (:obj:`bool`, optional): Specifying `True` a hint is
            dipslayed persistently, specifying `False` the hint is
            displayed when the component has focus. Default to `False`.
        valid_msg (:obj:`bool`, optional): Specifying `True` a hint is
            dipslayed only when validations fails. Default to `False`.
        dense (:obj:`bool`, optional): Specifying `True` the component
            dipslayed densely. Default to `False`.
    """


class PasswordInput(MDCTextMixin, widgets.PasswordInput):
    """Password input widget compatible with Material Components for the Web.

    args:
        attrs (:obj:`dict`, optional): A dictionary containing HTML
            attributes to be set on the rendered widget.
        label (:obj:`str`, optional): Words displayed on a form.
        auto_init (:obj:`bool`, optional): If spacify `True`, You can use
            automatical instantiation of components by *mdc-auto-init*.
            If you want to instantiate components manually, specify `False`.
            Default to `True`.
        hint (:obj:`str`, optional): Words displayed as hint.
        persistent (:obj:`bool`, optional): Specifying `True` a hint is
            dipslayed persistently, specifying `False` the hint is
            displayed when the component has focus. Default to `False`.
        valid_msg (:obj:`bool`, optional): Specifying `True` a hint is
            dipslayed only when validations fails. Default to `False`.
        dense (:obj:`bool`, optional): Specifying `True` the component
            dipslayed densely. Default to `False`.
        auth_validate (:obj:`bool`, optional): If `True` is specified,
            part of Django's password varidation is implemented in the
            component. Default to `False`
    """

    def __init__(self, *args, auth_validate=False, **kwargs):
        super().__init__(*args, **kwargs)
        self.auth_validate = auth_validate

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        if (self.auth_validate):
            for validator in get_password_validators(settings.AUTH_PASSWORD_VALIDATORS):  # NOQA
                if isinstance(validator, MinimumLengthValidator):
                    if 'pattern' not in context['widget']['attrs']:
                        context['widget']['attrs']['pattern'] = r'.{%d}.*' % validator.min_length  # NOQA
                    if not context['hint']:
                        context['hint'] = ungettext(
                            "Your password must contain at least %(min_length)d character.",   # NOQA
                            "Your password must contain at least %(min_length)d characters.",  # NOQA
                            validator.min_length
                        ) % {'min_length': validator.min_length}
                    break
                if isinstance(validator, NumericPasswordValidator):
                    if 'pattern' not in context['widget']['attrs']:
                        context['widget']['attrs']['pattern'] = r'.*[^\d].*'
                    if not context['hint']:
                        context['hint'] = _("Your password can't be entirely numeric.")  # NOQA
                    break
        return context


class Select(MDCWidgetMixin, widgets.Select):
    """Select widget compatible with Material Components for the Web.

    args:
        attrs (:obj:`dict`, optional): A dictionary containing HTML
            attributes to be set on the rendered widget.
        choices (:obj:`iter`, optional): If this argument is specified,
            the widget override choices that is specified by :obj:`Field`.
        label (:obj:`str`, optional): Words displayed on a form.
        auto_init (:obj:`bool`, optional): If spacify `True`, You can use
            automatical instantiation of components by *mdc-auto-init*.
            If you want to instantiate components manually, specify `False`.
            Default to `True`.
    """

    template_name = 'mdc/forms/widgets/select.html'
    option_template_name = 'django/forms/widgets/select_option.html'
    mdc_class = 'mdc-select__native-control'


class CheckboxInput(MDCWidgetMixin, widgets.CheckboxInput):
    """Checkbox widget compatible with Material Components for the Web.

    args:
        attrs (:obj:`dict`, optional): A dictionary containing HTML
            attributes to be set on the rendered widget.
        label (:obj:`str`, optional): Words displayed on a form.
        auto_init (:obj:`bool`, optional): If spacify `True`, You can use
            automatical instantiation of components by *mdc-auto-init*.
            If you want to instantiate components manually, specify `False`.
            Default to `True`.
    """

    template_name = 'mdc/forms/widgets/checkbox.html'
    mdc_class = 'mdc-checkbox__native-control'


class RadioSelect(MDCWidgetMixin, widgets.RadioSelect):
    """Radio button widget compatible with Material Components for the Web.

    args:
        attrs (:obj:`dict`, optional): A dictionary containing HTML
            attributes to be set on the rendered widget.
        choices (:obj:`iter`, optional): If this argument is specified,
            the widget override choices that is specified by :obj:`Field`.
        label (:obj:`str`, optional): Words displayed on a form.
        auto_init (:obj:`bool`, optional): If spacify `True`, You can use
            automatical instantiation of components by *mdc-auto-init*.
            If you want to instantiate components manually, specify `False`.
            Default to `True`.
    """

    template_name = 'mdc/forms/widgets/radio.html'
    option_template_name = 'mdc/forms/widgets/radio_option.html'
    mdc_class = 'mdc-radio__native-control'

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        if self.mdc_class:
            for optgroup in context['widget']['optgroups']:
                for option in optgroup[1]:
                    if 'class' in option['attrs']:
                        option['attrs']['class'] += ' ' + self.mdc_class
                    else:
                        option['attrs']['class'] = self.mdc_class
        return context


class Textarea(MDCWidgetMixin, widgets.Textarea):
    """Textarea widget compatible with Material Components for the Web.

    args:
        attrs (:obj:`dict`, optional): A dictionary containing HTML
            attributes to be set on the rendered widget.
        label (:obj:`str`, optional): Words displayed on a form.
        auto_init (:obj:`bool`, optional): If spacify `True`, You can use
            automatical instantiation of components by *mdc-auto-init*.
            If you want to instantiate components manually, specify `False`.
            Default to `True`.
    """

    template_name = 'mdc/forms/widgets/textarea.html'
    mdc_class = 'mdc-text-field__input'


class Slider(MDCWidgetMixin, Widget):
    """Slider widget compatible with Material Components for the Web.

    args:
        attrs (:obj:`dict`, optional): A dictionary containing HTML
            attributes to be set on the rendered widget.
        label (:obj:`str`, optional): Words displayed on a form.
        auto_init (:obj:`bool`, optional): If spacify `True`, You can use
            automatical instantiation of components by *mdc-auto-init*.
            If you want to instantiate components manually, specify `False`.
            Default to `True`.
        hint (:obj:`str`, optional): Words displayed as hint.
        persistent (:obj:`bool`, optional): Specifying `True` a hint is
            dipslayed persistently, specifying `False` the hint is
            displayed when the component has focus. Default to `False`.
        valid_msg (:obj:`bool`, optional): Specifying `True` a hint is
            dipslayed only when validations fails. Default to `False`.
        dense (:obj:`bool`, optional): Specifying `True` the component
            dipslayed densely. Default to `False`.
    """

    template_name = 'mdc/forms/widgets/slider.html'
    mdc_class = 'mdc-slider'

    def __init__(self, *args,
                 discrete=False, step=0, display_merkers=False,
                 uses_form=False,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.discrete = discrete
        self.step = step
        self.display_merkers = display_merkers
        self.uses_form = uses_form

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        cssclasses = [context['widget']['attrs']['class']]
        if self.discrete:
            cssclasses.append('mdc-slider--discrete')
        if self.step:
            context['widget']['attrs']['data-step'] = self.step
        if self.display_merkers:
            cssclasses.append('mdc-slider--display-markers')
        context['widget']['attrs']['class'] = ' '.join(cssclasses)
        context['discrete'] = self.discrete
        context['displaymerkers'] = self.display_merkers
        context['usesform'] = self.uses_form
        return context
