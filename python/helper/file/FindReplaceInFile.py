import fileinput

read_file = open("C:\\Users\\touhid\\Desktop\\jimsenergy.sql", "r", errors='ignore')
data = read_file.read()

open_file = open("C:\\Users\\touhid\\Desktop\\db.sql", "w", errors='ignore')
open_file.write(data)
print(data)