import happybase
import csv

# Kết nối đến HBase Thrift server
connection = happybase.Connection('localhost', port=9090)
table_name = 'real_estate'

# Tạo bảng nếu chưa có
if table_name.encode() not in connection.tables():
    connection.create_table(
        table_name,
        {'info': dict()}  # column family
    )

table = connection.table(table_name)

# Đọc file CSV
with open('output.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for idx, row in enumerate(reader):
        row_key = f"row{idx}"
        table.put(row_key, {
            b'info:TieuDe': row['TieuDe'].encode(),
            b'info:Gia': row['Gia'].encode(),
            b'info:DienTich': row['DienTich'].encode(),
            b'info:GiaTrenM2': row['GiaTrenM2'].encode(),
            b'info:PhongNgu': row['PhongNgu'].encode(),
            b'info:WC': row['WC'].encode(),
            b'info:Quan': row['Quan'].encode(),
            b'info:TinhThanh': row['TinhThanh'].encode()
        })

print("Dữ liệu đã được import vào HBase.")
