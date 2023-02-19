from datetime import datetime, timedelta


def minus_five_days():
    return datetime.today() - timedelta(days=5)


def print_days():
    print(datetime.today() - timedelta(days=1))
    print(datetime.today())
    print(datetime.today() + timedelta(days=1))


def no_microseconds_str(datetime1):
    return datetime1.strftime("%Y-%m-%d %H:%M:%S")


def diff_in_seconds(datetime1, datetime2):
    return int(datetime1.toordinal()*86400 + datetime1.second - datetime2.toordinal()*86400 - datetime2.second)
