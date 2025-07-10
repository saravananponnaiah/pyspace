from datetime import datetime 

def get_date(datetime_string):
    return datetime.strptime(datetime_string, '%Y-%m-%d %H:%M:%S').date()

def add(a, b):
    return a+b

def subtract(a, b):
    return a-b
