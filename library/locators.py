from selenium.webdriver.common.by import By

class LoginPageLocators():
    
    USERNAME = (By.NAME, 'email')
    PASSWORD = (By.NAME, 'password')
    SUBMIT_BUTTON = (By.XPATH, '//*[@id="root"]/div/div/main/div/form/button/span[1]')
    LOGOUT = (By.XPATH, '//*[@id="root"]/div/div/div[1]/div[2]/div/div/div[3]/div/a/div')
    
class NavigationPageLocators():

    NAVIGATION_BUTTON = (By.XPATH, '//*[@id="root"]/div/div/div[2]/header/div/div[1]/button')
    DASHBOARD = (By.XPATH, '//*[@id="root"]/div/div/div[1]/div[2]/div/div/div[3]/div/ul[1]/a[1]')
    MAPS = (By.XPATH, '//*[@id="root"]/div/div/div[1]/div[2]/div/div/div[3]/div/ul[1]/a[2]')
    RBAC_DOWN = (By.XPATH, '//*[@id="root"]/div/div/div[1]/div[2]/div/div/div[3]/div/ul[3]/div')
    ADMIN_DOWN = (By.XPATH, '//*[@id="root"]/div/div/div[1]/div[2]/div/div/div[3]/div/ul[4]/div')
    ALARM_DOWN = (By.XPATH, '//*[@id="root"]/div/div/div[1]/div[2]/div/div/div[3]/div/ul[5]/div')

    PERMISSION = (By.XPATH, '//*[@id="root"]/div/div/div[1]/div[2]/div/div/div[3]/div/ul[3]/div[2]/div/div/div/a[1]/li/div[1]')
    ROLE = (By.XPATH, '//*[@id="root"]/div/div/div[1]/div[2]/div/div/div[3]/div/ul[3]/div[2]/div/div/div/a[2]/li/div[1]')
    USERS = (By.XPATH, '//*[@id="root"]/div/div/div[1]/div[2]/div/div/div[3]/div/ul[3]/div[2]/div/div/div/a[3]/li/div[1]')

    COMPANY = (By.XPATH, '//*[@id="root"]/div/div/div[1]/div[2]/div/div/div[3]/div/ul[4]/div[2]/div/div/div/a[1]/li/div[1]')
    VESSEL = (By.XPATH, '//*[@id="root"]/div/div/div[1]/div[2]/div/div/div[3]/div/ul[4]/div[2]/div/div/div/a[2]/li/div[1]')
    ALARM_VALUES = (By.XPATH, '//*[@id="root"]/div/div/div[1]/div[2]/div/div/div[3]/div/ul[5]/div[2]/div/div/div[2]/a[3]/li/div[1]')
    ALARM_CONDITIONS = (By.XPATH, '//*[@id="root"]/div/div/div[1]/div[2]/div/div/div[3]/div/ul[5]/div[2]/div/div/div[2]/a[2]/li/div[1]')
    ALARM_TRIGGERS = (By.XPATH, '//*[@id="root"]/div/div/div[1]/div[2]/div/div/div[3]/div/ul[5]/div[2]/div/div/div[2]/a[1]/li/div[1]')
    ADMIN_DEVICES = (By.XPATH, '//*[@id="root"]/div/div/div[1]/div[2]/div/div/div[3]/div/ul[4]/div[2]/div/div/div/a[3]/li/div[1]')
    SUBCATEGORY = (By.XPATH, '//*[@id="root"]/div/div/div[1]/div[2]/div/div/div[3]/div/ul[4]/div[2]/div/div/div/a[4]/li/div[1]')

class DashboardLocators():

    ANNOUNCEMENTS_TABLE = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div/div[2]/div')

class MapsLocators():

    MAPS_BREADCRUMB = '//*[@id="root"]/div/div/div[2]/header/div/div[3]/div/div/nav/ol/li[3]/p'

class PermissionLocators():

    PERMISSION_BREADCRUMB = '//*[@id="root"]/div/div/div[2]/header/div/div[3]/div/div/nav/ol/li[3]/p'
    
    CREATE_PERMISSION_PAGE = '//*[@id="form-dialog-title"]/h2'
    UPDATE_PERMISSION_PAGE = '//*[@id="form-dialog-title"]/h2'

    INPUT_PERMISSION_NAME = (By.XPATH, '//*[@id="name"]')
    INPUT_PERMISSION_DETAILS = (By.XPATH, '//*[@id="details"]')

    CREATE_SUBMIT_BTN = (By.XPATH, '/html/body/div[3]/div[3]/div/div[3]/button[2]')
    UPDATE_SUBMIT_BTN = (By.XPATH, '/html/body/div[3]/div[3]/div/div[3]/button[2]')

    CREATE_PERMISSION_BTN = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/button[2]')
    DELETE_PERMISSION_BTN = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/button[1]')
    UPDATE_PERMISSION_BTN = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/button[3]') 

    NEXT_PAGINATION = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[3]/button[2]')
    TOTAL_ITEMS = (By.XPATH,  '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/p[2]')

    BEFORE_XPATH_KEY = '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[1]/table/tbody/tr['
    AFTER_XPATH_KEY = "]/td[2]"
    AFTER_XPATH_CHECKBOX = ']/td[1]/span/span[1]/input'

    ITEM_KEY = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[1]/table/tbody/tr/td[2]')
    ITEM_BOX = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[1]/table/tbody/tr/td[1]/span/span[1]/input')


class RoleLocators():

    ROLE_BREADCRUMB = '//*[@id="root"]/div/div/div[2]/header/div/div[3]/div/div/nav/ol/li[3]/p'

    CREATE_ROLE_PAGE = '//*[@id="form-dialog-title"]/h2'
    UPDATE_ROLE_PAGE = '//*[@id="form-dialog-title"]/h2'

    INPUT_ROLE_NAME = (By.XPATH, '//*[@id="roleName"]')
    INPUT_ROLE_DETAILS = (By.XPATH, '//*[@id="roleDetails"]')
    SELECT_PERMISSIONS = (By.XPATH, '//*[@id="select-selectedPermissions"]')

    CREATE_SUBMIT_BTN = (By.XPATH, '/html/body/div[3]/div[3]/div/div[3]/button[2]')
    UPDATE_SUBMIT_BTN = (By.XPATH, '/html/body/div[3]/div[3]/div/div[3]/button[2]')

    CREATE_ROLE_BTN = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/button[2]')
    DELETE_ROLE_BTN = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/button[1]')
    UPDATE_ROLE_BTN = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/button[3]')

    NEXT_PAGINATION = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[3]/button[2]')
    TOTAL_ITEMS = (By.XPATH,  '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/p[2]')

    BEFORE_XPATH_KEY = '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[1]/table/tbody/tr['
    AFTER_XPATH_KEY = ']/td[2]'
    AFTER_XPATH_CHECKBOX = ']/td[1]/span/span[1]/input'

    SELECT_PERMISSION_UL = (By.XPATH,'//*[@id="menu-selectedPermissions"]/div[3]/ul')
    BEFORE_PERMISSION_PATH = '//*[@id="menu-selectedPermissions"]/div[3]/ul/li['
    AFTER_PERMISSION_PATH = ']/span[1]/span[1]/input'
    AFTER_PERMISSION_KEY = ']/div/span'
    TARGET_UL = (By.XPATH, '//*[@id="menu-selectedPermissions"]/div[2]/ul/li[11]/span[1]/span[1]/input')

    ITEM_KEY = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[1]/table/tbody/tr/td[2]')
    ITEM_BOX = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[1]/table/tbody/tr/td[1]/span/span[1]/input')


class CompanyLocators():

    COMPANY_BREADCRUMB = (By.XPATH, '//*[@id="root"]/div/div/div[2]/header/div/div[3]/div/div/nav/ol/li[3]/p')

    CREATE_COMPANY_PAGE = (By.XPATH, '//*[@id="form-dialog-title"]/h2')
    UPDATE_COMPANY_PAGE = (By.XPATH, '//*[@id="form-dialog-title"]/h2')

    INPUT_COMPANY_NAME = (By.XPATH, '//*[@id="companyName"]')
    INPUT_COMPANY_VESSEL = (By.XPATH, '//*[@id="companyVessel"]')
    SELECT_COMPANY_VESSEL = '//*[@id="companyVessel"]'

    CREATE_SUBMIT_BTN = (By.XPATH, '/html/body/div[3]/div[3]/div/div[3]/button[2]')
    UPDATE_SUBMIT_BTN = (By.XPATH, '/html/body/div[3]/div[3]/div/div[3]/button[2]')

    CREATE_COMPANY_BTN = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/button[2]')
    DELETE_COMPANY_BTN = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/button[1]')
    UPDATE_COMPANY_BTN = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/button[3]')

    NEXT_PAGINATION = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[3]/button[2]')
    TOTAL_ITEMS = (By.XPATH,  '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/p[2]')

    BEFORE_XPATH_KEY = '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[1]/table/tbody/tr['
    AFTER_XPATH_KEY = ']/td[2]'
    AFTER_XPATH_CHECKBOX = ']/td[1]/span/span[1]/input'

    ITEM_KEY = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[1]/table/tbody/tr/td[2]')
    ITEM_BOX = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[1]/table/tbody/tr/td[1]/span/span[1]/input')

class AlarmValuesLocators():

    ALARM_VALUES_BREADCRUMB = '//*[@id="root"]/div/div/div[2]/header/div/div[3]/div/div/nav/ol/li[7]/p'

    CREATE_ALARM_VALUE_PAGE = '//*[@id="form-dialog-title"]/h2'
    UPDATE_ALARM_VALUE_PAGE = '//*[@id="form-dialog-title"]/h2'

    INPUT_ALARM_VALUE_NAME = (By.XPATH, '//*[@id="alarmValueName"]')

    INPUT_ALARM_VALUE_VESSEL = (By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/form/div[2]/div/div/div/div/div[1]/p')
    INPUT_ALARM_VALUE_VESSEL_DELETE = (By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/form/div[2]/div/div/div/div/div[2]/div[1]')
    INPUT_ALARM_VALUE_VESSEL_AUTO = (By.XPATH, '//*[@id="vesselName"]')

    INPUT_ALARM_VALUE_DEVICE = (By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/form/div[3]/div/div/div/div/div[1]/p')
    INPUT_ALARM_VALUE_DEVICE_DELETE = (By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/form/div[3]/div/div/div/div/div[2]/div[1]')
    INPUT_ALARM_VALUE_DEVICE_AUTO = (By.XPATH, '//*[@id="deviceName"]')

    INPUT_ALARM_VALUE_DEVICE_TYPE = (By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/form/div[4]/div/div/div/div/div[1]/p')
    INPUT_ALARM_VALUE_DEVICE_TYPE_DELETE = (By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/form/div[4]/div/div/div/div/div[2]/div[1]')
    INPUT_ALARM_VALUE_DEVICE_TYPE_AUTO = (By.XPATH, '//*[@id="deviceType"]')

    INPUT_ALARM_VALUE_MODULE = (By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/form/div[5]/div/div/div/div/div[1]/p')
    INPUT_ALARM_VALUE_MODULE_DELETE = (By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/form/div[5]/div/div/div/div/div[2]/div[1]')
    INPUT_ALARM_VALUE_MODULE_AUTO = (By.XPATH, '//*[@id="moduleName"]')

    INPUT_ALARM_VALUE_OPTION = (By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/form/div[6]/div/div/div/div/div[1]/p')
    INPUT_ALARM_VALUE_OPTION_DELETE = (By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/form/div[6]/div/div/div/div/div[2]/div[1]')
    INPUT_ALARM_VALUE_OPTION_AUTO = (By.XPATH, '//*[@id="optionName"]')

    INPUT_ALARM_VALUE = (By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/form/div[7]/div/div/div/div/div[1]/p')
    INPUT_ALARM_VALUE_DELETE = (By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/form/div[7]/div/div/div/div/div[2]/div[1]')
    INPUT_ALARM_VALUE_AUTO = (By.XPATH, '//*[@id="valueName"]')

    # CREATE_SUBMIT_BTN = (By.XPATH, '/html/body/div[4]/div[3]/div/div[3]/button[2]')
    CREATE_SUBMIT_BTN = (By.XPATH, '/html/body/div[3]/div[3]/div/div[3]/button[2]')
    UPDATE_SUBMIT_BTN = (By.XPATH, '/html/body/div[3]/div[3]/div/div[3]/button[2]')

    CREATE_ALARM_VALUE_BTN = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/button[1]')
    UPDATE_ALARM_VALUE_BTN = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/button[2]')
    DELETE_ALARM_VALUE_BTN = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/button[3]')

    NEXT_PAGINATION = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[3]/button[2]')
    TOTAL_ITEMS = (By.XPATH,  '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/p[2]')

    ITEM_KEY = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[1]/table/tbody/tr/td[2]')
    ITEM_BOX = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[1]/table/tbody/tr/td[1]/span/span[1]/input')
    
    BEFORE_XPATH_KEY = '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[1]/table/tbody/tr['
    AFTER_XPATH_KEY = ']/td[2]'
    AFTER_XPATH_CHECKBOX = ']/td[1]/span/span[1]/input'

class AlarmConditionsLocators():

    ALARM_CONDITIONS_BREADCRUMB = '//*[@id="root"]/div/div/div[2]/header/div/div[3]/div/div/nav/ol/li[7]/p'

    CREATE_ALARM_CONDITION_PAGE = '//*[@id="form-dialog-title"]/h2'
    UPDATE_ALARM_CONDITION_PAGE = '//*[@id="form-dialog-title"]/h2'

    INPUT_ALARM_COMMENT = (By.XPATH, '//*[@id="alarmConditionComment"]')

    INPUT_ALARM_OPERATOR = (By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/form/div[2]/div/div/div/div/div[1]/p')
    INPUT_ALARM_OPERATOR_DELETE = (By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/form/div[2]/div/div/div/div/div[2]/div[1]')
    INPUT_ALARM_OPERATOR_AUTO = (By.XPATH, '//*[@id="conditionOperator"]')

    INPUT_ALARM_PARAM1 = (By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/form/div[3]/div/div/div/div/div[1]/p')
    INPUT_ALARM_PARAM2 = (By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/form/div[4]/div/div/div/div/div[1]/p')
    INPUT_ALARM_PARAM3 = (By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/form/div[5]/div/div/div/div/div[1]/p')

    INPUT_ALARM_PARAM1_DEL = (By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/form/div[3]/div/div/div/div/div[2]/div[1]')
    INPUT_ALARM_PARAM2_DEL = (By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/form/div[4]/div/div/div/div/div[2]/div[1]')
    INPUT_ALARM_PARAM3_DEL = (By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/form/div[5]/div/div/div/div/div[2]/div[1]')

    INPUT_PARAM1_AUTO = (By.XPATH, '//*[@id="conditionParameter1"]')
    INPUT_PARAM2_AUTO = (By.XPATH, '//*[@id="conditionParameter2"]')
    INPUT_PARAM3_AUTO = (By.XPATH, '//*[@id="conditionParameter3"]')

    CREATE_SUBMIT_BTN = (By.XPATH, '/html/body/div[3]/div[3]/div/div[3]/button[2]')
    UPDATE_SUBMIT_BTN = (By.XPATH, '/html/body/div[3]/div[3]/div/div[3]/button[2]')

    CREATE_ALARM_CONDITION_BTN = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/button[1]')
    UPDATE_ALARM_CONDITION_BTN = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/button[2]')
    DELETE_ALARM_CONDITION_BTN = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/button[3]')
    
    NEXT_PAGINATION = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[3]/button[2]')
    TOTAL_ITEMS = (By.XPATH,  '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/p[2]')

    BEFORE_XPATH_KEY = '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[1]/table/tbody/tr['
    AFTER_XPATH_KEY = ']/td[2]'
    AFTER_XPATH_CHECKBOX = ']/td[1]/span/span[1]/input'

    ITEM_KEY = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[1]/table/tbody/tr/td[2]')
    ITEM_BOX = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[1]/table/tbody/tr/td[1]/span/span[1]/input')
    
class AlarmTriggersLocators():

    ALARM_TRIGGERS_BREADCRUMB = '//*[@id="root"]/div/div/div[2]/header/div/div[3]/div/div/nav/ol/li[7]/p'

    CREATE_ALARM_TRIGGER_PAGE = '//*[@id="form-dialog-title"]/h2'
    UPDATE_ALARM_TRIGGER_PAGE = '//*[@id="form-dialog-title"]/h2'

    INPUT_ALARM_TRIGGER_LABEL = (By.XPATH, '//*[@id="alarmTriggerLabel"]')
    INPUT_ALARM_TRIGGER_DESC = (By.XPATH, '//*[@id="alarmTriggerDescription"]')
    INPUT_ALARM_ENABLED = (By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/form/div[3]/label/span[1]/span[1]/span[1]/input')
    INPUT_ALARM_ACKNOWLEDGE = (By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/form/div[4]/label/span[1]/span[1]/span[1]/input')
    
    INPUT_ALARM_TYPE = (By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/form/div[5]/div/div/div/div/div[1]/p')
    INPUT_ALARM_TYPE_DELETE = (By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/form/div[5]/div/div/div/div/div[2]/div[1]')
    
    INPUT_ALARM_CONDITION = (By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/form/div[6]/div/div/div/div/div[1]/p')
    INPUT_ALARM_CONDITION_DELETE = (By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/form/div[6]/div/div/div/div/div[2]/div[1]')
    
    INPUT_ALARM_TYPE_AUTO = (By.XPATH, '//*[@id="alarmTypes"]')
    INPUT_ALARM_CONDITION_AUTO = (By.XPATH, '//*[@id="alarmConditions"]')

    CREATE_SUBMIT_BTN = (By.XPATH, '/html/body/div[3]/div[3]/div/div[3]/button[2]')
    UPDATE_SUBMIT_BTN = (By.XPATH, '/html/body/div[3]/div[3]/div/div[3]/button[2]')

    CREATE_ALARM_TRIGGER_BTN = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/button[1]')
    UPDATE_ALARM_TRIGGER_BTN = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/button[2]')
    DELETE_ALARM_TRIGGER_BTN = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/button[3]')

    NEXT_PAGINATION = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[3]/button[2]')
    TOTAL_ITEMS = (By.XPATH,  '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/p[2]')

    BEFORE_XPATH_KEY = '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[1]/table/tbody/tr['
    AFTER_XPATH_KEY = ']/td[4]'
    AFTER_XPATH_CHECKBOX = ']/td[1]/span/span[1]/input'

    ITEM_KEY = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[1]/table/tbody/tr/td[4]')
    ITEM_BOX = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[1]/table/tbody/tr/td[1]/span/span[1]/input')

class UsersLocators():

    USERS_BREADCRUMB = '//*[@id="root"]/div/div/div[2]/header/div/div[3]/div/div/nav/ol/li[3]/p'
    INVITE_USER = '//*[@id="form-dialog-title"]/h2'
    UPDATE_USER = '//*[@id="form-dialog-title"]/h2'

    DELETE_BTN = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/button[1]')
    DISABLE_BTN = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/button[2]')
    ENABLE_BTN = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/button[3]')
    INVITE_BTN = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/button[4]')
    EDIT_BTN = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/button[5]')
    RESEND_INVITE_BTN = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/button[6]')

    UPDATE_USER_BTN = (By.XPATH, '/html/body/div[3]/div[3]/div/div[3]/button[2]')
    SEND_INVITE_BTN = (By.XPATH, '/html/body/div[3]/div[3]/div/div[3]/button[2]')

    NEXT_PAGINATION = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[3]/button[2]')
    TOTAL_ITEMS = (By.XPATH,  '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/p[2]')

    BEFORE_XPATH_KEY = '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[1]/table/tbody/tr['
    AFTER_XPATH_KEY = ']/td[4]'
    AFTER_XPATH_CHECKBOX = ']/td[1]/span/span[1]/input'

    INPUT_FIRST_NAME = (By.XPATH, '//*[@id="userFName"]')
    INPUT_MIDDLE_NAME = (By.XPATH, '//*[@id="userMName"]')
    INPUT_LAST_NAME = (By.XPATH, '//*[@id="userLName"]')
    INPUT_EMAIL = (By.XPATH, '//*[@id="userEmail"]')

    INPUT_COMPANY = (By.XPATH, '//*[@id="userCompany"]')
    SELECT_COMPANY = '//*[@id="userCompany"]'

    INPUT_ROLE = (By.XPATH, '//*[@id="userRole"]')
    SELECT_ROLE = '//*[@id="userRole"]'
    VESSEL_TABLE = (By.XPATH, '/html/body/div[3]/div[2]/div[2]/form/table/thead/tr/th[1]')

    BEFORE_XPATH_TABLE = '/html/body/div[3]/div[2]/div[2]/form/table/tbody/tr['
    AFTER_XPATH_TABLE = ']/td[1]'
    AFTER_XPATH_TOGGLE = ']/td[2]/label/span[1]/span[1]/span[1]/input'

    MAPS_BREADCRUMB = (By.XPATH, '//*[@id="root"]/div/div/div[2]/header/div/div[3]/div/div/nav/ol/li[3]/p')

    ITEM_KEY = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[1]/table/tbody/tr/td[2]')
    ITEM_BOX = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[1]/table/tbody/tr/td[1]/span/span[1]/input')

    CONFIRM_DISABLE = (By.XPATH, '/html/body/div[3]/div[3]/div/div[3]/button[1]')
    CONFIRM_ENABLE = (By.XPATH, '/html/body/div[3]/div[3]/div/div[3]/button[1]')
    CONFIRM_DELETE = (By.XPATH, '/html/body/div[3]/div[3]/div/div[3]/button[1]')
    CONFIRM_RESEND = (By.XPATH, '/html/body/div[3]/div[3]/div/div[3]/button[1]')

class CommonLocators():
    
    MESSAGE_BAR = (By.XPATH, '//*[@id="client-snackbar"]')


class VesselLocators():

    VESSEL_BREADCRUMB = '//*[@id="root"]/div/div/div[2]/header/div/div[3]/div/div/nav/ol/li[3]/p'

    CREATE_VESSEL_PAGE = '//*[@id="form-dialog-title"]/h2'

    INPUT_VESSEL_NAME = (By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/div/div[1]/div/div/div/input')
    INPUT_VESSEL_IMO = (By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/div/div[2]/div/div/div/input')

    CREATE_SUBMIT_BTN = (By.XPATH, '/html/body/div[3]/div[3]/div/div[3]/button[2]')

    CREATE_VESSEL_BTN = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/button[1]')
    DELETE_VESSEL_BTN = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/button[2]')


    NEXT_PAGINATION = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[3]/button[2]')
    TOTAL_ITEMS = (By.XPATH,  '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/p[2]')

    BEFORE_XPATH_KEY = '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[1]/table/tbody/tr['
    AFTER_XPATH_KEY = ']/td[3]'
    AFTER_XPATH_CHECKBOX = ']/td[1]/span/span[1]/input'

    ITEM_KEY = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[1]/table/tbody/tr/td[3]')
    ITEM_BOX = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[1]/table/tbody/tr/td[1]/span/span[1]/input')

    CONFIRM_DELETE = (By.XPATH, '/html/body/div[3]/div[3]/div/div[3]/button[1]')

class SubCategoryLocators():

    SUBCATEGORY_BREADCRUMB = '//*[@id="root"]/div/div/div[2]/header/div/div[3]/div/div/nav/ol/li[3]/p'

    CREATE_SUBCATEGORY_PAGE = '//*[@id="form-dialog-title"]/h2'
    UPDATE_SUBCATEGORY_PAGE = '//*[@id="form-dialog-title"]/h2'

    INPUT_SUBCATEGORY_NAME = (By.XPATH, '//*[@id="subCategoryName"]')
    SELECT_OPTION = (By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/form/div[2]/div/div/div[1]/div[1]')
    SELECT_OPTION_AUTO = (By.XPATH, '//*[@id="subCategoryOptions"]')
    SELECT_OPTION_DELETE = (By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/form/div[2]/div/div/div[2]/div[1]')

    CREATE_SUBMIT_BTN = (By.XPATH, '/html/body/div[3]/div[3]/div/div[3]/button[2]')
    UPDATE_SUBMIT_BTN = (By.XPATH, '/html/body/div[3]/div[3]/div/div[3]/button[2]')

    UPDATE_SUBCATEGORY_BTN = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/button[3]')
    CREATE_SUBCATEGORY_BTN = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/button[2]')
    DELETE_SUBCATEORY_BTN = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/button[1]')

    NEXT_PAGINATION = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/div[3]/button[2]')
    TOTAL_ITEMS = (By.XPATH,  '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/p[2]')

    BEFORE_XPATH_KEY = '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[1]/table/tbody/tr['
    AFTER_XPATH_KEY = ']/td[2]'
    AFTER_XPATH_CHECKBOX = ']/td[1]/span/span[1]/input'

    ITEM_KEY = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[1]/table/tbody/tr/td[2]')
    ITEM_BOX = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[1]/table/tbody/tr/td[1]/span/span[1]/input')

class DeviceImageLocators():

    DEVICE_IMAGE_BREADCRUMB = '//*[@id="root"]/div/div/div[2]/header/div/div[3]/div/div/nav/ol/li[3]/p'
    UPLOAD_DEVICE_IMAGE = '//*[@id="form-dialog-title"]/h2'

    UPLOAD_DEVICE_IMAGE_BUTTON = (By.XPATH, '/html/body/div[4]/div[3]/div/div[2]/div/div/div/div[2]/div/button')
    DELETE_DEVICE_IMAGE = (By.XPATH, '/html/body/div[4]/div[3]/div/div[3]/button[1]')
    BEFORE_TABLE_KEY = '//*[@id="panel'
    AFTER_TABLE_KEY = 'bh-content"]/div/table'

    ROW_BEFORE_KEY = '/tr['
    ROW_DEVICE_AFTER_KEY = ']/td[1]'
    ROW_IMAGE_AFTER_KEY = ']/td[2]'
    ROW_ICON_UPLOAD_KEY = ']/td[3]/button'
    # DELETE_UPLOAD = ']/td[2]/svg/path'
    DELETE_UPLOAD = "/*[name()='svg']/*[name()='path']"
    UPLOAD_IMG = (By.XPATH, '//input[@type="file"]')

    TEST = (By.XPATH, '//*[@id="panelALP WINGERbh-content"]/div/table/tr[1]/td[1]')
    TEST2 = (By.XPATH, '//*[@id="panelALP Wingerbh-content"]/div/table/tr[2]/td[2]/svg/path')
