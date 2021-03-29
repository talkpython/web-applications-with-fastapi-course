from pathlib import Path
from typing import Callable, Optional

import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, AsyncSession
from sqlalchemy.orm import Session

from data.modelbase import SqlAlchemyBase

__factory: Optional[Callable[[], Session]] = None
__async_engine: Optional[AsyncEngine] = None


def global_init(db_file: str):
    global __factory, __async_engine

    if __factory:
        return

    if not db_file or not db_file.strip():
        raise Exception("You must specify a db file.")

    folder = Path(db_file).parent
    folder.mkdir(parents=True, exist_ok=True)

    # Post-recording update:
    # SQLAlchemy started enforcing the underlying Python DB API was truly async
    # We don't really get that with SQLite but when you switch something like Postgres
    # It would "light up" with async. Since recording, SQLAlchemy throws and error
    # if this would be the case. We need to explicitly switch to aiosqlite as below.
    conn_str = 'sqlite+pysqlite:///' + db_file.strip()
    async_conn_str = 'sqlite+aiosqlite:///' + db_file.strip()
    print("Connecting to DB with {}".format(async_conn_str))

    # Adding check_same_thread = False after the recording. This can be an issue about
    # creating / owner thread when cleaning up sessions, etc. This is a sqlite restriction
    # that we probably don't care about in this example.
    engine = sa.create_engine(conn_str, echo=False, connect_args={"check_same_thread": False})
    __async_engine = create_async_engine(async_conn_str, echo=False, connect_args={"check_same_thread": False})
    __factory = orm.sessionmaker(bind=engine)

    # noinspection PyUnresolvedReferences
    import data.__all_models

    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global __factory

    if not __factory:
        raise Exception("You must call global_init() before using this method.")

    session: Session = __factory()
    session.expire_on_commit = False

    return session


def create_async_session() -> AsyncSession:
    global __async_engine

    if not __async_engine:
        raise Exception("You must call global_init() before using this method.")

    session: AsyncSession = AsyncSession(__async_engine)
    session.sync_session.expire_on_commit = False

    return session
