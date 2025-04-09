import pyodbc

# Thay đổi thông tin dưới đây với thông tin của bạn
server = '192.168.1.84\\SQLEXPRESS,1433'  # Địa chỉ IP và cổng SQL Server
database = "LOGIN"

# Chuỗi kết nối
conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes'

try:
    conn = pyodbc.connect(conn_str)
    print("Kết nối thành công!")
    conn.close()
except Exception as e:
    print(f"Lỗi kết nối: {e}")
    print(f"Chi tiết lỗi: {e.args}") 