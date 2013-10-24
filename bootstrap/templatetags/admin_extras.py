from django import template
from django.conf import settings
from django.contrib.admin.views.main import (PAGE_VAR)
from django.utils.html import escape
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def bootstrap_page_number(cl,page_range):
    default_template= u'<div class="pagination"><ul>%(prev)s %(numbers)s %(next)s</ul></div>'
    prev_page = u'<li><a href="%s">&laquo;</a>' % escape(cl.get_query_string({PAGE_VAR: 0}))
    next_page = u'<li><a href="%s">&raquo;</a>' % escape(cl.get_query_string({PAGE_VAR: cl.paginator.num_pages-1}))
    substitutions = {
        'next': next_page,
        'numbers': '',
        'prev': prev_page,
    }

    
    if cl.page_num == 0:
        substitutions['prev'] = '<li class="disabled"><span>&laquo;</span>' 
    elif cl.page_num == cl.paginator.num_pages-1:
        substitutions['next'] = '<li class="disabled"><span>&raquo;</span>' 

    for i in page_range:
        if i == '.':
            substitutions['numbers'] += '... '
        elif i == cl.page_num:
            substitutions['numbers'] += u'<li class="disabled"><span class="this-page">%d</span>'%(i+1)
        else:
            substitutions['numbers'] += u'<li><a href="%s"%s>%d</a>'%(escape(cl.get_query_string({PAGE_VAR: i})), (i == cl.paginator.num_pages-1 and ' class="end"' or ''), i+1)
    return mark_safe(default_template % substitutions)

# settings value
@register.simple_tag
def settings_value(name):
  return getattr(settings, name, "")
