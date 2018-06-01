# jmeter
Jmeter for Performance and stress tests

Tools used: apache-jmeter-4.0

Test Script Description:
○	API Load Test for HTTP GET request without failure case
■	This test will send 6000 GET requests in time of 1 second without getting any errors and generating visualization graphs
○	API Load Test for HTTP POST request without failure case
■	This test will send 500 POST requests in time of 1 second without getting any errors and generating visualization graphs
○	API Load Test for HTTP GET request in failure case
■	This test will send 10000 GET requests in time of 1 second, in this case we are getting errors and generating visualization graphs
○	API Load Test for HTTP POST request in failure case
■	This test will send 500 POST requests in time of 1 second in this case we are getting errors and generating visualization graphs
○	API Test Case for HTTP GET request using timers
■	This test is expecting GET request response in 1 millisecond
○	API Test Case for HTTP POST request using timers
■	This test is expecting POST request response in 1 millisecond