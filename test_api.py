#%%
from PIL import Image 
import requests 
import base64
from io import BytesIO

test_img = Image.open('./images/fashion/dresses/9815337.jpg')
test_img
# %%
URL = "http://127.0.0.1:5000/process_image/"

# sending post request and saving response as response object
r = requests.post(url = URL, files={'file': open('./images/fashion/dresses/9815337.jpg', 'rb')})
# %%
r.json()
# %%
def decode_images(encoded_images):
    decoded_images = []
    for encoded_image in encoded_images:
        # Decode the base64-encoded image
        decoded_data = base64.b64decode(encoded_image)
        
        # Create a BytesIO object to treat the binary data as an image file
        image_buffer = BytesIO(decoded_data)
        
        # Open the image using PIL (Python Imaging Library)
        image = Image.open(image_buffer)
        
        # Append the decoded image to the list
        decoded_images.append(image)
    
    return decoded_images

# %%
decoded_images = decode_images(r.json()['files'])


# %%
for img in decoded_images:
    display(img)

# %%
