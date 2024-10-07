import random
import requests
from faker.providers import BaseProvider

# ZipCloud API的URL
URL = 'https://zipcloud.ibsnet.co.jp/api/search'

class PostalCodeProvider(BaseProvider):

    # 生成7位随机邮便番号并判断其有效性
    def random_postal_code(self):
        while True:
            postal_code = ''.join([str(random.randint(0, 9)) for _ in range(7)])
            res = requests.get(URL, params={'zipcode': postal_code})
            data = res.json()
            
            if data['status'] == 200 and data['results']:
                return postal_code
            # 如果无效则继续生成

    # 根据邮便番号获取address1（都道府県名）
    def get_address1(self, postal_code_column):
        postal_code = self.get_postal_code_from_column(postal_code_column)
        if not postal_code:
            return "N/A"
        
        res = requests.get(URL, params={'zipcode': postal_code})
        data = res.json()

        if data['status'] == 200 and data['results']:
            return data['results'][0]['address1']
        else:
            return "都道府県が見つかりませんでした"  # 默认提示信息

    # 根据邮便番号获取address2（市区町村名）
    def get_address2(self, postal_code_column):
        postal_code = self.get_postal_code_from_column(postal_code_column)
        if not postal_code:
            return "N/A"
        
        res = requests.get(URL, params={'zipcode': postal_code})
        data = res.json()

        if data['status'] == 200 and data['results']:
            return data['results'][0]['address2']
        else:
            return "市区町村が見つかりませんでした"  # 默认提示信息

    # 根据邮便番号获取address3（町域名）
    def get_address3(self, postal_code_column):
        postal_code = self.get_postal_code_from_column(postal_code_column)
        if not postal_code:
            return "N/A"
        
        res = requests.get(URL, params={'zipcode': postal_code})
        data = res.json()

        if data['status'] == 200 and data['results']:
            return data['results'][0]['address3']
        else:
            return "町域が見つかりませんでした"  # 默认提示信息

    # 根据邮便番号获取完整地址
    def get_full_address(self, postal_code_column):
        postal_code = self.get_postal_code_from_column(postal_code_column)
        if not postal_code:
            return "N/A"

        res = requests.get(URL, params={'zipcode': postal_code})
        data = res.json()

        if data['status'] == 200 and data['results']:
            result = data['results'][0]
            full_address = f"{result['address1']} {result['address2']} {result['address3']}"
            return full_address
        else:
            return "住所が見つかりませんでした"  # 默认提示信息

    # 从已生成的列中获取邮便番号
    def get_postal_code_from_column(self, postal_code_column):
        # 假设邮便番号列已经生成在某一列，提供获取该列内容的逻辑
        if postal_code_column and postal_code_column.isdigit():
            # 获取已生成数据的邮便番号列，假设列号从1开始
            postal_code_column_index = int(postal_code_column) - 1
            # 这里需要访问已生成数据的某种方式，比如通过faker实例或全局变量
            if 0 <= postal_code_column_index < len(self.generated_data_row):
                return self.generated_data_row[postal_code_column_index]
        return None
