import torch
import numpy as np

def bfloat16arr_to_uint8_arr(nparr, endian='little'):
    # Directly convert bfloat16 to uint8 since numpy does not support bfloat16
    if nparr.dtype != torch.bfloat16:
        raise ValueError('bfloat16_to_uint8: nparr must be of type bfloat16')
    if nparr.ndim != 1:
        nparr = nparr.reshape(-1)
    uint8_list = []
    # Since bfloat16 does not offer bitwise operation, we need to convert to int16 first
    nparr = nparr.view(torch.int16)
    for elem in nparr:
        if endian == 'little':
            uint8_list.append(elem & 0xFF)
            uint8_list.append((elem >> 8) & 0xFF)
        elif endian == 'big':
            uint8_list.append((elem >> 8) & 0xFF)
            uint8_list.append(elem & 0xFF)
        else:
            raise ValueError('bfloat16arr_to_uint8: endian must be either little or big')
    nparr = np.array(uint8_list, dtype=np.uint8)
    return nparr

def fp16arr_to_uint8_arr(nparr, endian='little'):
    # Directly convert bfloat16 to uint8 since numpy does not support bfloat16
    
    if nparr.ndim != 1:
        nparr = nparr.reshape(-1)
    uint8_list = []
    # pdb.set_trace()
    # Since bfloat16 does not offer bitwise operation, we need to convert to int16 first
    nparr = nparr.view(torch.int16) # int32로
    for elem in nparr:
        if endian == 'little':
            uint8_list.append(elem & 0xFF)
            uint8_list.append((elem >> 8) & 0xFF)

        elif endian == 'big':
            uint8_list.append((elem >> 8) & 0xFF)
            uint8_list.append(elem & 0xFF)
        else:
            raise ValueError('bfloat16arr_to_uint8: endian must be either little or big')
    nparr = np.array(uint8_list, dtype=np.uint8)
    return nparr