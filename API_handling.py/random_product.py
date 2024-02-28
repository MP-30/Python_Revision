import requests

def fetch_data():
    url = "https://api.freeapi.app/api/v1/public/randomproducts/30"
    responce = requests.get(url)
    data = responce.json()
    
    if data["success"]and "data" in data :
        user_data = data["data"]
        description = user_data["description"]
        price = user_data["price"]
        return description, price
    else:
        raise Exception("Failed to fetch user data")
def main():
    try:
        description, price = fetch_data()
        print('Description is {a} \nPrice is {b}'.format(a = description, b = price))
    except Exception as e:
        print(str(e))

if __name__ == "__main__":  
    main()