from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, MetaData

# Define the database URL
db_url = "postgresql://user:password@localhost/database_name"

# Connect to the database using SQLAlchemy
engine = create_engine(db_url)
conn = engine.connect()

# Define the table structure using SQLAlchemy
metadata = MetaData()
table = Table("example_table", metadata,
    Column("id", Integer, primary_key=True),
    Column("column_1", Integer),
    Column("column_2", Integer),
)

# Create the table in the database
table.create(conn, checkfirst=True)

# Execute a database migration
conn.execute("ALTER TABLE example_table ADD COLUMN column_3 INTEGER")

# Close the connection to the database
conn.
