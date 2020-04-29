e = 3
c = 219878849218803628752496734037301843801487889344508611639028
n = 245841236512478852752909734912575581815967630033049838269083

 # n1 € N
 # c = m^e (mod n)
 # (c + n1 * n) % n = (m^e) % n
 # c + n1 * n = m^e
 # m = e_root(c + n1 * n)
# n1 = 0
# while True:
#     m = int((c + n * n1) ** (1. / 3))
#     n1 += 1
#     try:
#         string = str(bytes.fromhex(hex(m)[2:]).decode())
#         if '{' in string and '}' in string:
#             print(string)
#             print(m)
#     except UnicodeDecodeError as e:
#         continue
#     except ValueError as e:
#         continue
