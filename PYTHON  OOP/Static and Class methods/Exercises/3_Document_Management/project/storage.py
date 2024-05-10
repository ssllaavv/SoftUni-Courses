from project.category import Category
from project.topic import Topic
from project.document import Document

class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def _find_category_by_id(self, id):
        category = None
        for c in self.categories:
            if c.id == id:
                category = c
                break
        return category

    def _find_document_by_id(self, id):
        document = None
        for d in self.documents:
            if d.id == id:
                document = d
                break
        return document

    def _find_topic_by_id(self, id):
        topic = None
        for t in self.topics:
            if t.id == id:
                topic = t
                break
        return topic

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category = self._find_category_by_id(category_id)
        if category:
            category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = self._find_topic_by_id(topic_id)
        if topic:
            topic.topic = new_topic
            topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        document = self._find_document_by_id(document_id)
        if document:
            document.file_name = new_file_name

    def delete_category(self, category_id: int):
        category = self._find_category_by_id(category_id)
        if category:
            self.categories.remove(category)

    def delete_topic(self, topic_id: int):
        topic = self._find_topic_by_id(topic_id)
        if topic:
            self.topics.remove(topic)

    def delete_document(self, document_id: int):
        document = self._find_document_by_id(document_id)
        if document:
            self.documents.remove(document)

    def get_document(self, document_id: int):
        return self._find_document_by_id(document_id)

    def __repr__(self):
        result = ""
        for d in self.documents:
            result += str(d) + "\n"

        result = result[:-1:]
        return result






