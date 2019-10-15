#!/bin/python3.6

import os
from flask import Flask, flash, render_template, request, redirect, session, make_response
import search
import hlight

App = Flask(__name__)
App.config["DEBUG"] = True
App.secret_key = 'dong1lkim, University of Seoul'

@App.route('/', methods=['GET','POST',])
def index():
    if request.method == 'POST':
        rctgr = request.form.getlist('ctgr')
        ctgr = rctgr.pop(0)
        for c in rctgr: ctgr += ',' + c
        sort = request.form['sort'] if 'sort' in request.form else ''
        product = request.form['product']
        return redirect('?s='+request.form['s']+'&product='+product+'&sort='+sort+'&ctgr='+ctgr)

    s = request.args['s'] if 's' in request.args else None
    p = int(request.args['p']) if 'p' in request.args else 1
    sort = request.args['sort'] if 'sort' in request.args else None
    ctgr = request.args['ctgr'].split(',') if 'ctgr' in request.args else None
    product = request.args['product'] if 'product' in request.args else None

    if s == None: return render_template('index.html')

    rctgr,temp = list(ctgr),list(ctgr)
    ctgr = temp.pop(0)
    for c in temp: ctgr += ',' + c

    result,total = search.issue(s,page=p,product=product,sort=sort,ctgr=rctgr)

    pagination = {'current':p,"total":total//10,"max":total}
    opts = {'sort':sort,'product':product,'ctgr':ctgr,'rctgr':rctgr}

    if total == 0: result,total = search.issue(s,page=p,product=product,sort=sort,ctgr=rctgr,op='or')

    for i in result: i['_source'].update({'Issue Details':hlight.hlight_term(i['_source']['Issue Details'],s.split())})

    return make_response(
        render_template('result.html',s=s,pagination=pagination,result=result,opts=opts,hist=[])
    )

@App.route('/issueView', methods=['GET'])
def issueView():
    issueId = request.args['issueId']
    return redirect('https://ims.tmaxsoft.com/tody/ims/issue/issueView.do?issueId='+issueId)

if __name__ == '__main__': App.run(host='0.0.0.0',port='8888')
