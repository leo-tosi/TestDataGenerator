import random
from faker.providers import BaseProvider

# 商品类别和对应的商品基础名（日语）
categories = {
    "服装": ["Tシャツ", "シャツ", "ズボン", "ジャケット", "スカート", "帽子", "靴下", "手袋", "マフラー"],
    "運動器具": ["ランニングマシン", "フィットネス器具", "ヨガマット", "ダンベル", "バーベル", "フィットネスバンド", "フィットネスボール"],
    "オフィス消耗品": ["プリント用紙", "インクカートリッジ", "ノート", "ファイルフォルダー", "ホチキス", "蛍光ペン", "中性ペン", "付箋紙"],
    "スポーツ用品": ["バスケットボール", "サッカーボール", "バドミントンラケット", "卓球ラケット", "縄跳び", "ヨガブロック", "スケートボード", "テニスラケット"],
    "電子製品": ["スマートフォン", "ノートパソコン", "ヘッドフォン", "タブレット", "カメラ", "モニター", "スピーカー"],
    "家具": ["ソファ", "テーブル", "椅子", "本棚", "ベッド", "クローゼット", "コーヒーテーブル"],
    "キッチン用品": ["鍋", "包丁", "食器", "オーブン", "電子レンジ", "炊飯器", "ミキサー"]
}

# 修饰词（日语）
modifiers = ["高級", "専門", "運動型", "おしゃれ", "多機能", "ポータブル", "大きい", "小さい", "子供用", "大人用"]

# 产地（日语）
origins = ["日本", "中国", "ドイツ", "アメリカ", "フランス", "イタリア", "韓国", "インド"]

# 材料（日语）
materials = ["プラスチック", "金属", "木材", "ガラス", "綿", "ナイロン", "革"]

# 自定义商品名生成的Provider
class ProductNameProvider(BaseProvider):
    def product_name(self, use_modifier=True, use_material=True, use_origin=True):
        # 随机选择一个类别
        category = random.choice(list(categories.keys()))
        
        # 随机选择一个基础商品名
        base_name = random.choice(categories[category])
        
        # 随机决定是否添加修饰词
        modifier = random.choice(modifiers) if use_modifier and random.random() < 0.7 else ""
        
        # 随机决定是否添加材料
        material = random.choice(materials) if use_material and random.random() < 0.5 and category in ["服装", "家具", "キッチン用品"] else ""
        
        # 随机决定是否添加产地
        origin = random.choice(origins) if use_origin and random.random() < 0.6 else ""
        
        # 生成商品名
        product_name = f"{modifier}{base_name}"
        
        # 添加材料信息
        if material:
            product_name += f"（{material}）"
        
        # 添加产地信息
        if origin:
            product_name += f" - {origin}製造"
        
        return product_name
