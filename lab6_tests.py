import data
import lab6
import unittest

from lab6 import swap_case


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1

    # arbitrary test of functionality
    def test_selection_sort_books_1(self):
        booklist = [data.Book(['Neil Gaiman'], 'Good Omens'),
                    data.Book(['Neil Gaiman'], 'A Good Omen'),
                    data.Book(['Neil Gaiman'], 'Illustrated Good Omens')]
        expected = [data.Book(['Neil Gaiman'], 'A Good Omen'),
                    data.Book(['Neil Gaiman'], 'Good Omens'),
                    data.Book(['Neil Gaiman'], 'Illustrated Good Omens')]
        lab6.selection_sort_books(booklist)
        self.assertEqual(expected, booklist)

    # test with empty booklist
    def test_selection_sort_books_2(self):
        booklist = []
        expected = []
        lab6.selection_sort_books(booklist)
        self.assertEqual(expected, booklist)

    # test of funcitonality with two equal values
    def test_selection_sort_books_3(self):
        booklist = [data.Book(['Neil Gaiman'], 'Good Omens'),
                    data.Book(['Terry Pratchett'], 'Good Omens'),
                    data.Book(['Terry Pratchett'], 'Illustrated Good Omens')]
        expected = [data.Book(['Neil Gaiman'], 'Good Omens'),
                    data.Book(['Terry Pratchett'], 'Good Omens'),
                    data.Book(['Terry Pratchett'], 'Illustrated Good Omens')]
        actual = lab6.selection_sort_books(booklist)
        self.assertEqual(expected, booklist)

    # Part 2

    # Arbitrary test of functionality
    def test_swap_case_1(self):
        input = "Hello World"
        expected = "hELLO wORLD"
        actual = swap_case(input)
        self.assertEqual(expected, actual)
    # test with non alphabetical characters, and non english characters
    def test_swap_case_2(self):
        input = "hello+=,.,lá"
        expected = "HELLO+=,.,LÁ"
        actual = swap_case(input)
        self.assertEqual(expected, actual)

    # test empty list
    def test_swap_case_3(self):
        input = ""
        expected = ""
        actual = swap_case(input)
        self.assertEqual(expected, actual)

    # Part 3

    # arbitrary test of functionality
    def test_str_translate_1(self):
        input_str = "The dog is running"
        new = "was"
        old = "is"
        expected = "The dog was running"
        actual = lab6.str_translate(input_str, old, new)
        self.assertEqual(expected, actual)

    # arbitrary test of functionality
    def test_str_translate_2(self):
        input_str = "dog"
        old = "dog"
        new = "cat"
        expected = "cat"
        actual = lab6.str_translate(input_str, old, new)
        self.assertEqual(expected, actual)

    # test replacement of a word within a string
    def test_str_translate_3(self):
        input_str = 'thisiscoool'
        old = 'coool'
        new = 'fun'
        expected = 'thisisfun'
        actual = lab6.str_translate(input_str, old, new)
        self.assertEqual(expected, actual)



    # Part 4

    # test of arbitrary string of words with single instances of a word
    def test_histogram_1(self):
        input = "The dog is running"
        expected = {'The': 1, 'dog': 1, 'is': 1, 'running': 1}
        actual = lab6.histogram(input)
        self.assertEqual(expected, actual)
    # test multiple instances of a word
    def test_histogram_2(self):
        input = "The dog is running and the dog is running"
        expected = {'The': 1, 'dog': 2, 'is': 2, 'running': 2, 'and': 1,'the':1}
        actual = lab6.histogram(input)
        self.assertEqual(expected, actual)
    # test empty string
    def test_histogram_3(self):
        input = ""
        expected = {}
        actual = lab6.histogram(input)
        self.assertEqual(expected, actual)







if __name__ == '__main__':
    unittest.main()
