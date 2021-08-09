# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class RightmovePipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect('rightmove.db')
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS rightmove""")
        self.curr.execute("""CREATE TABLE rightmove(
            title text,
            address text,
            price text,
            date_added text,
            phone text,
            seller text,
            description text
        )""")
    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""INSERT INTO rightmove VALUES(?,?,?,?,?,?,?)""",(
            item['title'],
            item['address'],
            item['price'],
            item['date_added'],
            item['phone'],
            item['seller'],
            item['description']
        ))
        self.conn.commit()
