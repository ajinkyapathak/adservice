from datetime import datetime


def get_datetime_object_from_string(str_date):
    return datetime.strptime(str_date, "%d/%m/%Y")


def get_str_datetime(date):
    try:
        return date.strftime('%d %b %Y %H:%M')
    except Exception as e:
        return ''
