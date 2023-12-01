# rest_framework
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# django
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import JsonResponse

# import models & serializers
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer, DepositProductsSerializer, DepositOptionSerializer, SavingProductsSerializer, SavingOptionSerializer
from .models import Article, Comment, DepositProducts, DepositOptions, SavingProducts, SavingOptions

# for API key
from django.conf import settings
import requests

# -----게시판 view-----
# ---------------------
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def article_list(request):
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # serializer.save()
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def comment_list(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comments = Comment.objects.filter(article=article)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


# 댓글은 수정하더라도 한 가지의 옵션에서만 수정을 할 수 있기 때문에 파샬...?이 필요 없다구? 
@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
def comment_create(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



# -----예/적금 비교 view-----
# --------------------------

# 예금 데이터 저장
@api_view(['GET'])
def deposit_product_save(request):
    api_key = settings.CMP_API_KEY
    url = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
    pageNo = 1
    while True:
        params = {
            'auth': api_key,
            'topFinGrpNo': '020000',
            'pageNo': pageNo
        }
        response = requests.get(url, params=params).json().get('result')

        # 상품 저장
        for li in response.get('baseList'):
            fin_prdt_cd = li.get('fin_prdt_cd')
            
            # filter를 통해 이미 존재하는 상품에 대한 저장을 피한다.
            existing_instance = DepositProducts.objects.filter(fin_prdt_cd=fin_prdt_cd).first()
            if existing_instance:
                continue
            save_data = {
                'fin_prdt_cd' : fin_prdt_cd,
                'dcls_month' : li.get('dcls_month'),
                'kor_co_nm' : li.get('kor_co_nm'),
                'fin_prdt_nm' : li.get('fin_prdt_nm'),

                'etc_note' : li.get('etc_note'),
                'join_deny' : li.get('join_deny'),
                'join_member' : li.get('join_member'),
                'join_way' : li.get('join_way'),
                'spcl_cnd' : li.get('spcl_cnd'),

            }
            serializer = DepositProductsSerializer(data=save_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()

        # 옵션 저장
        for li in response.get('optionList'):
            save_data = {
                'fin_prdt_cd' : li.get('fin_prdt_cd'),
                'intr_rate_type_nm' : li.get('intr_rate_type_nm'),
                'intr_rate' : li.get('intr_rate'),
                'intr_rate2' : li.get('intr_rate2'),
                'save_trm' : li.get('save_trm'),
            }
            if save_data['intr_rate']:
                pass
            else:
                save_data['intr_rate'] = 0
            
            existing_option = DepositOptions.objects.filter(
                fin_prdt_cd=save_data['fin_prdt_cd'],
                intr_rate_type_nm=save_data['intr_rate_type_nm'],
                save_trm=save_data['save_trm']
            ).first()

            if existing_option:
                continue

            product = DepositProducts.objects.get(fin_prdt_cd = save_data['fin_prdt_cd'])
            options_serializer = DepositOptionSerializer(data=save_data)

            if options_serializer.is_valid(raise_exception=True):
                options_serializer.save(product=product)


        # page의 max값에 도달하지 않았을경우, pageNo를 1 증가시키고 반복한다.
        if response.get('max_page_no') == pageNo:
            break
        pageNo+=1
    # return JsonResponse({'message': 'okay'})
    return JsonResponse(response)


# 적금 데이터 저장
@api_view(['GET'])
def saving_product_save(request):
    api_key = settings.CMP_API_KEY
    url = 'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json'
    pageNo = 1
    while True:
        params = {
            'auth': api_key,
            'topFinGrpNo': '020000',
            'pageNo': pageNo
        }
        response = requests.get(url, params=params).json().get('result')

        # 상품 저장
        for li in response.get('baseList'):
            fin_prdt_cd = li.get('fin_prdt_cd')
            
            # filter를 통해 이미 존재하는 상품에 대한 저장을 피한다.
            existing_instance = SavingProducts.objects.filter(fin_prdt_cd=fin_prdt_cd).first()
            if existing_instance:
                continue
            save_data = {
                'fin_prdt_cd' : fin_prdt_cd,
                'dcls_month' : li.get('dcls_month'),
                'kor_co_nm' : li.get('kor_co_nm'),
                'fin_prdt_nm' : li.get('fin_prdt_nm'),

                'etc_note' : li.get('etc_note'),
                'join_deny' : li.get('join_deny'),
                'join_member' : li.get('join_member'),
                'join_way' : li.get('join_way'),
                'spcl_cnd' : li.get('spcl_cnd'),

            }
            serializer = SavingProductsSerializer(data=save_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()

        # 옵션 저장
        for li in response.get('optionList'):
            save_data = {
                'fin_prdt_cd' : li.get('fin_prdt_cd'),
                'intr_rate_type_nm' : li.get('intr_rate_type_nm'),
                'intr_rate' : li.get('intr_rate'),
                'intr_rate2' : li.get('intr_rate2'),
                'save_trm' : li.get('save_trm'),
                'rsrv_type_nm' : li.get('rsrv_type_nm'),
            }
            existing_option = SavingOptions.objects.filter(
                fin_prdt_cd=save_data['fin_prdt_cd'],
                intr_rate_type_nm=save_data['intr_rate_type_nm'],
                save_trm=save_data['save_trm'],
                rsrv_type_nm=save_data['rsrv_type_nm'],
            ).first()

            if existing_option:
                continue

            if save_data['intr_rate']:
                pass
            else:
                save_data['intr_rate'] = 0
            if save_data['rsrv_type_nm']:
                pass
            else:
                save_data['rsrv_type_nm'] = '-'

            product = SavingProducts.objects.get(fin_prdt_cd = save_data['fin_prdt_cd'])
            options_serializer = SavingOptionSerializer(data=save_data)

            if options_serializer.is_valid(raise_exception=True):
                options_serializer.save(product=product)


        # page의 max값에 도달하지 않았을경우, pageNo를 1 증가시키고 반복한다.
        if response.get('max_page_no') == pageNo:
            break
        pageNo+=1
    # return JsonResponse({'message': 'okay'})
    return JsonResponse(response)


# 예금 DB 출력페이지
@api_view(['GET'])
def deposit_product_DB(request):
    deposit_products = DepositProducts.objects.all()
    serializer = DepositProductsSerializer(deposit_products, many=True)

    for product_data in serializer.data:
        fin_prdt_cd = product_data['fin_prdt_cd']
        options = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
        options_serializer = DepositOptionSerializer(options, many=True)
        product_data['options'] = options_serializer.data

    return Response(serializer.data)

@api_view(['GET'])
def deposit_option_DB(request):
    deposit_options = DepositOptions.objects.all()
    serializer = DepositOptionSerializer(deposit_options, many=True)

    return Response(serializer.data)

# 적금 DB 출력 페이지
@api_view(['GET'])
def saving_product_DB(request):
    saving_products = SavingProducts.objects.all()
    serializer = SavingProductsSerializer(saving_products, many=True)

    for product_data in serializer.data:
        fin_prdt_cd = product_data['fin_prdt_cd']
        options = SavingOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
        options_serializer = SavingOptionSerializer(options, many=True)
        product_data['options'] = options_serializer.data

    return Response(serializer.data)

@api_view(['GET'])
def saving_option_DB(request):
    saving_options = SavingOptions.objects.all()
    serializer = SavingOptionSerializer(saving_options, many=True)

    return Response(serializer.data)


# -----환율 비교 view-----
# -----------------------
@api_view(['GET'])
def exchanges(request):
    api_key = settings.EXC_API_KEY
    url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'
    params = {
        'authkey': api_key,
        'data': 'AP01'
    }
    response = requests.get(url, params=params).json()
    return Response(response) 