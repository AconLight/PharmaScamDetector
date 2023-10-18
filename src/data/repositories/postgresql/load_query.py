from pathlib import Path

import sqlalchemy

queries_path = Path.cwd() / 'src' / 'data' / 'repositories' / 'postgresql' / 'queries'


def query(directory, name):
    query_file = open((queries_path / directory / name).__str__())
    return sqlalchemy.text(query_file.read())
