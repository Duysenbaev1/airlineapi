from django.db.models import *

class Plane(Model):
	name = CharField('Name', max_length=256)
	characteristics = CharField('characteristics', max_length=256, blank=True, null=True)
	capacity = IntegerField('capacity')
	def __str__(self):
		return f'{self.name}'

class Airlane(Model):
	name = CharField('Name', max_length=256)
	created_at = DateTimeField('Date', auto_now_add=True)
	planes = ForeignKey(Plane, on_delete=CASCADE)
	
	def __str__(self):
		return f'{self.name}'

class Flight(Model):
	from_1 = CharField('From', max_length=256)
	to = CharField('To', max_length=256)
	plane = ForeignKey(Plane, on_delete=CASCADE)
	airlane = ForeignKey(Airlane, on_delete=CASCADE)
	price = IntegerField('Price')

	def __str__(self):
		return f'{self.from_1}'

