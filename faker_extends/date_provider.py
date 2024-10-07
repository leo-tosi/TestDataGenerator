from faker.providers import BaseProvider
from datetime import datetime, date, timezone
import random

class DateProvider(BaseProvider):

    # 日期生成函数
    def generate_date(self, date_type="Datetime", generation_method="current", specific_date=None):
        # 当前时间
        now = datetime.now()

        if generation_method == "current":
            if date_type == "Date":
                return now.date()
            elif date_type == "Datetime":
                return now
            elif date_type == "Timestamp":
                return int(now.timestamp())
        
        elif generation_method == "random":
            random_date = datetime.fromtimestamp(random.randint(0, int(now.timestamp())))
            if date_type == "Date":
                return random_date.date()
            elif date_type == "Datetime":
                return random_date
            elif date_type == "Timestamp":
                return int(random_date.timestamp())
        
        elif generation_method == "specific":
            if specific_date:
                specific_datetime = datetime.strptime(specific_date, "%Y-%m-%d %H:%M:%S")
                if date_type == "Date":
                    return specific_datetime.date()
                elif date_type == "Datetime":
                    return specific_datetime
                elif date_type == "Timestamp":
                    return int(specific_datetime.timestamp())
        
        # 默认返回当前日期时间
        return now
