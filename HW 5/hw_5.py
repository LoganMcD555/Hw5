import json

# Define the list of tickers
tickers = ["AAPL", "ADBE", "COIN", "DJT", "GOOG", "JPM", "META", "NVDA", "PEP", "TGT"]

# Initialize a dictionary to store results
results = {}

# Function to save results to a JSON file
def saveResults(results):
    with open("results.json", "w") as outfile:
        json.dump(results, outfile, indent=4)

# Define meanReversionStrategy function
def meanReversionStrategy(prices):
    buy = 0
    total_profit = 0
    first_buy = None
    i = 0  # Index for iterating through prices

    for price in prices:
        # Calculate the moving average only if we have at least 5 previous prices
        if i > 4:
            avg_price = sum(prices[i-5:i]) / 5  # 5-day moving average

            # Buy condition: price < avg_price * 0.98
            if price < avg_price * 0.98 and buy == 0:
                buy = price
                if first_buy is None:  # Track the first buy price
                    first_buy = buy
                print("buying at:", price)

            # Sell condition: price > avg_price * 1.02
            elif price > avg_price * 1.02 and buy != 0:
                profit = price - buy
                total_profit += profit
                print("selling at:", price)
                print("trade profit:", round(profit, 2))
                buy = 0  # Reset buy to 0 (not holding stock)

        i += 1  # Increment index

    # Calculate return percentage based on the first buy price
    if first_buy is not None:
        final_return_percentage = (total_profit / first_buy) * 100
    else:
        final_return_percentage = 0

    print("-----------------------")
    print("Total profit:", round(total_profit, 2))
    print("First buy:", first_buy)
    print("Percent return:", round(final_return_percentage, 2))

    return total_profit, final_return_percentage

# Define simpleMovingAverageStrategy function
def simpleMovingAverageStrategy(prices):
    buy = 0
    total_profit = 0
    first_buy = None
    i = 0  # Index for iterating through prices

    for price in prices:
        # Calculate the moving average only if we have at least 5 previous prices
        if i > 4:
            avg_price = sum(prices[i-5:i]) / 5  # 5-day moving average

            # Buy condition: price > avg_price
            if price > avg_price and buy == 0:
                buy = price
                if first_buy is None:  # Track the first buy price
                    first_buy = buy
                print("buying at:", price)

            # Sell condition: price < avg_price
            elif price < avg_price and buy != 0:
                profit = price - buy
                total_profit += profit
                print("selling at:", price)
                print("trade profit:", round(profit, 2))
                buy = 0  # Reset buy to 0 (not holding stock)

        i += 1  # Increment index

    # Calculate return percentage based on the first buy price
    if first_buy is not None:
        final_return_percentage = (total_profit / first_buy) * 100
    else:
        final_return_percentage = 0

    print("-----------------------")
    print("Total profit:", round(total_profit, 2))
    print("First buy:", first_buy)
    print("Percent return:", round(final_return_percentage, 2))

    return total_profit, final_return_percentage

# Loop through each ticker to load prices
for ticker in tickers:
    # Construct the file path for each ticker
    file_path = "HW 5/" + ticker + ".txt"
    
    # Open the file and read the prices
    with open(file_path, 'r') as file:
        lines = file.readlines()
        prices = [round(float(line.strip()), 2) for line in lines]
    
    # Store prices in the results dictionary
    results[ticker + "_prices"] = prices
    
    # Run mean reversion strategy and store results
    mr_profit, mr_return = meanReversionStrategy(prices)
    results[ticker + "_mr_profit"] = mr_profit
    results[ticker + "_mr_returns"] = mr_return
    
    # Run simple moving average strategy and store results
    sma_profit, sma_return = simpleMovingAverageStrategy(prices)
    results[ticker + "_sma_profit"] = sma_profit
    results[ticker + "_sma_returns"] = sma_return

# Save all results to a JSON file
saveResults(results)

print("Results saved to results.json")
