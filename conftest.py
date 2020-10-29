import pytest
from pytest_jsonreport.plugin import JSONReport

def pytest_json_modifyreport(json_report):
    """Modifies the report that comes out of --json-report 
    """
    # this report is not a debug tool- we only need to know IF there were warnings
    num_warnings = len(json_report['warnings']) if 'warnings' in json_report else 0
    # the root will vary depending on the device it is run on. We only care if it's run in the group2 directory.
    root = json_report['root'].split("\\")[-1]
    summary_keys = list(json_report['summary'].keys())

    # test is considered a success IF:
        # there are no warnings generated
        # the tests were run at the top-level "group2" directory
        # the summary only has 'passed', 'total', and 'collected' fields. NO XFAIL, XPASS, or FAIL.
    success = True if num_warnings == 0 and root == 'group2' and summary_keys == ['passed', 'total', 'collected'] else False
    
    json_report['success'] = success
    json_report['root'] = root
    json_report['warnings'] = num_warnings

    # not useful information for us
    to_delete = ['environment', 'tests', 'collectors']
    for item in to_delete:
        del json_report[item]
