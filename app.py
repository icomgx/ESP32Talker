#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   app.py
@Contact :   851151418@qq.com
@License :   (C)Copyright 2016-2020, iCOMgx's Atai

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020-04-19 21:50   Atai      1.0         None
"""

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/simple', methods=['GET', 'POST'])
def simple():
    if request.method == 'POST':
        test = request.data
        print(test)
        return 'POST'
    elif request.method == 'GET':
        return 'GET'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=720)
