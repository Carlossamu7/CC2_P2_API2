import unittest
import json
import sys, os.path
from server import *

class Test_API2(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_v2_24h(self):
        response = self.app.get('/servicio/v2/prediccion/24horas')
        self.assertEqual(response.status_code, 200)

    def test_v2_48h(self):
        response = self.app.get('/servicio/v2/prediccion/48horas')
        self.assertEqual(response.status_code, 200)

    def test_v2_72h(self):
        response = self.app.get('/servicio/v2/prediccion/72horas')
        self.assertEqual(response.status_code, 200)
