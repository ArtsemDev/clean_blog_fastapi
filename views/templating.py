from datetime import datetime

from fastapi.templating import Jinja2Templates


def datetimeformat(value: datetime, format: str) -> str:
    return value.strftime(format)


templates = Jinja2Templates(directory='templates')
templates.env.filters['datetimeformat'] = datetimeformat
templates.env.globals['now'] = datetime.now
