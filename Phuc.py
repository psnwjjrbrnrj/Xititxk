import plistlib, base64

input_file = "profile.mobileconfig"
output_file = "certificate.crt"

with open(input_file, "rb") as f:
    plist = plistlib.load(f)

def extract_cert(payloads, index=1):
    for payload in payloads:
        if payload.get("PayloadType") in ["com.apple.security.root", "com.apple.security.pem"]:
            cert_data = payload.get("PayloadContent")
            if cert_data:
                fname = f"certificate_{index}.crt" if index > 1 else output_file
                with open(fname, "wb") as f:
                    f.write(base64.b64decode(cert_data))
                print(f"✅ Xuất chứng chỉ: {fname}")
                index += 1
        if "PayloadContent" in payload and isinstance(payload["PayloadContent"], list):
            index = extract_cert(payload["PayloadContent"], index)
    return index

if "PayloadContent" in plist:
    extract_cert(plist["PayloadContent"])
else:
    print("❌ Không tìm thấy chứng chỉ trong file.")
