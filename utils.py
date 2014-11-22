opcodes = {
    'addi': 0b00001,
    'ldi': 0b00001,  # Pseudo instruction
    'ldc': 0b00010,
    'sw': 0b00100,
    'lw': 0b01000,
    'thread_finished': 0b10000,
    }

instruction_formats = {
    'r': ['add', 'sub', 'and', 'or', 'xor', 'slt', 'sll', 'srl', 'sra', 'mv'],
    'i': ['lw', 'sw', 'ldc', 'addi', 'ldi', 'thread_finished'],
    'nop': ['nop'],
    }

funct_codes = {
    'sll': 0x00,
    'srl': 0x01,
    'sra': 0x02,
    'slt': 0x03,
    'add': 0x04,
    'mv': 0x04,
    'sub': 0x05,
    'and': 0x06,
    'or':  0x07,
    'xor': 0x08,
}

named_registers = {
    "zero": "0",
    "id_hi": "1",
    "id_lo": "2",
    "address_hi": "3",
    "address_lo": "4",
    "lsu_data": "5",
    "data": "5",
    "mask": "6",
}


def get_instruction_format(opcode):
    for key, value in instruction_formats.iteritems():
        if opcode in value:
            return key


def get_funct_code(instruction):
    return funct_codes[instruction]


def get_opcode(instruction):
    return opcodes[instruction]


def register_for_name(name):
    return named_registers.get(name, name)
