from rest_framework import viewsets, permissions
from .models import Ad, ExchangeProposal
from .serializers import AdSerializer, ExchangeProposalSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class AdViewSet(viewsets.ModelViewSet):
    """
    Эндпоинт для управления объявлениями.

    list:
    Получение списка всех объявлений (с возможностью фильтрации).

    Возможные параметры фильтрации:
    - category: фильтрация по категории
    - condition: фильтрация по состоянию товара (new/used)
    - search: ключевые слова в заголовке и описании
    """

    queryset = Ad.objects.all().order_by('-created_at')
    serializer_class = AdSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category', 'condition']
    search_fields = ['title', 'description']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ExchangeProposalViewSet(viewsets.ModelViewSet):
    """
    Эндпоинт для управления предложениями обмена.

    list:
    Получение всех предложений.

    retrieve:
    Получение одного предложения по ID.

    create:
    Создание нового предложения.

    update:
    Обновление статуса предложения.

    destroy:
    Удаление предложения.
    """

    queryset = ExchangeProposal.objects.all().order_by('-created_at')
    serializer_class = ExchangeProposalSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

