import random
from faker.providers import BaseProvider
import string

# 自定义Provider，生成商品バーコード
class BarcodeProvider(BaseProvider):
    def barcode(self, length=12):
        # Code128支持的字符集是字母和数字的组合
        alphanumeric_characters = string.ascii_uppercase + string.digits
        
        # 随机生成指定长度的半角英数字字符串
        barcode = ''.join(random.choices(alphanumeric_characters, k=length))
        return barcode

# 示例：
# fake.barcode() -> 生成一个随机的符合Code128标准的商品バーコード
