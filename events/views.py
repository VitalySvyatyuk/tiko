from django.utils import timezone
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from .models import Event
from .permissions import EventPermission
from .serializers import EventSerializer, RegisterSerializer


class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def get_queryset(self):
        if self.action == 'mine':
            return self.queryset.filter(owner=self.request.user)
        return self.queryset

    def get_permissions(self):
        if self.action in ['destroy', 'update', 'partial_update']:
            self.permission_classes = [EventPermission]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=False, methods=['GET'])
    def mine(self, request):
        return self.list(request)

    @action(detail=True, methods=['POST'])
    def register(self, request, pk=None):
        event = self.get_object()
        if timezone.now() < event.start_date:
            event.attendees.add(request.user)
            return Response(
                {'result': f'You have registered to event {event.name}'}
            )
        return Response(
            {'result': "Can't register to the past event"},
            status=HTTP_400_BAD_REQUEST
        )

    @action(detail=True, methods=['POST'])
    def unregister(self, request, pk=None):
        event = self.get_object()
        if timezone.now() < event.start_date:
            event.attendees.remove(request.user)
            return Response(
                {'result': f'You have unregistered from event {event.name}'}
            )
        return Response(
            {'result': "Can't unregister from the past event"},
            status=HTTP_400_BAD_REQUEST
        )
