from parse import parse
from utils import get_instruction_format


def parse_r_type(opcode, line):
    if opcode in ['add', 'sub', 'and', 'or', 'xor']:
        return parse("{} ${}, ${}, ${}", line)
    if opcode in ['sll', 'srl', 'sra']:
        return parse("{} ${}, ${}, {}", line)


def parse_i_type(opcode, line):
    if opcode in ['sw', 'lw', 'thread_finished']:
        return [opcode]
    if opcode == 'ldc':
        return parse("{} ${}, {}", line)
    if opcode == 'addi':
        return parse("{} ${}, ${}, {}", line)


def scan(input):
    instructions = []
    for line in input:
        opcode = line.strip().split(" ")[0]

        instruction_format = get_instruction_format(opcode)

        encoded_instruction = 0  # Default to nop
        if instruction_format == 'r':
            encoded_instruction = parse_r_type(opcode, line)
        if instruction_format == 'i':
            encoded_instruction = parse_i_type(opcode, line)
        if opcode == 'nop':
            encoded_instruction = ('nop')

        instructions.append(encoded_instruction)
    return instructions
