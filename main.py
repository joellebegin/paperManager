from importlib import resources

from sqlalchemy import and_, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import asc, desc, func

from modules.models import Author, Paper
from modules.query_database import *

# def main():
"""Main entry point of program"""

# Connect to the database using SQLAlchemy
sqlite_filepath = "data.db"
engine = create_engine(f"sqlite:///{sqlite_filepath}")
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

# Output hierarchical authors data
# authors = get_authors(session)
# tree(authors)

# auth=get_author_by_lastname(session,"Tegmark")
# list_papers_by_author(auth)
# list_tags(session)
tag = get_tag(session,"helium")
list_papers_by_tag(tag)
# if __name__ == "__main__":
#     main()
