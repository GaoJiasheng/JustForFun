#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pandas as pd

if __name__ == "__main__":
    # read data
    data = pd.read_excel('./data/Test_Pandas.xlsx', sheet_name='duplicate_title_sg')
    columns = data.columns

    # how many shops
    shop_num = data.shopid.nunique()
    # how many unique preferred and cross border shops
    refered_and_cross_num = data.query('cb_option == 1 and is_preferred == 1').shopid.nunique()
    # how many zero sold count items
    data_temp = data[['itemid', 'sold_count']].groupby('itemid').sum()
    zero_sold_count_num = data_temp[data_temp.sold_count != 0].count()
    # how many products were created in 2018
    data['year'] = pd.to_datetime(data.item_creation_date, format='%d/%m/%Y').apply(lambda x: x.year)
    item_creation_2018_num = data[data.year == 2018].groupby(by='itemid').nunique().count()

    # Top 3 Preferred shops’ shopid that have the largest number of unique product
    shop_num = data[['shopid', 'itemid']].groupby(by='shopid').count().max()
    # Top 3 Categories that have the largest number of unique cross-border product
    product_num = data[['category', 'cb_option', 'itemid']].query('cb_option==1').groupby(by='category').count().sort_values(by='itemid', ascending=False).head(3)

    # Top 3 shopid with the highest revenue
    data_temp = data[['shopid', 'itemid', 'price', 'sold_count']]
    data_temp['revenue'] = data_temp.price * data_temp.sold_count
    shop_top3_revenue_num = data_temp.groupby('shopid').sum().sort_values(by='revenue').head(3)

    # number of products that have more than 3 variations
    item_num = data[['itemid', 'item_variation']].groupby('itemid').nunique()

    # sign duplicated
    data['is_duplicated'] = data.duplicated(['item_name', 'item_description'])
    data['is_duplicated'] = 1 if data.is_dumplicated else 0

    # Find duplicate listings that has less than 2 sold count
    data_out = data.query('is_duplicated == 1 and sold_count < 2')
    pd.to_excel('./duplicated_listings.xlsx', sheet=0)

    # Find the preferred shop shopid that have the most number of duplicated listing
    data.groupby(by='shopid').sum(by='duplicated').sort_values(by='duplicated').head()

