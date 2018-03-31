import base64

def hex_to_b64(hex_string):
    byte_string = bytes.fromhex(hex_string)
    b64_string = base64.b64encode(byte_string)
    return b64_string
