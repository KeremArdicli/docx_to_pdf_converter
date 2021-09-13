from docx2pdf import convert
import tkinter.filedialog

directory_input = tkinter.filedialog.askdirectory(title='Select the directory where word files are located')
directory_output = tkinter.filedialog.askdirectory(title='Select the directory where you want to save pdf files')
convert(directory_input, directory_output)
