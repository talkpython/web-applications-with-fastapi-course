from pathlib import Path
from typing import Callable, Optional

import sqlalchemy as sa
import sqlalchemy.orm as orm
from data.modelbase import SqlAlchemyBase
from sqlalchemy.orm import Session

__factory: Optional[Callable[[], Session]] = None


def global_init(db_file: str):
    global __factory

    if __factory:
        return

    if not db_file or not db_file.strip():
        raise Exception('You must specify a db file.')

    folder = Path(db_file).parent
    folder.mkdir(parents=True, exist_ok=True)

    conn_str = 'sqlite:///' + db_file.strip()
    print('Connecting to DB with {}'.format(conn_str))

    # Adding check_same_thread = False after the recording. This can be an issue about
    # creating / owner thread when cleaning up sessions, etc. This is a sqlite restriction
    # that we probably don't care about in this example.
    engine = sa.create_engine(conn_str, echo=False, connect_args={'check_same_thread': False})
    __factory = orm.sessionmaker(bind=engine)

    # noinspection PyUnresolvedReferences
    import data.__all_models

    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global __factory

    if not __factory:
        raise Exception('You must call global_init() before using this method.')

    session: Session = __factory()
    session.expire_on_commit = False

    return session
