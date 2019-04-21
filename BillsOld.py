from flask import Flask
app = Flask(__name__)

@app.route('/bills/')



def hello_world():

	bill = 'Mortgage'
	ouputtext = bill+'hello world'
	return ouputtext

if __name__ == '__main__':
   app.run(debug = True)