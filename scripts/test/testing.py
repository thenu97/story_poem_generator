import urllib3
import unittest
import pytest
import requests
from flask import abort, url_for

url = "http://35.246.16.90/"

############################################################### testing url ###############################################################
def test_urlmanager_home():
    r = requests.get(url)
    assert r.status_code == 200


def test_getresponse():
    r = requests.get(url)
    assert isinstance(r.text, str)