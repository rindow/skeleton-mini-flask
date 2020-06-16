

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Posts' in response.data
    assert b'Added new post' not in response.data
    assert b'testpost' not in response.data


def test_crud_post(client):
    # login
    response = client.get('/create')
    assert response.status_code == 302
    assert response.headers['Location'] == 'http://localhost/login?next=%2Fcreate'
    response = client.get('/login')
    assert response.status_code == 200
    assert b'>Login<' in response.data
    response = client.post('/login',
        data={'username':'user@demo.com', 'password':'password'})
    assert response.status_code == 302
    assert response.headers['Location'] == 'http://localhost/'
    # get create page
    response = client.get('/create')
    assert response.status_code == 200
    assert b'<input' in response.data
    assert b'Delete' not in response.data
    # send post data
    response = client.post('/create',
        data={'title':'testpost', 'body':'text'})
    assert response.status_code == 302
    assert response.headers['Location'] == 'http://localhost/'
    # get index page
    response = client.get('/')
    assert response.status_code == 200
    assert b'Added new post' in response.data
    assert b'testpost' in response.data
    # get update page
    response = client.get('/update/1')
    assert response.status_code == 200
    assert b'testpost' in response.data
    assert b'Delete' in response.data
    # get update page
    response = client.post('/update/1',
        data={'title':'updatepost', 'body':'newtext'})
    assert response.status_code == 302
    assert response.headers['Location'] == 'http://localhost/'
    response = client.get('/')
    assert response.status_code == 200
    assert b'Update post' in response.data
    assert b'updatepost' in response.data
    response = client.post('/delete/1',
        data={'submit':'Delete'})
    assert response.status_code == 302
    assert response.headers['Location'] == 'http://localhost/'
    response = client.get('/')
    assert response.status_code == 200
    assert b'deleted post' in response.data


def test_get_no_post(client):
    # login
    response = client.get('/update/1')
    assert response.status_code == 302
    assert response.headers['Location'] == 'http://localhost/login?next=%2Fupdate%2F1'
    response = client.get('/login')
    assert response.status_code == 200
    assert b'>Login<' in response.data
    response = client.post('/login',
        data={'username':'user@demo.com', 'password':'password'})
    assert response.status_code == 302
    assert response.headers['Location'] == 'http://localhost/'
    # no post
    response = client.get('/update/1')
    assert response.status_code == 404
    assert b'doesn\'t exist' in response.data
