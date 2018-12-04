#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from operator import and_

from flask import request, jsonify, g, current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

import time

from app import create_app
   
import flask,sys
from flask import request, send_from_directory
from flask import make_response



# reload(sys)
# sys.setdefaultencoding('utf-8')

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

@app.errorhandler(404)
def page_not_found(error):
    #print error
    return jsonify({'status':'504', 'msg': 'page not found!'})

if __name__ == "__main__":
    # ConnectDB().monitor_to_db()
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=True)





