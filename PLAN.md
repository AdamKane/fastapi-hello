# Salesforce Bridge Microservice Development Plan

## 1. Application Description

This is a microservice application to interface with Salesforce. We want to be able to do things like:

- Get a list of all Salesforce Account record names.
- Get a list of all Contact records for a given account.
- Get a list of all Opportunity records for a given Account.
- Get the list of all Opportunity records names where the stage is 'Proposal Due'.
- Get a list of all Lead records, sorted by name.
- Get the total count of all Lead records.
- Get a list of all fields for a given Salesforce object (e.g. Account).
- Get a list of all fields for a specific Salesforce object: Lead.
- Across all Lead records, get a list of the least used fields. Where "least used" is defined as the field that has the highest number of null values.

## 2. Application Architecture

This application is a microservice responsible for interfacing with Salesforce. It uses FastAPI as the web framework and simple-salesforce for Salesforce integration. 

Design principles:

    - Minimize the number of external libraries used.
    - Refer to requirements.txt for a list of external libraries used.
    - If a library must be used, prefer libraries already in the requirements.txt file.
    - Minimize complexity, focus on delivering features described in the application description.
    - Do not implement comprehensive error handling and logging
    - Do not implement authentication and authorization
    - Do not implement rate limiting
    - Do not implement pagination for large result sets
    - Do not implement caching
    - Do not implement more detailed error messages

## 3. Current State

- [x] Able to create a connection to Salesforce
- [x] Able to get salesforce instance name
- [x] Fixed the NameError in main.py
- [x] Implemented basic FastAPI application structure
- [x] Created unit tests for Salesforce connection functions
- [x] Created unit tests for FastAPI endpoints
- [x] All current tests are passing
- [x] Implemented all basic Salesforce operations mentioned in the application description

## 4. Next Steps

- [ ] Get the total count of all Lead records.
- [ ] Get a list of all Lead records, sorted by name.
- [ ] Get a list of all fields for a given Salesforce object (e.g. Account).
- [ ] Get a list of all fields for a specific Salesforce object: Lead.
- [ ] Across all Lead records, get a list of the least used fields.
- [ ] Implement comprehensive error handling and logging
- [ ] Add authentication and authorization to the API
- [ ] Implement rate limiting to prevent API abuse
- [ ] Add pagination for large result sets
- [ ] Create more detailed API documentation

## 5. Next Step

Get the total count of all Lead records:

- [ ] Add a new function in salesforce.py to query the total count of Lead records
- [ ] Create a new FastAPI endpoint in main.py to expose this functionality
- [ ] Write a unit test for the new Salesforce function in test_salesforce.py
- [ ] Write a unit test for the new FastAPI endpoint in test_main.py
- [ ] Update the API documentation to include the new endpoint


