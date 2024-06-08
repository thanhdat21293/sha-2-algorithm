import hashlib
import uuid
import pandas as pd
import json


# legalids = []
# for i in range(1, 200000):
#     legalids.append({ 'legalid': uuid.uuid4().hex })

# # f = open('ids.json');
# # legalids = json.load(f)

# for i in range(len(legalids)):
#     legalidEncode = legalids[i]['legalid'].encode()
#     legalidHash = hashlib.sha256(legalidEncode)
#     legalids[i]['hash1'] = legalidHash.hexdigest()

#     legalidEncode2 = legalids[i]['legalid'].encode()
#     legalidHash2 = hashlib.sha256(legalidEncode2)
#     legalids[i]['hash2'] = legalidHash2.hexdigest()

#     legalidEncode3 = legalids[i]['legalid'].encode()
#     legalidHash3 = hashlib.sha256(legalidEncode3)
#     legalids[i]['hash3'] = legalidHash3.hexdigest()

#     legalidEncode4 = legalids[i]['legalid'].encode()
#     legalidHash4 = hashlib.sha256(legalidEncode4)
#     legalids[i]['hash4'] = legalidHash4.hexdigest()

#     legalidEncode5 = legalids[i]['legalid'].encode()
#     legalidHash5 = hashlib.sha256(legalidEncode5)
#     legalids[i]['hash5'] = legalidHash5.hexdigest()

# # print(legalids)

# df = pd.DataFrame(legalids)

# df.to_excel(r"C:\Users\thanh\Downloads\abc.xlsx", index=False)


legalidEncode5 = 'e0935c4718524d1f9629d3869476496b'.encode()
legalidHash5 = hashlib.sha256(legalidEncode5)
print(legalidHash5.hexdigest())
