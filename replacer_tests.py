import unittest

from replace_text import replacer


class ReplacerTests(unittest.TestCase):

    def test_single(self):
        self.assertEqual(
            ["no,the,answer,is,no", True,
             "yes: replaced 2 times"],
            replacer("yes,the,answer,is,yes", ["yes"], ["no"])
        )

    def test_many(self):
        self.assertEqual(
            ["no,a,answer,is,no", True,
             "yes: replaced 2 times" +
             "the: replaced 1 time" +
             "twelve: replaced 0 times"],
            replacer("yes,the,answer,is,yes",
                     ["yes", "the", "twelve"], ["no", "a", "thirteen"])
        )

    def test_len_not_equal(self):
        self.assertEqual(
            ['yes,the,answer,is,yes', False, 'List lengths do not match'],
            replacer("yes,the,answer,is,yes", ["yes", "the"], ["no"])
        )

    def test_duplicated_values_in_words_to_be_changed(self):
        with self.assertRaises(ValueError):
            replacer("yes,the,answer,is,yes", ["yes","yes" , "the"], ["no"])

    def test_wrong_input_in_string(self):
        with self.assertRaises(ValueError):
            replacer(1, ["yes", "the"], ["no"])

    def test_wrong_input_in_words_to_be_changed(self):
        with self.assertRaises(ValueError):
            replacer("test,dfdf,sdfdsf", [1, "the"], ["no"])

    def test_wrong_input_in_words_that_will_change(self):
        with self.assertRaises(ValueError):
            replacer("test,dfdf,sdfdsf", ["test", "the"], ["no" , 1])

    def test_empty_string(self):
        with self.assertRaises(ValueError):
            replacer("", ["test", "the"], ["no" , "test"])

    def test_empty_argument_word_to_change(self):
        with self.assertRaises(ValueError):
            replacer("test, thirteen, the", ["", "the"], ["no" , "test"])

    def test_delete_word_in_string(self):
        self.assertEqual(
            [",a,answer,is,", True,
             "yes: replaced 2 times" +
             "the: replaced 1 time" +
             "twelve: replaced 0 times"],
            replacer("yes,the,answer,is,yes",
                     ["yes", "the", "twelve"], ["", "a", "thirteen"])
        )

    def test_change_two_words_in_string_with_same_value(self):
        self.assertEqual(
            ["no,no,answer,is,no", True,
             "yes: replaced 2 times" +
             "the: replaced 1 time" +
             "twelve: replaced 0 times"],
            replacer("yes,the,answer,is,yes",
                     ["yes", "the", "twelve"], ["no", "no", "thirteen"])
        )


if __name__ == '__main__':
    unittest.main()
