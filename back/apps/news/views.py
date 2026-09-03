from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import News
from .serializers import NewsSerializers


@api_view(["GET", "POST"])
def news(request):

    if request.method == "GET":
        news = News.objects.all()
        serializer = NewsSerializers(news, many=True)

        return Response(serializer.data)

    if request.method == "POST":
        serializer = NewsSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["PATCH", "DELETE"])
def news_detail(request, news_id):

    try:
        news = News.objects.get(id=news_id)
    except News.DoesNotExist:
        return Response(
            {"error": "News not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "PATCH":
        serializer = NewsSerializers(
            news,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    if request.method == "DELETE":
        news.delete()

        return Response(
            {"message": "News deleted"},
            status=status.HTTP_204_NO_CONTENT
        )
