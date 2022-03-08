"""
This program builds the author_book_publisher Sqlite database from the
author_book_publisher.csv file.
"""

import os
import csv
from importlib import resources
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modules.models import Base, Author, Paper, Tag

def get_data(filepath):
    """
    This function gets the data from the csv file
    """
    with open(filepath) as csvfile:
        csv_reader = csv.DictReader(csvfile)
        data = [row for row in csv_reader]
        return data


def populate_database(session, data):
    # insert the data
    for row in data:
        
        paper = (
            session.query(Paper)
            .filter(Paper.title == row["title"])
            .one_or_none()
        )
        if paper is None:
            paper = Paper(title=row["title"], year=row["year"])
            session.add(paper)
        
        #=====================================================#
        #======================== TAGS =======================#
        #=====================================================#
        tags = row["tags"].split(",")
        
        for t in tags:
        
            tag_word = list(filter(None,t.split(" ")))[0]
            
            tag = (
                session.query(Tag)
                .filter(Tag.tag == tag_word)
                .one_or_none()
            )
            if tag is None:
                tag = Tag(tag=tag_word)
                session.add(tag)
        
            tag.papers.append(paper)
            paper.tags.append(tag)

            session.commit()
        
        
        #=====================================================#
        #======================= AUTHORS =====================#
        #=====================================================#
        authors = row["authors"].split(",")
        for auth in authors:
            name = list(filter(None,auth.split(" ")))
            #print(names)
            
            author = (
            session.query(Author)
            .filter(Author.last_name == name[1])
            .one_or_none()
            )
            if author is None:
                author = Author(first_name=name[0], last_name=name[1])
                session.add(author)

            author.papers.append(paper)
            paper.authors.append(author)

            session.commit()
        

    session.close()


def main():
    print("starting")

    # get the author/book/publisher data into a dictionary structure
    csv_filepath = "table.csv"
    data = get_data(csv_filepath)

    # get the filepath to the database file
    sqlite_filepath="data.db"
    # does the database exist?
    if os.path.exists(sqlite_filepath):
        os.remove(sqlite_filepath)

    # create the database
    engine = create_engine(f"sqlite:///{sqlite_filepath}")
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    populate_database(session, data)

    print("finished")


if __name__ == "__main__":
    main()
