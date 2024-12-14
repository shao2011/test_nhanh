

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

# Connect to Cassandra
cluster = Cluster(["my-cassandra-0"])  # Replace with your Cassandra service IP or hostname # "my-cassandra.default.svc.cluster.local:9042"
session = cluster.connect()

# Create Keyspace and Table
session.execute("""
    CREATE KEYSPACE IF NOT EXISTS test_keyspace
    WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '3'}
""")

session.set_keyspace("test_keyspace")

session.execute("""
    CREATE TABLE IF NOT EXISTS user_data (
        id INT PRIMARY KEY, 
        name TEXT, 
        age INT
    )
""")

# Insert Data
session.execute("""
    INSERT INTO user_data (id, name, age) 
    VALUES (1, 'Alice', 30)
""")
session.execute("""
    INSERT INTO user_data (id, name, age) 
    VALUES (2, 'Bob', 25)
""")

# Query Data
rows = session.execute("SELECT * FROM user_data")
for row in rows:
    print(f"ID: {row.id}, Name: {row.name}, Age: {row.age}")

# Close Connection
cluster.shutdown()

