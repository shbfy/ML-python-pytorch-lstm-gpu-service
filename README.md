# ML-python-pytorch-lstm-gpu-service

Quickstart project for executing an IMDB classifier using the PyTorch framework on a GPU.

Running `pip install requirements.txt` and then python `app.py` will start the app on localhost where the user can send POST requests to perform inference.

### API

**Method**|**Pattern**|**Handler**|**Action**
:-----:|:-----:|:-----:|:-----:
POST|/imdb|IMDB|Classify a given movie review for positive and negative sentiment

### Local testing

Execute a prediction using a POST request.

`curl -X "POST" "http://localhost:8080/imdb \
      -H "Content-Type: text/plain \
      -d "Awesome movie!"`
