"""
This program builds the author_book_publisher Sqlite database from the
author_book_publisher.csv file.
"""

import os
import csv
from importlib import resources
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modules.models import Base, Author, Paper, Tag1, Tag2, Tag3

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

        #========== tag1 ==========#
        tag1 = (
            session.query(Tag1)
            .filter(Tag1.tag1 == row["tag1"])
            .one_or_none()
        )
        if tag1 is None:
            tag1 = Tag1(tag1=row["tag1"])
            session.add(tag1)

        #========== tag2 ==========#
        tag2 = (
            session.query(Tag2)
            .filter(Tag2.tag2 == row["tag2"])
            .one_or_none()
        )

        if tag2 is None:
            tag2 = Tag2(tag2=row["tag2"])
            session.add(tag2)

        #========== tag3 ==========#
        tag3 = (
            session.query(Tag3)
            .filter(Tag3.tag3 == row["tag3"])
            .one_or_none()
        )
        if tag3 is None:
            tag3 = Tag3(tag3=row["tag3"])
            session.add(tag3)
        
        paper.tag1s.append(tag1)
        paper.tag2s.append(tag2)
        paper.tag3s.append(tag3)
        
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
