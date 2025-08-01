import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from masterapp import app

def test_generator():
    print("\nREGISTERED ROUTES:")
    for rule in app.url_map.iter_rules():
        print(rule)

    client = app.test_client()
    response = client.get("/api/fake")
    assert response.status_code == 200
