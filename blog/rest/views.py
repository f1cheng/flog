from django.shortcuts import render
from django.views import View 
from django.http import JsonResponse
# Create your views here.
from rest.models import FeeItem
from rest.models import Article
from rest.models import Comment 
from rest.models import User
from rest.permissions import IsAdminUserOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import BasicAuthentication
from rest_framework.authtoken.models import Token

from rest_framework import permissions, pagination
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView


import json
import base64
import time
from django.contrib.auth.hashers import check_password, make_password

class RegisterAPIView(APIView):
    def post(self, request, *args, **kwargs):
        '''
        json format : {'data': [{'a':1, 'b':2}, {'c':3, 'd':4}], 'msg':'create', 'status': 200}
        '''
        body = request.body.decode()
        print("body for user register: ", body)
        item = json.loads(body)
        name = item.get('username')
        pwd = item.get('password')
        email = item.get('email')
        user = User.objects.filter(username=name)
        if user:
            print('user exists')
            return Response({'data': [], 'msg': 'failed to register, name exists', 'status': 200})
        else:
            # Forbidden: /post/article/
            #User.objects.create_user(username=name, password=pwd)
            # to create super user for admin permission
            User.objects.create_superuser(username=name, password=pwd, email=email)
            user = User.objects.get(username=name)
            Token.objects.get_or_create(user=user)
            token = Token.objects.get(user=user)

            userinfo = {
                'token': token.key,
                'username': user.username,
            }
            items = [userinfo]
            result = {'data': items, 'msg': 'succeed to register', 'status': 200}
            return Response(result)


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        '''
        json format : {'data': [{'a':1, 'b':2}, {'c':3, 'd':4}], 'msg':'create', 'status': 200}
        '''
        body = request.body.decode()
        print("body for user login: ", body)
        item = json.loads(body)
        name = item.get('username')
        pwd = item.get('password')
        user = User.objects.filter(username=name)
        if user:
            print('api user exists')
            check_pwd = check_password(pwd, user[0].password)
            if check_pwd:
                user = User.objects.get(username=name)
                Token.objects.get_or_create(user=user)
                token = Token.objects.get(user=user)
            else:
               return Response({'data': [], 'msg': 'failed to login, password wrong', 'status': 200})
        else:
            print('user not exist')
            return Response({'data': [], 'msg': 'failed to login, username wrong', 'status': 200})

        userinfo = {
            'token': token.key,
            'username': user.username,
        }
        items = [userinfo]
        result = {'data': items, 'msg': 'succeed to login', 'status': 200}
        return Response(result)


class ArticleAPIView(APIView):

    #ok one permission_classes = [IsAdminUser,]
    #nok authentication_classes = (TokenAuthentication,)
    #permission_classes = (AllowAny,)
    #permission_classes = (IsAdminUser,)
    #permission_classes = (IsAuthenticated, )
    permission_classes = [IsAdminUserOrReadOnly]
    authentication_classes = [TokenAuthentication,]

    def get(self, request, *args, **kwargs):
        title = request.GET.get('title')
        print('title:', title)
        items = []
        if title:
            items = Article.objects.filter(title__icontains=title)
        else:
            items = Article.objects.all() 
        data_values = []
        for i in items:
            each = {'id': i.id, 'title': i.title, 'description': i.description, 'content': i.content}
            data_values.append(each)
        result = {'data': data_values, 'msg': 'query', 'status': 200} 
        print('result: ', result)
        #return Response(result, json_dumps_params={"ensure_ascii": False})
        return Response(result)

    def post(self, request, *args, **kwargs):
        '''
        json format : {'data': [{'a':1, 'b':2}, {'c':3, 'd':4}], 'msg':'create', 'status': 200}
        '''
        #host = 'http://81.68.228.238:9000/'
        host = 'http://111.230.243.15:9000/'
        #img = request.POST.get('img')
        bb = request.body.decode()
        bb = json.loads(bb)
        #bb = request.POST
        img = bb.get('img')
        print('APIView---')
        '''
        body = request.body.decode()
        item = json.loads(body)
        img = item.get('img')
        '''
        '''
        img = request.POST.get('img')
        '''
        if img is not None:
            print('img ok')
            #img = json.loads(img)
            #img = json.dumps(img)
            print (img)

            img_url = img['url']
            img_name = img['name']
            img_url_list = img_url.split(',')
            img_data = base64.b64decode(img_url_list[1])
            image_name = int(round(time.time() * 1000))
            img_url = 'media/img' + '/' + str(image_name) + '-' + img_name
            with open(img_url, 'wb') as f:
                f.write(img_data)
            u = host + img_url
            result = {'data': u, 'msg': 'create', 'status': 200}
            return Response(result)
        else:
            print('img emtpy')
        #body = request.body.decode()
        #body = request.data.decode()
        #body = request.data
        #body = request.data
        #bb = json.loads(bb)
        body = bb
        print("body: ", body)

        item = body
        #payid = item.get('payid')
        #ret = FeeItem.objects.create(payid=payid, name=name, fee=fee, paydate=paydate)
        ret = Article.objects.create(**item)
        print('ret: ', ret)
        items = [item]
        result = {'data': items, 'msg': 'create', 'status': 200}
        return Response(result)

    def put(self, request, *args, **kwargs):
        '''
        json format : {'data': [{'a':1, 'b':2}, {'c':3, 'd':4}], 'msg':'update', 'status': 200}
        '''
        body = request.body.decode()
        print("put body: ", body)
        item = json.loads(body)
        title = item.get('title')
        #FeeItem.objects.filter(name=name).update(payid=payid, name=name)
        ret = Article.objects.filter(title=title).update(**item)
        print('ret: ', ret) 
        items = [item]
        result = {'data': items, 'msg': 'update', 'status': 200}
        return Response(result)

    def delete(self, request, *args, **kwargs):
        '''
        json format : {'data': [{'a':1, 'b':2}, {'c':3, 'd':4}], 'msg':'delete', 'status': 200}
        '''
        body = request.body.decode()
        print("body: ", body)
        item = json.loads(body)
        title = item.get('title')
        ret = Article.objects.filter(title=title).delete()
        print('ret: ', ret) 
        items = [item]
        result = {'data': items, 'msg': 'delete', 'status': 200}
        return Response(result)


class CommentAPIView(APIView):

    def get(self, request, *args, **kwargs):
        article_id = request.GET.get('article_id')
        print('article_id:', article_id)
        items = []
        if article_id:
            article1 = Article.objects.get(id=article_id)
            if article1:
              items = Comment.objects.filter(article=article1)
        else:
            #items = Comment.objects.all() 
            items = []
        data_values = []
        for i in items:
            each = {'article_id': article_id, 'message': i.message}
            data_values.append(each)
        result = {'data': data_values, 'msg': 'query', 'status': 200} 
        print('result: ', result)
        return Response(result)

    def post(self, request, *args, **kwargs):
        '''
        json format : {'data': [{'a':1, 'b':2}, {'c':3, 'd':4}], 'msg':'create', 'status': 200}
        '''
        bb = request.body.decode()
        bb = json.loads(bb)
        item = bb
        print("body: ", item)
        article_id = item.get('article_id')
        article1 = Article.objects.get(id=article_id)
        msg = item.get('message')
        ret = Comment.objects.create(article=article1, message=msg)
        print('ret: ', ret)
        items = [{'article_id':article_id, 'message':msg}]
        result = {'data': items, 'msg': 'create', 'status': 200}
        return Response(result)

    def put(self, request, *args, **kwargs):
        '''
        Nooooo
        json format : {'data': [{'a':1, 'b':2}, {'c':3, 'd':4}], 'msg':'update', 'status': 200}
        '''
        body = request.body.decode()
        print("put body: ", body)
        item = json.loads(body)
        title = item.get('title')
        #FeeItem.objects.filter(name=name).update(payid=payid, name=name)
        ret = Article.objects.filter(title=title).update(**item)
        print('ret: ', ret) 
        items = [item]
        result = {'data': items, 'msg': 'update', 'status': 200}
        return Response(result)

    def delete(self, request, *args, **kwargs):
        '''
        Nooooo
        json format : {'data': [{'a':1, 'b':2}, {'c':3, 'd':4}], 'msg':'delete', 'status': 200}
        '''
        body = request.body.decode()
        print("body: ", body)
        item = json.loads(body)
        title = item.get('title')
        ret = Article.objects.filter(title=title).delete()
        print('ret: ', ret) 
        items = [item]
        result = {'data': items, 'msg': 'delete', 'status': 200}
        return Response(result)




class DecorationCartView(APIView):
    def get(self, request, *args, **kwargs):
        '''
        json format : {'data': [{'a':1, 'b':2}, {'c':3, 'd':4}], 'msg':'query', 'status': 200}
        '''
        name = request.GET.get('name')
        print('naming:', name)
        items = []
        if name:
            items = FeeItem.objects.filter(name__icontains=name)
        else:
            items = FeeItem.objects.all() 
        data_values = []
        for i in items:
            each = {'payid': i.payid, 'name': i.name, 'fee': i.fee, 'paydate': i.paydate}
            data_values.append(each)
        result = {'data': data_values, 'msg': 'query', 'status': 200} 
        #print('result: ', result)
        #return JsonResponse(result, json_dumps_params={"ensure_ascii": False})
        return Response(result)

    def post(self, request, *args, **kwargs):
        '''
        json format : {'data': [{'a':1, 'b':2}, {'c':3, 'd':4}], 'msg':'create', 'status': 200}
        '''
        body = request.body.decode()
        print("body: ", body) 
        item = json.loads(body)
        #payid = item.get('payid')
        #ret = FeeItem.objects.create(payid=payid, name=name, fee=fee, paydate=paydate)
        ret = FeeItem.objects.create(**item)
        print('ret: ', ret) 
        
        items = [item]
        result = {'data': items, 'msg': 'create', 'status': 200}
        return Response(result)

    def put(self, request, *args, **kwargs):
        '''
        json format : {'data': [{'a':1, 'b':2}, {'c':3, 'd':4}], 'msg':'update', 'status': 200}
        '''
        body = request.body.decode()
        print("body: ", body)
        item = json.loads(body)
        name = item.get('name')
        payid = item.get('payid')
        #FeeItem.objects.filter(name=name).update(payid=payid, name=name)
        ret = 0
        if payid is None:
            ret = FeeItem.objects.filter(name=name).update(**item)
        else:
            ret = FeeItem.objects.filter(payid=payid).update(**item)
        print('ret: ', ret) 
        items = [item]
        result = {'data': items, 'msg': 'update', 'status': 200}
        return Response(result)
    
    def delete(self, request, *args, **kwargs):
        '''
        json format : {'data': [{'a':1, 'b':2}, {'c':3, 'd':4}], 'msg':'delete', 'status': 200}
        '''
        body = request.body.decode()
        print("body: ", body)
        item = json.loads(body)
        name = item.get('name')
        ret = FeeItem.objects.filter(name=name).delete()
        print('ret: ', ret) 
        items = [item]
        result = {'data': items, 'msg': 'delete', 'status': 200}
        return Response(result)
