import requests as req
import json

def eb_req(st):
    header={'Authorization':"Bearer v^1.1#i^1#r^0#I^3#f^0#p^1#t^H4sIAAAAAAAAAOVYa2wUVRTu9sWjIDE8VMBkmQI+YHbntY8Z2A3bB7KxpdtuqWWV1Lszd9qxszPTmTu0awypjYJiCETABF+UkKjxh4qmPxTiDwk/DBGjRglECYgQooIRQyoEjHempWwraZFusIn7ZzPnnnvu+b7vnHvvDNVdOuXhjas29k/3TCrs7aa6Cz0euoyaUlqy5K6iwrklBVSOg6e3e2F3cU/RueUWyKiG0AAtQ9cs6O3KqJoluMYIYZuaoANLsQQNZKAlIFFIxmprBMZHCYapI13UVcIbr4oQIMzRUojjKAmyEs/x2Kpdj9moRwiZZgCkZYkHNJDSIQmPW5YN45qFgIYiBEMxFEkFSIZppIICSwks7WMDbIrwNkHTUnQNu/goIuqmK7hzzZxcR08VWBY0EQ5CROOxlcm6WLyqenXjcn9OrOggD0kEkG0Nf6rUJehtAqoNR1/Gcr2FpC2K0LIIf3RgheFBhdj1ZG4jfZdqOc1SYYkJhBk2kOa5QF6oXKmbGYBGz8OxKBIpu64C1JCCsmMxitlIPwVFNPi0GoeIV3mdv3obqIqsQDNCVFfE1sYSCSIak3BI8ChpmEBEiiKSiYYqUuKoEBNOB3mSYVmaS3P04DoDwQZZHrFQpa7hWBis5V2towqIk4YjqWFyqMFOdVqdGZORk1CuX/g6hVwo5Wg6IKKN2jRHVpjBPHjdx7EFGJqNkKmkbQSHIowccBnCXWUYikSMHHRLcbB6uqwI0YaQIfj9nZ2dvk7Wp5utfoaiaH9zbU1SbIMZQDi+Tq+7/srYE0jFhSJCPNNSBJQ1cC5duFRxAlorEeWoAMY4yPvwtKIjrf8w5GD2D2+IfDUIB0UYTNMhhpd5OiQH89Eg0cEa9Tt5wDTIkhlgtkNkqECEpIjrzM5AU5EENiAzbFiGpBTkZZLjZZlMB6QgScsQUhCm0yIf/h/1ya1WehKKJkT5KfV8lXkdw1TZflvnG6QmSa2V4RomUxFkQHtNcyqhVnA8aFhix9saG6rrI7faDDcHL+oGTOiqImbzwoDT63ljgTWlBDBRNglVFRvGBdRygE4skZ35Fg4ADMXn9LVP1DN+HeAN3TG1uBmPC3PMMOKZjI1AWoXxPG3m/81GflN4Cr7pTChMWL8BIRVp4Iric9X0WetFnwkt3Tbx7cxX5xzZjXo71PAOiExdVaHZRI9b6Duvr9Pro/Lx786K24Oex3vKBCptUVVwBbVMNGR3QlAFTLCzmA7wFM3wFDs+XJWupI3ZiXYKrdItBKWxoBVX3sad2j/8BT9a4P7oHk8f1ePZV+jxUH5qEV1OLSgtWlNcNG2upSDoU4Dss5RWDb+3mtDXDrMGUMzCUo+xBvy8KOeTQu866t6hjwpTiuiynC8M1PwbIyX0jHumY0oCDEMFWaxiiiq/MVpMzyme9cPh5lOe3yez1fGr146Vv7AYoD5ATR9y8nhKCop7PAU7P9rdpjev2Nl9V8Lf/Hr1A/edTJe1Xuv55Yx3+64LR459/Vfljwee/rZgNpxa/+G+jpYT56TU8x2bTz/40ouH3p+5rW8mffyx7/jPOy5dfDXcV/vcLnJ/KrtsT3jrtq02FEveM0Ov9S/bvO5Izb5g/cU29M3B7ac/OHBhxZetM97Yf3zSF5vnbTi7qatlQWTDwgOJu5u+P7i1gdvx1rTHryx94mjvZ30XNv328q/JvVfkd3YvPkvd/2SBVBD1zlrWn3r3bXS26XzNFsBNFo6W9W25pL+54/wnS/88fO7M/ENFF8290z4O7Zmzs7L86slXHjrece2rbZf/2DD78oln+z9lS2f8tPYR73r9VOWmeYeemTog39/qTaAa7BEAAA==",
            'X-EBAY-C-MARKETPLACE-ID':'EBAY_US',
    'Content-Type':'application/json',
    "Accept": "application/json"
            }
    r=req.get('https://api.ebay.com/buy/browse/v1/item_summary/search?q='+st+'&limit=3&fieldgroups=ASPECT_REFINEMENTS', headers=header)
    print(r.json())
    print(r.json()['refinement']['dominantCategoryId'])
    r1=req.get('https://api.ebay.com/buy/browse/v1/item_summary/search?q='+st+'&limit=3&category_ids='+str(r.json()['refinement']['dominantCategoryId']), headers=header)
    print(r1.json())
    p_id=str(r1.json()['itemSummaries'][0]['itemId'])
    print(p_id)
    print(type(p_id))
    prd_data={
        "shippingAddress": {
            "recipient": "Aditya K",
            "phoneNumber": "790 401 8249",
            "addressLine1": "535,63rd Cross,Rajajinagar",
            "city": "Bengaluru",
            "stateOrProvince": "Karnataka",
            "postalCode": "560010",
            "country": "IN"
        },
        "lineItemInputs": [
            {
                "quantity": 1,
                "itemId": p_id
            }
        ]
    }
    r=req.post('https://apix.ebay.com/buy/order/v1/guest_checkout_session/initiate',headers=header,data=json.dumps(prd_data))
    print(r.json())
    return r1
