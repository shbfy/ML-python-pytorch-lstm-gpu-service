# Using py.test framework
from service import IMDB


def test_example_message(client):
    """Example message should be returned"""
    client.app.add_route('/imdb', IMDB())

    result = client.simulate_get('/imdb')
    assert result.json == {
        'message':
            'This service verifies a model using the IMDB Test data set. '
            'Invoke by sending a POST request to the /imdb endpoint. '
            'The client accepts plain/text requests'}


def test_classification_request(client):
    """Sentiment classification for request should be returned"""
    client.app.add_route('/imdb', IMDB())

    result = client.simulate_post('/imdb',
                                  headers={"Content-Type": "text/plain"},
                                  body="Great movie!")
    assert result.status == "200 OK", \
        "Test will fail until a trained model has been approved"
    assert "Negative Proba" in result.json
    assert "Positive Proba" in result.json
