from tzinfo import tzinfo


def test_offset():
    ttzi = tzinfo.TZInfo()
    ttzi.offset(5.5)
    assert len(ttzi.matched) == 2


def test_match():
    ttzi = tzinfo.TZInfo()
    ttzi.match("Calcutta")
    assert len(ttzi.matched) == 1


def test_match_offset_both():
    ttzi = tzinfo.TZInfo()
    ttzi.match("Calcutta")
    ttzi.offset(5.5)
    assert len(ttzi.matched) == 2


def test_offset_absolute_value():
    ttzi = tzinfo.TZInfo()
    ttzi.offset(5.5)

    ttzi2 = tzinfo.TZInfo()
    ttzi2.offset(-5.5)

    assert ttzi.matched == ttzi2.matched
