from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CurrencyModel
from .serializers import CurrencySerializer


class CurrencyViewSet(GenericAPIView):
    queryset = CurrencyModel.objects.all()
    serializer_class = CurrencySerializer
    http_method_names = ["post"]

    def get_coin_info(self, symbol):
        return {}

    def get(self, request, *args, **kwargs):
        symbol = request.data.get("symbol")

        if not symbol:
            return Response(
                {"error": "Symbol is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        coin_info = self.get_coin_info(symbol)

        return Response(coin_info, status=status.HTTP_200_OK)
