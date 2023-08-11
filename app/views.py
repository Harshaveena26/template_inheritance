from django.shortcuts import render

# Create your views here.
def parent_mdb(request):
    return render(request,'parent_mdb.html')



def child(request):
    return render(request,'child.html')




