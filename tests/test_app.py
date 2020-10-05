from app import index


def test_index():
    assert index() == "flaskapp deployed on heroku"
