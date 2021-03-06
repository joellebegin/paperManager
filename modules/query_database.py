
from sqlalchemy import and_, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import asc, desc, func

from modules.models import Author, Paper, Tag
from treelib import Tree

import numpy as np


def list_authors(session):
    """Get a list of author objects sorted by last name"""
    return session.query(Author).order_by(Author.last_name).all()

def get_author_by_lastname(session, lastname):
    return session.query(Author).filter_by(last_name=lastname).all()[0]

def get_tag(session, tag_name):
    return session.query(Tag).filter_by(tag=tag_name).all()[0]

def list_papers_by_author(author):
    """Get list of all papers by given author

    Args:
        author: author object as defined in models
        
    Returns:
        List: list of papers by that author
    """

    print(f"\nPapers by {author.first_name} {author.last_name}:\n")
    for paper in author.papers:
        #tags = [paper.tag1s[0].tag1, paper.tag2s[0].tag2, paper.tag3s[0].tag3]
        #tags_formatted = list(filter(None,tags))
        tags = [i.tag for i in paper.tags]
        author_lastnames = [i.last_name for i in paper.authors]
        print('%s.' % ', '.join(map(str, author_lastnames)),f"{paper.title} ({paper.year})")
        print('  [%s]' % ', '.join(map(str, tags)),"\n")
        # print(paper.title)
    
def list_papers_by_tag(tag):
    for paper in tag.papers:
        tags = [i.tag for i in paper.tags]
        author_lastnames = [i.last_name for i in paper.authors]
        print('%s.' % ', '.join(map(str, author_lastnames)),f"{paper.title} ({paper.year})")
        print('  [%s]' % ', '.join(map(str, tags)),"\n")


def list_tags(session):
    tags_objects = session.query(Tag).order_by(Tag.tag).all()
    tags=[i.tag for i in tags_objects]
    print('[%s]' % ', '.join(map(str, tags)),"\n")



def tree(authors):
    """
    Outputs the author/book/publisher information in
    a hierarchical manner

    :param authors:         the collection of root author objects
    :return:                None
    """
    authors_tree = Tree()
    authors_tree.create_node("Authors", "authors")
    for author in authors:
        author_id = f"{author.first_name} {author.last_name}"
        authors_tree.create_node(author_id, author_id, parent="authors")
        for paper in author.papers:
            paper_id = f"{author_id}:{paper.title}"
            authors_tree.create_node(paper.title, paper_id, parent=author_id)
    authors_tree.show()