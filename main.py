import json
import google_auth_oauthlib
import googleapiclient.discovery
import googleapiclient.http
import requests
import urllib
import time
import os


### user interface ###

class Colors:
    white  = "\033[97m"
    purpl  = "\033[35m"
    brown  = "\033[33m"

class Interface:
    def sleep(xtime):
        return time.sleep(xtime)
    
    def clear():
        return os.system("cls" if os.name == "nt" else "clear")
    
    def title(xtitle: str):
        if os.name == 'nt':
            return os.system(f"title {xtitle}")


### bg code ###

def auth_yt():
    flow  = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file("./utils/client.json", ["https://www.googleapis.com/auth/youtube.upload"])
    creds = flow.run_local_server()
    yt    = googleapiclient.discovery.build("youtube", "v3", credentials=creds)

    Interface.clear()

    return yt

def upload(id: str, comment: str):
    be, se, af   = comment.partition('#')
    data         = json.load(open("./utils/config.json"))
    request_body = {"snippet": {"categoryId": "22", "title": be, "description": f"#{af}", "tags": []}, "status":{"privacyStatus": data['status']}}
    media_file   = f"./{id}.mp4"
    request      = auth_yt().videos().insert(part="snippet,status", body=request_body, media_body=googleapiclient.http.MediaFileUpload(media_file, chunksize=-1, resumable=True))
    response     = None 

    while response is None:
        status, response = request.next_chunk()

        print(f" {Colors.white}uploaded youtube with id{Colors.purpl} : {Colors.white}{response['id']}")

def download(id: str):
    api = f'https://api16-normal-useast5.us.tiktokv.com/tiktok/v1/videos/detail/?aweme_ids=[{id}]'

    response    = requests.get(api).json()
    video       = response["aweme_details"][0]["video"]["play_addr"]["url_list"][0]
    username    = response["aweme_details"][0]["author"]["unique_id"]
    description = response["aweme_details"][0]["desc"]
    content     = urllib.request.urlopen(video).read()
    with open(f"./{id}.mp4".format(id), "wb") as f:
        f.write(content)

    return description, username


### main code ###

def main():
    while True:
        Interface.title("github.com/petrovxc")
        Interface.clear()
        link = input(f" {Colors.white}enter tiktok video link{Colors.purpl} : {Colors.white}")
        url  = requests.get(link).url
        id   = url.split('/')[5].split('?')[0]
        desc, user = download(id)
        Interface.clear()
        print(f" {Colors.white}downloaded {Colors.purpl}{user}{Colors.white}'s video{Colors.purpl} ! {Colors.white}")
        print(f" {Colors.white}the description is{Colors.purpl} : {Colors.white}{desc}")
        Interface.sleep(5)
        upload(id, desc)
        os.remove(f"./{id}.mp4")
        Interface.sleep(10)

if __name__ == "__main__":
    main()
