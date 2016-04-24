from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import numpy as np
import json
import asterion.calculate_orbits as co
import asterion.read_database as rd

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

@csrf_exempt    
def check(request):
    if request.method == 'POST':
        a = float(request.POST.get('a'))
        e = float(request.POST.get('e'))
        w = float(request.POST.get('w'))
        i = float(request.POST.get('i'))
        om = float(request.POST.get('om'))
        
        i_r = np.radians(i)
        om_r = np.radians(om)
        w_r = np.radians(w)
        
        q = a * (1 - e)
        clf = rd.loadObject('classifier.p')
        pha = clf.predict(np.array([q, w]))[0]
        
        moid = co.get_moid(a, e, w_r, i_r, om_r)
        
        response_data = {}
        response_data['moid'] = moid
        response_data['pha'] = 1 if (moid <= 0.05) else 0

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
    
def about(request):
    return render(request, "index2.html")
