def adjust_time(hour, timezone_offset):
    return (hour + timezone_offset) % 12