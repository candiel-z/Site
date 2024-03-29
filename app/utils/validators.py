from wtforms.validators import ValidationError


class Unique(object):
	def __init__(self, model, field, message):
		self.model = model
		self.field = field
		self.message = message

	def __call__(self, form, field):
		check = self.model.query.filter(self.field == field.data).first()
		if check:
			raise ValidationError(self.message)


class Exists(object):
	def __init__(self, model, field, message):
		self.model = model
		self.field = field
		self.message = message

	def __call__(self, form, field):
		check = self.model.query.filter(self.field == field.data).first()
		if not check:
			raise ValidationError(self.message)


class IsNumeric(object):
	def __init__(self, message):
		self.message = message

	def __call__(self, form, field):
		check = not field.data.isnumeric()
		if check:
			raise ValidationError(self.message)
