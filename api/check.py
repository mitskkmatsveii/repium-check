def handler(request):
    key = request.args.get("key", "")
    
    VALID_KEYS = [
        "PREM-A1B2-C3D4",
        "PREM-X9Y8-Z7W6",
    ]
    
    if key in VALID_KEYS:
        return "valid"
    else:
        return "invalid"
