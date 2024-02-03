import ibm_db
from shhh import *

# Connect to DB2
dsn_hostname = ibm_hostname
dsn_uid = ibm_uid
dsn_pwd = ibm_passwd
dsn_port = ibm_port
dsn_database = "bludb"
dsn_driver = "{IBM DB2 ODBC DRIVER}"
dsn_protocol = "TCPIP"
dsn_security = "SSL"

dsn = (
    f"DRIVER={dsn_driver};"
    f"DATABASE={dsn_database};"
    f"HOSTNAME={dsn_hostname};"
    f"PORT={dsn_port};"
    f"PROTOCOL={dsn_protocol};"
    f"UID={dsn_uid};"
    f"PWD={dsn_pwd};"
    f"SECURITY={dsn_security};"
)
conn = ibm_db.connect(dsn, "", "")
print("Connected to database:", dsn_database, "as user:", dsn_uid, "on host:", dsn_hostname)

# Find out the last rowid from DB2 data warehouse
def get_last_rowid():
    SQL = "SELECT MAX(ROWID) FROM sales_data"
    stmt = ibm_db.exec_immediate(conn, SQL)
    res = ibm_db.fetch_both(stmt)
    return int(res[0])

last_row_id = get_last_rowid()
print("Last row id on production datawarehouse:", last_row_id)

# List out all records in MySQL database with rowid greater than the one on the Data warehouse
def get_latest_records(rowid):
    SQL = "SELECT * FROM sales_data WHERE rowid > ?"
    stmt = ibm_db.prepare(conn, SQL)
    ibm_db.bind_param(stmt, 1, rowid)
    ibm_db.execute(stmt)
    new_records = []
    row = ibm_db.fetch_tuple(stmt)
    while row:
        new_records.append(row)
        row = ibm_db.fetch_tuple(stmt)
    return new_records


new_records = get_latest_records(last_row_id)

print("New rows on staging datawarehouse:", len(new_records))

# Insert the additional records from MySQL into DB2 data warehouse
def insert_records(records):
    SQL = "INSERT INTO sales_data(rowid, product_id, customer_id, quantity) VALUES (?, ?, ?, ?)"
    stmt = ibm_db.prepare(conn, SQL)

    for record in records:
        ibm_db.execute(stmt, record)

insert_records(new_records)
print("New rows inserted into production datawarehouse:", len(new_records))

# Disconnect from DB2 data warehouse
ibm_db.close(conn)

# End of program
