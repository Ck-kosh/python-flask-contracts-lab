#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response

# Sample contracts data with unique IDs and contract information
contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]

# Sample customers data - storing customer names
customers = ["bob","bill","john","sarah"]

app = Flask(__name__)


@app.route('/contract/<int:id>')
def get_contract(id):
    """
    Retrieve contract information by contract ID.
    
    Args:
        id (int): The contract ID to look up
        
    Returns:
        200: Plain text contract information if found
        404: Not found if contract ID doesn't exist
    """
    # Search for contract with matching ID in the contracts list
    for contract in contracts:
        if contract["id"] == id:
            # Return contract information as plain text with 200 status
            return contract["contract_information"], 200
    
    # Return 404 if contract ID not found
    return make_response("", 404)


@app.route('/customer/<customer_name>')
def get_customer(customer_name):
    """
    Check if a customer exists (without returning sensitive data).
    
    Args:
        customer_name (str): The customer name to look up
        
    Returns:
        204: No content if customer found (empty response body for privacy)
        404: Not found if customer doesn't exist
    """
    # Search for customer in the customers list (case-insensitive)
    if customer_name.lower() in [c.lower() for c in customers]:
        # Return 204 No Content with empty body for privacy
        return make_response("", 204)
    
    # Return 404 if customer not found
    return make_response("", 404)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
