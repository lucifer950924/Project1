from behave import given, when, then
from Pages.Automation1 import Automation1_Pages

@given('Hit the URL')
def hit_url(context):
    context.driver = Automation1_Pages.Automation1Steps()
    context.driver.HitURL()

@then('Automate the page')
def Automate_actions(context):
    context.driver.fill_text_by_id_with_Wait('name',context.driver.data['name'])
    context.driver.fill_text_in_fields_by_id('email',context.driver.data['email'])
    context.driver.fill_text_in_fields_by_id('phone',context.driver.data['phone'])
    context.driver.fill_text_by_text('Address:',context.driver.data['address'])
    context.driver.select_option_by_value('Colors:','Yellow'.lower())

@then('Close the page')
def close_broswer(context):
    context.driver.quit_browser()



        