# E-Commerce API with CI/CD

## About:
This is an E-Commerce API with endpoints for CRUD operations for Customers and their associated accounts as well as CRUD endpoints for products and orders.  There is a CI/CD
pipeline that has been integrated through a github workflow.  This will automaticall test and deploy the app to Render if the tests are passed.
The enpoints for this system require verification through a token that is generated when a user logs into thier account.  The token is required as well as the user's role.
There are also other imporvements to these endpoints such as Caching and a limiter that handles the ammount of requests that can be made to a certain endpoint.

## How to set up:
- Open a terminal

- Visit github.com/rpeloso21/Mod-16-Project-E-Commerce-API-CI-CD

- Clone the repository

- cd into the project directory 'Mod 16 Project E-Commerce API CI CD'.

- compile the code.

##  Using Postman
- The requests for this API are grouped into collections in Post Man.

## Using Swagger
- There is also the option to test these routes using the Swagger documentation.  This is all located at https://mod-16-project-e-commerce-api-ci-cd.onrender.com/api/docs/#/
