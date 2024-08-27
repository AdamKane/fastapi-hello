# Salesforce Bridge Microservice 

## 1. Application Description

This is a microservice application to interface with Salesforce. We want to be able to do things like:

- Get a list of all Salesforce Account record names.
- Get a list of all Contact records for a given account.
- Get a list of all Opportunity records for a given Account.
- Get a list of all Opportunity record names.
- Get the list of all Opportunity records names where the stage is 'Proposal Due'.

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
- [x] Fix the failing test for Salesforce connection failure

## 4. Next Steps

- [ ] Create the API in Salesforce
- [ ] Integrate Salesforce connection with FastAPI
- [ ] Implement comprehensive error handling and logging
- [ ] Add more endpoints for specific Salesforce operations
- [ ] Implement dependency injection for Salesforce connection
- [ ] Add authentication and authorization

## 5. Next Step

Create the API in Salesforce and integrate it with FastAPI:

- [ ] Design the Salesforce API structure
- [ ] Create necessary custom objects or fields in Salesforce (if required)
- [ ] Set up API endpoints in Salesforce
- [ ] Update the `salesforce.py` file to interact with the new Salesforce API
- [ ] Create new FastAPI endpoints that correspond to the Salesforce API
- [ ] Implement error handling for API interactions
- [ ] Write unit tests for the new FastAPI endpoints
- [ ] Update documentation to reflect the new API integration

