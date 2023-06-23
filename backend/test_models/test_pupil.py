#!/usr/bin/python3

"""
    Contains the TestPupilDocs classes
"""

import inspect
import models
import pycodestyle
import unittest

BaseModel = models.basemodel.BaseModel
Pupil = models.pupil.Pupil
pupil_doc = models.pupil.__doc__


class TestPupilDocs(unittest.TestCase):
    """Tests to check the documentation and style of Pupil class"""

    @classmethod
    def setUpClass(self):
        """Set up for docstring tests by extracting all the function
           object.
        """
        self.pupil_funcs = inspect.getmembers(Pupil, inspect.isfunction)

    def test_pep8_conformance(self):
        """Test that models/pupil.py conforms to PEP8 (pycodestyle)."""
        for path in ['models/pupil.py',
                     'test_pupil.py']:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_pupil_docstring(self):
        """Test for the existence of model docstring"""
        self.assertIsNot(pupil_doc, None,
                         "pupil.py needs a docstring")
        self.assertTrue(len(pupil_doc) > 1,
                        "pupil.py needs a docstring")

    def test_pupil_class_docstring(self):
        """Test for the Pupil class docstring"""
        self.assertIsNot(Pupil.__doc__, None,
                         "Pupil class needs a docstring")
        self.assertTrue(len(Pupil.__doc__) >= 1,
                        "Pupil class needs a docstring")

    def test_pupil_func_docstrings(self):
        """Test for the presence of docstrings in pupil methods"""
        for func in self.pupil_funcs:
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


class TestPupil(unittest.TestCase):
    """Test the Pupil class"""
    def test_is_subclass(self):
        """Test that Pupil is a subclass of BaseModel"""
        pup = Pupil()
        self.assertIsInstance(pup, BaseModel)
        self.assertTrue(hasattr(pup, "id"))
        self.assertTrue(hasattr(pup, "created_at"))
        self.assertTrue(hasattr(pup, "updated_at"))

    def test_school_id_attr(self):
        """Test Pupil has attr school_id, and it's None"""
        pup = Pupil()
        self.assertTrue(hasattr(pup, "school_id"))
        self.assertEqual(pup.school_id, None)

    def test_parent_id_attr(self):
        """Test Pupil has attr parent_id, and it's None"""
        pup = Pupil()
        self.assertTrue(hasattr(pup, "parent_id"))
        self.assertEqual(pup.parent_id, None)

    def test_first_name_attr(self):
        """Test Pupil has attr first_name, and it's None"""
        pup = Pupil()
        self.assertTrue(hasattr(pup, "first_name"))
        self.assertEqual(pup.first_name, None)
        
    def test_last_name_attr(self):
        """Test Pupil has attr last_name, and it's None"""
        pup = Pupil()
        self.assertTrue(hasattr(pup, "last_name"))
        self.assertEqual(pup.last_name, None)

    def test_other_name_attr(self):
        """Test Pupil has attr other_name, and it's None"""
        pup = Pupil()
        self.assertTrue(hasattr(pup, "other_name"))
        self.assertEqual(pup.other_name, None)

    def test_gender_attr(self):
        """Test Pupil has attr gender, and it's None"""
        pup = Pupil()
        self.assertTrue(hasattr(pup, "gender"))
        self.assertEqual(pup.gender, None)

    def test_allergy_attr(self):
        """Test Pupil has attr allergy, and it's None"""
        pup = Pupil()
        self.assertTrue(hasattr(pup, "allergy"))
        self.assertEqual(pup.allergy, None)

    def test_dob_attr(self):
        """Test Pupil has attr dob, and it's None"""
        pup = Pupil()
        self.assertTrue(hasattr(pup, "dob"))
        self.assertEqual(pup.dob, None)

    def test_class_grade_attr(self):
        """Test Pupil has attr class_grade, and it's None"""
        pup = Pupil()
        self.assertTrue(hasattr(pup, "class_grade"))
        self.assertEqual(pup.class_grade, None)

    def test_parent_fullname_attr(self):
        """Test Pupil has attr parent_fullname, and it's None"""
        pup = Pupil()
        self.assertTrue(hasattr(pup, "parent_fullname"))
        self.assertEqual(pup.parent_fullname, None)

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        pup = Pupil()
        new_dic = pup.to_dict()
        self.assertEqual(type(new_dic), dict)
        self.assertFalse("_sa_instance_state" in new_dic)
        for attr in pup.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_dic)
        self.assertTrue("__class__" in new_dic)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        pup = Pupil()
        dic = pup.to_dict()
        self.assertEqual(dic["__class__"], "Pupil")
        self.assertEqual(type(dic["created_at"]), str)
        self.assertEqual(type(dic["updated_at"]), str)
        self.assertEqual(dic["created_at"], pup.created_at.strftime(t_format))
        self.assertEqual(dic["updated_at"], pup.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        pup = Pupil()
        string = "[Pupil] ({}) {}".format(pup.id, pup.__dict__)
        self.assertEqual(string, str(pup))


if __name__ == '__main__':
    unittest.main()
