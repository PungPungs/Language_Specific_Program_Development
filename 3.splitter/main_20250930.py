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
        self.interval = segy.stats.binary_file_header["sample_interval_in_microseconds"] / 1000
        if (self.interval == 0):
            return
        for trace in segy.traces:
            temp.append([trace.meta.segy.trace_header.get('unpacked_header')[72:76], trace.meta.segy.trace_header.get('unpacked_header')[76:80]])
        gps = (np.frombuffer(np.array(temp),dtype=">i4")).reshape([-1,2])

        start_idx, end_idx = int(float(self.le_time_min.text())/self.interval), int(float(self.le_time_max.text())/self.interval)
        new = np.hstack((gps,trace_data),dtype=float)[:][start_idx:end_idx]


        pre_x = new[(new[:,0] > int(self.le_x_min.text())) & (new[:,0] < int(self.le_x_max.text()))]
        pre_all = pre_x[(pre_x[:,1] > int(self.le_y_min.text())) & (pre_x[:,1] < int(self.le_y_max.text()))]



        with open("test.txt", "w") as f:
            all_str = np.array(new.tolist(), dtype=str)
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