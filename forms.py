<<<<<<< HEAD
from flask_wtf import FlaskForm
from wtforms import widgets, SelectMultipleField, RadioField

class MultiCheckboxField(SelectMultipleField):
  widget = widgets.ListWidget(prefix_label=False)
  option_widget = widgets.CheckboxInput()


class SimpleForm(FlaskForm):
  universities = [{'id':'1', 'name':'University of Auckland'}, {'id':'2', 'name':'University of Canterbury'}, {'id':'3', 'name':'Victoria University of Wellington'}, {'id':'4', 'name':'University of Waikato'}, {'id':'5', 'name':'Auckland University of Technology'}, {'id':'6', 'name':'Massey University'}, {'id':'7', 'name':'Lincoln University'}, {'id':'8', 'name':'University of Otago'}]
  subjects = [{'id': '1', 'name': 'Calculus'}, {'id': '2', 'name': ' Physics'}, {'id': '3', 'name': ' Chemistry'}, {'id': '4', 'name': ' Visual Arts'}, {'id': '5', 'name': ' Biology'}, {'id': '6', 'name': ' History of Art'}, {'id': '7', 'name': ' History'}, {'id': '8', 'name': ' Health Education'}, {'id': '9', 'name': ' Economics'}, {'id': '10', 'name': ' Classical Studies'}, {'id': '11', 'name': ' Business Studies'}, {'id': '12', 'name': ' Drama'}, {'id': '13', 'name': ' Biology'}, {'id': '14', 'name': ' Earth and Space Science'}, {'id': '15', 'name': ' Agriculture & Horticulture'}, {'id': '16', 'name': ' Home Economics'}, {'id': '17', 'name': ' English'}, {'id': '18', 'name': ' Geography'}, {'id': '19', 'name': ' Religious Studies'}, {'id': '20', 'name': ' Social Studies'}, {'id': '21', 'name': ' Te Reo Maori'}]
  # create a list of value/description tuples
  uni = [(x['id'], x['name']) for x in universities]
  subject = [(x['id'], x['name']) for x in subjects]

  uni_data = MultiCheckboxField('Label', choices=uni)
  subject_data = MultiCheckboxField('Label', choices=subject)

=======
from flask_wtf import FlaskForm
from wtforms import widgets, SelectMultipleField, RadioField

class MultiCheckboxField(SelectMultipleField):
  widget = widgets.ListWidget(prefix_label=False)
  option_widget = widgets.CheckboxInput()


class SimpleForm(FlaskForm):
  universities = [{'id':'1', 'name':'University of Auckland'}, {'id':'2', 'name':'University of Canterbury'}, {'id':'3', 'name':'Victoria University of Wellington'}, {'id':'4', 'name':'University of Waikato'}, {'id':'5', 'name':'Auckland University of Technology'}, {'id':'6', 'name':'Massey University'}, {'id':'7', 'name':'Lincoln University'}, {'id':'8', 'name':'University of Otago'}]
  subjects = [{'id': '1', 'name': 'Calculus'}, {'id': '2', 'name': ' Physics'}, {'id': '3', 'name': ' Chemistry'}, {'id': '4', 'name': ' Visual Arts'}, {'id': '5', 'name': ' Biology'}, {'id': '6', 'name': ' History of Art'}, {'id': '7', 'name': ' History'}, {'id': '8', 'name': ' Health Education'}, {'id': '9', 'name': ' Economics'}, {'id': '10', 'name': ' Classical Studies'}, {'id': '11', 'name': ' Business Studies'}, {'id': '12', 'name': ' Drama'}, {'id': '13', 'name': ' Biology'}, {'id': '14', 'name': ' Earth and Space Science'}, {'id': '15', 'name': ' Agriculture & Horticulture'}, {'id': '16', 'name': ' Home Economics'}, {'id': '17', 'name': ' English'}, {'id': '18', 'name': ' Geography'}, {'id': '19', 'name': ' Religious Studies'}, {'id': '20', 'name': ' Social Studies'}, {'id': '21', 'name': ' Te Reo Maori'}]
  # create a list of value/description tuples
  uni = [(x['id'], x['name']) for x in universities]
  subject = [(x['id'], x['name']) for x in subjects]

  uni_data = MultiCheckboxField('Label', choices=uni)
  subject_data = MultiCheckboxField('Label', choices=subject)

>>>>>>> e348695b14ed8e11a78c654fd157a32156a54054
  radio = RadioField('Label', choices=[('alphabet','Alphabet'),('likes','Likes')], default='alphabet')