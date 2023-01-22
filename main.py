bin_or_dec = input("Digite b para binário ou d para decimal: ")
num_real = input("Digite o número: ")


def decimal_to_bin(num):
    inv_bin = [0] * 8
    q = num
    i = 0
    while q >= 1:
        q = num // 2
        inv_bin[i] = num % 2
        num = q
        i += 1
    inv_bin.reverse()
    return inv_bin


def bin_to_dec(bin, exp=0):
    if len(bin) == 4:
        exp -= 4

    int_decimal = 0
    for item in reversed(range(len(bin))):
        int_decimal += bin[item] * 2 ** exp
        exp += 1
    return int_decimal


def invert(int_bin):
    i = 0
    for item in int_bin:
        if item == 0:
            int_bin[i] = 1
        else:
            int_bin[i] = 0
        i += 1
    return int_bin


def op_dec_bin(num_real):
    if '.' in num_real:
        num_real = float(num_real)
    else:
        num_real = int(num_real)

    num = abs(int(num_real))

    if num > 127:
        print("OverflowError")
        exit()

    int_bin = (decimal_to_bin(num))
    if type(num_real) == int:
        if num_real < 0:
            result = invert(int_bin)
        else:
            result = int_bin

        return ''.join(str(e) for e in result)

    elif type(num_real) == float:
        deci_bin = []
        deci = abs(num_real - int(num_real))
        for item in range(8):
            deci *= 2
            deci_bin.append(int(deci))
            if deci > 1:
                deci -= 1
            elif deci == 1:
                break
        comma_bin = int_bin + deci_bin

        if 1 in int_bin:
            exp = len(int_bin) - int_bin.index(1)

        elif 1 in deci_bin:
            exp = - deci_bin.index(1)
        else:
            print("UnderflowError")
            exit()

        # print(exp)
        if exp < -4:
            print("UnderflowError")
            exit()
        elif exp > 3:
            print("OverflowError")
            exit()

        exp_bin = (decimal_to_bin(exp + 4)[5:])
        # print(exp_bin)

        i = 0
        manti = [0] * 4
        for k, j in zip(manti, comma_bin[comma_bin.index(1):comma_bin.index(1) + 4]):
            manti[i] = k + j
            i += 1
        # print(manti)
        # print(comma_bin)

        if num_real > 0:
            neg_vect = [0]
        else:
            neg_vect = [1]

        float_bin = neg_vect + exp_bin + manti
        return ''.join(str(e) for e in float_bin)


def op_bin_dec(num_real):
    num_bin = num_real
    int_bin = []
    int_decimal = 0
    operation = int(input("Pressione 1 para inteiro ou 2 para float: "))

    if len(num_bin) > 8:
        print("OverflowError")
        exit()

    for j in ('{:08d}'.format(int(num_bin))):
        int_bin.append(int(j))

    if 1 not in int_bin and int_bin != [0] * 8:
        print("ValueError")
        exit()

    if operation == 1:
        neg = 1
        if int_bin[0] == 1:
            int_bin = invert(int_bin)
            neg = -1

        # print(int_bin)
        return neg * bin_to_dec(int_bin)

    elif operation == 2:
        if int_bin[4] == 0:
            print("ValueError")
            exit()

        neg = 1
        if int_bin[0] == 1:
            neg = -1

        exp = bin_to_dec(int_bin[1:4]) - 4
        result = neg * bin_to_dec(int_bin[4:], exp)
        return result

    else:
        print("Error")
        exit()



if bin_or_dec.lower() == 'd':
    print(op_dec_bin(num_real))
elif bin_or_dec.lower() == 'b':
    print(op_bin_dec(num_real))
else:
    print("Error")


'''
j = 0
for i in range(-127, 128):
    if not op_bin_dec(op_dec_bin(str(i))) == i:
        j += 1
    print(True)
print(j)


for i in list(map(lambda x: 2**x, range(-4,3))):
    if not op_bin_dec(op_dec_bin(str(i))) == i:
        j += 1
        print(i)
    print(True)
print(j)
'''