from report import generate_report
import unittest

class ReportTestCase(unittest.TestCase):
    def test_generate_report(self):
        report = generate_report()
        self.assertIn('My Report', report)
