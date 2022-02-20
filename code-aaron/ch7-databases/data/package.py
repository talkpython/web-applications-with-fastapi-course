from typing import List
import sqlalchemy as sa
import sqlalchemy.orm as orm
from datetime import datetime
from data.release import Release
from data.modelbase import SqlAlchemyBase

class Package(SqlAlchemyBase):
    __tablename__ = 'packages'
    id: str = sa.Column(sa.String, primary_key=True)
    created_date: datetime = sa.Column(sa.DateTime, index=True, default=datetime.now)
    last_updated: datetime = sa.Column(sa.DateTime, index=True, default=datetime.now)
    summary : str = sa.Column(sa.String, nullable=False)
    description : str = sa.Column(sa.String, nullable=True)
    
    home_page : str = sa.Column(sa.String)
    docs_url : str = sa.Column(sa.String)
    package_url : str = sa.Column(sa.String)
    
    author_name : str = sa.Column(sa.String)
    author_email : str = sa.Column(sa.String, index=True)
    
    license : str = sa.Column(sa.String, index=True)
    
    #releases relationship
    releases: List[Release] = orm.relation("Release", order_by = [
        Release.major_ver.desc(),
        Release.minor_ver.desc(),
        Release.build_ver.desc(),
    ], back_populates='package')
    
    def __repr__(self):
        return f"<Package {self.id}>"