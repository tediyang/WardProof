#!/usr/bin/python3

"""
    Contains the TestActivityDocs classes
"""

import inspect
import models
import pycodestyle
import unittest

BaseModel = models.basemodel.BaseModel
Activity = models.activity.Activity
activity_doc = models.activity.__doc__


class TestActivityDocs(unittest.TestCase):
    """Tests to check the documentation and style of Activity class"""

    @classmethod
    def setUpClass(self):
        """Set up for docstring tests by extracting all the function
           object.
        """
        self.act_funcs = inspect.getmembers(Activity, inspect.isfunction)

    def test_pep8_conformance(self):
        """Test that models/activity.py conforms to PEP8 (pycodestyle)."""
        for path in ['models/activity.py',
                     'test_activity.py']:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_activity_docstring(self):
        """Test for the existence of model docstring"""
        self.assertIsNot(activity_doc, None,
                         "activity.py needs a docstring")
        self.assertTrue(len(activity_doc) > 1,
                        "activity.py needs a docstring")

    def test_activity_class_docstring(self):
        """Test for the Activity class docstring"""
        self.assertIsNot(Activity.__doc__, None,
                         "Activity class needs a docstring")
        self.assertTrue(len(Activity.__doc__) >= 1,
                        "Activity class needs a docstring")

    def test_activity_func_docstrings(self):
        """Test for the presence of docstrings in Activity methods"""
        for func in self.act_funcs:
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


class TestActivity(unittest.TestCase):
    """Test the Activity class"""
    def test_is_subclass(self):
        """Test that Activity is a subclass of BaseModel"""
        act = Activity()
        self.assertIsInstance(act, BaseModel)
        self.assertTrue(hasattr(act, "id"))
        self.assertTrue(hasattr(act, "created_at"))
        self.assertTrue(hasattr(act, "updated_at"))

    def test_school_id_attr(self):
        """Test Activity has attr school_id, and it's None"""
        act = Activity()
        self.assertTrue(hasattr(act, "school_id"))
        self.assertEqual(act.school_id, None)

    def test_pupil_id_attr(self):
        """Test Activity has attr pupil_id, and it's None"""
        act = Activity()
        self.assertTrue(hasattr(act, "pupil_id"))
        self.assertEqual(act.pupil_id, None)

    def test_parent_id_attr(self):
        """Test Activity has attr parent_id, and it's None"""
        act = Activity()
        self.assertTrue(hasattr(act, "parent_id"))
        self.assertEqual(act.parent_id, None)

    def test_action_attr(self):
        """Test Activity has attr action, and it's None"""
        act = Activity()
        self.assertTrue(hasattr(act, "action"))
        self.assertEqual(act.action, None)

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        act = Activity()
        new_dic = act.to_dict()
        self.assertEqual(type(new_dic), dict)
        self.assertFalse("_sa_instance_state" in new_dic)
        for attr in act.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in new_dic)
        self.assertTrue("__class__" in new_dic)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        act = Activity()
        dic = act.to_dict()
        self.assertEqual(dic["__class__"], "Activity")
        self.assertEqual(type(dic["created_at"]), str)
        self.assertEqual(type(dic["updated_at"]), str)
        self.assertEqual(dic["created_at"], act.created_at.strftime(t_format))
        self.assertEqual(dic["updated_at"], act.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        act = Activity()
        string = "[Activity] ({}) {}".format(act.id, act.__dict__)
        self.assertEqual(string, str(act))


if __name__ == '__main__':
    unittest.main()
