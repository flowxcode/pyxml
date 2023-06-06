import xml.etree.ElementTree as ET

MSTEST_NAMESPACE = 'http://microsoft.com/schemas/VisualStudio/TeamTest/2010'

### parse the XML log file given from the Testbench ###
# Arguments: 
# 		- Path to the XML file
# Return:
#		- array of: [[Test Name, Test Outcome, error description], number of tests, number of fails, number of skipped tests]
def parse_xml_result(path_to_xml):
    root = ET.parse(path_to_xml).getroot()
    test_result = []
    FirstIteration = 0
    TestOutcome = ""
    cntr_total = 0
    cntr_failed = 0
    cntr_skipped = 0

    results_node = root.find('{%s}Results' % MSTEST_NAMESPACE)
    results = results_node.findall('{%s}UnitTestResult' % MSTEST_NAMESPACE)

    for result in results:
        error_descr = ""
        TestName = result.attrib.get('testName')
        TestOutcome = result.attrib.get('outcome')
        if TestOutcome == "Failed":
            error_descr = result.find(
                '{%s}Output/{%s}ErrorInfo/{%s}Message' % (MSTEST_NAMESPACE, MSTEST_NAMESPACE, MSTEST_NAMESPACE)).text
            cntr_failed = cntr_failed + 1
        if TestOutcome == "Skipped" or TestOutcome == "NotExecuted":
            error_descr = result.find(
                '{%s}Output/{%s}ErrorInfo/{%s}Message' % (MSTEST_NAMESPACE, MSTEST_NAMESPACE, MSTEST_NAMESPACE)).text
            cntr_skipped = cntr_skipped + 1

        test_result.append([TestName, TestOutcome, error_descr])
        cntr_total = cntr_total + 1

    return [test_result, cntr_total, cntr_failed, cntr_skipped]

print("start v2")

# 3. Parse XML file
xml_file_path = "SxTestResult.trx"
print("Parse log file: " + xml_file_path)
XMLParsed = parse_xml_result(xml_file_path)
TestResultParsed = XMLParsed[0]
TestResultParsed.sort()
TotalTests = XMLParsed[1]
FailedTests = XMLParsed[2]
SkippedTests = XMLParsed[3]

print("end v2")