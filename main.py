import yfinance as yf # Module to get stock data
import pandas as pd # Module to manipulate data
import openpyxl # Module to write data to Excel
import datetime # Module to get the current date
import os # Module to check if a file exists

class StockData:
    def __init__(self, stock):
        self.stock = stock
        self.data = None
        self.filename = None
    
    def get_data(self):
        self.data = yf.download(self.stock)
        return self.data

    def write_to_excel(self):
        self.filename = f"{self.stock}_{datetime.datetime.now().strftime('%Y-%m-%d')}.xlsx"
        self.data.to_excel(self.filename)
    
    def check_file(self):
        return os.path.exists(self.filename)
    
    def read_excel(self):
        return pd.read_excel(self.filename)
    
    def get_data_from_excel(self):
        if self.check_file():
            return self.read_excel()
        else:
            self.get_data()
            self.write_to_excel()
            return self.read_excel()

print(StockData("AAPL").get_data())
