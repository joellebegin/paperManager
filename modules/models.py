from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


author_paper = Table(
    "author_paper",
    Base.metadata,
    Column("author_id", Integer, ForeignKey("author.author_id")),
    Column("paper_id", Integer, ForeignKey("paper.paper_id")),
)

paper_tag1 = Table(
    "paper_tag1",
    Base.metadata,
    Column("paper_id", Integer, ForeignKey("paper.paper_id")),
    Column("tag1_id", Integer, ForeignKey("tag1.tag1_id")),
)

paper_tag2 = Table(
    "paper_tag2",
    Base.metadata,
    Column("paper_id", Integer, ForeignKey("paper.paper_id")),
    Column("tag2_id", Integer, ForeignKey("tag2.tag2_id")),
)

paper_tag3 = Table(
    "paper_tag3",
    Base.metadata,
    Column("paper_id", Integer, ForeignKey("paper.paper_id")),
    Column("tag3_id", Integer, ForeignKey("tag3.tag3_id")),
)

class Author(Base):
    __tablename__ = "author"
    author_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    papers = relationship(
        "Paper", secondary=author_paper, back_populates="authors"
    )


class Paper(Base):
    __tablename__ = "paper"
    paper_id = Column(Integer, primary_key=True)
    title = Column(String)
    year = Column(String)
    
    authors = relationship(
        "Author", secondary=author_paper, back_populates="papers"
    )

    tag1s = relationship(
        "Tag1", secondary=paper_tag1, back_populates="papers"
    )
    tag2s = relationship(
        "Tag2", secondary=paper_tag2, back_populates="papers"
    )
    tag3s = relationship(
        "Tag3", secondary=paper_tag3, back_populates="papers"
    )
    

class Tag1(Base):
    __tablename__ = "tag1"
    tag1_id = Column(Integer, primary_key=True)
    tag1 = Column(String)
    papers = relationship(
        "Paper", secondary=paper_tag1, back_populates="tag1s"
    )

class Tag2(Base):
    __tablename__ = "tag2"
    tag2_id = Column(Integer, primary_key=True)
    tag2 = Column(String)
    papers = relationship(
        "Paper", secondary=paper_tag2, back_populates="tag2s"
    )

class Tag3(Base):
    __tablename__ = "tag3"
    tag3_id = Column(Integer, primary_key=True)
    tag3 = Column(String)
    papers = relationship(
        "Paper", secondary=paper_tag3, back_populates="tag3s"
    )

