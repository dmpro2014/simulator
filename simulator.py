from sys import stdin
from scanner import scan
from utils import get_instruction_format
from memory import memory_read, memory_write, memory_dump
from Tkinter import Tk, Canvas, PhotoImage, mainloop

WIDTH, HEIGHT = 512, 256

constant_memory = [0]*256

instructions = scan(stdin)
print instructions
num_threads = WIDTH * HEIGHT


def execute_r_instruction(instruction, registers):
    opcode = instruction[0]

    if opcode in ['add', 'sub', 'and', 'or', 'xor', 'mul', 'slt']:
        rd, rs, rt = map(eval, list(instruction)[1:4])

        if opcode == 'add':
            registers[rd] = registers[rs] + registers[rt]
        if opcode == 'sub':
            registers[rd] = registers[rs] - registers[rt]
        if opcode == 'and':
            registers[rd] = registers[rs] & registers[rt]
        if opcode == 'or':
            registers[rd] = registers[rs] | registers[rt]
        if opcode == 'xor':
            registers[rd] = registers[rs] ^ registers[rt]
        if opcode == 'mul':
            registers[rd] = registers[rs] * registers[rt]
        if opcode == 'slt':
            # print 'slt', registers[rs], registers[rt]
            registers[rd] = registers[rs] < registers[rt]

    if opcode in ['sll', 'srl', 'sra']:
        rd, rt, sh = map(eval, list(instruction)[1:4])

        if opcode == 'sll':
            registers[rd] = registers[rt] << sh
        if opcode == 'srl':
            registers[rd] = (registers[rt] % 0x100000000) >> sh
        if opcode == 'sra':
            registers[rd] = registers[rt] >> sh


def execute_i_instruction(instruction, registers):
    opcode = instruction[0]

    if opcode == 'sw':
        memory_write(registers[3], registers[4], registers[5])
    if opcode == 'lw':
        registers[5] = memory_read(registers[3], registers[4])
    if opcode == 'ldc':
        rd, immediate = map(eval, list(instruction)[1:3])
        registers[rd] = constant_memory[immediate]
    if opcode == 'addi':
        rd, rs, immediate = map(eval, list(instruction)[1:4])
        registers[rd] = registers[rs] + immediate


for thread_id in range(num_threads):
    registers = [0] * 16
    registers[1] = thread_id >> 16
    registers[2] = thread_id % 2**16
    for instruction in instructions:
        if instruction[-2] and registers[6]:  # Mask
            # print instruction[-1]
            continue
        instruction_format = get_instruction_format(instruction[0])

        if instruction_format == 'i':
            execute_i_instruction(instruction, registers)
        if instruction_format == 'r':
            execute_r_instruction(instruction, registers)


def convert_color(color):
    red = (0b1111100000000000 & color) >> 11
    green = (0b0000011111100000 & color) >> 5
    blue = (0b0000000000011111 & color)

    red = red << 3
    green = green << 2
    blue = blue << 3
    return "#%02x%02x%02x" % (red, green, blue)


def display():
    window = Tk()
    canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="#000000")
    canvas.pack()
    img = PhotoImage(width=WIDTH, height=HEIGHT)
    canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")

    data = ""
    for i in range(256):
        data += '{' + ' '.join(map(
            convert_color,
            memory_dump(i*WIDTH, i*WIDTH + WIDTH)
        )) + '} '
    img.put(data[:-1])

    mainloop()

display()

#print memory_dump(0, 100)
