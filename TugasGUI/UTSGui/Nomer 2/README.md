# Hasil Running

| Screenshot |
| ---------- |
| ![click](https://user-images.githubusercontent.com/58881125/120745465-68592080-c527-11eb-8336-fdf4f277d3a2.PNG) |

## Penjelasan
```python
app = QApplication([])
button = QPushButton('Click')
```
Membuat variabel app dan button

```python
def on_button_clicked():
    alert = QMessageBox()
    alert.setText('You clicked the button!')
    alert.exec_()
```
Membuat message box menggunakan fugnsi QMessageBox lalu isi text menggunakan setText setelah itu eksekusi

```python
button.clicked.connect(on_button_clicked)
button.show()
app.exec_();
```
Memberi fungsi button.clicked agar tombol dapat di klik menggunakan konesi connect(on_button_clicked), lalu eksekusi program menggunakan app.exec_()

