# Salesforce Bridge Microservice 

## 1. Application Description

This is a microservice application to interface with Salesforce.

## 2. Application Architecture

This application is a microservice responsible for interfacing with Salesforce. It uses FastAPI as the web framework and simple-salesforce for Salesforce integration.

Design principles:

    - Minimize the number of external libraries used.
    - Refer to requirements.txt for a list of external libraries used.
    - If a library must be used, prefer libraries already in the requirements.txt file.

## 3. Current State

- [x] Import the simple-salesforce package
- [x] Create a connection to Salesforce
- [x] Create a function to sanity-check the connection
- [x] Set up basic FastAPI application structure
- [x] Implement basic error handling for Salesforce connection
- [x] Create unit tests for Salesforce connection functions
- [x] Create unit tests for FastAPI endpoints

## 4. Next Steps

- [ ] Fix the failing test for Salesforce connection failure
- [ ] Create the API in Salesforce
- [ ] Integrate Salesforce connection with FastAPI
- [ ] Implement comprehensive error handling and logging
- [ ] Add more endpoints for specific Salesforce operations
- [ ] Implement dependency injection for Salesforce connection
- [ ] Add authentication and authorization

## 5. Next Step

Fix the failing test for Salesforce connection failure:

- [ ] Review the `test_create_salesforce_connection_failure` test in test_salesforce.py
- [ ] Identify the cause of the test failure (mismatch in error messages)
- [ ] Update the `create_salesforce_connection` function in salesforce.py to handle different error types
- [ ] Modify the test to expect the correct error message
- [ ] Run the tests again to ensure all tests pass
- [ ] Update error handling documentation if necessary

