# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy.orm import sessionmaker
from models import Properties, db_connect, create_properties_table

class ScraperPipeline(object):
    def __init__(self):
        """Initializes database connection and sessionmaker.
        Creates properties table.
        """
        engine = db_connect()
        create_properties_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save properties in the database.
        This method is called for every item pipeline component.
        """
        session = self.Session()
        prop = Properties(**item)

        try:
            session.add(prop)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
        return item
