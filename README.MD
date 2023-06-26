# README

## SuperPY

super py is a program to help keep track of profit revenue and inventory

## Buy a product

you can buy a product by using the following command:

```
python superpy.py buy -product_name <your product name> -price <your price> -expiration_date  <your expiration dat in  YYYY-MM-DD format>
```

## Sell a product:

you can sell a product by using the following commands:

```
python superpy.py sell -product_name <your product name> -price <your price>
```

## Show inventory

you can see the inventory of a product by using the following command:

```
 python superpy.py report inventory -today
```

```
python superpy.py report inventory -yesterday
```

```
python superpy.py report inventory -date <enter YYYY-MM-DD for specific date>
```

## report

you can see a report with the following command

```
python superpy.py report revenue (options are -today -yesterday - date<enter YYYY-MM for the month YYYY-MM-DD for specific date>)
```

```
python superpy.py report profit (options are -today -yesterday - date<enter YYYY-MM for the month YYYY-MM-DD for specific date>)
```

```
python superpy.py report table (options are -today -yesterday - date<enter YYYY-MM for the month YYYY-MM-DD for specific date>)
```

## advance time

to advance time use this command

```
python main.py --advance_time <enter number of days you want to advance>

```

## Settings

you can change the text color and alignment you can change today and remove data and simulate the program over a number of days you find it in the data section

to enter the settings
use the following command

```
python superpy.py settings
```
