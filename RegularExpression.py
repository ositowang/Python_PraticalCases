import re
line = "XXX出生于2001年6月1日"
line = "XXX出生于2001/6/1"
line = "XXX出生于2001-6-1"
line = "XXX出生于2001-06-01"
line = "XXX出生于2001-06"
regex = ".*出生于(\d{4}[年/-]\d{1,2}([月/-]\d{1,2}|[月/-]|$))"
match_obj = re.match(regex,line)
if match_obj:
    print(match_obj.group(1))
