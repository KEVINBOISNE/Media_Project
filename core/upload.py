from imagekitio import ImageKit

imagekit = ImageKit(
    public_key='TON_PUBLIC_KEY',
    private_key='TON_PRIVATE_KEY',
    url_endpoint='https://ik.imagekit.io/nnatxct7i/'
)

upload = imagekit.upload_file(
    file=open("monimage.jpg", "rb"),  # image sur ton PC
    file_name="monimage.jpg"
)

print(upload)
print("Image URL :", upload['response']['url'])
