from sys import stdin
from scanner import scan
from utils import get_instruction_format, get_funct_code, get_opcode
import argparse


def parse_r_instruction(instruction_tokens):
    instruction = instruction_tokens[0]

    alu_function = get_funct_code(instruction)
    opcode = 0

    if instruction in ['add', 'sub', 'and', 'or', 'xor', 'slt']:
        rd, rs, rt = map(eval, list(instruction_tokens)[1:4])
        sh = 0

    if instruction in ['sll', 'srl', 'sra']:
        rd, rt, sh = map(eval, list(instruction_tokens)[1:4])
        rs = 0

    return (opcode << 26) + (rs << 21) + (rt << 16) + (rd << 11) + (sh << 6) + alu_function


def parse_i_instruction(instruction_tokens):
    instruction = instruction_tokens[0]

    opcode = get_opcode(instruction)

    if instruction in ['sw', 'lw', 'nop', 'thread_finished']:
        return (opcode << 26)
    if instruction == 'ldc':
        rd, immediate = map(eval, list(instruction_tokens)[1:3])
        return (opcode << 26) + (rd << 16) + immediate
    if instruction == 'addi':
        rd, rs, immediate = map(eval, list(instruction_tokens)[1:4])
        return (opcode << 26) + (rs << 21) + (rd << 16) + immediate


def assemble(source, nop_count=0):
    program = []
    tail = ['nop'] * nop_count + ['thread_finished']

    for instruction_tokens in scan(source) + scan(tail):
        instruction_format = get_instruction_format(instruction_tokens[0])
        print instruction_tokens[0], instruction_format

        encoded_instruction = 0
        if instruction_format == 'i':
            encoded_instruction = parse_i_instruction(instruction_tokens)
        if instruction_format == 'r':
            encoded_instruction = parse_r_instruction(instruction_tokens)

        if instruction_tokens[-2]:  # Mask
            encoded_instruction += (1 << 31)

        program.append('X"{:08x}", -- {}'.format(encoded_instruction, instruction_tokens[-1]))

    program[-1] = program[-1].replace(',', '', 1)
    return program

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="MIPS Assembler")
    parser.add_argument(
        '--hostcomm',
        dest='hostcomm',
        action='store_true',
        help='Will reverse endianness, and produce bare hex output')
    parser.add_argument(
        '--nop',
        dest='nop_count',
        type=int,
        nargs='?',
        default=0,
        help='How many nops to be appended')
    args = parser.parse_args()

    program = assemble(stdin, nop_count=args.nop_count)
    print '\n'.join(map(lambda line: line.strip(), program))
