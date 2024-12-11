import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/testdb")
ELASTICSEARCH_URL = os.getenv("ELASTICSEARCH_URL", "http://localhost:9200")
