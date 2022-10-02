# tzinfo

poetry run python tzinfo/tzinfo.py --offset 5.5			[//]: <> (returns 2 timezone for offset 5.5)
[{'value': 'India Standard Time', 'abbr': 'IST', 'offset': 5.5, 'isdst': False, 'text': '(UTC+05:30) Chennai, Kolkata, Mumbai, New Delhi', 'utc': ['Asia/Kolkata', 'Asia/Calcutta']}, {'value': 'Sri Lanka Standard Time', 'abbr': 'SLST', 'offset': 5.5, 'isdst': False, 'text': '(UTC+05:30) Sri Jayawardenepura', 'utc': ['Asia/Colombo']}]

poetry run python tzinfo/tzinfo.py --offset -5.5		[//]: <> (returns 2 timezone even for offset 5.5)
[{'value': 'India Standard Time', 'abbr': 'IST', 'offset': 5.5, 'isdst': False, 'text': '(UTC+05:30) Chennai, Kolkata, Mumbai, New Delhi', 'utc': ['Asia/Kolkata', 'Asia/Calcutta']}, {'value': 'Sri Lanka Standard Time', 'abbr': 'SLST', 'offset': 5.5, 'isdst': False, 'text': '(UTC+05:30) Sri Jayawardenepura', 'utc': ['Asia/Colombo']}]


poetry run python tzinfo/tzinfo.py --match calcutta 		[//]: <> (returns 1 timezone for keyword search 'calcatta', which is in 'utc')
[{'value': 'India Standard Time', 'abbr': 'IST', 'offset': 5.5, 'isdst': False, 'text': '(UTC+05:30) Chennai, Kolkata, Mumbai, New Delhi', 'utc': ['Asia/Kolkata', 'Asia/Calcutta']}]

poetry run python tzinfo/tzinfo.py --match kolkata 		[//]: <> (returns 1 timezone for keyword search 'Kolkata', which is in 'utc' and 'text')
[{'value': 'India Standard Time', 'abbr': 'IST', 'offset': 5.5, 'isdst': False, 'text': '(UTC+05:30) Chennai, Kolkata, Mumbai, New Delhi', 'utc': ['Asia/Kolkata', 'Asia/Calcutta']}]


poetry run python tzinfo/tzinfo.py --match kolkata --offset 5.5		[//]: <> (return 2 timezones for both offset and keyword search)
[{'value': 'India Standard Time', 'abbr': 'IST', 'offset': 5.5, 'isdst': False, 'text': '(UTC+05:30) Chennai, Kolkata, Mumbai, New Delhi', 'utc': ['Asia/Kolkata', 'Asia/Calcutta']}, {'value': 'Sri Lanka Standard Time', 'abbr': 'SLST', 'offset': 5.5, 'isdst': False, 'text': '(UTC+05:30) Sri Jayawardenepura', 'utc': ['Asia/Colombo']}]
