import sys
from PyQt5 import uic
from PyQt5.QtCore import QThread, pyqtSignal, QDate
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, \
    QPushButton, QCalendarWidget
from scrapper import get_max_price   # scrapper.py dosyasından get_data fonksiyonunu içe aktarıyoruz


class ScrapperThread(QThread):
    onStart = pyqtSignal(str)  # iş parçacığı başladığında bir sinyal gönderir
    onScrapping = pyqtSignal(object)  # veri çekildiğinde bir sinyal gönderir
    onFinish = pyqtSignal(str)  # iş parçacığı tamamlandığında bir sinyal gönderir

    def __init__(self, year, month, day):
        super().__init__()
        self.year = year
        self.month = month
        self.day = day

    def run(self):
        self.onStart.emit("Yukleniyor ...")     # iş parçacığı başladığında başlangıç mesajı gönderir

        data = get_max_price(self.year, self.month, self.day)  # scrapper modülünden veri çeker
        self.onScrapping.emit(data)  # çekilen veriyi gönderir

        self.onFinish.emit('')  # iş parçacığı tamamlandığında mesaj gönderir


class   98MainWindow(QMainWindow):
    cw_date: QCalendarWidget
    btn_query: QPushButton
    lbl_result: QLabel
    scrapper_thread: ScrapperThread

    def __init__(self, flags=None, *args, **kwargs):
        super().__init__(flags, *args, **kwargs)

        uic.loadUi('form.ui', self)      # Qt Designer ile tasarlanmış arayüzü yükler
        self.initialise()

    def initialise(self):
        self.btn_query.clicked.connect(lambda: self.on_query())     # Sorgula düğmesine tıklandığında on_query metodunu çağırır

    def set_scrapping(self, year, month, day):
        self.scrapper_thread = ScrapperThread(year, month, day)  # Veri çekme iş parçacığını başlatır
        self.scrapper_thread.onStart.connect(lambda msg: self.statusbar.showMessage(msg))  # iş parçacığı başladığında bir mesaj gösterir
        self.scrapper_thread.onFinish.connect(lambda msg: self.statusbar.showMessage(msg))  # iş parçacığı bittiğinde bir mesaj gösterir
        self.scrapper_thread.onScrapping.connect(lambda credit: self.on_scrapped(credit))  # iş parçacığından gelen veriyi işler
        self.scrapper_thread.start()  # iş parçacığını başlatır
        # max_price = get_max_price(year, month, day)
        # if max_price != "Data not found":
        #     self.lbl_result.setText(str(max_price) + " TL")
        # else:
        #     self.lbl_result.setText("Data not found")

    def on_scrapped(self, price: float):
        if price != "Veri Bulunamadı":
            self.lbl_result.setText(str(price) + " TL")  # veri varsa ekrana yazdırır
        else:
            self.lbl_result.setText("Veri Yok!")  # veri yoksa ekrana "Veri Yok!" yazdırır

    # def on_scrapped(self, data: list):
    #     if len(data) > 1:
    #         self.lbl_result.setText(str(data[1]) + " TL")  # veri varsa ekrana yazdırır
    #     else:
    #         self.lbl_result.setText("Veri Yok!")  # veri yoksa ekrana "Veri Yok!" yazdırır

    def on_query(self):
        selected_date: QDate = self.cw_date.selectedDate()  # Seçilen tarihi alır
        self.set_scrapping (
            year=selected_date.year(),
            month=selected_date.month(),
            day=selected_date.day()
        )  # Veri çekme iş parçacığını başlatır


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()  # Uygulamayı görünür hale getirir
    sys.exit(app.exec_())  # Uygulamadan çıkış yapana kadar uygulamayı çalıştır
