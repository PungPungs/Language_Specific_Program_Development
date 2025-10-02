import mmap
import numpy as np
from dtype import LITTLE_BINARY_HEADER_REV2, BIG_BINARY_HEADER_REV2, DATA_SAMPE_FORMAT

class SGY:
    def __init__(self):
        self.textual_header = None
        self.binary_header = None
        self.traces = None
        self.endian = None

    def read(self, file_path):
        with open(file_path, "rb") as sgy:
            mm = mmap.mmap(sgy.fileno(), 0 , access=mmap.ACCESS_READ)
        try:
            self.textual_header = mm[:3200].decode("ascii")
        except UnicodeDecodeError:
            self.textual_header = mm[:3200].decode("EBCDIC")

        if int.from_bytes(mm[3224:3226], byteorder="big") < 8:
            binary_header = np.frombuffer(mm[3200:3600],dtype=BIG_BINARY_HEADER_REV2)
            self.endian = ">"
        else:
            binary_header = np.frombuffer(mm[3200:3600],dtype=LITTLE_BINARY_HEADER_REV2)
            self.endian = "<"


        self.interval = binary_header["sample_interval"]
        self.num_of_trace = binary_header["samples_per_trace"].item()
        self.data_format = DATA_SAMPE_FORMAT.get(binary_header["data_sample_format"].item())


        TRACE = np.dtype([
            ("header", ("u1", 240)), # 따로 정의
            ("data",(self.endian + self.data_format, self.num_of_trace))
        ])

        self.traces = np.frombuffer(mm, dtype=TRACE, offset=3600)
    
    def info(self):
        print("Textual Header : ",self.interval)
        print("interval : ",self.interval)
        print("num of traces : ", self.num_of_trace)
        print("edian : ", self.endian)
        

    def get_trace_header(self):
        return self.traces["header"]
    
    def get_trace_data(self):
        return self.traces["data"]
    
    def get_gps(self):
        self.traces["header"]["gps"]



if __name__ == "__main__":
    a = SGY()
    a.read(file_path="0922_mado7-1_all.sgy")
    a.info()