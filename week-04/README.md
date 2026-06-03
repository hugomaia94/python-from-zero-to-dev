## OOP: Classes and Methods

**Car Class →** Create a class `Car` with the attributes `brand`, `model`, and `year`. Add a method `display()` that prints the three pieces of information in a sentence.

**Bank Account →** Create a class `BankAccount` with the attributes `owner` and `balance` (starting at 0). Add the method `deposit(amount)` to add money to the balance, `withdraw(amount)` to subtract money only if there is enough balance available, and `check_balance()` to display the current balance. If there is not enough balance, print `"Insufficient balance."`

**Student Average →** Create a class `Student` with the attribute `name` and a list `grades` received in `__init__`. Add the method `calculate_average()` to return the average grade and the method `status()` to return `"Approved"` if the average is greater than or equal to 7, otherwise return `"Failed"`.

**Product Management →** Create a class `Product` with the attributes `name`, `price`, and `stock`. Add the method `apply_discount(percentage)` to apply a discount to the price, `sell(quantity)` to reduce the stock only if enough items are available, `restock(quantity)` to increase the stock, and `is_available()` to return `True` if the product is available or `False` otherwise. If there is not enough stock, print `"Out of stock."`

**Library System →** Create a class `Library` with the attribute `books`, starting as an empty list. Add the method `add_book(title, author)` to store a dictionary containing the title and author, `remove_book(title)` to remove a book by title, `list_books()` to display all registered books, and `search_by_author(author)` to display all books written by a specific author. If the book is not found, print `"Book not found."`

---

## PostgreSQL + Python

**Database Connection →** Create a file `connection.py` that connects to the PostgreSQL database and prints `"Connected successfully!"`. Close the connection at the end.

**Create and Populate Table →** Create a file `create_table.py` that creates a table `products` with the columns `id`, `name`, `price`, and `stock`. Insert 3 products using `INSERT` and save the changes with `commit()`.

**Fetch All Products →** Create a file `get_products.py` with a function `get_all_products()` that connects to the database, fetches all products from the `products` table, and prints each one formatted with id, name, price, and stock.

**Product CRUD →** Create a file `product_crud.py` with three functions: `insert_product(name, price, stock)` to insert a new product, `update_price(product_id, new_price)` to update the price of a product by id, and `delete_product(product_id)` to delete a product by id. Each function must open and close the connection on its own.

**Search by Price →** Create a file `search_by_price.py` with a function `search_by_price(min_price, max_price)` that fetches all products with a price between the two given values using `WHERE price BETWEEN %s AND %s` and prints each result formatted.

### Extra Exercises PostgreSQL

**Create Users Table →** Create a file `create_users_table.py` that creates a table `users` with the columns `id`, `name`, and `email`. Print `"Table created successfully!"` at the end.

**Insert User →** Create a file `insert_user.py` with a function `insert_user(name, email)` that inserts a new user into the `users` table and prints `"User inserted successfully!"`.

**Get All Users →** Create a file `get_all_users.py` with a function `get_all_users()` that fetches all users from the `users` table and prints each one formatted with `id`, `name`, and `email`.

**Delete User →** Create a file `delete_user.py` with a function `delete_user(user_id)` that deletes a user by `id` and prints `"User deleted successfully!"`. If no user is found, print `"User not found."`.

**Update Email →** Create a file `update_email.py` with a function `update_email(user_id, new_email)` that updates the email of a user by `id` and prints `"Email updated successfully!"`.

**Search by Name →** Create a file `search_by_name.py` with a function `search_by_name(name)` that fetches all users whose name contains the searched term using `WHERE name ILIKE %s` and prints each result formatted.

**Count Products →** Create a file `count_products.py` with a function `count_products()` that returns and prints the total number of products in the `products` table using `SELECT COUNT(*) FROM products`.

**Low Stock Products →** Create a file `low_stock.py` with a function `get_low_stock_products(limit)` that fetches all products where `stock` is less than or equal to the given limit using `WHERE stock <= %s`, and prints each one formatted. Test with `limit = 20`.

**Most Expensive Products →** Create a file `most_expensive.py` with a function `get_most_expensive(quantity)` that fetches the most expensive products using `ORDER BY price DESC LIMIT %s` and prints each one formatted. Test with `quantity = 3`.

**Product Report →** Create a file `product_report.py` with a function `generate_report()` that prints a complete report of the `products` table containing:

- Total number of products using `COUNT(*)`
- Most expensive product using `MAX(price)`
- Cheapest product using `MIN(price)`
- Average price using `AVG(price)`
- Total stock using `SUM(stock)`

All in a single query using:

```sql
SELECT COUNT(*), MAX(price), MIN(price), AVG(price), SUM(stock)
FROM products;
```
