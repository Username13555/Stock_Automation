import yfinance as yf # Module to get stock data
import pandas as pd # Module to manipulate data
import openpyxl # Module to write data to Excel
import datetime # Module to get the current date
import os # Module to check if a file exists
import matplotlib.pyplot as plt

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
    
def plot_data(data):
    data.to_csv('data.csv')
    csv = pd.read_csv('data.csv', index_col=0)

    d = pd.DataFrame(data.loc[:, ["Close"]])

    plot = d.plot(title="DataFrame Plot")
    plt.show()

stock_name = "AAPL" # Stock name, users should find the name used in the market

stock_data_from_market = StockData(stock_name).get_data()
stock_data_store = pd.DataFrame(columns = ["Name", "Bought Price", "Current Price", "Profit/Loss", "Percentage"])

#target_price = 0
#stock_amount = 0
#current_price = stock_data_from_market["Close"][-1]
#bought_price = current_price
#changing_amount = 0
#total_amount = 0
#change in profit = 0


for i in range(0,len(stock_data_store)):
    if stock_data_store["Bought Price"][i] / stock_data_from_market["Close"][-1] * 100 > 100:
        stock_data_store["Profit/Loss"][i] = "Profit"
        stock_data_store["Percentage"][i] = (stock_data_store["Bought Price"][i] / stock_data_from_market["Close"][-1] * 100) - 100
    else:
        stock_data_store["Profit/Loss"][i] = "Loss"
        stock_data_store["Percentage"][i] = 100 - (stock_data_store["Bought Price"][i] / stock_data_from_market["Close"][-1] * 100)

print(stock_data_from_market)
print(stock_data_store)

plot_data(stock_data_from_market)
