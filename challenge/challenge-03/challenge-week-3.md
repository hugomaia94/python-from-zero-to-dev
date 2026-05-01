### Challenge: CRUD System in Terminal

You must develop a program in a programming language of your choice that simulates a simple CRUD (Create, Read, Update, Delete) system using the terminal.

The system should allow the user to manage a collection of users stored in memory using lists and/or dictionaries.

#### 📋 Requirements:

1. When the program starts, it should display a menu with at least 5 options, for example:
   - 1: Add new user
   - 2: List all users
   - 3: Update a user
   - 4: Delete a user
   - 5: Exit

2. The program must keep running using a loop (e.g., `while`), showing the menu repeatedly until the user chooses to exit.

3. The system must implement all CRUD operations:
   - **Create (Add new user):**
     The program must ask the user to input:
     - Name (string)
     - Age (integer)
     - Email (string)

     The data must be stored in a structured format (e.g., dictionary inside a list).

   - **Read (List users):**
     Display all registered users in a clear and organized format.

   - **Update (Edit user):**
     Allow the user to select a user (by index or ID) and update their information (name, age, or email).

   - **Delete (Remove user):**
     Allow the user to select a user (by index or ID) and remove them from the system.

4. Use functions to organize your code:
   - Each operation (create, read, update, delete) should be handled by a separate function.

5. Use appropriate data structures:
   - Use lists and dictionaries to store user data.

6. The program must handle invalid input:
   - If the user selects an invalid option, display an error message and show the menu again.
   - Validate inputs when updating or deleting users (e.g., invalid index or ID).
   - Ensure age is a valid number.

7. (Optional - Bonus):
   - Add unique IDs for each user
   - Prevent duplicate emails
   - Validate email format
   - Improve output formatting
