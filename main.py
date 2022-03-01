from importlib import resources

from sqlalchemy import and_, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import asc, desc, func

from modules.models import Author, Paper 
from modules.query_database import tree, get_author_by_lastname, get_papers_by_author, get_authors

# def main():
"""Main entry point of program"""

# Connect to the database using SQLAlchemy
sqlite_filepath = "data.db"
engine = create_engine(f"sqlite:///{sqlite_filepath}")
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

# Output hierarchical authors data
authors = get_authors(session)
tree(authors)

adrian=get_author_by_lastname(session,"Liu")
get_papers_by_author(adrian)

# if __name__ == "__main__":
#     main()
