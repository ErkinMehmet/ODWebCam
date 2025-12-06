import os
from yoloapp.utils.funcs import encodeImageToBase64, decodeBase64ToImage
from flask import Flask, request, jsonify,render_template,Response
from flask_cors import CORS,cross_origin

app=Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
@cross_origin()
def predictRoute():
    try:
        image=request.json['image']
        decodeBase64ToImage(image,clApp.filename)
        # run script, with best weights, size of image of 416, confidence 0.5, source as data/filename
        os.system("cd yolov5/ && python detect.py --weights best.pt --img 416 --conf-thres 0.5 --source ../data/"+clApp.filename)
        opencodedbase64=encodeImageToBase64("data/exp/"+clApp.filename)
        os.system("rm -rf yolov5/runs")
        return jsonify({'image':opencodedbase64})
    except Exception as e:
        print(e)
        return jsonify({'error':str(e)})

@app.route('/live',methods=['GET'])
@cross_origin()
def detectLive():
    try:
        os.system("cd yolov5/ ¦¦ python detect.py --weights best.pt --img 416 --conf .5 --source 0")
        os.system("rm -rf yolov5/runs")
        return "Camera Feed Processed"
    except Exception as e:
        print(e)
        return jsonify({'error':str(e)})



if __name__ == "__main__":
    clApp=ClientApp()
    app.run(host='0.0.0.0', port=8080,debug=True)