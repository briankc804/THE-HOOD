from django.shortcuts import render

# Create your views here.

posts = [
    {
    'author':'Brian',
    'title':'Passionate in Coding',
    'content':'The best site for coding',
    'date_posted':'June 19, 2022',
    },
    
    {'author':'Tonia',
    'title':'Passionate in swiming',
    'Content':'The best swimmer',
    'date_posted':'June 19, 2022',}
]

def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'rubic/home.html', context)

def about(request):
    return render(request, 'rubic/about.html', {'title': 'About'})
