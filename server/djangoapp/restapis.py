import requests
import json
# import related models here
from .models import CarDealer
from requests.auth import HTTPBasicAuth

# Create a `get_request` to make HTTP GET requests
# e.g., response = requests.get(url, params=params, headers={'Content-Type': 'application/json'},
#                                     auth=HTTPBasicAuth('apikey', api_key))
def get_request(url, **kwargs):
    print(kwargs)
    print("GET from {}".format(url))
    try:
        response = requests.get(
            url, header={'Content-Type': 'application/json'},
            params=kwargs
        )
    except:
        print("Network exception occued")
    status_code = response.status_code
    print("With status {}".format(status_code))
    json_data = json.loads(response.text)
    return json_data

# Create a `post_request` to make HTTP POST requests
# e.g., response = requests.post(url, params=kwargs, json=payload)


# Create a get_dealers_from_cf method to get dealers from a cloud function
def get_dealers_from_cf(url, **kwargs):
    # - Call get_request() with specified arguments
    # - Parse JSON results into a CarDealer object list
    results = []
    json_result = get_request(url)
    if json_result:
        dealer = json_result["entries"]
        for dealer_doc in dealers:
            # dealer_doc = dealer
            dealer_obj = CarDealer(
                address = dealer_doc["address"],
                city = dealer_doc["city"],
                full_name = dealer_doc["full_name"],
                id_ = dealer_doc["id"],
                lat = dealer_doc["lat"], 
                long_ = dealer_doc["long"],
                short_name = dealer_doc["short_name"],
                st = dealer_doc["st"],
                zip_ = dealer_doc["zip"],
            )
            results.append(dealer_obj)
    return results

# Create a get_dealer_reviews_from_cf method to get reviews by dealer id from a cloud function
# - Call get_request() with specified arguments
# - Parse JSON results into a DealerView object list
def get_dealer_by_id_from_cf(url, dealerId):
    result = []
    json_result = get_request(url, dealerId=dealerId)
    if json_result:
        dealer = json_result["entries"]
        for dealer_doc in dealers:
            # dealer_doc = dealer
            dealer_obj = CarDealer(
                address = dealer_doc["address"],
                city = dealer_doc["city"],
                full_name = dealer_doc["full_name"],
                id_ = dealer_doc["id"],
                lat = dealer_doc["lat"], 
                long_ = dealer_doc["long"],
                short_name = dealer_doc["short_name"],
                st = dealer_doc["st"],
                zip_ = dealer_doc["zip"],
            )
            results.append(dealer_obj)
    return results


# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
def analyze_review_sentiments(text):
# - Call get_request() with specified arguments
# - Get the returned sentiment label such as Positive or Negative



