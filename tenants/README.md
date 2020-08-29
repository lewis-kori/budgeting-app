# core app functionality

base urls: <http://domain.com/api/>

## create and list tenants

    v1/tenants/

keys expected

* name
* business_phone_number
* business_email as an integer, 1-12 representing the months.

## retrieve and update a tenant

     v1/tenants/{tenant_id}/

## create and list departments

    v1/departments/

keys expected is `name`

## retrieve and update a department

     v1/departments/{department_id}/
