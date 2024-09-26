from requests_html import HTMLSession
import os
import requests

# Step 1: Start an HTML session
session = HTMLSession()

# Step 2: Fetch the page
url = 'https://example.com'
response = session.get(url)

# Step 3: Render JavaScript (if necessary)
response.html.render()

# Step 4: Find all image tags
images = response.html.find('img')

# Step 5: Create a directory to store the images
os.makedirs('requests_html_images', exist_ok=True)

# Step 6: Loop through and download images
for img in images:
    img_url = img.attrs['src']
    
    # Handle relative URLs
    if not img_url.startswith(('http', 'https')):
        img_url = response.urljoin(img_url)
    
    img_name = os.path.join('requests_html_images', img_url.split('/')[-1])
    
    # Download and save the image
    img_data = requests.get(img_url).content
    with open(img_name, 'wb') as handler:
        handler.write(img_data)
    
    print(f"Image saved: {img_name}")
