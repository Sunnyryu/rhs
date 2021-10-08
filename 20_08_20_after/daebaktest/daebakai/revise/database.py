
import os
import csv
from dotenv import load_dotenv
import datetime
import pandas as pd
from daebakai import db

load_dotenv()
#pw = os.getenv("PASSWORD")
#user = os.getenv("USER_NAME")
#print(db)
#db = os.getenv("DB")
rows = None

class Database():
    def HandleSearch(handle):
        sql = '''
        SELECT * FROM product where handle = %s
        '''
        cursor= db.get_db().cursor()
        cursor.execute(sql, handle)
        rows = cursor.fetchall()
        cursor.close()
        return rows
    def VendorSearch(vendor_get):
        sql = '''
        SELECT DISTINCT handle, title FROM product where vendor = %s
        '''
        cursor = db.get_db().cursor
        a = cursor.execute(sql, vendor_get)
        rows = cursor.fetchall()
        cursor.close()
        return rows
    def ValueSearch(vendor):
        sql = '''
        SELECT DISTINCT * FROM product where vendor = %s
        '''
        cursor = db.get_db().cursor()
        a = cursor.execute(sql, vendor)
        rows = cursor.fetchall()
        cursor.close()
        return rows
    def IndexValueread():
        sql = '''
        SELECT handle, title, image_src, variant_price FROM product
        '''
        cursor= db.get_db().cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        cursor.close()
        return rows
    def Make_csv(vendor):
        sql = f'''
        SELECT handle, title, body_HTML, vendor, type, tags, published, option1_name, option1_value, option2_name, option2_value,
                        option3_name, option3_value, variant_sku, variant_grams, variant_inventory_tracker, variant_inventory_qty, variant_inventory_policy, variant_fullfillment_service, variant_price, variant_compare_at_price, varient_requires_shipping, variant_taxable,
                        variant_barcord, image_src, image_position, image_alt_text, gift_card, seo_title, seo_description, google_shopping_google_product_category, google_shopping_gender, goggle_shopping_age_group, google_shopping_mpn, google_shopping_adwords_grouping,
                        google_shopping_adwords_labels, google_shopping_condition, google_shopping_custom_product, google_shopping_custion_label0, google_shopping_custion_label1, google_shopping_custion_label2, google_shopping_custion_label3, google_shopping_custion_label4, variant_image, variant_weight_unit, variant_tax_code, cost_per_item
                        FROM product where vendor = '{vendor}'
        '''
        cursor= db.get_db().cursor()
        cursor.execute(sql)
        b = f'make_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}'
        cursor.close()
        result = pd.read_sql_query(sql,db.get_db())
        result.rename(columns={'handle': 'Handle', 'title': 'Title', 'body_HTML':'Body (HTML)','vendor':'Vendor', 'type':'Type', 'tags':'Tags', 'published':'Published', 'option1_name':'Option1 Name', 'option1_value':'Option1 Value',
            'option2_name':'Option2 Name', 'option2_value':'Option2 Value', 'option3_name':'Option3 Name', 'option3_value':'Option3 Value', 'variant_sku':'Variant SKU', 'variant_grams':'Variant Grams', 'variant_inventory_tracker':'Variant Inventory Tracker',
            'variant_inventory_qty':'Variant Inventory Qty', 'variant_inventory_policy':'Variant Inventory Policy','variant_fullfillment_service':'Variant Fulfillment Service', 'variant_price':'Variant Price', 'variant_compare_at_price':'Variant Compare At Price',
            'varient_requires_shipping':'Variant Requires Shipping', 'variant_taxable':'Variant Taxable', 'variant_barcode':'Variant Barcode', 'image_src':'Image Src', 'image_position':'Image Position', 'image_alt_text':'Image Alt Text',
            'gift_card':'Gift Card', 'seo_title':'SEO Title', 'seo_description':'SEO Description', 'google_shopping_google_product_category':'Google Shopping / Google Product Category', 'google_shopping_gender':'Google Shopping / Gender',
            'google_shopping_age_group':'Google Shopping / Age Group', 'google_shopping_mpn':'Google Shopping / MPN', 'google_shopping_adwords_grouping':'Google Shopping / AdWords Grouping', 'google_shopping_adwords_labels':'Google Shopping / AdWords Labels',
            'google_shopping_condition':'Google Shopping / Condition', 'google_shopping_custom_product':'Google Shopping / Custom Product', 'google_shopping_custom_label_0':'Google Shopping / Custom Label 0', 'google_shopping_custion_label1':'Google Shopping / Custom Label 1',
            'google_shopping_custion_label2':'Google Shopping / Custom Label 2', 'google_shopping_custion_label3':'Google Shopping / Custom Label 3', 'google_shopping_custion_label4':'Google Shopping / Custom Label 4',
            'variant_image':'Variant Image', 'variant_weight_unit':'Variant Weight Unit', 'variant_tax_code':'Variant Tax Code', 'cost_per_item':'Cost per item'  }, inplace=True)
        result.to_csv(rf'{b}.csv',index=False)
        return b
    def Make_csv2(vendor):
        sql = f'''
        SELECT handle, title, body_HTML, vendor, type, tags, published, option1_name, option1_value, option2_name, option2_value,
                        option3_name, option3_value, variant_sku, variant_grams, variant_inventory_tracker, variant_inventory_qty, variant_inventory_policy, variant_fullfillment_service, variant_price, variant_compare_at_price, varient_requires_shipping, variant_taxable,
                        variant_barcord, image_src, image_position, image_alt_text, gift_card, seo_title, seo_description, google_shopping_google_product_category, google_shopping_gender, goggle_shopping_age_group, google_shopping_mpn, google_shopping_adwords_grouping,
                        google_shopping_adwords_labels, google_shopping_condition, google_shopping_custom_product, google_shopping_custion_label0, google_shopping_custion_label1, google_shopping_custion_label2, google_shopping_custion_label3, google_shopping_custion_label4, variant_image, variant_weight_unit, variant_tax_code, cost_per_item
                        FROM product where vendor = '{vendor}'
        '''
        cursor= db.get_db().cursor()
        cursor.execute(sql)
        b = f'make_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}'
        cursor.close()
        result = pd.read_sql_query(sql,db.get_db())
        result.rename(columns={'handle': 'Handle', 'title': 'Title', 'body_HTML':'Body (HTML)','vendor':'Vendor', 'type':'Type', 'tags':'Tags', 'published':'Published', 'option1_name':'Option1 Name', 'option1_value':'Option1 Value',
            'option2_name':'Option2 Name', 'option2_value':'Option2 Value', 'option3_name':'Option3 Name', 'option3_value':'Option3 Value', 'variant_sku':'Variant SKU', 'variant_grams':'Variant Grams', 'variant_inventory_tracker':'Variant Inventory Tracker',
            'variant_inventory_qty':'Variant Inventory Qty', 'variant_inventory_policy':'Variant Inventory Policy','variant_fullfillment_service':'Variant Fulfillment Service', 'variant_price':'Variant Price', 'variant_compare_at_price':'Variant Compare At Price',
            'varient_requires_shipping':'Variant Requires Shipping', 'variant_taxable':'Variant Taxable', 'variant_barcode':'Variant Barcode', 'image_src':'Image Src', 'image_position':'Image Position', 'image_alt_text':'Image Alt Text',
            'gift_card':'Gift Card', 'seo_title':'SEO Title', 'seo_description':'SEO Description', 'google_shopping_google_product_category':'Google Shopping / Google Product Category', 'google_shopping_gender':'Google Shopping / Gender',
            'google_shopping_age_group':'Google Shopping / Age Group', 'google_shopping_mpn':'Google Shopping / MPN', 'google_shopping_adwords_grouping':'Google Shopping / AdWords Grouping', 'google_shopping_adwords_labels':'Google Shopping / AdWords Labels',
            'google_shopping_condition':'Google Shopping / Condition', 'google_shopping_custom_product':'Google Shopping / Custom Product', 'google_shopping_custom_label_0':'Google Shopping / Custom Label 0', 'google_shopping_custion_label1':'Google Shopping / Custom Label 1',
            'google_shopping_custion_label2':'Google Shopping / Custom Label 2', 'google_shopping_custion_label3':'Google Shopping / Custom Label 3', 'google_shopping_custion_label4':'Google Shopping / Custom Label 4',
            'variant_image':'Variant Image', 'variant_weight_unit':'Variant Weight Unit', 'variant_tax_code':'Variant Tax Code', 'cost_per_item':'Cost per item'  }, inplace=True)
        return result

    def Vendor_read():
        sql = '''
        SELECT DISTINCT vendor FROM product
        '''
        cursor = db.get_db().cursor()
        a = cursor.execute(sql)
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def Update_table_main(value_new_id, value_new_title, value_new_body_HTML, value_new_price, value_new_option1_value, value_new_revise_times, value_new_revise_last_time):
        sql = '''
        UPDATE product Set title=%s, body_HTML=%s, option1_value =%s, variant_price=%s, revise=%s, revise_last_time=%s where id = %s
        '''
        cursor = db.get_db().cursor()
        cursor.execute(sql,(value_new_title, value_new_body_HTML, value_new_option1_value, value_new_price, value_new_revise_times, value_new_revise_last_time, value_new_id))
        rows = cursor.fetchall()
        db.get_db().commit()
        cursor.close()
        return rows



    def Update_table_etc(value_new_id, value_new_price, value_new_option1_value, value_new_revise_times, value_new_revise_last_time):
        sql = '''
        UPDATE product Set option1_value =%s, variant_price=%s, revise=%s, revise_last_time=%s  where id = %s
        '''

        cursor = db.get_db().cursor()
        cursor.execute(sql,(value_new_option1_value, value_new_price, value_new_revise_times, value_new_revise_last_time, value_new_id))
        rows = cursor.fetchall()
        db.get_db().commit()
        cursor.close()
        return rows
    def Delete_value(c):
        #print(c)
        csv_read = open(c,'r', encoding='utf-8')
        csv_reader = csv.reader(csv_read)
        next(csv_reader)
        cursor = db.get_db().cursor()
        for row in csv_reader:
            sql = '''
            DELETE FROM product WHERE handle = %s
            '''
            cursor.execute(sql, row[0])
        db.get_db().commit()
        csv_read.close()
        cursor.close()
    def Insert_value(c):
        csv_read = open(c,'r', encoding='utf-8')
        csv_reader = csv.reader(csv_read)
        cursor = db.get_db().cursor()
        next(csv_reader)
        for row in csv_reader:
            sql = '''
            INSERT INTO product(handle, title, body_HTML, vendor, type, tags, published, option1_name, option1_value, option2_name, option2_value,
            option3_name, option3_value, variant_sku, variant_grams, variant_inventory_tracker, variant_inventory_qty, variant_inventory_policy, variant_fullfillment_service, variant_price, variant_compare_at_price, varient_requires_shipping, variant_taxable,
            variant_barcord, image_src, image_position, image_alt_text, gift_card, seo_title, seo_description, google_shopping_google_product_category, google_shopping_gender, goggle_shopping_age_group, google_shopping_mpn, google_shopping_adwords_grouping,
            google_shopping_adwords_labels, google_shopping_condition, google_shopping_custom_product, google_shopping_custion_label0, google_shopping_custion_label1, google_shopping_custion_label2, google_shopping_custion_label3, google_shopping_custion_label4, variant_image, variant_weight_unit, variant_tax_code, cost_per_item, revise, revise_last_time)
            values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 0, 0)
            '''
            cursor.execute(sql, row)
        db.get_db().commit()
        csv_read.close()
        cursor.close()
