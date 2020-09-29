from django.test import TestCase
from os import path

from .controller import parsing_xlsx
from .controller import recording_in_db

from .models import Home


BASE_PATH = path.abspath(path.dirname(__file__))
FILE = path.join(BASE_PATH, "test.xlsx")


class TestParsingXlsx(TestCase):
    def setUp(self):
        self.result = parsing_xlsx(input_file=FILE,
                                   start_row=2,
                                   stop_row=5,
                                   start_col=1,
                                   stop_col=23,
                                   sheet=None,
                                   cells=(0, 1, 2, 3, 4, 5, 6, 7))

    def tearDown(self):
        del self.result

    def test_list_result(self):
        self.assertIsInstance(self.result, list)

    def test_list_result2(self):
        self.assertIsInstance(self.result[0], list)

    def test_data_in_list(self):
        self.assertEqual(self.result[0][0], 15270020)

    def test_none_to_zero_in_list(self):
        self.assertEqual(self.result[1][5], 0)


class TestRecordingInDB(TestCase):
    def setUp(self):
        self.data = [[1, "Кирово-Чепецк", "Калинина", 15, 0],
                     [2, "Кирово-Чепецк", "Красноармейская", 3, 0]]

    def tearDown(self):
        pass

    def test_check(self):
        recording_in_db(self.data, Home)
        entry = Home.objects.all()
        print(entry)
        self.assertEqual(entry.home_number, 15)
