from SOSEMANUK import SOSEMANUK
key = 0x0123456789ABCDEF0123456789ABCDEF
initialVector = 0xFEDCBA9876543210FEDCBA9876543210
output = ""

Sose = SOSEMANUK(key, initialVector)
for i in range(7900):
    output += Sose.run()

with open("sosemanuk.hieu.txt", "w") as f:
    f.write(output)