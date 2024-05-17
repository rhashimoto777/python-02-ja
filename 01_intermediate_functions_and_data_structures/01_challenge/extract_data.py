import re

def extract_data(text):
    patten = r"[a-zA-Z0-9]+:[a-zA-Z0-9]+"
    return re.findall(patten, text)

def better_extract_data(text):
    patten = r"([a-zA-Z0-9]+):([a-zA-Z0-9]+)"
    result = re.findall(patten, text)
    return result




test_input = "The subject has Age:25 and Height:180cm.Other details are not relevant.Weight:70kg was noted."
print(extract_data(test_input))
print(better_extract_data(test_input))
