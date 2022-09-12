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
        if api_key:
            response = requests.get(
                url, 
                header={'Content-Type': 'application/json'},
                params=kwargs,
                auth=HTTPBasicAuth('apikey, api_key')
            )
        else if dealerId:
            response = requests.get(
                url, 
                header={'Content-Type': 'application/json'},
                params={'dealer_id': dealerId}, # if get review by dealer id: pass a json obj
            )
        else:
            response = requests.get(
                url, 
                header={'Content-Type': 'application/json'},
                params=kwargs,
            )
    except:
        print("Network exception occured")
    status_code = response.status_code
    print("With status {}".format(status_code))
    json_data = json.loads(response.text)
    return json_data

# Create a `post_request` to make HTTP POST requests
# e.g., response = requests.post(url, params=kwargs, json=payload)
def post_request(url, payload, **kwargs):
    print(kwargs)
    print("POST to {}".formate(url))
    try:
        response = requests.post(url, params=kwargs, json=payload)
    except:
        print("Network exception occured")
    status_code = response.status_code
    print("With status {}.format(status_code))
    json_data = json.lodas(response.text)
    return json_data


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

          
def get_dealer_by_id_from_cf(url, dealerId):
    results = []
    for dealer_obj in get_dealers_from_cf(url):
        if dealer_obj.id_ == dealerId:
            results.append(dealer_obj)
    return result

# Create a get_dealer_reviews_from_cf method to get reviews by dealer id from a cloud function
# - Call get_request() with specified arguments
# - Parse JSON results into a DealerView object list
def get_dealer_reviews_from_cf(url, dealer_Id):
    result = []
    json_result = get_request(url, dealerId=dealer_Id)
    if json_result:
        reviews = json_result["entries"]
        for review in dealers:
            # dealer_doc = dealer
            review_obj = DealerReview(
                dealership = dealer_doc["dealership"],
                name = dealer_doc["name"],
                purchase = dealer_doc["purchase"],
                id_ = dealer_doc["id"],
                review = dealer_doc["review"], 
                purchase_date = dealer_doc["purchase_date"],
                car_make = dealer_doc["car_make"],
                car_model = dealer_doc["car_model"],
                car_year = dealer_doc["car_year"],
            )
            review_obj.sentiment = analyze_review_sentiments(review_obj.review)
            results.append(review_obj)
    return results

# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
def analyze_review_sentiments(text):
    params = dict()
    url = "https://api.us-east.natural-language-understanding.watson.cloud.ibm.com/instances/5b5d04bf-2b6e-4bdc-b714-1b848d031245"
    api_key = "ysEVtjUvwAz7k95vINBOPwJpvarIiijqThYtfkoepnLX"
    authenticator = IAMAuthenticator(api_key) 
    natural_language_understanding = NaturalLanguageUnderstandingV1(version='2021-08-01',authenticator=authenticator) 
    natural_language_understanding.set_service_url(url) 
    response = natural_language_understanding.analyze(text, 
        features=Features(sentiment=SentimentOptions(targets=[]))).get_result()
    label = json.dumps(response, indent=2)
    label = response['sentiment']['document']['label'] 
    return label
    
    
# - Call get_request() with specified arguments
# - Get the returned sentiment label such as Positive or Negative



