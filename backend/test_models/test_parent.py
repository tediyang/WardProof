#!/usr/bin/python3

"""
    Contains the TestParentDocs classes
"""

import inspect
import models
import pycodestyle
import unittest

BaseModel = models.basemodel.BaseModel
Parent = models.parent.Parent
parent_doc = models.parent.__doc__


class TestParentDocs(unittest.TestCase):
    """Tests to check the documentation and style of Parent class"""

    @classmethod
    def setUpClass(self):
        """Set up for docstring tests by extracting all the function
           object.
        """
        self.parent_funcs = inspect.getmembers(Parent, inspect.isfunction)

    def test_pep8_conformance(self):
        """Test that models/parent.py conforms to PEP8 (pycodestyle)."""
        for path in ['models/parent.py',
                     'test_parent.py']:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_parent_docstring(self):
        """Test for the existence of model docstring"""
        self.assertIsNot(parent_doc, None,
                         "parent.py needs a docstring")
        self.assertTrue(len(parent_doc) > 1,
                        "parent.py needs a docstring")

    def test_parent_class_docstring(self):
        """Test for the Parent class docstring"""
        self.assertIsNot(Parent.__doc__, None,
                         "Parent class needs a docstring")
        self.assertTrue(len(Parent.__doc__) >= 1,
                        "Parent class needs a docstring")

    def test_parent_func_docstrings(self):
        """Test for the presence of docstrings in parent methods"""
        for func in self.parent_funcs:
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


class TestParent(unittest.TestCase):
    """Test the Parent class"""
    def test_is_subclass(self):
        """Test that Parent is a subclass of BaseModel"""
        par = Parent()
        self.assertIsInstance(par, BaseModel)
        self.assertTrue(hasattr(par, "id"))
        self.assertTrue(hasattr(par, "created_at"))
        self.assertTrue(hasattr(par, "updated_at"))

    def test_email_attr(self):
        """Test Parent has attr email, and it's None"""
        par = Parent()
        self.assertTrue(hasattr(par, "email"))
        self.assertEqual(par.email, None)

    def test_password_attr(self):
        """Test Parent has attr password, and it's encrypted"""
        par = Parent()
        par.password = "Wardproof123#"
        self.assertTrue(hasattr(par, "password"))
        self.assertNotEqual(par.password, "Wardproof123#")

    def test_first_name_attr(self):
        """Test Parent has attr first_name, and it's None"""
        par = Parent()
        self.assertTrue(hasattr(par, "first_name"))
        self.assertEqual(par.first_name, None)

    def test_last_name_attr(self):
        """Test Parent has attr last_name, and it's None"""
        par = Parent()
        self.assertTrue(hasattr(par, "last_name"))
        self.assertEqual(par.last_name, None)

    def test_other_name_attr(self):
        """Test Parent has attr other_name, and it's None"""
        par = Parent()
        self.assertTrue(hasattr(par, "other_name"))
        self.assertEqual(par.other_name, None)

    def test_gender_attr(self):
        """Test Parent has attr gender, and it's None"""
        par = Parent()
        self.assertTrue(hasattr(par, "gender"))
        self.assertEqual(par.gender, None)

    def test_tag_attr(self):
        """Test Parent has attr tag, and it's None"""
        par = Parent()
        self.assertTrue(hasattr(par, "tag"))
        self.assertEqual(par.tag, None)

    def test_dob_attr(self):
        """Test Parent has attr dob, and it's None"""
        par = Parent()
        self.assertTrue(hasattr(par, "dob"))
        self.assertEqual(par.dob, None)

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        par = Parent()
        new_dic = par.to_dict()
        self.assertEqual(type(new_dic), dict)
        self.assertFalse("_sa_instance_state" in new_dic)
        for attr in par.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in new_dic)
        self.assertTrue("__class__" in new_dic)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        par = Parent()
        dic = par.to_dict()
        self.assertEqual(dic["__class__"], "Parent")
        self.assertEqual(type(dic["created_at"]), str)
        self.assertEqual(type(dic["updated_at"]), str)
        self.assertEqual(dic["created_at"], par.created_at.strftime(t_format))
        self.assertEqual(dic["updated_at"], par.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        par = Parent()
        string = "[Parent] ({}) {}".format(par.id, par.__dict__)
        self.assertEqual(string, str(par))


if __name__ == '__main__':
    unittest.main()
