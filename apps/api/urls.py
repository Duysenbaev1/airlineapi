from .views import PlaneAPIView, AirlaneAPIView, FlightAPIView
from .views import PlaneDetailAPIView, AirlaneDetailAPIView, FlightDetailAPIView
from django.urls import path, include

urlpatterns = [
	path('plane/', PlaneAPIView.as_view()),
	path('plane/<int:pk>/', PlaneDetailAPIView.as_view()),

	path('airplane/', AirlaneAPIView.as_view()),
	path('airplane/<int:pk>/', AirlaneDetailAPIView.as_view()),

	path('flight/', FlightAPIView.as_view()),
	path('flight/<int:pk>/', FlightDetailAPIView.as_view()),

	path('auth/', include('dj_rest_auth.urls'))

]