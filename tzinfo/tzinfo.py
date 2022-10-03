'''
display timezone info based on tz offset value and/or keyword search in text,utc,value or abbr
'''
import json
import argparse
import os
import re
import yaml


class TZInfo:
    ''' class definition of timezone info  '''
    def __init__(self, filename="timezones.json"):
        filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
        with open(filename, "r") as fp:
            self.json = json.load(fp)
        self.matched = []

    def __eq__(self, other):
        ''' method to compare two TZInfo object '''
        for iii in other.matched:
            if iii not in self.matched:
                return False
        return True

    def offset(self, offset=None):
        ''' method to find offset value in timezone json '''
        for tz in self.json:
            if abs(tz["offset"]) == abs(offset) and (tz not in self.matched):
                self.matched.append(tz)

    def match(self, matchstr=None):
        ''' method to find search string in timezone json object '''
        for tz in self.json:
            for field in ["value", "text", "abbr", "utc"]:
                if field == "utc":
                    res = re.search(matchstr, " ".join(tz[field]), re.IGNORECASE)
                else:
                    res = re.search(matchstr, tz[field], re.IGNORECASE)
                if res and (tz not in self.matched):
                    self.matched.append(tz)

    def to_json(self):
        ''' returns json object if match found '''
        if self.matched:
            return json.dumps(self.matched)
        return None

    def to_yaml(self):
        ''' returns yaml object if match found '''
        if self.matched:
            return yaml.dump(self.matched)
        return None


def _main():
    cliparser = argparse.ArgumentParser()
    cliparser.add_argument(
        "-m",
        "--match",
        help="try string match found anyone of the timezone fields in value, text and utc",
    )
    cliparser.add_argument(
        "-o",
        "--offset",
        type=float,
        help="list timezones based on based on offset value",
    )

    cliargs = cliparser.parse_args()

    tzi = TZInfo("timezones.json")
    # print(tzi.json[0])

    if cliargs.match:
        tzi.match(cliargs.match)
    if cliargs.offset:
        # print(cliargs.offset, type(cliargs.offset))
        tzi.offset(cliargs.offset)

    if tzi.matched:
        print(tzi.matched)
        # print(len(tzi.matched))

    # print(tzi.to_json())
    # print(tzi.to_yaml())


if __name__ == "__main__":
    _main()
