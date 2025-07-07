class Time:
    def __init__(tinu, hour =0, minute =0, second =0):
        tinu._hour = hour
        tinu._minute = minute
        tinu._second = second

    @property
    def hour(tinu):
        return tinu._hour
    @hour.setter
    def hour(tinu, hourValue):
        if hourValue not in range(0, 24):
            raise ValueError("Invalid hour value")
        tinu._hour = hourValue
        return tinu._hour
    @property
    def minute(tinu):
        return tinu._minute

    @minute.setter
    def minute(tinu, minuteValue):
        if minuteValue not in range(0, 60):
            raise ValueError("Invalid minute value")
        tinu._minute = minuteValue
        return tinu._minute
    @property
    def second(tinu):
        return tinu._second

    @second.setter
    def second(tinu, secondValue):
        if secondValue not in range(0, 60):
            raise ValueError("Invalid second value")
        tinu._second = secondValue
        return tinu._second
    def set_time(tinu, hour =0, minute =0, second =0):
        tinu.hour = hour
        tinu.minute = minute
        tinu.second = second

    def __str__(tinu):
        return f"{tinu.hour:0>2}:{tinu.minute:0>2}:{tinu.second:0>2}"


time_one = Time(hour=12, minute=24, second=13)
time_one.set_time(hour=12, minute=24, second=59)
print(time_one)

