from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, StringField
from wtforms.validators import DataRequired, Length

from app.utils.validators import Unique, Exists, IsNumeric
from app.models import Client, Order, Product


class AddOrderForm(FlaskForm):
	class Meta:
		csrf = False

	order_id = StringField('№', validators=[
		Unique(
			model=Client, 
			field=Client.order_id,
			message='Замовлення з таким номером уже існує.'),
		IsNumeric(message='Номер замовлення введено неправильно.')
		])
	first_name = StringField('Ім\'я')
	second_name = StringField('Прізвище')
	mobile_number = StringField('Номер тел.', validators=[
		IsNumeric(message='Номер телефону введено неправильно.')
		])

	product_name = StringField('Назва', validators=[
		Exists(
			model=Product, 
			field=Product.product_name,
			message='Товару з такою назвою не існує.'),])
	product_amount = StringField('Кількість')

	submit = SubmitField('Зберегти')

class AddProductForm(FlaskForm):
	class Meta:
		csrf = False

	product_name = StringField('Назва', validators=[
		Unique(
			model=Product,
			field=Product.product_name,
			message='Такий товар уже існує.')])
	product_price = StringField('Ціна', validators=[
		IsNumeric(message='Ціну введено неправильно.')])

	add_submit = SubmitField('Додати')


class DeleteProductForm(FlaskForm):
	class Meta:
		csrf = False

	del_name = StringField('')

	del_submit = SubmitField('Видалити')
