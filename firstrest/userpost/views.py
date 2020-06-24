from django.shortcuts import render
from userpost.models import UserPost
from userpost.serializer import UserSerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

# Create your views here.

class UserPostViewSet(viewsets.ModelViewSet): #{
    queryset = UserPost.objects.all()
    serializer_class = UserSerializer 

    # 검색 기능
    filter_backends = [SearchFilter]
    search_fields = ('title',) # 어떤 column을 기반으로 검색할 것인지! 무조건 튜플을 인풋으로 받는다

    # 필터 기능
    def get_queryset(self): #{
        # 여기 내부에서 쿼리셋을 관리하고 queryset 리턴하는게 효율적!
        qs = super().get_queryset()
        # qs = qs.filter(author__id = 2)

        # 지금 만약 로그인이 되어있다면, 로그인한 유저의 글만 필터링 해라
        if self.request.user.is_authenticated:
            qs = qs.filter(author=self.request.user)

        # 만약 로그인이 안되어있다면, 비어있는 쿼리셋을 리턴해라
        else:
            qs = qs.none()

        # .filter .exclude
        return qs
    #}
#}
