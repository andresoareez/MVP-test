from django.contrib.auth.models import User
from .serializer import DemandaDePecasSerializer
from .models import DemandasDePecas
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.response import Response


class DemandasList(generics.ListAPIView):
    serializer_class = DemandaDePecasSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @property
    def get_queryset(self):
        user = self.request.user
        return DemandasDePecas.objects.filter(anunciante=user)




