from flask import Flask, request, jsonify
from fastai.vision.all import *
from pathlib import Path

path = Path('../../export.pkl')

app = Flask(__name__)

learn = load_learner(path)

def predict_input_image(img):
    input_image = PILImage.create(img)
    prediction = learn.predict(input_image)

    return prediction
    

@app.route('/', methods=['GET'])
def index():
    return 'hello world'

@app.route('/api', methods=['POST'])
def prediction():
    pred,pred_idx,probs = predict_input_image(request.files['uploaded_image']) 
       
    return jsonify({
        'prediction': str(pred),
        'probability': str(f'{probs[pred_idx]:.04f}')
    }) 

if __name__ == '__main__':
    app.run(debug=True)