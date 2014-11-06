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

        instruction_tokens = ['nop']
        if instruction_format == 'r':
            instruction_tokens = parse_r_type(opcode, line)
        if instruction_format == 'i':
            instruction_tokens = parse_i_type(opcode, line)

        instructions.append(list(instruction_tokens) + [line])
    return instructions
