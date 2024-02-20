from datetime import datetime


# Serialize datetime objects to strings using a custom function
def format_datetime(obj):
    if isinstance(obj, datetime):
        return obj.strftime('%Y-%m-%d %H:%M:%S')
    raise TypeError(f'Type {type(obj)} not serializable')