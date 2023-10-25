from rest_framework.serializers import *
from apps.post.models import Plane, Airlane, Flight

class PlaneSerializer(ModelSerializer):
	class Meta:
		model = Plane
		fields = '__all__'

class AirlaneSerializer(ModelSerializer):
	class Meta:
		model = Airlane
		fields = '__all__'

class FlightSerializer(ModelSerializer):
	class Meta:
		model = Flight
		fields = '__all__'

class PlaneDetailSerializer(ModelSerializer):
	class Meta:
		model = Plane
		fields = '__all__'
class AirlaneDetailSerializer(ModelSerializer):
	class Meta:
		model = Airlane
		fields = '__all__'

class FlightDetailSerializer(ModelSerializer):
	class Meta:
		model = Flight
		fields = '__all__'