import sqlite3

class ProductDatabase:
    def __init__(self, db_name='products.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            price REAL NOT NULL)''')
        self.conn.commit()

    def insert_product(self, name, price):
        cursor = self.conn.cursor()
        cursor.execute('''INSERT INTO products (name, price) VALUES (?, ?)''', (name, price))
        self.conn.commit()

    def update_product_price(self, product_id, new_price):
        cursor = self.conn.cursor()
        cursor.execute('''UPDATE products SET price = ? WHERE id = ?''', (new_price, product_id))
        self.conn.commit()

    def delete_product(self, product_id):
        cursor = self.conn.cursor()
        cursor.execute('''DELETE FROM products WHERE id = ?''', (product_id,))
        self.conn.commit()

    def select_product(self, product_id):
        cursor = self.conn.cursor()
        cursor.execute('''SELECT * FROM products WHERE id = ?''', (product_id,))
        return cursor.fetchone()

    def close_connection(self):
        self.conn.close()

# 샘플 데이터 추가
def insert_sample_data(product_db):
    sample_data = [
        ("Laptop", 1500.0),
        ("Smartphone", 800.0),
        ("Tablet", 400.0),
        ("Headphones", 100.0),
        ("Smartwatch", 300.0),
        ("Camera", 600.0),
        ("Desktop", 1200.0),
        ("Speaker", 200.0),
        ("Printer", 250.0),
        ("Monitor", 350.0)
    ]

    for name, price in sample_data:
        product_db.insert_product(name, price)

# 테스트
if __name__ == "__main__":
    product_db = ProductDatabase()
    insert_sample_data(product_db)

    # 특정 제품 조회
    product_id = 3
    product = product_db.select_product(product_id)
    if product:
        print("Product found:")
        print("ID:", product[0])
        print("Name:", product[1])
        print("Price:", product[2])
    else:
        print("Product not found.")

    # 제품 가격 업데이트
    product_id = 2
    new_price = 850.0
    product_db.update_product_price(product_id, new_price)
    print("Product price updated.")

    # 제품 삭제
    product_id = 5
    product_db.delete_product(product_id)
    print("Product deleted.")

    product_db.close_connection()
