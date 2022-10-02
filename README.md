# tzinfo

### How to run tzinfo:

`poetry run python tzinfo/tzinfo.py --offset 5.5`			===>>> (returns 2 timezone for offset 5.5)

[{'value': 'India Standard Time', 'abbr': 'IST', 'offset': 5.5, 'isdst': False, 'text': '(UTC+05:30) Chennai, Kolkata, Mumbai, New Delhi', 'utc': ['Asia/Kolkata', 'Asia/Calcutta']}, {'value': 'Sri Lanka Standard Time', 'abbr': 'SLST', 'offset': 5.5, 'isdst': False, 'text': '(UTC+05:30) Sri Jayawardenepura', 'utc': ['Asia/Colombo']}]
___

`poetry run python tzinfo/tzinfo.py --offset -5.5`			===>>> (returns 2 timezone even for offset 5.5)

[{'value': 'India Standard Time', 'abbr': 'IST', 'offset': 5.5, 'isdst': False, 'text': '(UTC+05:30) Chennai, Kolkata, Mumbai, New Delhi', 'utc': ['Asia/Kolkata', 'Asia/Calcutta']}, {'value': 'Sri Lanka Standard Time', 'abbr': 'SLST', 'offset': 5.5, 'isdst': False, 'text': '(UTC+05:30) Sri Jayawardenepura', 'utc': ['Asia/Colombo']}]
___

`poetry run python tzinfo/tzinfo.py --match calcutta` 			===>>> (returns 1 timezone for keyword search 'calcatta', which is in 'utc')

[{'value': 'India Standard Time', 'abbr': 'IST', 'offset': 5.5, 'isdst': False, 'text': '(UTC+05:30) Chennai, Kolkata, Mumbai, New Delhi', 'utc': ['Asia/Kolkata', 'Asia/Calcutta']}]
___

`poetry run python tzinfo/tzinfo.py --match kolkata` 			===>>> (returns 1 timezone for keyword search 'Kolkata', which is in 'utc' and 'text')

[{'value': 'India Standard Time', 'abbr': 'IST', 'offset': 5.5, 'isdst': False, 'text': '(UTC+05:30) Chennai, Kolkata, Mumbai, New Delhi', 'utc': ['Asia/Kolkata', 'Asia/Calcutta']}]
___


`poetry run python tzinfo/tzinfo.py --match kolkata --offset 5.5`		===>>> (return 2 timezones for both offset and keyword search)

[{'value': 'India Standard Time', 'abbr': 'IST', 'offset': 5.5, 'isdst': False, 'text': '(UTC+05:30) Chennai, Kolkata, Mumbai, New Delhi', 'utc': ['Asia/Kolkata', 'Asia/Calcutta']}, {'value': 'Sri Lanka Standard Time', 'abbr': 'SLST', 'offset': 5.5, 'isdst': False, 'text': '(UTC+05:30) Sri Jayawardenepura', 'utc': ['Asia/Colombo']}]
___


### How to run TestCases:

`poetry  run pytest -vv`

<pre>
====================================== test session starts ======================================
platform linux -- Python 3.9.2, pytest-7.1.3, pluggy-1.0.0 -- ..../.cache/pypoetry/virtualenvs/tzinfo-6siPToyp-py3.9/bin/python
cachedir: .pytest_cache
rootdir: ......./.../tzinfo
collected 9 items                                                                               

tests/test_init.py::test_version PASSED                                                   [ 11%]
tests/test_tzinfo.py::test_offset PASSED                                                  [ 22%]
tests/test_tzinfo.py::test_match PASSED                                                   [ 33%]
tests/test_tzinfo.py::test_match_offset_both PASSED                                       [ 44%]
tests/test_tzinfo.py::test_offset_absolute_value PASSED                                   [ 55%]
tests/test_tzinfo_2nd.py::TestTZInfo::test_match PASSED                                   [ 66%]
tests/test_tzinfo_2nd.py::TestTZInfo::test_match_offset_both PASSED                       [ 77%]
tests/test_tzinfo_2nd.py::TestTZInfo::test_offset PASSED                                  [ 88%]
tests/test_tzinfo_2nd.py::TestTZInfo::test_offset_absolute_value PASSED                   [100%]

======================================= 9 passed in 0.10s =======================================
</pre>
