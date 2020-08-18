import allure

'''
这个在这里无法运行。
可以运行的在WebUIAuto里面。还可以在一个case的所有setup, teardown都会把相应的attachement加到里面去。
'''


def test_multiple_attachments():
    # allure.attach.file('./data/totally_open_source_kitten.png', attachment_type=allure.attachment_type.PNG)
    allure.attach('<head></head><body> a page </body>', 'Attach with HTML type', allure.attachment_type.HTML)
