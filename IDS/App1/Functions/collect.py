from App1.models import IdentityInfo

def save_id_data(data_dict):
    IdentityInfo.objects.create(
        name=data_dict.get("Name"),
        id_type=data_dict.get("Document Type"),
        id_number=data_dict.get("Aadhaar Number") or data_dict.get("PAN Number") or data_dict.get("Voter ID Number") or data_dict.get("DL Number"),
        address=data_dict.get("Address"),
        mobile=data_dict.get("Mobile"),
        pincode=data_dict.get("Pincode")
    )
