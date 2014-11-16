from parse import parse
from utils import get_instruction_format, register_for_name


def parse_r_type(opcode, line):
    if opcode in ['add', 'sub', 'and', 'or', 'xor', 'mul', 'slt']:
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
        comment_index = line.find(';')
        if comment_index < 0:
            comment_index = len(line)
        bare_line = line[0:comment_index].replace('?', '').strip()
        opcode = bare_line.split(" ")[0]

        masked = line[0] == '?'

        instruction_format = get_instruction_format(opcode)

        instruction_tokens = ['nop']
        if instruction_format == 'r':
            instruction_tokens = parse_r_type(opcode, bare_line)
        if instruction_format == 'i':
            instruction_tokens = parse_i_type(opcode, bare_line)

        instruction_tokens = map(register_for_name, instruction_tokens)

        instructions.append(list(instruction_tokens) + [masked, line])
    return instructions
