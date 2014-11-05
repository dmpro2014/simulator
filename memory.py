sram_memory = [0]*1048576


def memory_write(address_hi, address_low, data):
    address = (address_hi << 16) + address_low
    sram_memory[address] = data


def memory_read(address_hi, address_low):
    address = (address_hi << 16) + address_low
    return sram_memory[address]


def memory_dump(start, end):
    return sram_memory[start:end]
