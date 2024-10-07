import os
import sys
from flask import Flask, json, render_template, request, jsonify
from faker import Faker

# 确保项目根目录在 sys.path 中，以便正确导入自定义 provider
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 从各个文件中导入自定义 Provider
from faker_extends.string_provider import RandomStringProvider
from faker_extends.flag_provider import FlagProvider
from faker_extends.date_provider import DateProvider
from faker_extends.number_provider import NumberProvider
from faker_extends.postal_code_provider import PostalCodeProvider
from faker_extends.barcode_provider import BarcodeProvider
from faker_extends.product_name_provider import ProductNameProvider

app = Flask(__name__)
faker = Faker("ja")

# 添加自定义 Providers
faker.add_provider(RandomStringProvider)
faker.add_provider(FlagProvider)
faker.add_provider(DateProvider)
faker.add_provider(NumberProvider)
faker.add_provider(PostalCodeProvider)
faker.add_provider(BarcodeProvider)
faker.add_provider(ProductNameProvider)

formats_folder = "formats"  # 模板文件夹路径

@app.route('/')
def index():
    return render_template('index.html')

# 获取可用的模板列表
@app.route('/get-templates', methods=['GET'])
def get_templates():
    try:
        templates = []
        for file in os.listdir(formats_folder):
            if file.endswith('.json'):
                with open(os.path.join(formats_folder, file), 'r', encoding='utf-8') as f:
                    template_data = json.load(f)
                    templates.append({"file": file, "name": template_data.get("template_name", file)})
        return jsonify({"templates": templates})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 加载指定模板内容
@app.route('/load-template', methods=['GET'])
def load_template():
    template_file = request.args.get('file')
    if not template_file:
        return jsonify({"error": "未提供模板文件"}), 400

    try:
        with open(os.path.join(formats_folder, template_file), 'r', encoding='utf-8') as f:
            template_data = json.load(f)
        return jsonify(template_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 生成测试数据
@app.route('/generate', methods=['POST'])
def generate_data():
    try:
        config = request.json
        rows = config.get("rows", 10)
        total_columns = config.get("total_columns", None)
        columns_config = config["columns"]

        data = generate_row_data(rows, columns_config, total_columns)
        return jsonify({'message': '数据生成成功', 'data': data})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def generate_row_data(num, columns_config, total_columns):
    data = []
    for i in range(num):
        row = [''] * total_columns
        for column in columns_config:
            position = column["position"] - 1
            row[position] = generate_data_by_type(column)
        data.append(row)
    return data

def generate_data_by_type(column_config):
    data_type = column_config["type"]

    if data_type == "number":
        start = column_config.get("start", 1)
        step = column_config.get("step", 1)
        return faker.random_int(min=column_config.get("min", 0), max=column_config.get("max", 100))

    elif data_type == "string":
        length = column_config.get("length", 10)
        return faker.random_string(length=length, string_type=column_config.get("string_type", "any"))

    elif data_type == "zipcode":
        return faker.random_postal_code()

    elif data_type == "address1":
        postal_code_column = column_config.get("postal_code_column")
        return faker.get_address1(postal_code_column)

    elif data_type == "date":
        date_format = column_config.get("format", "YYYY-MM-DD")
        return faker.date(pattern=date_format)

    elif data_type == "flag":
        flag_type = column_config.get("flag_type", "random")
        return faker.flag(flag_type)

    elif data_type == "product_name":
        return faker.product_name()

    elif data_type == "barcode":
        return faker.barcode()

    return "N/A"

if __name__ == '__main__':
    app.run(debug=True)
