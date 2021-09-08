import unittest
import json
from classes.main import Main

class VerificarPangramaTests(unittest.TestCase):
    def test_convert_epoch(self):
        epoch = m.convert_epoch("2000-01-01T00:00:00.000Z")
        
        # Assert
        self.assertIsInstance(epoch, int)

    def test_check_HFSI(self):
        j = json.loads('{"merchant": "McDonald\'s", "amount": 10, "time": 1550055601}')
        HFSI = m.check_HFSI(j)
        
        # Assert
        self.assertIsInstance(HFSI, int)

    def test_check_DT(self):
        j = json.loads('{"merchant": "McDonald\'s", "amount": 10, "time": 1550055601}')
        DT = m.check_DT(j)
        
        # Assert
        self.assertIsInstance(DT, int)

if __name__ == '__main__':

    string = '''{"account": {"active-card": true, "available-limit": 100}}
    {"transaction": {"merchant": "Burger King", "amount": 20, "time": "2019-02-13T10:00:00.000Z"}}
    {"transaction": {"merchant": "Habbib's", "amount": 90, "time": "2019-02-13T11:00:00.000Z"}}
    {"transaction": {"merchant": "McDonald's", "amount": 30, "time": "2019-02-13T12:00:00.000Z"}}'''
    content_list = string.split("\n")
    m = Main()
    m.check_ops(content_list)
    unittest.main()
        