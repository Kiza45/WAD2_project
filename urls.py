from django.urls import path

urlspatterns = [
	path('accounts/', include('registration.backends.simple.urls')),
]
