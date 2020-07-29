import allure


#
# class Severity(str, Enum):
#     BLOCKER = 'blocker'
#     CRITICAL = 'critical'
#     NORMAL = 'normal'
#     MINOR = 'minor'
#     TRIVIAL = 'trivial'

@allure.severity(allure.severity_level.TRIVIAL)
def test_with_trivial_severity():
    print("severity level")


@allure.severity(allure.severity_level.CRITICAL)
def test_with_critical_severity():
    print("severity level")