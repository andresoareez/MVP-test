from .serializer import DemandaDePecasSerializer
from .models import DemandasDePecas
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

#EndPoints para a API, o ModelViewSet da a possibilidade de todos as requesições desejadas para cada
# requisito pedido.


# Endpoints para anunciantes
class DemandasViewSet(viewsets.ModelViewSet):
    queryset = DemandasDePecas.objects.all()
    serializer_class = DemandaDePecasSerializer
    filters_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['anunciante']
    search_fields = ['anunciante', 'Estado', 'Cidade']
    filterset_fields = ['status']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return DemandasDePecas.objects.filter(anunciante=user)


#Endpoints para admin, caso seja necessário acesso por fora do django admin
class AdminViewSet(viewsets.ModelViewSet):
    queryset = DemandasDePecas.objects.all()
    serializer_class = DemandaDePecasSerializer
    filters_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['anunciante']
    search_fields = ['anunciante', 'estado', 'Cidade']
    filterset_fields = ['status']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]




