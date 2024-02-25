import math


def main():
    ieee754_converted = ""
    remainder = []
    number_in_front_of_decimal = []
    exponent_bias_binary = []
    real_number = float(input('Enter a real number: '))
    whole_number = abs(int(real_number))
    whole_to_binary(whole_number, remainder)
    remainder.reverse()
    binary_of_whole = (''.join(map(str, remainder)))
    decimal_portion_str = str(real_number).split('.')[1]
    decimal_portion = float('0.' + decimal_portion_str)
    decimal_to_binary(decimal_portion, number_in_front_of_decimal)
    binary_of_decimal = (''.join(map(str,  number_in_front_of_decimal)))
    combined = float(binary_of_whole + "." + binary_of_decimal)
    combined_string = str(combined)
    combined_list = list(combined_string)
    decimal_place = combined_list.index('.') - 1
    exponent_bias = int(127 + decimal_place)
    whole_to_binary(exponent_bias, exponent_bias_binary)
    exponent_bias_binary.reverse()
    binary_of_exponent_bias = (''.join(map(str, exponent_bias_binary)))
    combined_list.pop(0)
    combined_list.remove('.')
    combined_string_final = (''.join(map(str,  combined_list)))
    if real_number >= 0:
        ieee754_converted += "0"
        ieee754_converted += binary_of_exponent_bias
        ieee754_converted += combined_string_final
        size_binary = len(ieee754_converted)
        num_zero = 32 - size_binary
        ieee754_converted += "0" * num_zero
        print("IEEE 754 Single Precision: " + ieee754_converted)
    else:
        ieee754_converted += "1"
        ieee754_converted += binary_of_exponent_bias
        ieee754_converted += combined_string_final
        size_binary = len(ieee754_converted)
        num_zero = 32 - size_binary
        ieee754_converted += "0" * num_zero
        print("IEEE 754 Single Precision: " + ieee754_converted)

    ieee754 = str(input('Enter IEEE 754 Single Precision: '))
    exponent_in_binary = str(ieee754[1:9])
    index = len(exponent_in_binary) - 1
    power_val_compute = len(exponent_in_binary) - 1
    calculating_val = 0
    while index >= 0:
        bit_value = int(exponent_in_binary[index])
        exponent_val = int(power_val_compute - index)
        current_val = int(bit_value * (2 ** exponent_val))
        calculating_val += current_val
        index -= 1
    exponent = calculating_val - 127
    mantissa = str(ieee754[9:18])
    mantissa_index = len(mantissa)
    index_counter = int(0)
    counter = int(1)
    calculating_val = 0
    while counter < mantissa_index + 1:
        bit_value = int(mantissa[index_counter])
        exponent_val = counter * -1
        current_val = bit_value * (2 ** exponent_val)
        calculating_val += current_val
        counter += 1
        index_counter += 1
    if ieee754[0] == "0":
        real_number_converted = (1 + calculating_val) * (2 ** exponent)
        print("Real number: " + str(real_number_converted))
    elif ieee754[0] == "1":
        real_number_converted = -1 * (1 + calculating_val) * (2 ** exponent)
        print("Real number: " + str(real_number_converted))


def whole_to_binary(number, remainder):
    while number != 0:
        remainder_val = number % 2
        remainder += [remainder_val]
        number = number // 2
        return whole_to_binary(number, remainder)


def decimal_to_binary(decimal_portion, number_in_front_of_decimal):
    while decimal_portion != 0.00:
        decimal_portion = float(decimal_portion * 2)
        decimal_portion = float(format(decimal_portion, '.2f'))
        num_in_front = math.floor(decimal_portion)
        number_in_front_of_decimal += [num_in_front]
        decimal_portion -= num_in_front
        return decimal_to_binary(decimal_portion, number_in_front_of_decimal)


main()
