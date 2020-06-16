

def test_register_success(client):
    response = client.get('/register')
    assert response.status_code == 200
    assert b'>Register<' in response.data
    response = client.post('/register',
        data={'username':'user2@demo.com', 'password':'password', 'confirm':'password'})
    assert response.status_code == 302
    assert response.headers['Location'] == 'http://localhost/login'
    response = client.get('/login')
    assert b'User registered' in response.data


def off_test_register_confirm_error(client):
    response = client.get('/register')
    assert response.status_code == 200
    assert b'>Register<' in response.data
    response = client.post('/register',
        data={'username':'user@demo.com', 'password':'password', 'confirm':'wrong'})
    assert response.status_code == 302
    assert response.headers['Location'] == 'http://localhost/register'
    response = client.get('/register')
    assert response.status_code == 200
    assert b'password and confirm do not match' in response.data


def off_test_register_duplicate_error(client):
    response = client.get('/register')
    assert response.status_code == 200
    assert b'>Register<' in response.data
    response = client.post('/register',
        data={'username':'user@demo.com', 'password':'password', 'confirm':'password'})
    assert response.status_code == 302
    assert response.headers['Location'] == 'http://localhost/register'
    response = client.get('/register')
    assert response.status_code == 200
    assert b'The user cannot register' in response.data


def off_test_login_success(client):
    # redirect
    response = client.get('/create')
    assert response.status_code == 302
    assert response.headers['Location'] == 'http://localhost/login?next=%2Fcreate'
    response = client.get('/login?next=%2Fcreate')
    assert response.status_code == 200
    assert b'>Login<' in response.data
    # login
    response = client.post('/login?next=%2Fcreate',
        data={'username':'user@demo.com', 'password':'password'})
    assert response.status_code == 302
    assert response.headers['Location'] == 'http://localhost/create'
    response = client.get('/create')
    assert response.status_code == 200
    assert b'Logged in successfully' in response.data


def off_test_login_password_incorect(client):
    # redirect
    response = client.get('/create')
    assert response.status_code == 302
    assert response.headers['Location'] == 'http://localhost/login?next=%2Fcreate'
    response = client.get('/login?next=%2Fcreate')
    assert response.status_code == 200
    assert b'>Login<' in response.data
    # login
    response = client.post('/login?next=%2Fcreate',
        data={'username':'user@demo.com', 'password':'invalid'})
    assert response.status_code == 302
    assert response.headers['Location'] == 'http://localhost/login'
    response = client.get('/login')
    assert response.status_code == 200
    assert b'Invalid username or password' in response.data


def off_test_login_user_notfound(client):
    # redirect
    response = client.get('/create')
    assert response.status_code == 302
    assert response.headers['Location'] == 'http://localhost/login?next=%2Fcreate'
    response = client.get('/login?next=%2Fcreate')
    assert response.status_code == 200
    assert b'>Login<' in response.data
    # login
    response = client.post('/login?next=%2Fcreate',
        data={'username':'nouser@demo.com', 'password':'password'})
    assert response.status_code == 302
    assert response.headers['Location'] == 'http://localhost/login'
    response = client.get('/login')
    assert response.status_code == 200
    assert b'Invalid username or password' in response.data
