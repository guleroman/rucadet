from flask import Flask, jsonify, request, json, make_response, send_file,render_template
from flask_sslify import SSLify

from OpenSSL import SSL
context = SSL.Context(SSL.PROTOCOL_TLSv1_2)
context.use_privatekey_file('web.key')
context.use_certificate_file('web.crt')

app = Flask(__name__)



@app.route('/')
def dash_overview():
	return render_template('index.html')
@app.route('/index.html')
def dash_overview_2():
	return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug = True, ssl_context = context)