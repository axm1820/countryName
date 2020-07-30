#!/usr/bin/python
import requests
import pytest
import sys
import json
import pytest

def main(argv):
 testCountry()
 testCountry2()

def getCapital(country):
 url = "https://restcountries.eu/rest/v2/name/{country}".format(country=country)
 response = requests.get(url)
 json_data = response.json()
 if (len(json_data)) >= 2:
  return json_data[1][u'capital']
 else:
  return json_data[0][u'capital']


def testCountry():
    assert getCapital("india") == "New Delhi"
    assert getCapital("pakistan") == "Islamabad"

def testCountry2():
    assert getCapital("america") != "Washington"
    assert getCapital("an") != "Islamabad"


if __name__  == "__main__":
 main()
