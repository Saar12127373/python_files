open_File = open(r"C:\8200\statring_binary\file.txt", "rb")
data = open_File.read()
open_File.close()

open_File = open(r"C:\8200\statring_binary\file.txt", "wb")


for i in range(len(data)):
    
    open_File.write((data[i]^5).to_bytes(1,"little"))
    
open_File.close()