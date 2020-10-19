from django.test import TestCase

from app.views import UploadView


def generate_csv_test():
    pass


class CsvTestCase(TestCase):
    def setUp(self):
        pass

    def test_vazio(self):
        """Animals that can speak are correctly identified"""
        csv = './repo1.csv'
        print(csv)
        up = UploadView()
        up.csv_file = csv
        test = up.handle_csv()
        self.assertEqual(test, True)

    def test_no_requireds(self):
        csv = './repo2.csv'
        print(csv)
        up = UploadView()
        up.csv_file = csv
        test = up.handle_csv()
        self.assertEqual(test, True)
