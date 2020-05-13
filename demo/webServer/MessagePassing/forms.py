from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, IntegerField, HiddenField
from wtforms.validators import DataRequired, Length, Optional, InputRequired

class ScoreForm(FlaskForm):
	pid = HiddenField('Id', [Optional()])
	name = StringField('Name', [Optional()])
	score = IntegerField('Score', [InputRequired()])
	submit = SubmitField('Submit')

	def validate(self):
		if not super(ScoreForm, self).validate():
			return False
		if not self.name.data and not self.pid.data:
			self.name.errors.append('Please Input Name')
			return False
		return True