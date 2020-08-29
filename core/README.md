# core app functionality

base urls: <http://domain.com/api/>

## create a new account

    v1/accounts/

pass `name` and `amount` as keys

## create and list budgets

    v1/budgets/

keys expected

* department as a foreign key
* source as a foreign key to [accounts](#create-a-new-account)
* month as an integer, 1-12 representing the months.
* year as an integer
* amount as an integer

## list departmental budgets

    v1/budgets/department/{department_id}/

## create and list expenses

    v1/expenses/

keys expected

* budget as a foreign key to a [budget](#create-and-list-budgets)
* date. This is a date field in the format `YYYY-MM-DD`
* use as text
* amount as an integer

## list departmental expenses

    v1/expenses/department/{department_id}/
