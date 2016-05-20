from nose.tools import *
from bin.app import app
from tests.tools import assert_response
import os

def test_index():
#check that we get a 404 on the / url
    resp= app.request("/")
    assert_response(resp)

def test_hello():
#test GET request for /hello    
    resp=app.request("/hello")
    assert_response(resp)
#making sure default values work for form    
    resp= app.request("/hello", method="POST")
    assert_response(resp, contains="Nobody")
#testing expected values    
    data= {'name':'Zed','greet':'Hola'}
    resp= app.request("/hello",method="POST", data=data)
    assert_response(resp, contains="Zed")
    

  