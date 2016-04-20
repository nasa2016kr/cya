from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    h = request.POST.get('h', '')
    
    resultClass = ''
    result = ''
    if (h != ''):
        if (h == '1'):
            resultClass = "resultSuccess"
            result = 'CLEAN'
        else:
            resultClass = "resultFail"
            result = 'RISK: 82.4%'

    return render(request, "index.html", {
        'h': h,
        'resultClass': resultClass,
        'result': result
    })