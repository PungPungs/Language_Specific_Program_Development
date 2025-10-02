from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog,QMessageBox
import numpy as np
import sys
from ui import Ui_MainWindow
from obspy import read


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


        self.interval = segy.stats.binary_file_header["sample_interval_in_microseconds"] / 100
        if self.interval == 0:
            QMessageBox.information(self,"경고","interval의 값이 0 입니다.")
            return


        if self.le_time_min.text() == "" and self.le_time_max.text() == "":
            QMessageBox.information(self,"경고","Time을 작성해주세요")
            return
        


        trace_data = np.array(segy.traces)
        num_of_trace = trace_data.shape[1]

        start_idx, end_idx = int(float(self.le_time_min.text())/self.interval) * 10, int(float(self.le_time_max.text())/self.interval) *10


        for trace in segy.traces:
            temp.append([trace.meta.segy.trace_header.get('unpacked_header')[72:76], trace.meta.segy.trace_header.get('unpacked_header')[76:80]])

        if self.rb_psbp.isChecked():
            _gps = (np.frombuffer(np.array(temp),dtype="<i4")).reshape([-1,2]) / 100
        elif self.rb_4ch.isChecked():
            _gps = (np.frombuffer(np.array(temp),dtype="<i4")).reshape([-1,2]) / 10
        else:
            QMessageBox.information(self,"경고","파일 타입을 선택해주세요")
        temp.clear()
        broad_cast_time = np.arange(0, num_of_trace, 1).reshape(-1,1) * self.interval
        broad_cast_time = np.round(broad_cast_time, 3)

        for i in range(len(_gps)):
            broad_cast_gps = np.ones((num_of_trace, 2)) * _gps[i]
            t = np.hstack((broad_cast_gps, broad_cast_time, trace_data[i].T.reshape(-1, 1)))
            temp.append(t)
        _temp = np.array(temp)
        post_time_slice = _temp[:, start_idx:end_idx]
        min_x, max_x, min_y, max_y = int(self.le_x_min.text()), int(self.le_x_max.text()), int(self.le_y_min.text()), int(self.le_y_max.text())
        col_x = (post_time_slice[:,:,0] >= min_x) & (post_time_slice[:,:,0] <= max_x)
        col_y = (post_time_slice[:,:,1] >= min_y) & (post_time_slice[:,:,1] <= max_y)
        mask = np.all(col_x & col_y, axis=1)
        filtered = post_time_slice[mask]

        try:
            post_data = np.vstack((filtered))
            with open(file_path[0].replace(".sgy",".txt"), "w") as f:
                all_str = np.array(post_data.tolist(), dtype=str)
                for all in all_str:
                    f.write(",".join(all)+"\n")
        except:
            trace_x_min, trace_x_max = np.min(post_time_slice[:,:,0]), np.max(post_time_slice[:,:,0])
            trace_y_min, trace_y_max = np.min(post_time_slice[:,:,1]), np.max(post_time_slice[:,:,1])
            QMessageBox.information(self,"경고", f"변환 실패 : x = ({trace_x_min} ~ {trace_x_max}) \n y = ({trace_y_min} ~ {trace_y_max})")
            return
       

if __name__ == "__main__":
    main = QApplication(sys.argv)
    splitter = Splitter()
    splitter.show()
    sys.exit(main.exec())


'''
1. min max 불러오기
2. x,y 스케일 자동 감지 (6, 7)

'''