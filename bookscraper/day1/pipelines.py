import csv

class BookscraperPipeline:
    def open_spider(self, spider):
        self.file = open("books.csv", "w", newline="", encoding="utf-8")
        self.writer = csv.writer(self.file)
        self.writer.writerow(["title", "category", "description", "price"])

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):  # ✔ fixed name
        self.writer.writerow([
            item.get("title"),
            item.get("category"),
            item.get("description"),
            item.get("price")
        ])
        return item
