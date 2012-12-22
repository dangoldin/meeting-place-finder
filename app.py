from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('base.html')

@app.route('/dir')
def directions():
    return render_template('dir.html')

# http://maps.googleapis.com/maps/api/directions/json?origin=Toronto&destination=Montreal&sensor=false

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
