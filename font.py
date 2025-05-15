import requests


def font(text, style):
    try:
        response = requests.get("https://raw.githubusercontent.com/Mishel-07/Fonts/main/fonts.json")
        fonts = response.json()

        if style not in fonts:
            return "style not found"

        data = fonts[style]
        result = ""

        for l in text:
            result += data.get(l, l)  
        return result

    except Exception as e:
        return f"error: {str(e)}"
