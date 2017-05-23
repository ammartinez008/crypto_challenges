
import sys

# Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.

def hex_to_base(hex_str):
    if not hex_str:
        return None
    else:
        return hex_str.decode("hex").encode("base64")

print hex_to_base(sys.argv[1])
