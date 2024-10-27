from django.shortcuts import render,redirect
def nanda(request):
    d={"name":"nandass"}
    return render(request,"nanda.html",d)
def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')
def home(request):
    return render(request,'home.html')
def help(request):
    return render(request,'help.html')
def palind(request,s):
    result=(s==s[::-1])
    d={"nanda":result}
    return render(request,'palindrome.html',d)
def redrect(request):
    return redirect("homepage")