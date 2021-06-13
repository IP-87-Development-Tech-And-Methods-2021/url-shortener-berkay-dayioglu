def test_redirect(testapp):
    res = testapp.get('/test', status=302)
    assert 'https://google.com' in res.location


def test_notfound(testapp):
    res = testapp.get('/badurl', status=404)
    assert res.status_code == 404
