from behave import given, when, then
from Pages.Automation1 import Automation1_Pages

@given('Hit the URL')
def hit_url(context):
    context.logger.info('Hitting the URL')
    context.driver = Automation1_Pages.Automation1Pages()
    context.driver.HitURL()
    context.logger.info('URL hit successfully')

@then('Automate the page')
def Automate_actions(context):
    context.logger.info('Automating the page')
    context.logger.info('Filling the form fields')
    context.driver.fill_text_by_id_with_Wait('name',context.driver.data['name'])
    context.logger.info('Filling the form fields name with id and wait successful')
    context.driver.fill_text_in_fields_by_id('email',context.driver.data['email'])
    context.logger.info('Filling the form fields email with id and wait successful')
    context.driver.fill_text_in_fields_by_id('phone',context.driver.data['phone'])
    context.logger.info('Filling the form fields phone with id and wait successful')
    context.driver.fill_text_by_text('Address:',context.driver.data['address'])
    context.logger.info('Filling the form fields address with text and wait successful')
    context.driver.select_option_by_value('Colors:','Yellow'.lower())
    context.logger.info('Filling the form fields colors with id and wait successful')

@then('Close the page')
def close_broswer(context):
    context.logger.info('Closing the browser')
    context.driver.quit_browser()

@then('Upload the File')
def upload_file(context):
    context.logger.info('Uploading the file')
    context.driver.upload_file_byinput(context.driver.data['uploadFilepath'])
    context.logger.info('File uploaded successfully')
    context.logger.info('Performing mouse hover and drag and drop actions')
    context.driver.hover_element('Point Me')
    context.logger.info('Mouse hover action performed successfully')
    context.logger.info('Performing drag and drop action')
    context.driver.drag_element('Drag me to my target','Drop here')
    context.logger.info('Drag and drop action performed successfully')

        