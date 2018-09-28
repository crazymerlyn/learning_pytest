"""Demonstrate tmpdir_factory."""

import json
import pytest

@pytest.fixture(scope='module')
def author_file_json(tmpdir_factory):
    """Write some authors to a data file."""
    python_author_data = {
        'Ned': {'City': 'Boston'},
        'Brian': {'City': 'Portland'},
        'Luciano': {'City': 'San Paulo'},
    }
    author_file = tmpdir_factory.mktemp('data').join('author_file.json')
    print('file:{}'.format(str(author_file)))

    with author_file.open('w') as f:
        json.dump(python_author_data, f)

    return author_file
