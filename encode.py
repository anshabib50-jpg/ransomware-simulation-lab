import os, base64

folder = r"D:\ransom_test"

for file in os.listdir(folder):
    path = os.path.join(folder, file)

    if os.path.isfile(path):
        with open(path, "rb") as f:
            data = f.read()

        encoded = base64.b64encode(data)

        with open(path, "wb") as f:
            f.write(encoded)

        print("Encoded:", file)

print("Encoding done.")
