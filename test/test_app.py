


def test_app(client):

    res = client.get('/')
    assert res.status_code == 200

def test_dir(one):
    print(one)
    assert one == 12

