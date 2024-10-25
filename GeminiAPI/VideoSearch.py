import google.generativeai as genai
import os



# Set up API key
def genURL(input1):
    prompt = f'''minimise "{input1}" into words separated by underscores, the answer should contain only the words nothing else
    '''
    genai.configure(api_key=os.environ["API_KEY"])
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    prom = response.text
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={prom}&key=AIzaSyBejvvt97IB4Cs4Sdd2ce92uM9H-ragVl8"
    return url