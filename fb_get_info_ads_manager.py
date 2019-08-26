from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.ad import Ad
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adsinsights import AdsInsights
from facebook_business.adobjects.adsinsights import AdsInsights
import sys
def get_list_campaign(account_ids):
    my_account = AdAccount(account_ids)
    campaign = my_account.get_campaigns()
    return campaign

def get_campaign(campaign_list):
    campaigns = campaign_list.api_get(fields=[Campaign.Field.id, Campaign.Field.name])
    return campaign_list

def get_adset(adset):
    adsets = campaign.get_ad_sets(fields=[AdSet.Field.name,AdSet.Field.id])
    return adsets

def get_ads(adset_id):
    ads = adset.get_ads(fields=[Ad.Field.id,Ad.Field.name])
    return ads

def get_insight(ads_id):
    params = {
        #'date_preset': {'yesterday'
        #                },
        #'time_range': {
        #    'since': '2019-08-23',
        #    'until': '2019-08-23'
        #},
        'fields': [
            AdsInsights.Field.ad_id,
            AdsInsights.Field.ad_name,
            AdsInsights.Field.impressions,
            AdsInsights.Field.spend,
            AdsInsights.Field.clicks,
            AdsInsights.Field.frequency,
            AdsInsights.Field.unique_clicks,
            AdsInsights.Field.cost_per_inline_link_click,
            AdsInsights.Field.inline_link_clicks,
            AdsInsights.Field.reach,
            AdsInsights.Field.objective,
            AdsInsights.Field.cpc,
            AdsInsights.Field.cpm,
            AdsInsights.Field.cpp,
            AdsInsights.Field.ctr,
            AdsInsights.Field.actions
        ]
    }
    insights = ad.get_insights(fields=params.get('fields'), params=params)
    return insights



if __name__ == "__main__":
    my_app_id = 'XXXXXXXXXXXXXXXXXXXX'
    my_app_secret = 'XXXXXXXXXXXXXXXXXXXX'
    my_access_token = 'XXXXXXXXXXXXXXXXXXXX'
    FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
    account = ('act_XXXXXXXXXXXXXXXXXXXX')
    campaign_list = list(get_list_campaign(account))
    for campaign_info in campaign_list:
        campaign = get_campaign(campaign_info)
        campaign_name = campaign.get('name')
        campaign_id = campaign.get('id')
        print("==============================")
        print("LIST CAMPAIGN ID ", campaign_id, " NAME ", campaign_name)
        adsets = get_adset(campaign_id)
        for adset in adsets:
            adset_id = adset['id']
            adset_name = adset['name']
            print('LIST ADSET ID ',adset_id, " NAME ",adset_name)
            ads = get_ads(adset_id)
            for ad in ads:
                ad_id = ad['id']
                ad_name = ad['name']
                ad_insights = Ad(ad_id)
                print('LIST AD ID ',ad_id, " NAME ",ad_name)
                insights =  get_insight(ad_insights)
                if insights is not None:
                    for insight in insights:
                        insight_id = insight['ad_id']
                        insight_name = insight['ad_name']
                        insight_clicks = insight['clicks']
                        insight_cpc = insight['cpc']
                        insight_cpm = insight['cpm']
                        insight_cpp = insight['cpp']
                        insight_ctr = insight['ctr']
                        insight_spend = insight['spend']
                        insight_dict = {'insight_id':insight_id,'insight_name':insight_name,'insight_clicks':insight_clicks,'insight_cpc':insight_cpc,'insight_cpm':insight_cpm,'insight_cpp':insight_cpp,'insight_ctr':insight_ctr,'insight_spend':insight_spend}
                        print('INSIGHT RESULT  ', insight_dict)








'''
RESULT 
INSIGHT RESULT   {'insight_id': '23843523751520251', 'insight_name': 'AD1', 'insight_clicks': '97', 'insight_cpc': '0.082371', 'insight_cpm': '2.136364', 'insight_cpp': '2.633487', 'insight_ctr': '2.593583', 'insight_spend': '7.99'}

'''