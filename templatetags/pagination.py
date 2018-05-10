from django.contrib.humanize.templatetags.humanize import intcomma
from django.template import Library
from django.utils.html import format_html

from utilities.web import add_query_to_url

register = Library()


@register.simple_tag
def paginator_number(request, page_obj):
    return paginater_num(request,
                         page_obj.paginator.num_pages,
                         page_obj.number)


@register.simple_tag
def paginater_num(request, num_pages, page_number):
    results = []
    edge_number = 2
    center_number = 3
    nav_icon = {
        'disable': '<span class="mdcd-button-like mdc-button--dense'
                   ' mdcd-button--disabled">'
                   '<i class="material-icons">{}</i>'
                   '</span>',
        'able':    '<a href="{}" class="mdc-button mdc-button--dense">'
                   '<i class="material-icons">{}</i>'
                   '</a>'
    }
    if page_number == 1:
        results.append(nav_icon['disable'].format('chevron_left'))
    else:
        results.append(nav_icon['able'].format(
            add_query_to_url(request, 'page', page_number - 1),
            'chevron_left',
        ))
    for i in range(1, num_pages+1):
        if i <= edge_number or num_pages - edge_number < i \
                or abs(page_number - i) <= center_number:
            if i == page_number:
                results.append('<span class="mdcd-button-like'
                               f' mdc-button--dense current">{intcomma(i)}'
                               '</span>')
            else:
                results.append(
                    f'<a href="{add_query_to_url(request, "page", i)}"'
                    f' class="mdc-button mdc-button--dense">{intcomma(i)}</a>'
                )
        elif edge_number + 1 == i < page_number \
                or num_pages - edge_number == i > page_number:
            results.append(nav_icon['disable'].format('more_horiz'))
    if page_number == num_pages:
        results.append(nav_icon['disable'].format('chevron_right'))
    else:
        results.append(nav_icon['able'].format(
            add_query_to_url(request, 'page', page_number + 1),
            'chevron_right',
        ))
    return format_html('\n'.join(results))
