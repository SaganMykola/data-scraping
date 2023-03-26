# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector

class MySqlPipeline:
    def open_spider(self, spider):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="scrapy"
        )
        self.cursor = self.connection.cursor()
        spider.logger.info("Connected to MySQL ")
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS 
        items (
            id INT AUTO_INCREMENT,
            PRIMARY KEY (id),
            name VARCHAR(50) NOT NULL,
            url VARCHAR(500)
        );""")
        spider.logger.info("DB is ready ")

    def close_spider(self, spider):
        self.connection.close()
        spider.logger.info("Disconnected from MySQL ")

    def process_item(self, item, spider):
        if self.is_duplicate(item):
            self.cursor.execute("""
                                    UPDATE items
                                    WHERE name = %s
                                    """,
                                [item.get("name")]
                                )
        else:
            self.cursor.execute(
                "INSERT INTO items (name, url) VALUES (%s, %s);",
                [item.get("name"), item.get("url")])

        self.connection.commit()
        return item

    def is_duplicate(self, item):
        self.cursor.execute(
            "SELECT COUNT(id) FROM items WHERE name = %s;",
            [item.get("name")])
        count = self.cursor.fetchone()[0]
        return count > 0

class Lab3Pipeline:
    def process_item(self, item, spider):
        item["name"] = str(item.get("name").replace("«", "'").replace("»", "'").replace("\"", "'"))
        return item
