import unittest


class TestVariableAreLabelsNotBoxes(unittest.TestCase):
    def test_Should_Return_Same_List_When_Two_references_to_the_same_object_are_accessed(self):
        a = [1, 2, 3]
        b = a
        a.append(4)
        self.assertEqual(a is b, True)

    def test_Should_Make_distinction_Between_Aliases_And_Imposters_When_aliases_and_different_objects_are_compared(self):
        charles = {"name": "Charles L. Dodgson", "born": 1832}
        lewis = charles

        self.assertEqual(lewis is charles, True)
        self.assertEqual(id(lewis), id(charles))

        lewis["balance"] = 950

        alex = {"name": "Charles L. Dodgson", "born": 1832, "balance": 950}

        self.assertEqual(lewis["balance"], charles["balance"])

        self.assertEqual(alex is not charles, True)
        self.assertSequenceEqual(alex, charles)

if __name__ == "__main__":
    unittest.main()