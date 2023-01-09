# finalCapstone


A brief portfolio of projects undertaken during my HyperionDev Software Engineering Bootcamp

## Description

A simple Python program which reads text from the text file inventory.txt and performs a variety of functions to prepare the data for presentation. 

## Getting Started

### Installing

* Install and update Python, open inventory.py and run. 
* The program requires a inventory text file to run. 

### Executing program
The program will present a menu when run: 
![Screenshot 2023-01-09 at 10 44 45](https://user-images.githubusercontent.com/53863441/211290736-9a2c96a3-3893-4c26-b5ed-ff6b02dc50d7.png)

Using the following functions to manipulate the data: 

- get_cost: returns the cost of the items (in this case, shoes)
- get_quantity: returns the quantity of the items 
- read_shoes_data: opens and reads data from a file (inventory.txt) and creates and appends a shoe object to the shoe list. 
- capture_shoes: allows user to capture data about a shoe and create shoe object with said data and append shoe to list. 
- view_all: iterates over the shoes list and prints details of shoes in a table format. 
- re_stock: finds the shoe object with lowest quantity, giving user the options to re-stock this item, updating the file with new stock. 
- search_shoe: searches shoe list using shoe code and returns object to be printed. 
- value_per_item: calculates the total value for each item (value = cost * quantity)
- highest_qty: determines the product with the highest quantity 
```
As seen below: 

![Screenshot 2023-01-09 at 10 42 04](https://user-images.githubusercontent.com/53863441/211290641-a26d0651-40a2-4bf4-9fa9-da5877409cf9.png)
![Screenshot 2023-01-09 at 10 41 08](https://user-images.githubusercontent.com/53863441/211290643-d6f64a50-28b7-48f6-81ba-f27eca44ec98.png)
![Screenshot 2023-01-09 at 10 37 44](https://user-images.githubusercontent.com/53863441/211290644-d597f817-0ca0-4341-9588-4c4efc32c9f5.png)
![Screenshot 2023-01-09 at 10 37 20](https://user-images.githubusercontent.com/53863441/211290645-03035b14-7b68-4763-8c62-144336dc9e00.png)
![Screenshot 2023-01-09 at 10 36 31](https://user-images.githubusercontent.com/53863441/211290649-543e5c77-8694-4fe9-b15d-0ac688c8ed13.png)
![Screenshot 2023-01-09 at 10 33 40](https://user-images.githubusercontent.com/53863441/211290650-9524ae7e-f7e7-4db3-b3fe-a0b119912baf.png)



