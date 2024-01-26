from functools import wraps

from drf_yasg import openapi
from drf_yasg.openapi import Response as SwaggerResponse
from drf_yasg.utils import swagger_auto_schema


def request_currency_info_schema(view_func):
    request_body = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "symbol": openapi.Schema(type=openapi.TYPE_STRING),
        },
        required=["symbol"],
    )

    responses = {201: SwaggerResponse(description="Success")}

    @swagger_auto_schema(request_body=request_body, responses=responses)
    @wraps(view_func)
    def _wrapper(request, *args, **kwargs):
        return view_func(request, *args, **kwargs)

    return _wrapper
