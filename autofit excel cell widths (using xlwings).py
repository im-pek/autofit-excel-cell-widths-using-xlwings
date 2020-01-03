import xlwings as xw

#xw.Book(r'C:/path/to/file.xlsx') #open

app = xw.App()

wb = xw.Book(r"L:\My Documents\Desktop\input.xlsx")

ws1 = wb.sheets["Worksheet 1 Name"]

ws2 = wb.sheets["Worksheet 2 Name"]

ws1.autofit()

ws2.autofit()

wb.save()

#wb.save(r'C:\path\to\new_file_name.xlsx') #save

#xw.Book.close(self)

app.quit()