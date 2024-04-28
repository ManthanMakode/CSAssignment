def XOR_Function(a, b):
    return list(map(lambda x, y: x ^ y, a, b))

def RotateNibble(a):
    return a[4:] + a[:4]

def swapNibble_function(a):
    return a[:4] + a[12:] + a[8:12] + a[4:8]

def list_to_string(list):
    return ''.join(str(bit) for bit in list)

def string_to_list(string):
    return [int(bit) for bit in string]

def SubNib_function(rot_nib):
    temp = ''
    for nibble in [rot_nib[:4], rot_nib[4:]]:
        n_str = list_to_string(nibble)
        temp += s_box[n_str]
    return string_to_list(temp)

def SubNib_function_16bit(rot_nib,a):
    temp = ''
    for nibble in [rot_nib[:4], rot_nib[4:8],rot_nib[8:12],rot_nib[12:]]:
        n_str = list_to_string(nibble)
        temp += a[n_str]
    return string_to_list(temp)

def binary_to_hex(binary_num):
    decimal_num = int(binary_num, 2)
    hex_num = format(decimal_num, 'X')
    return hex_num

def hex_to_binary(hex_num):
    binary_num = format(int(hex_num, 16), '04b')
    return binary_num

def map_mixCols(value1, value2):
    if value1 == '1':
        return value2
    elif value2 == '1':
        return value1
    return mixColumns[value1][value2]

def mix_column_result(result):
    results = []
    for i in range(2):
        for j in range(2):
            for k in range(1):
                num1 = hex_to_binary(result[i][j][k])
                if k + 1 < len(result[i][j]):
                    num2 = hex_to_binary(result[i][j][k + 1])
                else:
                    num2 = hex_to_binary("00")
                num1_lst = [int(bit) for bit in num1]
                num2_lst = [int(bit) for bit in num2]
                result_xor = XOR_Function(num1_lst, num2_lst)
                results.extend(result_xor)
    return results

s_box = {
'0000':'1001','1000': '0110',
'0001': '0100','1001': '0010',
'0010': '1010','1010': '0000',
'0011': '1011','1011': '0011',
'0100': '1101','1100': '1100',
'0101': '0001','1101': '1110',
'0110': '1000','1110': '1111',
'0111': '0101','1111': '0111'
}

s_box_inverse = {
    '1001': '0000','0110': '1000', 
    '0100': '0001','0010': '1001', 
    '1010': '0010','0000': '1010', 
    '1011': '0011','0011': '1011', 
    '1101': '0100','1100': '1100', 
    '0001': '0101','1110': '1101',
    '1000': '0110','1111': '1110',
    '0101': '0111','0111': '1111'}

key_String = input("Enter the 16 bit key : ")
key_16bit =[]
for i in key_String:
    key_16bit.append(int(i))

w0 = key_16bit[:8]
w1 = key_16bit[8:]

RotNib_w2 = RotateNibble(w1)
SubNib_w2 = SubNib_function(RotNib_w2)
RCon_1 = [1,0,0,0,0,0,0,0]
XOR1 = XOR_Function(RCon_1,SubNib_w2)
w2 =  XOR_Function(w0,XOR1)
w3 = XOR_Function(w2,w1)

RotNib_w4 = RotateNibble(w3)
SubNib_w4 = SubNib_function(RotNib_w4)
RCon_2 = [0,0,1,1,0,0,0,0]
XOR2 = XOR_Function(RCon_2,SubNib_w4)
w4 =  XOR_Function(w2,XOR2)
w5 = XOR_Function(w4,w3)

Key_0 = w0 + w1
Key_1 = w2 + w3
Key_2 = w4 + w5

plain_text_ip = input("Enter the 16 bit plaintext : ")
plain_text =[]
for i in plain_text_ip:
    plain_text.append(int(i))

R0 = XOR_Function(plain_text,Key_0)
SubNib_R1 = SubNib_function_16bit(R0,s_box)
ShRow = swapNibble_function(SubNib_R1)

mixColumns = {
    '1': {'2': '2', '4': '4', '9': '9'},
    '2': {'2': '4', '4': '8', '9': '1'},
    '3': {'2': '6', '4': 'C', '9': '8'},
    '4': {'2': '8', '4': '3', '9': '2'},
    '5': {'2': 'A', '4': '7', '9': 'B'},
    '6': {'2': 'C', '4': 'B', '9': '3'},
    '7': {'2': 'E', '4': 'F', '9': 'A'},
    '8': {'2': '3', '4': '6', '9': '4'},
    '9': {'2': '1', '4': '2', '9': 'D'},
    'A': {'2': '7', '4': 'E', '9': '5'},
    'B': {'2': '5', '4': 'A', '9': 'C'},
    'C': {'2': 'B', '4': '5', '9': '6'},
    'D': {'2': '9', '4': '1', '9': 'F'},
    'E': {'2': 'F', '4': 'D', '9': '7'},
    'F': {'2': 'D', '4': '9', '9': 'E'}
}

A = binary_to_hex(list_to_string(ShRow[:4]))
B = binary_to_hex(list_to_string(ShRow[4:8]))
C = binary_to_hex(list_to_string(ShRow[8:12]))
D = binary_to_hex(list_to_string(ShRow[12:]))

matrix1 = [[A, B], [C, D]]
matrix2 = [['1','4'],['4','1']]
result = [['', ''],['', '']]
for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix1)):
            result[i][j] += map_mixCols(matrix1[i][k] , matrix2[k][j])

MixCol = mix_column_result(result)
R1 = XOR_Function(Key_1,MixCol)
R2 = XOR_Function(Key_2,swapNibble_function(SubNib_function_16bit(R1,s_box)))
print(f"Encrypted text OR Cipher text = {R2}")

R0_decryption = XOR_Function(R2, Key_2)
IShRow = swapNibble_function(R0_decryption)
ISubNib = SubNib_function_16bit(IShRow,s_box_inverse)
R1_mixColm = XOR_Function(ISubNib,Key_1)

A1 = binary_to_hex(list_to_string(R1_mixColm[:4]))
B1 = binary_to_hex(list_to_string(R1_mixColm[4:8]))
C1 = binary_to_hex(list_to_string(R1_mixColm[8:12]))
D1 = binary_to_hex(list_to_string(R1_mixColm[12:]))

matrix_1 = [[A1, B1], [C1, D1]]
matrix_2 = [['9','2'],['2','9']]
result_1 = [['', ''],['', '']]

for i in range(len(matrix_1)):
    for j in range(len(matrix_2[0])):
        for k in range(len(matrix_1)):
            result_1[i][j] += map_mixCols(matrix_1[i][k] , matrix_2[k][j])

R1 = mix_column_result(result_1)

R2 = XOR_Function(SubNib_function_16bit(swapNibble_function(R1),s_box_inverse),Key_0)
print(f"Decrypted text = {R2}")