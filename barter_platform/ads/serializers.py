from rest_framework import serializers
from .models import Ad, ExchangeProposal

class AdSerializer(serializers.ModelSerializer):
    """Сериализатор для объявлений пользователей."""

    condition_display = serializers.CharField(source='get_condition_display', read_only=True)

    class Meta:
        model = Ad
        fields = [
            'id', 'user', 'title', 'description', 'image_url', 'category',
            'condition', 'condition_display', 'created_at'
        ]
        read_only_fields = ['id', 'user', 'created_at']
        extra_kwargs = {
            'condition': {'help_text': 'Состояние товара: "new" (новый) или "used" (б/у)'},
        }


class ExchangeProposalSerializer(serializers.ModelSerializer):
    """Сериализатор для предложений обмена."""

    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = ExchangeProposal
        fields = [
            'id', 'ad_sender', 'ad_receiver', 'comment',
            'status', 'status_display', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']
        extra_kwargs = {
            'status': {'help_text': 'Статус предложения: "pending", "accepted", "rejected"'},
        }

