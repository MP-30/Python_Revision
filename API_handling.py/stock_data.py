import requests

def fetch_data():
    url = "https://api.freeapi.app/api/v1/public/stocks/INFY"
    responce = requests.get(url)
    data = responce.json()
    
    if data["success"]and "data" in data :
        stock_data = data["data"]
        stock_name = stock_data["Name"]
        sym = stock_data["Symbol"]
        listingDate = stock_data["ListingDate"]
        mar_cap = stock_data["MarketCap"]
        current_price = stock_data["CurrentPrice"]
        high_low = stock_data["HighLow"]
        roe = stock_data["ROE"]
        face_value = stock_data["FaceValue"]
        
        return (stock_name, sym,listingDate,mar_cap,current_price,high_low, roe, face_value)
    else: raise Exception("Failed to fetch stock data")        

def main():
    stock_name, sym,listingDate,mar_cap,current_price,high_low, roe, face_value = fetch_data()
    print('Stock_name is {}\nSymbol is {} \nListing Data: {} \nMarketCap is {} \nCurrent_price: {}\nHigh/log is: {}\nROE : {}\nFace_value is: {}'.format(stock_name, sym,listingDate,mar_cap,current_price,high_low, roe, face_value))
    
if __name__ == "__main__":
    main()