import unittest
from CorporateData import CorporateData

class TestCorporateData(unittest.TestCase):
    def test_singleton_instance(self):
        instance1 = CorporateData.getInstance()
        instance2 = CorporateData.getInstance()
        
        self.assertIs(instance1, instance2, "CorporateData no está implementado como patron Singleton correctamente.")
        
        print("ID de instancia 1:", id(instance1))
        print("ID de instancia 2:", id(instance2))

if __name__ == '__main__':
    unittest.main()