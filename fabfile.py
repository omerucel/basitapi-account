from fabric.api import local

def test_cover():
    local('python basitapi_account/tests/runtests.py --with-coverage --cover-html --cover-package=bastapi_account')

def test():
    local('python basitapi_account/tests/runtests.py')
