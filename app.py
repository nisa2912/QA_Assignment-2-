from flask import Flask


app=Flask(__name__)

@app.route('/')
def index():

	return "Hello,there jojo!"

if __name__='__main__':
	app.run()
    