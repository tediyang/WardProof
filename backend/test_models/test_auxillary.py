#!/usr/bin/python3

"""
    Contains the TestAuxillaryGuardianDocs classes
"""

import inspect
import models
import pycodestyle
import unittest

BaseModel = models.basemodel.BaseModel
AuxillaryGuardian = models.auxillary.AuxillaryGuardian
auxillary_doc = models.auxillary.__doc__


class TestAuxillaryGuardianDocs(unittest.TestCase):
    """Tests to check the doc and style of AuxillaryGuardian class"""

    @classmethod
    def setUpClass(self):
        """Set up for docstring tests by extracting all the function
           object.
        """
        self.auxillary_funcs = inspect.getmembers(AuxillaryGuardian,
                                                  inspect.isfunction)

    def test_pep8_conformance(self):
        """Test that models/auxillary.py conforms to PEP8 (pycodestyle)."""
        for path in ['models/auxillary.py',
                     'test_auxillary.py']:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_auxillary_docstring(self):
        """Test for the existence of model docstring"""
        self.assertIsNot(auxillary_doc, None,
                         "auxillary.py needs a docstring")
        self.assertTrue(len(auxillary_doc) > 1,
                        "auxillary.py needs a docstring")

    def test_auxillary_class_docstring(self):
        """Test for the AuxillaryGuardian class docstring"""
        self.assertIsNot(AuxillaryGuardian.__doc__, None,
                         "AuxillaryGuardian class needs a docstring")
        self.assertTrue(len(AuxillaryGuardian.__doc__) >= 1,
                        "AuxillaryGuardian class needs a docstring")

    def test_auxillary_func_docstrings(self):
        """Test for the presence of docstrings in auxillary methods"""
        for func in self.auxillary_funcs:
            with self.subTest(function=func):
                self.assertIsNot(
                    func[1].__doc__,
                    None,
                    "{:s} method needs a docstring".format(func[0])
                )
                self.assertTrue(
                    len(func[1].__doc__) > 1,
                    "{:s} method needs a docstring".format(func[0])
                )


class TestAuxillaryGuardian(unittest.TestCase):
    """Test the AuxillaryGuardian class"""
    def test_is_subclass(self):
        """Test that AuxillaryGuardian is a subclass of BaseModel"""
        aux = AuxillaryGuardian()
        self.assertIsInstance(aux, BaseModel)
        self.assertTrue(hasattr(aux, "id"))
        self.assertTrue(hasattr(aux, "created_at"))
        self.assertTrue(hasattr(aux, "updated_at"))

    def test_super_id_attr(self):
        """Test AuxillaryGuardian has attr super_id, and it's None"""
        aux = AuxillaryGuardian()
        self.assertTrue(hasattr(aux, "super_id"))
        self.assertEqual(aux.super_id, None)

    def test_parent_id_attr(self):
        """Test AuxillaryGuardian has attr parent_id, and it's None"""
        aux = AuxillaryGuardian()
        self.assertTrue(hasattr(aux, "parent_id"))
        self.assertEqual(aux.parent_id, None)

    def test_first_name_attr(self):
        """Test AuxillaryGuardian has attr first_name, and it's None"""
        aux = AuxillaryGuardian()
        self.assertTrue(hasattr(aux, "first_name"))
        self.assertEqual(aux.first_name, None)

    def test_last_name_attr(self):
        """Test AuxillaryGuardian has attr last_name, and it's None"""
        aux = AuxillaryGuardian()
        self.assertTrue(hasattr(aux, "last_name"))
        self.assertEqual(aux.last_name, None)

    def test_other_name_attr(self):
        """Test AuxillaryGuardian has attr other_name, and it's None"""
        aux = AuxillaryGuardian()
        self.assertTrue(hasattr(aux, "other_name"))
        self.assertEqual(aux.other_name, None)

    def test_gender_attr(self):
        """Test AuxillaryGuardian has attr gender, and it's None"""
        aux = AuxillaryGuardian()
        self.assertTrue(hasattr(aux, "gender"))
        self.assertEqual(aux.gender, None)

    def test_tag_attr(self):
        """Test AuxillaryGuardian has attr tag, and it's None"""
        aux = AuxillaryGuardian()
        self.assertTrue(hasattr(aux, "tag"))
        self.assertEqual(aux.tag, None)

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        aux = AuxillaryGuardian()
        new_dic = aux.to_dict()
        self.assertEqual(type(new_dic), dict)
        self.assertFalse("_sa_instance_state" in new_dic)
        for attr in aux.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in new_dic)
        self.assertTrue("__class__" in new_dic)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        aux = AuxillaryGuardian()
        dic = aux.to_dict()
        self.assertEqual(dic["__class__"], "AuxillaryGuardian")
        self.assertEqual(type(dic["created_at"]), str)
        self.assertEqual(type(dic["updated_at"]), str)
        self.assertEqual(dic["created_at"], aux.created_at.strftime(t_format))
        self.assertEqual(dic["updated_at"], aux.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        aux = AuxillaryGuardian()
        string = "[AuxillaryGuardian] ({}) {}".format(aux.id, aux.__dict__)
        self.assertEqual(string, str(aux))


if __name__ == '__main__':
    unittest.main()
