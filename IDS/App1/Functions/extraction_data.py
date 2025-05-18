import re

def extract_id_info(text):
    info = {}

    # Aadhaar (12-digit number, often grouped as XXXX XXXX XXXX)
    aadhaar_match = re.search(r'\b(\d{4}\s\d{4}\s\d{4})\b', text)
    if aadhaar_match:
        info['Document Type'] = 'Aadhaar'
        info['Aadhaar Number'] = aadhaar_match.group(1)

    # PAN Card (5 letters + 4 digits + 1 letter)
    pan_match = re.search(r'\b([A-Z]{5}[0-9]{4}[A-Z])\b', text)
    if pan_match:
        info['Document Type'] = 'PAN'
        info['PAN Number'] = pan_match.group(1)

    # Voter ID (Usually 3 letters + 7 digits like ABC1234567)
    voter_id_match = re.search(r'\b([A-Z]{3}\d{7})\b', text)
    if voter_id_match:
        info['Document Type'] = 'Voter ID'
        info['Voter ID Number'] = voter_id_match.group(1)

    # Driving License (DL) formats like MH14 20110012345 or MH1420110012345
    dl_match = re.search(r'\b([A-Z]{2}\d{2}\s?\d{11,12})\b', text)
    if dl_match:
        info['Document Type'] = 'Driving License'
        info['DL Number'] = dl_match.group(1)

    # Name (Assuming "Name: XYZ" or appearing near keywords)
    name_match = re.search(r'(?:Name|Father\'s Name|S/O)\s*[:\-]?\s*([A-Z][a-zA-Z\s]+)', text)
    if name_match:
        info['Name'] = name_match.group(1).strip()

    # Mobile Number
    mobile_match = re.search(r'\b(\+91[-\s]?)?[6-9]\d{9}\b', text)
    if mobile_match:
        info['Mobile'] = mobile_match.group(0)

    # Pincode (6-digit Indian postal code)
    pincode_match = re.search(r'\b\d{6}\b', text)
    if pincode_match:
        info['Pincode'] = pincode_match.group(0)

    # Address: very heuristic (could be improved using NLP)
    address_match = re.search(r'Address\s*[:\-]?\s*(.*?)(?:\n|$)', text, re.IGNORECASE)
    if address_match:
        info['Address'] = address_match.group(1).strip()

    return info
