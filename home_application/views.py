# -*- coding: utf-8 -*-

from common.mymako import render_mako_context, render_json
from django.http import HttpResponse
from blueking.component.shortcuts import get_client_by_request
import settings, base64

def home(request):
    """
    首页
    """
    return render_mako_context(request, '/home_application/home.html')


def dev_guide(request):
    """
    开发指引
    """
    return render_mako_context(request, '/home_application/dev_guide.html')


def contactus(request):
    """
    联系我们
    """
    return render_mako_context(request, '/home_application/contact.html')

def jobtrans(request):
    inf = request.POST.get('inf')
    print inf
    client = get_client_by_request(request)


    fin = open("./home_application/test.txt")
    line = fin.readlines()
    fin.close()

    line[32] = "touch /"+inf+".txt"
    fin = open("./home_application/test.txt", "w")
    fin.writelines(line)
    fin.close()
    fin = open("./home_application/test.txt")
    aa = fin.read()
    fin.close()
    print aa
    jobdata = base64.encodestring(aa)

    jobdt= {'app_code': settings.APP_ID,
            'app_secret': settings.APP_TOKEN,
            'bk_token': "TcNjiE-HFALvkUWZ7gPXYr8RlIBAnpSEu2fquiQOE3k",
            'app_id': "2",
            'content': jobdata,
            'ip_list': [
            {
                "ip": "192.168.2.234",
                "source": 1
            }
        ], 'type': 1, 'account': "root"}

    print(jobdt)
    res = client.job.fast_execute_script(jobdt)

    print(res)
    return render_json ({'resshow': inf})
