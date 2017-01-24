import tempfile

DATASET_DATABASE_URI = 'sqlite:///{}'.format(tempfile.mktemp(suffix='db'))
TESTING = True