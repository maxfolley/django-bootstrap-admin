from django.contrib.admin.widgets import AdminFileWidget
from django.forms import CharField
from django.forms.util import flatatt
from django.forms.widgets import ClearableFileInput, Textarea, Widget
from django.utils.encoding import force_unicode
from django.utils.html import escape, conditional_escape
from django.utils.safestring import mark_safe

class PrettyFileWidget(AdminFileWidget):

    default_template = u'<div class="pretty-file-upload">%(pretty_input)s</div>'
    pretty_input = u'<div class="pretty-file-input"><div class="input-prepend"><button class="btn" type="button"><i class="icon-picture"></i></button><input class="span2" id="appendedInputButton" size="16" disabled="disabled" type="text" value="%(input_placeholder)s" ></div>%(input)s</div>'
    template_with_link = u'<div class="pretty-file-upload"><span>Currently: %(link)s</span> %(pretty_input)s</div>'

    def render(self, name, value, attrs=None):
        substitutions = {
            'input': super(ClearableFileInput, self).render(name, value, attrs), 
            'input_placeholder': 'No file chosen...',
        }

        if value and hasattr(value, 'url'):
            template = self.template_with_link
            substitutions['input_placeholder'] = "Change file..."
            substitutions['link'] = (u'<a href="%s" target="_blank">%s</a>' % (escape(value.url), escape(force_unicode(value))))
            substitutions['pretty_input'] = self.pretty_input % substitutions
        else:
            template = self.default_template
            substitutions['input_placeholder'] = "No file chosen..."
            substitutions['pretty_input'] = self.pretty_input % substitutions

        return mark_safe(template % substitutions)
        #return mark_safe("<div class='input-prepend'><button class='btn' type='button'><i class='icon-picture'></i></button><input class='span2' id='appendedInputButton' size='16' type='text'>" + template + "</div>")

class PrettyTextWidget(Widget):
  template = u"""
  <div class="pretty-text">
    <div id="wysihtml5-toolbar" style="display: none;">
      <a data-wysihtml5-command="bold" class="btn">bold</a>
      <a data-wysihtml5-command="italic" class="btn">italic</a>
      <a data-wysihtml5-command="createLink" class="btn">insert link</a>
      <div data-wysihtml5-dialog="createLink" style="display: none;">
        <input data-wysihtml5-dialog-field="href" value="http://" class="text" type="text">
        <a data-wysihtml5-dialog-action="save" class="btn">OK</a> <a data-wysihtml5-dialog-action="cancel" class="btn">Cancel</a>
      </div>
    </div>
    <textarea%s>%s</textarea>
  </div>
  """
  substitutions = {}
  def render(self, name, value, attrs=None):
    if value is None: value = ''
    attrs['id'] = 'wysihtml5-textarea'
    final_attrs = self.build_attrs(attrs, name=name)
    return mark_safe(self.template  % (flatatt(final_attrs),
                      conditional_escape(force_unicode(value))))
