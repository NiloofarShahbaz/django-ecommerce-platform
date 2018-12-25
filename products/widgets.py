from django_filters.widgets import LinkWidget
from django.forms.utils import flatatt
from django.utils.safestring import mark_safe


class CustomLinkWidget(LinkWidget):
    def option_string(self):
        return '<div class="mr-2">' \
               '<i class="fas fa-angle-left text-secondary ml-1"></i>' \
               '<a%(attrs)s href="?%(query_string)s">%(label)s</a>' \
               '</div>'

    def render(self, name, value, attrs=None, choices=(), renderer=None):
        if not hasattr(self, 'data'):
            self.data = {}
        if value is None:
            value = ''
        final_attrs = self.build_attrs(self.attrs, extra_attrs=attrs)
        output = ['<div%s>' % flatatt(final_attrs)]
        options = self.render_options(choices, [value], name)
        if options:
            output.append(options)
        output.append('</div>')
        return mark_safe('\n'.join(output))
