#!/usr/bin/python3

from datetime import datetime
import unittest
from models.base_model import BaseModel

class Test_Base_Model(unittest.TestCase):

    def test_created_class(self):
        base = BaseModel()
        self.assertEqual(BaseModel, type(base))
        self.assertEqual(str, type(base.id))
        self.assertEqual(datetime, type(base.created_at))
        self.assertEqual(datetime, type(base.updated_at))

    def test__init__kwargs(self):
        base = BaseModel()
        dic = base.to_dict()
        base2 = BaseModel(**dic)
        self.assertEqual(base.id, base2.id)
        self.assertNotEqual(base, base2)
        base.number = 10
        self.assertEqual(int, type(base.number))
        base.nomber = "carlos"
        self.assertEqual(str, type(base.nomber))

    def test_to_dict(self):
        base = BaseModel()
        dic = base.to_dict()
        self.assertEqual(str, type(dic['updated_at']))
        self.assertEqual(str, type(dic['created_at']))
        self.assertEqual("BaseModel", dic['__class__'])
        self.assertEqual(dict, type(base.to_dict()))

    def test_save(self):
        base = BaseModel()
        date = base.updated_at
        base.save()
        date2 = base.updated_at
        self.assertNotEqual(date, date2)



if __name__ == '__main__':
    unittest.main()
