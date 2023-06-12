import requests
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go

# Function to fetch LinkedIn data
def get_linkedin_data(access_token, url_follower, params):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0",
        "LinkedIn-Version": "202211"
    }

    response = requests.get(url_follower, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to fetch data: {response.text}")
        return None

def fetch_industry_data(access_token):
    url = "https://api.linkedin.com/v2/industries"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to fetch data: {response.text}")
        return None
def fetch_country_data(access_token):
    url = "https://api.linkedin.com/v2/countries"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to fetch data: {response.text}")
        return None
def fetch_seniority_data(access_token):
    url = "https://api.linkedin.com/v2/seniorities"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to fetch data: {response.text}")
        return None
def fetch_job_function_data(access_token):
    url = "https://api.linkedin.com/v2/functions"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to fetch data: {response.text}")
        return None


# Set your access token here
access_token = "AQUQBiCclRU7Z1lzzxPPxWVFEg-hm6zKrqUhTcSYsOg2LUpQVctHzMHtrLjRBC42IR9TTspm1RCyLfzaRXmNcfST91qafN_AJxKFFbLN1a2SrrhzX4VUrV627RvvDGQDswIl95qJ86NFKjBVMWv4KHXY0xV_B6eF26KsBaC3E_S3A9_YmqZIvwq7s_AU_C5b6gt4EQCt1AtNx4zKf_TrOp1R8uMrSQERJe4-awfq5Bw97nHAwOvTwro08rAP9J9CSAJzFpJc_lW_aZwMSR1JEphLDdzJH08qJQtsE6Yb1T7OjfU6ZMF21xlqgz3YDJC74ywOM_vmP9SNUBkyjceCJ15bO8xIDg"
#access_token = "AQWOPLcBhqG69GVBKhohha9g2jrXpBKvKaZ2wClPnSrqjNkdajMdLw8HHqtQX5qKcKnUCe9qiHZeZrWsfqGdKtu2FZje76t8SN-W6Bf3Owdd6KuSTIKB9zhtM4Svqu0HWQFAQ3QKggW_15E503ekdh_LzcB44hBoLcswv2JYyXw_oLjfdqoRIRNuUNBh5f4J0j92AepirJP9iLYZa78HgNKel85uiMDtziFHb-Zww_G7n4IFp-K_nrefTzdMoNLUY6kr6T6EWY_shIaBKrRSUEGngIJno43QbGNWyEtW8mKP9PcI-Wf4rmwwUcRBv-GNndLQyovx9G9lrlOLj6E5yZWiKDrLaw"
#access_token = "AQW2x2-m9dJp8zoeOzNc9185aYDBxV5kkz62rADU_Zgi1aPTlYKJLR12wtuTOC4i41AXHpEPyWqNgAy67bZCRRVsyjZP0K3K0mC5R9HCZoWMeuZrN7Lxe6iMDfbJ6xZw7t3jA43Yon19o92_H1K6mkuqOAMhyHpvXttsbNsVtoH9zjsHqJ2Fg7SWyD3oRWnZ6ZUl7rPe4O8hbCccVmh0EVVcVrgsZqEYz48VqHYtCzzsaZbo1pCr94tTyjCP3E1722shcugqvR5dacrRtFpH_2FcTnwdC7yC4pjO48XAOMfvWlV9R_m5_l-USlplq4q0Mk0ZVbJc6w9OTqaj4Q09ncNSprnakg"
# Set the LinkedIn API endpoint URL
url_follower = "https://api.linkedin.com/rest/organizationalEntityFollowerStatistics"

# Set the query parameters
params = {
    "q": "organizationalEntity",
    "organizationalEntity": "urn:li:organization:13741517"
}
# Fetch LinkedIn data using the access token and URL
linkedin_data = get_linkedin_data(access_token, url_follower, params)
industry_names = fetch_industry_data(access_token)
seniority = fetch_seniority_data(access_token)
job_function = fetch_job_function_data(access_token)
countries_data = fetch_country_data(access_token)


# Check if data is fetched successfully
if linkedin_data:

        # Extract followerCountsByGeoCountry list
    follower_counts = linkedin_data['elements'][0]['followerCountsByGeoCountry']

    # Create separate lists for keys and values
    keys = []
    values = []

    for item in follower_counts:
        keys.append(item['geo'])
        values.append(item['followerCounts']['organicFollowerCount'])

    # Create a DataFrame from the lists
    df_geo = pd.DataFrame({'Geo': keys, 'Follower Counts': values})
    # Sort the DataFrame by Follower Counts in descending order
    df_geo_sorted = df_geo.sort_values('Follower Counts', ascending=False)

    # Select the top two countries
    top_two_countries = df_geo_sorted.head(2)

    # Calculate the sum of follower counts for remaining countries
    remaining_count = df_geo_sorted.iloc[2:]['Follower Counts'].sum()

    # Create a new DataFrame for the top two countries and "Other"
    df_geo_pie = top_two_countries.append({'Geo': 'Other', 'Follower Counts': remaining_count}, ignore_index=True)
    
    # Extract followerCountsByStaffCountRange data
    follower_counts_company_size = linkedin_data['elements'][0]['followerCountsByStaffCountRange']
    # Create separate lists for keys and values
    keys = []
    values = []

    for item in follower_counts_company_size:
        keys.append(item['staffCountRange'])
        values.append(item['followerCounts']['organicFollowerCount'])

    # Create a DataFrame from the lists
    df_follower_company_size = pd.DataFrame({'Company_size': keys, 'Follower Counts': values})


    follower_counts_by_industry = linkedin_data['elements'][0]['followerCountsByIndustry']

    # Create separate lists for keys and values
    keys = []
    values = []

    for item in follower_counts_by_industry:
        keys.append(item['industry'])
        values.append(item['followerCounts']['organicFollowerCount'])

    # Create a DataFrame from the lists
    df_follower_counts_by_industry = pd.DataFrame({'industry': keys, 'Follower Counts': values})

    # Sort the dataframe by follower counts in descending order
    df_follower_counts_by_industry.sort_values(by='Follower Counts', ascending=False, inplace=True)

    # Select the top ten industries
    df_top_10_industries = df_follower_counts_by_industry.head(10).copy()
    df_top_10_industries.reset_index(drop=True, inplace=True)

    # Create a dictionary of industry names
    industry_dict = {}
    for element in industry_names["elements"]:
        urn = element["$URN"]
        name = element["name"]["localized"]["en_US"]
        industry_dict[urn] = name

    # Map industry names to the "industry" column in the dataframe
    df_top_10_industries["industry"] = df_top_10_industries["industry"].map(industry_dict)




    # Extract followerCountsSeniority list
    follower_counts_by_seniority = linkedin_data['elements'][0]['followerCountsBySeniority']

    # Create separate lists for keys and values
    keys = []
    values = []

    for item in follower_counts_by_seniority:
        keys.append(item['seniority'])
        values.append(item['followerCounts']['organicFollowerCount'])

    # Create a DataFrame from the lists
    df_follower_counts_by_seniority = pd.DataFrame({'seniority': keys, 'Follower Counts': values})
    urn_dict_seniority = {}
    for element in seniority["elements"]:
        urn = element["$URN"]
        name = element["name"]["localized"]["en_US"]
        urn_dict_seniority [urn] = name
    df_follower_counts_by_seniority["seniority"] = df_follower_counts_by_seniority["seniority"].map(urn_dict_seniority)

    # follower count by job_function
    
    follower_count_by_job_function= linkedin_data['elements'][0]['followerCountsByFunction']
    # Create separate lists for keys and values
    keys = []
    values = []

    for item in follower_count_by_job_function:
        keys.append(item['function'])
        values.append(item['followerCounts']['organicFollowerCount'])

    # Create a DataFrame from the lists
    df_follower_count_by_job_function = pd.DataFrame({'job_function': keys, 'Follower Counts': values})
    urn_dict_job_function = {}
    for element in job_function["elements"]:
        urn = element["$URN"]
        name = element["name"]["localized"]["en_US"]
        urn_dict_job_function  [urn] = name
    df_follower_count_by_job_function["job_function"] = df_follower_count_by_job_function["job_function"].map(urn_dict_job_function)

#visitors data starts from here
#
#
#
#

def get_linkedin_page_views_data(access_token, url):
    # Set the headers with the access token and desired API version
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0",
        "LinkedIn-Version": "202211"
    }

    # Make the API request
    response = requests.get(url, headers=headers,params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Return the JSON data
        data = response.json()
        return data
    else:
        # Print an error message if the request failed
        print(f"Failed to fetch data: {response.text}")
        return None

# Set your access token here
#access_token = "AQUQBiCclRU7Z1lzzxPPxWVFEg-hm6zKrqUhTcSYsOg2LUpQVctHzMHtrLjRBC42IR9TTspm1RCyLfzaRXmNcfST91qafN_AJxKFFbLN1a2SrrhzX4VUrV627RvvDGQDswIl95qJ86NFKjBVMWv4KHXY0xV_B6eF26KsBaC3E_S3A9_YmqZIvwq7s_AU_C5b6gt4EQCt1AtNx4zKf_TrOp1R8uMrSQERJe4-awfq5Bw97nHAwOvTwro08rAP9J9CSAJzFpJc_lW_aZwMSR1JEphLDdzJH08qJQtsE6Yb1T7OjfU6ZMF21xlqgz3YDJC74ywOM_vmP9SNUBkyjceCJ15bO8xIDg"
#access_token = "AQWOPLcBhqG69GVBKhohha9g2jrXpBKvKaZ2wClPnSrqjNkdajMdLw8HHqtQX5qKcKnUCe9qiHZeZrWsfqGdKtu2FZje76t8SN-W6Bf3Owdd6KuSTIKB9zhtM4Svqu0HWQFAQ3QKggW_15E503ekdh_LzcB44hBoLcswv2JYyXw_oLjfdqoRIRNuUNBh5f4J0j92AepirJP9iLYZa78HgNKel85uiMDtziFHb-Zww_G7n4IFp-K_nrefTzdMoNLUY6kr6T6EWY_shIaBKrRSUEGngIJno43QbGNWyEtW8mKP9PcI-Wf4rmwwUcRBv-GNndLQyovx9G9lrlOLj6E5yZWiKDrLaw"
# Set the LinkedIn API endpoint URL
url = "https://api.linkedin.com/rest/organizationPageStatistics"

# Set the query parameters
params = {
    "q": "organization",
    "organization": "urn:li:organization:13741517"
}
# Fetch LinkedIn data using the access token and URL
linkedin_data_page_views = get_linkedin_page_views_data(access_token, url)

# Extracting relevant data for page statistics by seniority
page_stats_seniority = linkedin_data_page_views['elements'][0]['pageStatisticsBySeniority']

seniorities = []
page_views_seniority = []

for stats in page_stats_seniority:
    seniorities.append(stats['seniority'])
    page_views_seniority.append(stats['pageStatistics']['views']['allPageViews']['pageViews'])

# Creating the dataframe for page statistics by seniority
df_page_seniority = pd.DataFrame({'Seniority': seniorities, 'AllPageViews': page_views_seniority})
df_page_seniority["Seniority"] = df_page_seniority["Seniority"].map(urn_dict_seniority)


# Extracting relevant data for page statistics by country
page_stats_country = linkedin_data_page_views['elements'][0]['pageStatisticsByCountry']

countries = []
page_views_country = []

for stats in page_stats_country:
    countries.append(stats['country'])
    page_views_country.append(stats['pageStatistics']['views']['allPageViews']['pageViews'])

# Extract URN and Value from the elements list
urn_list = [element["$URN"] for element in countries_data["elements"]]
value_list = [element["name"]["value"] for element in countries_data["elements"]]

# Create DataFrame
df_countries = pd.DataFrame({"URN": urn_list, "Country Name": value_list})

# Creating the dataframe for page statistics by country
df_page_country = pd.DataFrame({'Country': countries, 'AllPageViews': page_views_country})

# Extract URN and Value from the elements list
urn_list = [element["$URN"] for element in countries_data["elements"]]
value_list = [element["name"]["value"] for element in countries_data["elements"]]

# Create a dictionary mapping URN to Value in df_countries
urn_to_value = df_countries.set_index('URN')['Country Name'].to_dict()

# Map the URN column in df_page_country with the corresponding Value
df_page_country['Country'] = df_page_country['Country'].map(urn_to_value)

# Sort the df_page_country DataFrame by AllPageViews in descending order
df_page_country_sorted = df_page_country.sort_values(by='AllPageViews', ascending=False)

# Sort the df_page_country DataFrame by AllPageViews in descending order
df_page_country_sorted = df_page_country.sort_values(by='AllPageViews', ascending=False)

# Select the top two countries with maximum page views
top_countries = df_page_country_sorted.nlargest(2, 'AllPageViews')

# Sum the page views of remaining countries
other_countries_page_views = df_page_country_sorted[~df_page_country_sorted['Country'].isin(top_countries['Country'])]['AllPageViews'].sum()

# Create a DataFrame for top countries and other countries
df_top_countries = pd.concat([top_countries, pd.DataFrame({'Country': ['Other'], 'AllPageViews': [other_countries_page_views]})])

# Calculate the percentage of page views for each country
df_top_countries['Percentage'] = (df_top_countries['AllPageViews'] / df_top_countries['AllPageViews'].sum()) * 100



# Extracting relevant data for page statistics by job function
page_stats_job_function = linkedin_data_page_views['elements'][0]['pageStatisticsByFunction']

job_functions = []
page_views_job_function = []

for stats in page_stats_job_function:
    job_functions.append(stats['function'])
    page_views_job_function.append(stats['pageStatistics']['views']['allPageViews']['pageViews'])

# Creating the dataframe for page statistics by job function
df_page_job_function = pd.DataFrame({'Job Function': job_functions, 'AllPageViews': page_views_job_function})
df_page_job_function["Job Function"] = df_page_job_function["Job Function"].map(urn_dict_job_function)

# Extracting relevant data for page statistics by industry
page_stats_industry = linkedin_data_page_views['elements'][0]['pageStatisticsByIndustry']

industries = []
page_views_industry = []

for stats in page_stats_industry:
    industries.append(stats['industry'])
    page_views_industry.append(stats['pageStatistics']['views']['allPageViews']['pageViews'])

# Creating the dataframe for page statistics by industry
df_page_industry = pd.DataFrame({'Industry': industries, 'AllPageViews': page_views_industry})

# Mapping industry names using industry_dict (assuming you have a dictionary mapping industry names)
df_page_industry["Industry"] = df_page_industry["Industry"].map(industry_dict)

# Sorting the dataframe by 'AllPageViews' in descending order
df_page_industry = df_page_industry.sort_values('AllPageViews', ascending=False)

# Selecting the top ten industries
top_ten_industries = df_page_industry.head(10).copy()
top_ten_industries.reset_index(drop=True, inplace=True)


# Extracting relevant data for page statistics by company size
page_stats_company_size = linkedin_data_page_views['elements'][0]['pageStatisticsByStaffCountRange']

company_sizes = []
page_views_company_size = []

for stats in page_stats_company_size:
    company_sizes.append(stats['staffCountRange'])
    page_views_company_size.append(stats['pageStatistics']['views']['allPageViews']['pageViews'])

# Creating the dataframe for page statistics by company size
df_page_company_size = pd.DataFrame({'Company Size': company_sizes, 'AllPageViews': page_views_company_size})
#df_page_company_size["Company Size"] = df_page_company_size["Company Size"].map(urn_dict)


### Content Code starts from here
#
#
#
#

def get_linkedin_data_content(access_token, url, params=None):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0",
        "LinkedIn-Version": "202305"
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to fetch data: {response.text}")
        return None

# Set your access token here
#access_token = "AQUQBiCclRU7Z1lzzxPPxWVFEg-hm6zKrqUhTcSYsOg2LUpQVctHzMHtrLjRBC42IR9TTspm1RCyLfzaRXmNcfST91qafN_AJxKFFbLN1a2SrrhzX4VUrV627RvvDGQDswIl95qJ86NFKjBVMWv4KHXY0xV_B6eF26KsBaC3E_S3A9_YmqZIvwq7s_AU_C5b6gt4EQCt1AtNx4zKf_TrOp1R8uMrSQERJe4-awfq5Bw97nHAwOvTwro08rAP9J9CSAJzFpJc_lW_aZwMSR1JEphLDdzJH08qJQtsE6Yb1T7OjfU6ZMF21xlqgz3YDJC74ywOM_vmP9SNUBkyjceCJ15bO8xIDg"
#access_token = "AQWOPLcBhqG69GVBKhohha9g2jrXpBKvKaZ2wClPnSrqjNkdajMdLw8HHqtQX5qKcKnUCe9qiHZeZrWsfqGdKtu2FZje76t8SN-W6Bf3Owdd6KuSTIKB9zhtM4Svqu0HWQFAQ3QKggW_15E503ekdh_LzcB44hBoLcswv2JYyXw_oLjfdqoRIRNuUNBh5f4J0j92AepirJP9iLYZa78HgNKel85uiMDtziFHb-Zww_G7n4IFp-K_nrefTzdMoNLUY6kr6T6EWY_shIaBKrRSUEGngIJno43QbGNWyEtW8mKP9PcI-Wf4rmwwUcRBv-GNndLQyovx9G9lrlOLj6E5yZWiKDrLaw"
# Set the LinkedIn API endpoint URL
share_stats_url = "https://api.linkedin.com/rest/organizationalEntityShareStatistics"
posts_url = "https://api.linkedin.com/rest/posts"

# Set the query parameters for share statistics
share_stats_params = {
    "q": "organizationalEntity",
    "organizationalEntity": "urn:li:organization:13741517"
}

# Set the query parameters for posts
posts_params = {
    "q": "author",
    "author": "urn:li:organization:13741517",
    "count": "10",
    "sortBy": "LAST_MODIFIED",
    "viewContext": "AUTHOR"
}

# Fetch LinkedIn data for share statistics
linkedin_data_share = get_linkedin_data_content(access_token, share_stats_url, params=share_stats_params)

if linkedin_data_share:
    share_stats = linkedin_data_share['elements'][0]['totalShareStatistics']
    df_total_share = pd.DataFrame([share_stats])
    df_total_share.insert(0, "Month", "Lifetime")
    print(df_total_share)

# Fetch LinkedIn data for posts
linkedin_data_posts = get_linkedin_data_content(access_token, posts_url, params=posts_params)

if linkedin_data_posts:
    shares_dict = {}
    shares = linkedin_data_posts['elements']

    for i, share in enumerate(shares):
        shares_dict[f'shares[{i}]'] = share['id']

    share_posts = {}
    ugc_posts = {}

    ugc_index = 0

    for key, value in shares_dict.items():
        if value.startswith('urn:li:share'):
            share_posts[key] = value
        elif value.startswith('urn:li:ugcPost'):
            ugc_posts[f'ugcPosts[{ugc_index}]'] = value
            ugc_index += 1

# Fetch LinkedIn data for post types
linkedin_data_type_of_post = get_linkedin_data_content(access_token, posts_url, params=posts_params)

if linkedin_data_type_of_post:
    share_dict = {}

    for element in linkedin_data_type_of_post['elements']:
        try:
            share_id = element['id']
            media_id = element['content']['media']['id']
            share_dict[share_id] = media_id
        except KeyError:
            continue

    df_content_type = pd.DataFrame(share_dict.items(), columns=['share_URN', 'Content Type'])
    df_content_type['Content Type'] = df_content_type['Content Type'].apply(lambda x: x.split(':')[-2])






    # Define functions for each dashboard page


def display_follower_dashboard():
    st.title("Follower Dashboard")



        # Create a pie chart with the top two countries and "Other"
    st.subheader("Follower Counts by Country")
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(df_geo_pie['Follower Counts'], labels=df_geo_pie['Geo'], autopct='%1.1f%%')
    plt.tight_layout()

    # Set the aspect ratio to equal to ensure a circular pie chart
    ax.set_aspect('equal')

    # Display the chart using st.pyplot()
    st.pyplot(fig)

    # Display follower_by_industry data as a bar chart
    st.subheader("Follower Counts by Industry")
    fig_follower_by_industry, ax_follower_by_industry = plt.subplots()
    ax_follower_by_industry.bar(df_top_10_industries['industry'].astype(str), df_top_10_industries['Follower Counts'])
    ax_follower_by_industry.set_xlabel("Industry")
    ax_follower_by_industry.set_ylabel("Follower Counts")
    ax_follower_by_industry.tick_params(axis='x', rotation=90)
    # Add exact numbers at the top of each bar
    for i, v in enumerate(df_top_10_industries['Follower Counts']):
        ax_follower_by_industry.text(i, v, str(v), ha='center', va='bottom')
    st.pyplot(fig_follower_by_industry)

    # Display follower_counts_by_seniority data as a bar chart
    st.subheader("Follower Counts by Seniority")
    fig_follower_counts_by_seniority, ax_follower_counts_by_seniority = plt.subplots()
    ax_follower_counts_by_seniority.bar(df_follower_counts_by_seniority['seniority'], df_follower_counts_by_seniority['Follower Counts'])
    ax_follower_counts_by_seniority.set_xlabel("Seniority")
    ax_follower_counts_by_seniority.set_ylabel("Follower Counts")
    ax_follower_counts_by_seniority.tick_params(axis='x', rotation=90)
    # Add exact numbers at the top of each bar
    for i, v in enumerate(df_follower_counts_by_seniority['Follower Counts']):
        ax_follower_counts_by_seniority.text(i, v, str(v), ha='center', va='bottom')
    st.pyplot(fig_follower_counts_by_seniority)

    # Display follower_count_by_job_function data as a bar chart
    st.subheader("Follower Counts by Job Function")
    fig_follower_count_by_job_function, ax_follower_count_by_job_function = plt.subplots()
    ax_follower_count_by_job_function.bar(df_follower_count_by_job_function['job_function'], df_follower_count_by_job_function['Follower Counts'])
    ax_follower_count_by_job_function.set_xlabel("Job Function")
    ax_follower_count_by_job_function.set_ylabel("Follower Counts")
    ax_follower_count_by_job_function.tick_params(axis='x', rotation=90)
    # Add exact numbers at the top of each bar
    for i, v in enumerate(df_follower_count_by_job_function['Follower Counts']):
        ax_follower_count_by_job_function.text(i, v, str(v), ha='center', va='bottom',rotation='vertical')
    st.pyplot(fig_follower_count_by_job_function)

    #Display followerCountsByStaffCountRange data as a bar chart
    st.subheader("Follower Counts by Company Size")
    fig_company_size, ax_company_size = plt.subplots()
    ax_company_size.bar(df_follower_company_size['Company_size'], df_follower_company_size['Follower Counts'])
    ax_company_size.set_xlabel("Company Size")
    ax_company_size.set_ylabel("Follower Counts")
    ax_company_size.tick_params(axis='x', rotation=90)
    st.pyplot(fig_company_size)

def display_visitors_dashboard():
    st.title("Visitors Dashboard")

    # Display the dataframes as charts

    # Chart for page statistics by seniority
    st.subheader("Page Views by Seniority")
    fig_seniority, ax_seniority = plt.subplots()
    ax_seniority.bar(df_page_seniority['Seniority'], df_page_seniority['AllPageViews'])
    ax_seniority.set_xlabel('Seniority')
    ax_seniority.set_ylabel('Page Views')
    ax_seniority.tick_params(axis='x', rotation=90)
    # Add exact numbers at the top of each bar
    for i, v in enumerate(df_page_seniority['AllPageViews']):
        ax_seniority.text(i, v, str(v), ha='center', va='bottom')
    st.pyplot(fig_seniority)

    # Chart for page statistics by country
    st.subheader("Page Views by Country")
    # Generate a list of colors for the pie chart
    colors = plt.cm.Set3(np.linspace(0, 1, len(df_top_countries)))

    # Plot the pie chart
    fig_pie, ax_pie = plt.subplots()
    wedges, _, autotexts = ax_pie.pie(df_top_countries['AllPageViews'], labels=df_top_countries['Country'], autopct='%1.1f%%', colors=colors,
                                    wedgeprops=dict(width=0.3, edgecolor='w'))

    # Add color bars as hints of the names and colors
    legend_labels = [f"{country}: {percentage:.1f}%" for country, percentage in zip(df_top_countries['Country'], df_top_countries['Percentage'])]
    ax_pie.legend(wedges, legend_labels, loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    ax_pie.set_title('Page Views by Country')
    st.pyplot(fig_pie)
    
    # Chart for page statistics by job function
    st.subheader("Page Views by Job Function")
    fig_job_function, ax_job_function = plt.subplots()
    ax_job_function.bar(df_page_job_function['Job Function'], df_page_job_function['AllPageViews'])
    ax_job_function.set_xlabel('Job Function')
    ax_job_function.set_ylabel('Page Views')
    ax_job_function.tick_params(axis='x', rotation=90)
    # Add exact numbers at the top of each bar
    for i, v in enumerate(df_page_job_function['AllPageViews']):
        ax_job_function.text(i, v, str(v), ha='center', va='bottom',rotation='vertical')
    st.pyplot(fig_job_function)

    # Chart for page statistics by industry
    st.subheader("Page Views by Industry")
    fig_industry, ax_industry = plt.subplots()
    ax_industry.bar(top_ten_industries['Industry'].astype(str), top_ten_industries['AllPageViews'])
    ax_industry.set_xlabel('Industry')
    ax_industry.set_ylabel('Page Views')
    ax_industry.tick_params(axis='x', rotation=90)
    # Add exact numbers at the top of each bar
    for i, v in enumerate(top_ten_industries['AllPageViews']):
        ax_industry.text(i, v, str(v), ha='center', va='bottom')
    st.pyplot(fig_industry)

    # Plotting the data using a bubble chart
    st.subheader("Page Statistics by Company Size")

    fig, ax = plt.subplots()
    bar_chart = ax.bar(df_page_company_size.index, df_page_company_size['AllPageViews'], color='blue')
    ax.set_xlabel('Company Size')
    ax.set_ylabel('Page Views')
    ax.set_xticks(df_page_company_size.index)
    ax.set_xticklabels(df_page_company_size['Company Size'], rotation=45, ha='right')
    ax.set_title('Page Statistics by Company Size')

    # Display the values on top of each bar
    for i, row in df_page_company_size.iterrows():
        ax.text(i, row['AllPageViews'], str(row['AllPageViews']), ha='center', va='bottom')

    st.pyplot(fig)



def display_content_dashboard():
    st.title("Content Dashboard")
    # Add code for the content dashboard

    # Visualize share statistics in a bar chart
    fig, ax = plt.subplots()
    bar_chart = ax.bar(df_total_share.columns[1:], df_total_share.iloc[0, 1:])
    ax.set_title('Share Statistics')
    ax.set_xlabel('Metric')
    ax.set_ylabel('Value')
    ax.set_xticklabels(df_total_share.columns[1:], rotation=90, ha='center')
    st.pyplot(fig)


    # Calculate the percentage of page views for each country
    df_top_countries['Percentage'] = (df_top_countries['AllPageViews'] / df_top_countries['AllPageViews'].sum()) * 100

    # Create the pie chart
    fig, ax = plt.subplots()
    ax.pie(df_top_countries['Percentage'], labels=df_top_countries['Country'], autopct='%1.1f%%')
    ax.set_title('Page Views by Country')
    st.pyplot(fig)


# Download function for follower dataframes
def download_follower_dataframes():
    # Save df_follower_company_size to CSV
    df_follower_company_size.to_csv('follower_company_size.csv', index=False)

    # Save df_top_10_industries to CSV
    df_top_10_industries.to_csv('top_10_industries.csv', index=False)

    # Save df_follower_counts_by_seniority to CSV
    df_follower_counts_by_seniority.to_csv('follower_counts_by_seniority.csv', index=False)

    # Save df_follower_count_by_job_function to CSV
    df_follower_count_by_job_function.to_csv('follower_count_by_job_function.csv', index=False)

    st.success("Follower dataframes downloaded successfully!")

# Download function for visitor dataframes
def download_visitor_dataframes():
    # Save df_page_seniority to CSV
    df_page_seniority.to_csv('page_seniority.csv', index=False)

    # Save df_top_countries to CSV
    df_top_countries.to_csv('top_countries.csv', index=False)

    # Save df_page_job_function to CSV
    df_page_job_function.to_csv('page_job_function.csv', index=False)

    # Save top_ten_industries to CSV
    top_ten_industries.to_csv('top_ten_industries.csv', index=False)

    # Save df_page_company_size to CSV
    df_page_company_size.to_csv('page_company_size.csv', index=False)

    st.success("Visitor dataframes downloaded successfully!")

# Download function for content dataframes
def download_content_dataframes():
    # Save df_total_share to CSV
    df_total_share.to_csv('total_share.csv', index=False)

    st.success("Content dataframes downloaded successfully!")


# Main app code using Streamlit
def main():
    # Define the dashboard selection
    dashboard_selection = st.sidebar.selectbox("Select Dashboard", ["Follower", "Visitor", "Content"], key="dashboard")

    # Conditionally execute the selected dashboard
    if dashboard_selection == "Follower":
        display_follower_dashboard()
    elif dashboard_selection == "Visitor":
        display_visitors_dashboard()
    elif dashboard_selection == "Content":
        display_content_dashboard()

    # Add a dropdown menu for download options in the sidebar
    download_option = st.sidebar.selectbox("Select Download", ["Download Follower Dataframes", "Download Visitor Dataframes", "Download Content Dataframes"], key="download")

    # Trigger the download based on the selected option
    if download_option == "Download Follower Dataframes":
        download_follower_dataframes()
    elif download_option == "Download Visitor Dataframes":
        download_visitor_dataframes()
    elif download_option == "Download Content Dataframes":
        download_content_dataframes()


# Run the main function
if __name__ == "__main__":
    main()
