# Salesforce Bridge Microservice Development Plan

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

- [x] Able to create a connection to Salesforce
- [x] Able to get salesforce instance name
- [x] Fixed the NameError in main.py
- [x] Implemented basic FastAPI application structure
- [x] Created unit tests for Salesforce connection functions
- [x] Created unit tests for FastAPI endpoints
- [x] All current tests are passing

## 4. Next Steps

- [ ] Implement comprehensive logging
- [ ] Implement dependency injection for Salesforce connection
- [ ] Add authentication and authorization
- [ ] Implement pagination for large result sets
- [ ] Add more detailed error messages
- [ ] Implement caching to improve performance
- [ ] Add more endpoints for specific Salesforce operations

## 5. Next Step

Implement comprehensive logging:

- [ ] Choose a logging library (e.g., Python's built-in logging module)
- [ ] Set up a logging configuration (log levels, format, output destination)
- [ ] Add logging statements to main.py for API requests and responses
- [ ] Add logging statements to salesforce.py for Salesforce operations
- [ ] Implement error logging for exception handling
- [ ] Create a utility function for consistent log formatting
- [ ] Update existing functions to include appropriate log messages
- [ ] Test logging functionality to ensure it captures necessary information




