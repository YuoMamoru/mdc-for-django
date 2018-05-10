from django.conf import settings
from django.template import Library
from django.template.base import TemplateSyntaxError
from django.utils.html import format_html
from sass_processor.templatetags.sass_tags import SassSrcNode

from mdc import SUPPORTED_MDC_VERSION

register = Library()


class MdcCssNode(SassSrcNode):
    SASS_PATH = 'mdc/material-components-web.scss'
    LAST_PATH = 'https://unpkg.com/material-components-web/dist/' \
                'material-components-web.css'

    def __init__(self, path, uses_last=None):
        super().__init__(path)
        self.uses_last = uses_last

    @classmethod
    def handle_token(cls, parser, token):
        bits = token.split_contents()
        if len(bits) > 2:
            raise TemplateSyntaxError("'{0}' takes no argument".format(*bits))
        if len(bits) == 2:
            return cls(parser.compile_filter(f"'{cls.SASS_PATH}'"),
                       parser.compile_filter(bits[1]))
        return cls(parser.compile_filter(f"'{cls.SASS_PATH}'"))

    def render(self, context):
        if settings.DEBUG and \
                self.uses_last and self.uses_last.resolve(context):
            return self.LAST_PATH
        return super().render(context)


@register.tag
def mdc_sass_src(parser, token):
    """Return HTML link tag for import CSS of *Material Components for the Web*.

    Args:
        debug_latest (:obj:`bool`, optional): True if use MDC of latest
            version in *DEBUG mode*. Specifying False or not DEBUG mode,
            get the supported version.
    Returns:
        str: HTML link tag for downloading CSS of MDC.
    """
    # token.contents = "sass_src 'mdc/materical-components-web.scss'"
    return MdcCssNode.handle_token(parser, token)


@register.simple_tag
def import_js_tag(debug_latest=False):
    """Return HTML script tag for *Material Components for the Web*.

    Args:
        debug_latest (:obj:`bool`, optional): True if use MDC of latest
            version in *DEBUG mode*. Specifying False or not DEBUG mode,
            get the supported version.
    Returns:
        str: HTML script tag for downloading JavaScript of MDC.
    """
    if not settings.DEBUG:
        if hasattr(settings, 'PRODUCT_MDC_JS_PATH'):
            return format_html(
                f'<script src="{settings.PRODUCT_MDC_JS_PATH}"></script>'
            )
        return format_html(
            '<script src="https://unpkg.com/material-components-web@'
            f'{SUPPORTED_MDC_VERSION}/dist/material-components-web.min.js">'
            '</script>'
        )
    if debug_latest:
        return format_html(
            '<script src="https://unpkg.com/material-components-web/'
            'dist/material-components-web.js"></script>'
        )
    if hasattr(settings, 'DEPLOYMENT_MDC_JS_PATH'):
        return format_html(
            f'<script src="{settings.DEPLOYMENT_MDC_JS_PATH}"></script>'
        )
    return format_html(
        '<script src="https://unpkg.com/material-components-web@'
        f'{SUPPORTED_MDC_VERSION}/dist/material-components-web.js"></script>'
    )
