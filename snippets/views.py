# Create your views here.
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from snippets.Serializer.SnippetSerializer import SnippetSerializer
from snippets.models import Snippet


@api_view(["GET"])
def snippet_list(_):
    snippets = Snippet.objects.all()
    # シリアライザを使用してモデルをシリアライズ
    serializer = SnippetSerializer(snippets, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def snippet_new(request: HttpRequest) -> HttpResponse:
    """
    Create a new code snippet.
    """
    serializer = SnippetSerializer(data=request.data)
    if serializer.is_valid():
        # データを保存
        serializer.save()
        # レスポンスを返す
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    # データが無効な場合はエラーメッセージを返す
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def snippet_detail(request, snippet_id):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=snippet_id)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
