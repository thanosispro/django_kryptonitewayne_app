from django.shortcuts import render, HttpResponse, redirect
from .models import games , comments ,replies
from django.db.models import Q
# Create your views here.
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils import timezone

def home(request):
    return render(request, 'home/index.html')


def all_games(request):
    gaming = games.objects.all()
    category=[]
  
    for game in gaming:
         category.append(game.category)
    category=set(category)
    print(category)
    if(request.method == 'POST'):
        category_list=request.POST.get('category')
        print('a',category_list)
        print(category_list)
        if(category_list==' '):
            print('nice')
            category_q=games.objects.all()
        else:
             category_q=games.objects.filter(category=category_list)
        print(category_q)
        search_q = request.POST.get('search')
        q1 = Q(heading__icontains=search_q)
        q2 = Q(search__icontains=search_q)
        gaming = category_q.filter(q1 | q2)
        print(gaming,'that')
        return render(request, 'home/games.html', {'games': gaming,'category':category})
    
    print(gaming)
    return render(request, 'home/games.html', {'games': gaming,'category':category})


def games_post(request, id):
    actual_game = games.objects.filter(games_id=id)[0]
    actual_game.total_views+=1
    actual_game.save()
    print(actual_game)
    total_comments=comments.objects.filter(comment_id=actual_game)
    total_reply=replies.objects.all()
    
    return render(request, 'home/games_post.html', {'game': actual_game,'comments':total_comments,'replies':total_reply})


def handle_login(request):
    if(request.method == 'POST'):
        username = request.POST.get('susername')
        password = request.POST.get('spassword')
        user = authenticate(username=username, password=password)
        if(user is not None):
        	login(request, user)
        	messages.success(request, 'Successfully logged in into your account')
        else:
        	messages.error(request, 'Invalid Credentials2')
        previous_url = request.META.get('HTTP_REFERER', '/')
        return redirect(previous_url)
    else:
    	return HttpResponse('nice')


def handle_signup(request):

    if(request.method == 'POST'):

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        previous_url = request.META.get('HTTP_REFERER', '/')
        if User.objects.filter(username=username).exists():
        	messages.error(request,'Name already exist')
        	return redirect(previous_url)
        user = User.objects.create_user(username=username, password=password)
        user.email = email
        user.save()
        messages.success(request,'You have created your account ')
        print('nice')
        # Default to '/' if no referrer is found
        
        return redirect(previous_url)
    else:
    	return HttpResponse('404 internal errror')


def handle_logout(request):
	logout(request)
	previous_url=request.META.get('HTTP_REFERER', '/')
	return redirect(previous_url)

def handle_comments(request):
    if request.method=='POST':
        person=request.user
        comment=request.POST.get('comment',default=' ')
        id=request.POST.get('id')
        print(id)
        
        print('here')
        game_id=games.objects.filter(games_id=id).first()
        print('nice',game_id,id)
        post_comment=comments(person=person,comment=comment,comment_id=game_id,date=timezone.now())
        post_comment.save()
        previous_url=request.META.get('HTTP_REFERER', '/')
        messages.success(request,'Your comment has been poseted')
	    
        return redirect(previous_url)

    return HttpResponse('404')

def handle_replies(request):
    if(request.method=='POST'):
        print('nice one')
        reply=request.POST.get('reply')
        comment_id=request.POST.get('id')
        print(comment_id)
        print('that1')
        reply_id=comments.objects.filter(comments_id=comment_id).first()
        previous_url=request.META.get('HTTP_REFERER', '/')
        print('that')
        post_reply=replies(reply=reply,reply_id=reply_id,person=request.user,date=timezone.now())
        print('this')
        post_reply.save()
        messages.success(request,'Your comment has been poseted')

	   

        return redirect(previous_url)

    return HttpResponse('404')     