from flask import Flask, jsonify, request, json, make_response, send_file,render_template

app = Flask(__name__)

@app.route('/')
def dash_overview():
	return render_template('index.html')
@app.route('/index.html')
def dash_overview_2():
	return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)