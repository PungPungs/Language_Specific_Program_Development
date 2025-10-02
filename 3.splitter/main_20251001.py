from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog
import numpy as np
import sys
from ui import Ui_MainWindow
from obspy import read
import os


class Splitter(Ui_MainWindow, QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb_convert.clicked.connect(self.convert)
        self.show()

    def convert(self):



        file_path, _ = QFileDialog.getOpenFileNames(None, "파일 선택", "","segy (*.sgy)")
        temp = []
        segy = read(file_path[0])


        trace_data = np.array(segy.traces)
        num_of_trace = trace_data.shape[1]
        self.interval = segy.stats.binary_file_header["sample_interval_in_microseconds"] / 1000

        if self.le_time_min.text() == "" and self.le_time_max.text() == "":
            return
        start_idx, end_idx = int(float(self.le_time_min.text())/self.interval), int(float(self.le_time_max.text())/self.interval)


        for trace in segy.traces:
            temp.append([trace.meta.segy.trace_header.get('unpacked_header')[72:76], trace.meta.segy.trace_header.get('unpacked_header')[76:80]])

        _gps = (np.frombuffer(np.array(temp),dtype=">i4")).reshape([-1,2])
        temp.clear()

        broad_cast_time = np.arange(0, num_of_trace, 1).reshape(-1,1) * self.interval
        for i in range(len(_gps)):
            broad_cast_gps = np.ones((num_of_trace, 2)) * _gps[i]
            t = np.hstack((broad_cast_gps, broad_cast_time, trace_data[i].T.reshape(-1, 1)))

            temp.append(t)
        post_data = np.vstack((temp))








        with open("test.txt", "w") as f:
            all_str = np.array(post_data.tolist(), dtype=str)
            for all in all_str:
                f.write(",".join(all)+"\n")

        # print(len(trace_header.get('unpacked_header')))
        # print(trace_header)
        # print(np.frombuffer(trace_header.get('unpacked_header')[72:72+4],'>i4'))
        # print(np.frombuffer(trace_header.get('unpacked_header')[76:76+4],'>i4'))
        # # x,y,[traces],Option(amp)
        # # x,y,[traces],Option(amp)
        # # x,y,[traces],Option(amp)
        # # x,y,[traces],Option(amp)
        # # x,y,[traces],Option(amp)


if __name__ == "__main__":
    main = QApplication(sys.argv)
    splitter = Splitter()
    splitter.show()
    sys.exit(main.exec())