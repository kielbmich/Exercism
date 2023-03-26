handshake = ["wink", "double blink", "close your eyes", "jump"]

def commands(binary):
    binary_notation = int(binary, 2)
    out = []
    for index in range(len(handshake)):
        if binary_notation & 1 << index:
            out.append(handshake[index])
    return out if binary[0] == "0" else out[::-1]