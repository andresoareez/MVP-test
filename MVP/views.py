from django.contrib.auth.models import User
from .serializer import DemandaDePecasSerializer
from .models import DemandasDePecas
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics, viewsets
from rest_framework.response import Response


class DemandasViewSet(viewsets.ModelViewSet):
    queryset = DemandasDePecas.objects.all()
    serializer_class = DemandaDePecasSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return DemandasDePecas.objects.filter(anunciante=user)


class AdminDemandasViewSet(viewsets.ModelViewSet):
    queryset = DemandasDePecas.objects.all()
    serializer_class = DemandaDePecasSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]




