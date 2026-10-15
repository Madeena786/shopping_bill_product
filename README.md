## **Shopping Bill Generator**



###### **Project Description**



The Shopping Bill Generator is a Python program that creates a formatted shopping bill.



The program accepts the product name, quantity, and price from the user. It calculates the subtotal, discount, tax, and final amount, and displays all the purchased products in an itemized bill.



###### **Objective**



The main objective of this project is to practice Python programming concepts in a real-world shopping scenario.



**This project demonstrates:**



\- Lists

\- Dictionaries

\- For loops

\- Functions

\- Conditional statements

\- User input

\- Arithmetic calculations

\- Formatted output



###### **Technologies Used**



\- Python

\- IDLE / Python Editor



###### **Features**



\- Accepts multiple products from the user

\- Accepts product name, quantity, and price

\- Calculates the amount for each product

\- Calculates subtotal

\- Calculates discount

\- Calculates 18% tax

\- Calculates final bill amount

\- Displays an itemized shopping bill

\- Displays formatted output



###### **Discount Rules**



The program applies discount based on the subtotal.



\- Subtotal >= ₹5000 → 10% discount

\- Subtotal >= ₹2000 → 5% discount

\- Subtotal < ₹2000 → No discount


**Tax Calculation**
---



The program applies 18% tax after deducting the discount.



Tax = Amount After Discount × 18 / 100



###### **How the Program Works**



**Step 1:** Enter Number of Products



The user enters the number of products to purchase.



**Step 2:** Enter Product Details



For each product, the user enters:



\- Product name

\- Quantity

\- Price



**Step 3:** Store Product Details



Each product is stored as a dictionary containing:



\- name

\- quantity

\- price



All product dictionaries are stored inside a list.



**Step 4:** Calculate Subtotal



The program calculates the amount of every product using:



Quantity × Price



The amounts are added together to calculate the subtotal.



**Step 5:** Calculate Discount



The program checks the subtotal and applies the appropriate discount.



**Step 6:** Calculate Tax



The program calculates 18% tax on the amount after discount.



**Step 7:** Calculate Final Amount



The final amount is calculated using:



Final Amount = Amount After Discount + Tax



###### **Sample Input**



Enter number of products: 3



Product 1

Product name: rice

Quantity: 2

Price: 500



Product 2

Product name: oil

Quantity: 1

Price: 800



Product 3

Product name: milk

Quantity: 1

Price: 200



###### **Sample Output**



==================================================

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*SHOPPING BILL\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

==================================================

Product         Quantity        Price   Amount

\--------------------------------------------------

rice             2              500.0    1000.0

oil              1              800.0     800.0

milk             1              200.0     200.0

\--------------------------------------------------

Subtotal:     $ 2000.0

Discount:     $ 100.0

Tax (18%):    $ 342.0

Final Amount: $ 2242.0

==================================================

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*Thank You! Visit Again\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

==================================================



###### **Functions Used**



**calculate\_subtotal()**



This function calculates the total price of all products.



**calculate\_discount()**



This function calculates the discount based on the subtotal.



**calculate\_tax()**



This function calculates 18% tax.



###### **Conclusion**



The Shopping Bill Generator is a simple Python project that demonstrates how programming concepts can be used to solve a real-world billing problem.



The project helped in understanding lists, dictionaries, loops, functions, conditional statements, and mathematical calculations in Python.

