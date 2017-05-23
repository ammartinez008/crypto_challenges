
import sys

def xor_buffers(buffer_one, buffer_two):
    if len(buffer_one) != len(buffer_two):
        return None
    buffer_one_hex = buffer_one.decode("hex")
    buffer_two_hex = buffer_two.decode("hex")

    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(buffer_one_hex, buffer_two_hex)).encode("hex")

if len(sys.argv) < 2:
    sys.exit()

buffer_one = sys.argv[1]
buffer_two = sys.argv[2]

print xor_buffers(buffer_one, buffer_two)





