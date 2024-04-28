def shift(key,n):
  shifted_key = []
  for i in range (n,len(key)):
    shifted_key.append(key[i])
  for i in range(n):
      shifted_key.append(key[i])
  return shifted_key

def p8_conversion(final):
    a=[]
    n=(6, 3, 7, 4, 8, 5, 10, 9)
    for i in n:
        a += final[i-1]
    return a

def binary_to_decimal(binary):
    if binary == 0:
        return "0"
    decimal = 0
    power = len(binary) - 1
    for digit in binary:
        decimal += int(digit) * (2 ** power)
        power -= 1
    return decimal

def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal = decimal // 2
    return binary

def string_to_INT(binary_string):
    return [int(bit) for bit in binary_string]

def XOR_function(a,b):
    a = string_to_INT(a)
    b = string_to_INT(b)
    result = list(map(lambda x, y: x ^ y, a, b))
    return result

ip_key = str(input("Enter 10 bit string: "))
for i in ip_key.split():
    p  = { '1': i[0],
      '2': i[1],
      '3': i[2],
      '4': i[3],
      '5': i[4],
      '6': i[5],
      '7': i[6],
      '8': i[7],
      '9': i[8],
      '10': i[9],
      }

p10_keys=('3', '5', '2', '7', '4', '10', '1', '9', '8', '6')
p10 = list(map(p.get, p10_keys))
# print("P10 Permutation is: ",p10)

left = p10[:5]
right = p10[5:]

L_shifted_key1= shift(left,1)
L_shifted_key2= shift(right,1)
Combined_Key1 = L_shifted_key1 + L_shifted_key2
K1 = p8_conversion(Combined_Key1)
# print("Key1 is :",K1)

R_shifted_key1= shift(L_shifted_key1,2)
R_shifted_key2= shift(L_shifted_key2,2)
Combined_Key2 = R_shifted_key1 + R_shifted_key2
K2 = p8_conversion(Combined_Key2)
# print("Key2 is :",K2)

#Encryption Code
IP_Input = str(input("Enter 8 bit string: "))
for i in IP_Input.split():
    p  = { '1': i[0],
      '2': i[1],
      '3': i[2],
      '4': i[3],
      '5': i[4],
      '6': i[5],
      '7': i[6],
      '8': i[7],
      }

IP_keys=('2', '6', '3', '1', '4', '8', '5', '7')
IP = list(map(p.get, IP_keys))
left_IP = IP[:4]
right_IP = IP[4:]

EP_conversion = [4, 1, 2, 3, 2, 3, 4, 1]
Expanded_permutation_R = [right_IP[i - 1] for i in EP_conversion]

XOR_Key1 = XOR_function(K1,Expanded_permutation_R)

left_XOR_Key1 = XOR_Key1[:4]
right_XOR_Key1 = XOR_Key1[4:]

S0_Matrix = [[1,0,3,2],
      [3,2,1,0],
      [0,2,1,3],
      [3,1,3,2]]

S1_Matrix = [[0,1,2,3],
      [2,0,1,3],
      [3,0,1,0],
      [2,1,0,3]]

row_L = left_XOR_Key1[0], left_XOR_Key1[-1]
colm_L = left_XOR_Key1[1],left_XOR_Key1[-2]
row_L_decimal = binary_to_decimal(row_L)
col_L_decimal = binary_to_decimal(colm_L)
S0 = decimal_to_binary(S0_Matrix[row_L_decimal][col_L_decimal])

row_R = right_XOR_Key1[0], right_XOR_Key1[-1]
colm_R = right_XOR_Key1[1],right_XOR_Key1[-2]
row_R_decimal = binary_to_decimal(row_R)
col_R_decimal = binary_to_decimal(colm_R)
S1 = decimal_to_binary(S1_Matrix[row_R_decimal][col_R_decimal])

sbox_combine = []
sbox_combine.extend(string_to_INT(S0))
sbox_combine.extend(string_to_INT(S1))

p4_permutation = [2, 4, 3, 1]
p4 = [sbox_combine[i - 1] for i in p4_permutation]

p4_XOR = XOR_function(left_IP,p4)
combination = string_to_INT(right_IP) + p4_XOR

combination_l = combination[:4]
combination_r = combination[4:]

expansion_permutation = [4, 1, 2, 3, 2, 3, 4, 1]
expanded_right = [combination_r[i - 1] for i in expansion_permutation]

XOR_3 = XOR_function(K2,expanded_right)
XOR_3_l = XOR_3[:4]
XOR_3_r = XOR_3[4:]

row_left = XOR_3_l[0] , XOR_3_l[-1]
column_left = XOR_3_l[1] , XOR_3_l[-2]
row_left_decimal = binary_to_decimal(row_left)
column_left_decimal = binary_to_decimal(column_left)
S0_key2 = decimal_to_binary(S0_Matrix[row_left_decimal][column_left_decimal])

row_right = str(XOR_3_r[0]) + str(XOR_3_r[-1])
column_right = str(XOR_3_r[1]) + str(XOR_3_r[-2])
row_right_decimal = binary_to_decimal(row_right)
column_right_decimal = binary_to_decimal(column_right)
S1_key2 = decimal_to_binary(S1_Matrix[row_right_decimal][column_right_decimal])

SBox_Combination = list(S0_key2 + S1_key2)

p4_sbox = [SBox_Combination[i - 1] for i in p4_permutation]
XOR_4 = XOR_function(combination_l,p4_sbox)

combination2 = XOR_4 + combination_r

Inverse_Initial_Permutation = [4, 1, 3, 5, 7, 2, 8, 6]
cipher_text = [combination2[i - 1] for i in Inverse_Initial_Permutation]
print(f"8-bit Cipher Text will be : {cipher_text}")