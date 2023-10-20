import unittest
from log_analyzer import LogEntry

class TestLogAnalyzer(unittest.TestCase):
    
    # TODO: Write a unit test to validate that event_time is properly converting to a string
    def setUp(self):
        self.test_log = LogEntry('2022-01-01 00:18:38 UTC','10.248.203.131',20,'FTP - Data','Allow',186,'216.57.223.121','US','United States')

    def testtimeanalyzer(self):
        self.assertEqual(self.test_log.event_time.hour, 0)
        self.assertEqual(self.test_log.event_time.minute, 18)

    # TODO: Write a unit test to validate that ipv4_class is properly returning the correct class of IP.
        self.assertEqual(self.test_log.ipv4_class, "C")
    

if __name__ == '__main__':
    unittest.main()