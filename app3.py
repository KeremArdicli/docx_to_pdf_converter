from docx2pdf import convert
import tkinter.filedialog

directory_input = tkinter.filedialog.askdirectory(title='Word dosyalarının bulunduğu klasörü seçiniz!')
directory_output = tkinter.filedialog.askdirectory(title='PDF dosylarını kaydetmek istediğiniz klasörü seçiniz!')

convert(directory_input, directory_output)
