from main import *

account = Account(5000)

def test_getAmount():
    assert account.getBalance() == 5000

def test_withDrawAmount():
    account.withDrawAmount(1000)
    assert account.getBalance() == 4000

def test_depositAmount():
    account.depositAmount(1000)
    assert account.getBalance() == 5000