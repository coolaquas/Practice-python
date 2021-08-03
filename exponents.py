def Sample_1_raise_to_power(base, power):
    return base**power


print(Sample_1_raise_to_power(9, 0.5))


def Sample_2_raise_to_power(base, power):
    result = 1
    for index in range(power):
        result = result * base
    return result


print(Sample_2_raise_to_power(2, 10))
