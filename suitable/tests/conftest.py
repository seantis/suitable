import pytest
import shutil
import tempfile


@pytest.fixture()
def tempdir():
    tempdir = tempfile.mkdtemp()
    yield tempdir
    shutil.rmtree(tempdir)
