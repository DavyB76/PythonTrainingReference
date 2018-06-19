import unittest


class TestVariableAreLabelsNotBoxes(unittest.TestCase):
    def test_Should_Return_Same_List_When_Two_references_to_the_same_object_are_accessed(self):
        a = [1, 2, 3]
        b = a
        a.append(4)
        self.assertEqual(a is b, True)


if __name__ == "__main__":
    unittest.main()