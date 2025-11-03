import requests

api_key = "sk-TaniHE58ucoyl0BJewBhKTdYoKpnwBZoIzSixyjGisqsnAUg"
url = "https://api.stability.ai/v2beta/stable-image/generate/core"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Accept": "image/*"
}

total_images = 5

for i in range(1, total_images + 1):
    prompt = "a futuristic city skyline at sunset, digital art"

    form_data = {
        "prompt": (None, prompt),
        "cfg_scale": (None, "8"),
        "height": (None, "512"),
        "width": (None, "512"),
        "samples": (None, "1"),
        "steps": (None, "30")
    }

    response = requests.post(url, headers=headers, files=form_data)

    if response.status_code == 200:
        filename = f"image_{i}.png"
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"✅ File saved: {filename}")
    else:
        print(f"❌ Error: {response.status_code}")
        print(response.text)
