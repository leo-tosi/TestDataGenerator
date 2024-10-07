import random
from faker.providers import BaseProvider

class NumberProvider(BaseProvider):

    # 1. 任意数字生成 (指定起始和结束)
    def random_number_in_range(self, start, end):
        return random.randint(start, end)

    # 2. 规律数字生成 (指定接头，接尾，起始，结束，步长)
    def Generate_number(self, start, step, idx, length=None, prefix=None, suffix=None):
        number = start + step * idx
        number_str = str(number).zfill(length) if length else str(number)
        
        # 添加接头和接尾
        if prefix:
            number_str = f"{prefix}{number_str}"
        if suffix:
            number_str = f"{number_str}{suffix}"
        
        return number_str
