# blind-xss-detector

This code defines a test_blind_xss function that takes a URL and a payload as its parameters. The function makes a GET request to the specified URL with the payload passed as a parameter in the query string. It then uses the BeautifulSoup library to parse the HTML content of the response and the re library to search for the payload in the response text.

If the payload is found in the response text, the function prints "Blind XSS test successful. Payload executed.". If the payload is not found, the function prints "Blind XSS test failed. Payload not executed.". If the response status code is not 200, the function prints "Blind XSS test failed. Response code:", response.status_code.
The main function handles the input of the user and calls the test_blind_xss function.

Please use this script responsibly and only on systems that you have permission to test.
