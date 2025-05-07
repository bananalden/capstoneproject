from imagekitio import ImageKit
from django.conf import settings

imagekit = ImageKit(
    public_key=settings.IMAGEKIT_PUBLIC_KEY,
    private_key=settings.IMAGEKIT_PRIVATE_KEY,
    url_endpoint=settings.IMAGEKIT_URL_ENDPOINT,
)

def upload_to_imagekit(file_obj, filename):
    upload_response = imagekit.upload(
        file = file_obj,
        file_name = filename
    )

    if upload_response.get("response"):
        return upload_response["response"]["url"]
    return None