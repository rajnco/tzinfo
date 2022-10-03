from tzinfo import tzinfo
from unittest import TestCase


class TestTZInfo(TestCase):
    def setUp(self):
        self.ttzi = tzinfo.TZInfo()

    def test_offset(self):
        self.ttzi.offset(5.5)
        assert len(self.ttzi.matched) == 2

    def test_match(self):
        self.ttzi.match("Calcutta")
        assert len(self.ttzi.matched) == 1

    def test_match_offset_both(self):
        self.ttzi.match("Calcutta")
        self.ttzi.offset(5.5)
        assert len(self.ttzi.matched) == 2

    def test_offset_absolute_value(self):
        self.ttzi.offset(5.5)

        ttzi2 = tzinfo.TZInfo()
        ttzi2.offset(-5.5)

        assert self.ttzi.matched == ttzi2.matched

    def tearDown(self):
        del self.ttzi
