from faker.providers import BaseProvider
import random

class FlagProvider(BaseProvider):

    # 旗帜类型生成函数
    def flag(self, flag_type="random"):
        if flag_type == "0":
            return 0
        elif flag_type == "1":
            return 1
        else:
            # 默认生成 0 或 1 的随机值
            return random.choice([0, 1])