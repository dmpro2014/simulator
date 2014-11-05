opcodes = {
    'addi': 0b00001,
    'ldc': 0b00010,
    'sw': 0b00100,
    'lw': 0b01000,
    'thread_finished': 0b10000,
    }

instruction_formats = {
    'r': ['add', 'sub', 'and', 'or', 'xor', 'slt', 'sll', 'slr', 'sra'],
    'i': ['lw', 'sw', 'ldc', 'addi', 'thread_finished'],
    'nop': ['nop'],
    }


def get_instruction_format(opcode):
    for key, value in instruction_formats.iteritems():
        if opcode in value:
            return key
