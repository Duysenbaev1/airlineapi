from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *

from .serializers import PlaneSerializer, AirlaneSerializer, FlightSerializer
from .serializers import PlaneDetailSerializer, AirlaneDetailSerializer, FlightDetailSerializer
from apps.post.models import Plane, Airlane, Flight

class PlaneAPIView(APIView):
	def get(self, request):
		plane = Plane.objects.all()
		serializer = PlaneSerializer(plane, many=True)
		return Response(serializer.data, status=HTTP_200_OK)

	def post(self, request):
		serializer = PlaneSerializer(request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=HTTP_201_CREATED)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class PlaneDetailAPIView(APIView):
	def get(self, request, pk):
		try:
			plane = Plane.objects.get(pk=pk)
			serializer = PlaneDetailSerializer(plane)
			return Response(serializer.data, status=HTTP_200_OK)
		except Plane.DoesNotExist:
			return Response({"detail": "Plane not found"}, status=HTTP_404_NOT_FOUND)

	def patch(self,request,pk):
		plane = Plane.objects.get(pk=pk)
		serializer = PlaneDetailSerializer(plane, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=HTTP_202_ACCEPTED)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

	def delete(self,request,pk):
 		plane = Plane.objects.get(pk=pk)
 		plane.delete()
 		return Response(status=status.HTTP_204_NO_CONTENT)

# AIRPLANE

class AirlaneAPIView(APIView):
	def get(self, request):
		airlane = Airlane.objects.all()
		serializer = AirlaneSerializer(airlane, many=True)
		return Response(serializer.data, status=HTTP_200_OK)

	def post(self, request):
		serializer = AirlaneSerializer(request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=HTTP_201_CREATED)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class AirlaneDetailAPIView(APIView):
	def get(self, request, pk):
		try:
			airlane = Airlane.objects.get(pk=pk)
			serializer = AirlaneDetailSerializer(airlane)
			return Response(serializer.data, status=HTTP_200_OK)
		except Airlane.DoesNotExist:
			return Response({"detail": "Airlane not found"}, status=HTTP_404_NOT_FOUND)


	def patch(self,request,pk):
		airlane = Airlane.objects.get(pk=pk)
		serializer = AirlaneDetailSerializer(airlane, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=HTTP_202_ACCEPTED)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

	def delete(self,request,pk):
 		airlane = Airlane.objects.get(pk=pk)
 		airlane.delete()
 		return Response(status=status.HTTP_204_NO_CONTENT)



# FLIGHT

class FlightAPIView(APIView):
	def get(self, request):
		flight = Flight.objects.all()
		serializer = FlightSerializer(flight, many=True)
		return Response(serializer.data, status=HTTP_200_OK)

	def post(self, request):
		serializer = FlightSerializer(request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=HTTP_201_CREATED)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class FlightDetailAPIView(APIView):
	def get(self, request, pk):
		try:
			flight = Flight.objects.get(pk=pk)
			serializer = FlightDetailSerializer(flight)
			return Response(serializer.data, status=HTTP_200_OK)
		except Flight.DoesNotExist:
			return Response({"detail": "Flight not found"}, status=HTTP_404_NOT_FOUND)
	def patch(self,request,pk):
		flight = Flight.objects.get(pk=pk)
		serializer = FlightDetailSerializer(flight, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=HTTP_202_ACCEPTED)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

	def delete(self,request,pk):
 		flight = Flight.objects.get(pk=pk)
 		flight.delete()
 		return Response(status=status.HTTP_204_NO_CONTENT)