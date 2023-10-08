from flask import Flask,render_template,Response

from Test import emotion

detect = emotion()

app = Flask(__name__)

@app.route('/')
def hello_world():
   return render_template('index.html')

def gen(detect):
    
    while True:
        frame = detect.detect_emotion()
        yield(b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        

@app.route('/predict')

def predict():
    return Response(gen(detect),mimetype='multipart/x-mixed-replace;boundary=frame')
if __name__ == '__main__':
   app.run()