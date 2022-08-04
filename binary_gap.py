# LONGEST BINARY GAP 

# you can write to stdout for debugging purposes, e.g.
#  ("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    bit_string = _bitStringFromInt(N)
    if bit_string:
        boundaries = _firstAndLastOneBit(bit_string)
        if boundaries[0] == -1 or boundaries[0] == boundaries[1]:
            return 0
        return _binaryGapFromSliceOfBits(bit_string[boundaries[0]: boundaries[1] + 1])
    return 0

def _bitStringFromInt(N: int) -> str:
    if N:
        return format(N, 'b')
    return None

def _firstAndLastOneBit(bits: str) -> list:
    if bits:        
        first = bits.find('1')
        last = bits.rfind('1')
        return first, last
    else:
        return -1, -1
    
def _binaryGapFromSliceOfBits(bits: str) -> int:
    max_gap = 0    
    if bits:
        curr_gap = 0
        for bit in bits:
            if bit == '1':
                if curr_gap > max_gap:
                    max_gap = curr_gap
                curr_gap = 0
            else:
                curr_gap += 1
    return max_gap
