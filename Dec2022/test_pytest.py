import pytest
def testmethod():
    x=2
    y=3
    assert x+1==y, "test passed"
    assert x==y , "test failed"

testmethod()
