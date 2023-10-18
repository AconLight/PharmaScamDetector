import os
from pathlib import Path

import sqlalchemy

queries_path = Path.cwd() / 'src' / 'data' / 'repositories' / 'postgresql' / 'queries'


def query(directories, name):
    path = queries_path
    for directory in directories:
        path /= directory
    query_file = open((path / f'{name}.sql').__str__())
    return sqlalchemy.text(query_file.read())
