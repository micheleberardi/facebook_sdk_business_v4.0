from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign

def get_campaign(account_ids):
    my_account = AdAccount(account_ids)
    campaigns = my_account.get_campaigns()
    params = {
        'fields': [
            Campaign.Field.id,
            Campaign.Field.name
        ]
    }
    for campaign in campaigns:
        print(campaign)
        campaigns = campaign.api_get(fields=params.get('fields'), params=params)
        campaign_name = campaigns.get('name')
        campaign_id = campaigns.get('id')
        return {'campaign_ids': campaign_id, 'campaign_name': campaign_name}

if __name__ == "__main__":
    my_app_id = 'xxxxxxxxxxxxxx'
    my_app_secret = 'xxxxxxxxxxxxxx'
    my_access_token = 'xxxxxxxxxxxxxx'
    FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
    account = ('xxxxxxxxxxxxxx')

    campaign_info = get_campaign(account)
    print(campaign_info)


'''
RESULT 
{'campaign_ids': '23843269296450128', 'campaign_name': 'Michelone - Facebook'}

'''