#!/usr/bin/python
import json
import time

import falcon
import jsonpickle as jsonpickle
import onnx
import onnxruntime as ort
from torch import nn

PORT_NUMBER = 8080
start = time.time()

# Load the ONNX model
model = onnx.load("model.onnx")

# Check that the IR is well formed
onnx.checker.check_model(model)

so = ort.SessionOptions()
so.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL
sess = ort.InferenceSession('model.onnx', so)

# Capture metadata on model
input_name = sess.get_inputs()[0].name
output_name = sess.get_outputs()[0].name
input_len = model.graph.input[0].type.tensor_type.shape.dim[1].dim_value

# Load preprocessing step
with open('processor.json') as f:
    TEXT = jsonpickle.loads(f.read())

end = time.time()
print("Loading time: {0:f} secs)".format(end - start))


# API Handler
class IMDB(object):
    """Handles sentiment prediction tests for IMDB dataset"""

    def on_get(self, req, resp):
        resp.body = json.dumps(
            {"message": 
            "This service verifies a model using the IMDB Test data set. "
            "Invoke by sending a POST request to the /imdb endpoint. "
            "The client accepts plain/text requests"})
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        req.client_accepts('text/plain')
        doc = str(req.stream.read())
        processed = TEXT.process(([TEXT.preprocess(doc)]))
        padded = nn.ConstantPad1d(
            (0, input_len - processed.shape[1]), 0)(processed)
        result = sess.run([output_name], {input_name: padded.numpy()})

        # Subset results
        neg = str(round(result[0][0][0], 3))
        pos = str(round(result[0][0][1], 3))

        payload = {"Negative Proba": neg, "Positive Proba": pos}
        resp.content_type = "application/json"
        resp.body = json.dumps(payload)
