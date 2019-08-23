from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.ad import Ad
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adsinsights import AdsInsights
import sys

def get_account(account):
    account_ad = AdAccount(account)
    params = {
        'fields': [
            Campaign.Field.id,
            Campaign.Field.name,
            AdAccount.Field.timezone_id,
            AdAccount.Field.timezone_name,
            AdAccount.Field.timezone_offset_hours_utc
        ]
    }
    accounts = account_ad.api_get(fields=params.get('fields'), params=params)
    account_name = accounts.get('name')
    account_id = accounts.get('id')
    account_time_zone_id = accounts.get('timezone_id')
    account_time_zone_name = accounts.get('timezone_name')
    account_time_zone_offset_hours_utc = accounts.get('timezone_offset_hours_utc')
    return {'account_id':account_id,'account_name':account_name,'account_time_zone_id':account_time_zone_id,'account_time_zone_name':account_time_zone_name,'account_time_zone_offset_hours_utc':account_time_zone_offset_hours_utc}

if __name__ == "__main__":
    my_app_id = 'xxxxxxxxxxxxxx'
    my_app_secret = 'xxxxxxxxxxxxxx'
    my_access_token = 'xxxxxxxxxxxxxx'
    FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
    account = ('act_xxxxxxxxxxxxxx')

    account_info = get_account(account)
    print(account_info)


'''
RESULT 
{'account_id': 'act_XXXXXXXXXXX', 'account_name': 'michelone', 'account_time_zone_id': 7, 'account_time_zone_name': 'America/New_York', 'account_time_zone_offset_hours_utc': -4}

'''