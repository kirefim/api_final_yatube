from django.shortcuts import get_object_or_404
from rest_framework import filters, mixins, pagination, viewsets
from rest_framework.permissions import IsAuthenticated

from .permissions import IsAuthorOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer,
                          GroupSerializer, PostSerializer)
from posts.models import Group, Post


class PostViewSet(viewsets.ModelViewSet):
    '''
    Обработка запросов на получение/создание/изменение/удаление публикаций.
    Поддерживаемые HTTP-методы: GET/POST/PUT/PATCH/DELETE.
    '''
    queryset = Post.objects.select_related('author', 'group',)
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    pagination_class = pagination.LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    Обработка запросов на получение доступных групп.
    Поддерживаемые HTTP-методы: GET/.
    '''
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    '''
    Обработка запросов на получение/создание/изменение/удаление
    комментариев к публикациям.
    Поддерживаемые HTTP-методы: GET/POST/PUT/PATCH/DELETE.
    '''
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs.get("post_id"))

    def get_queryset(self):
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())


class FollowViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    '''
    Обработка запросов на получение/создание подписок на авторов публикаций.
    Поддерживаемые HTTP-методы: GET/POST.
    '''
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return (self.request.user.follower)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user,)
