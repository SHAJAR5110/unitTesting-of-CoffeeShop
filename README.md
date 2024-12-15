
# Coffee Shop System with Unit Testing

## **Overview**
This project is a simple Coffee Shop system built in Python. It includes functionality for managing a menu, calculating order totals, and updating menu prices. The system is accompanied by comprehensive unit tests to ensure that the core functionality works as expected.

---

## **Features**
1. **Calculate Order Total**: Computes the total cost for an order based on the number of coffees and sandwiches.
2. **Menu Price Management**: Allows updating of coffee and sandwich prices dynamically.
3. **Error Handling**: Prevents negative item counts by raising exceptions.
4. **Unit Testing**: Implements tests using Python's `unittest` module to validate core functionality.

---

## **File Structure**
- **`lab9.py`**  
   Contains the main implementation of the Coffee Shop system.
   - Class: `CoffeeShop`
   - Functions:
     - `calculate_total`: Calculates the total cost of an order.
     - `update_menu_prices`: Updates prices for coffee and sandwiches.

- **`test.py`**  
   Contains the unit tests for the Coffee Shop system, ensuring the code works as intended.

---

## **Setup and Usage**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/SHAJAR5110/coffee-shop-system.git
   ```

2. **Run the Tests**:
   Make sure you have Python installed. Run the tests using:
   ```bash
   python -m unittest test.py
   ```

3. **Expected Output**:
   If all tests pass, you will see:
   ```
   ....
   ----------------------------------------------------------------------
   Ran 4 tests in 0.002s

   OK
   ```

---

## **How It Works**
1. **Order Calculation**:
   - The `calculate_total` method computes the total cost based on the number of coffees and sandwiches.
   - Example:
     ```python
     shop = CoffeeShop()
     total = shop.calculate_total(2, 3)  # Total cost for 2 coffees and 3 sandwiches
     print(total)  # Output: 40
     ```

2. **Updating Menu Prices**:
   - The `update_menu_prices` method allows updating the prices of coffee and sandwiches.
   - Example:
     ```python
     shop = CoffeeShop()
     shop.update_menu_prices(coffee_price=6, sandwich_price=12)
     ```

3. **Testing**:
   - Tests cover scenarios for valid and invalid inputs, price updates, and more.

---

## **Technologies Used**
- **Programming Language**: Python
- **Testing Framework**: `unittest`

---

