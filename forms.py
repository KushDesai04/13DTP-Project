from flask_wtf import FlaskForm
from wtforms import widgets, SelectMultipleField, SubmitField

class MultiCheckboxField(SelectMultipleField):
  widget = widgets.ListWidget(prefix_label=False)
  option_widget = widgets.CheckboxInput()


class SimpleForm(FlaskForm):
  universities = [{'id':'1', 'name':'University of Auckland'}, {'id':'2', 'name':'University of Canterbury'}, {'id':'3', 'name':'Victoria University of Wellington'}, {'id':'4', 'name':'University of Waikato'}, {'id':'5', 'name':'Auckland University of Technology'}, {'id':'6', 'name':'Massey University'}, {'id':'7', 'name':'Lincoln University'}, {'id':'8', 'name':'University of Otago'}]
  # create a list of value/description tuples
  uni = [(x['id'], x['name']) for x in universities]
#   print(uni)
  test = MultiCheckboxField('Label', choices=uni)
  submit = SubmitField()