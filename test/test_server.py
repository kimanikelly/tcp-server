from server import *


def test_IP_ADDRESS():
    assert (isinstance(IP_ADDRESS, str) == True)


def test_PORT():
    assert (isinstance(PORT, int) == True)
