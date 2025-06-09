# Shorts Uploader

A simple tool for uploading your [TikTok](https://tiktok.com) videos to [YouTube](https://youtube.com) shorts. It copies the same hashtags and description from the TikTok video, makling this an easy 2-click upload.

Uploaded and working (09/06/25)

#### How this works
The software runs using the TikTok Mobile Api and the official [Google Cloud Console YouTube api v3](https://console.cloud.google.com/apis/library/youtube.googleapis.com?hl=de&pli=1&inv=1&invt=AbzrcQ). The TikTok Mobile Api allows me to download videos without the TikTok Watermark in the corner. After successfully downloading the video, it uses Google's services to re-upload it to YouTube in the shorts format. Hashtags and Title are copied from the TikTok video.

#

If you have any questions on the TikTok Mobile Api, message me via email.

## TikTok Api Response:

This is where to find the link to download the video without watermark:

```
"play_addr": {
              "data_size": 2074146,
              "file_cs": "c:0-20433-6b9c",
              "file_hash": "a386e11d47491860000bd3ab7015ec27",
              "height": 1024,
              "uri": "v24044gl0000d129lhfog65oqjh9apc0",
              "url_key": "v24044gl0000d129lhfog65oqjh9apc0_h264_540p_718225",
              "url_list": [
                "https://v16m-default.tiktokcdn-us.com/d243fff9ef4ab3d2de93c71d59a4e5fc/68478455/video/tos/no1a/tos-no1a-ve-0068c001-no/oEAgEFqFrRqvDmpDRfcBJdExgkElFleIyocUQw/?a=0&bti=OUBzOTg7QGo6OjZAL3AjLTAzYCMxNDNg&ch=0&cr=0&dr=0&er=0&lr=all&net=0&cd=0%7C0%7C0%7C0&cv=1&br=1402&bt=701&cs=0&ds=6&ft=H3NijvhlQ3pUxqGK2.0cF5j_YlgID5Q1GbKYwGZp8Z4ka&mime_type=video_mp4&qs=5&rc=aDo3O2RlOmY1NWY6aDRkZ0BpM3M8bXI5cms8NDMzbzczNUA0LmA2NjNgXjIxMi0yLzQzYSNgXmVuMmRjaS9hLS1kMTFzcw%3D%3D&vvpl=1&l=20250609190254E43705B42EE24C03C9CC&btag=e000b8000",
                "https://v16m-default.tiktokcdn-us.com/d243fff9ef4ab3d2de93c71d59a4e5fc/68478455/video/tos/no1a/tos-no1a-ve-0068c001-no/oEAgEFqFrRqvDmpDRfcBJdExgkElFleIyocUQw/?a=0&bti=OUBzOTg7QGo6OjZAL3AjLTAzYCMxNDNg&ch=0&cr=0&dr=0&er=0&lr=all&net=0&cd=0%7C0%7C0%7C0&cv=1&br=1402&bt=701&cs=0&ds=6&ft=H3NijvhlQ3pUxqGK2.0cF5j_YlgID5Q1GbKYwGZp8Z4ka&mime_type=video_mp4&qs=5&rc=aDo3O2RlOmY1NWY6aDRkZ0BpM3M8bXI5cms8NDMzbzczNUA0LmA2NjNgXjIxMi0yLzQzYSNgXmVuMmRjaS9hLS1kMTFzcw%3D%3D&vvpl=1&l=20250609190254E43705B42EE24C03C9CC&btag=e000b8000",
                "https://api16-normal-useast5.tiktokv.us/aweme/v1/play/?file_id=6d7a215e075c4252acc76b9a98c4177e&is_play_url=1&item_id=7513300401999858966&line=0&signaturev3=dmlkZW9faWQ7ZmlsZV9pZDtpdGVtX2lkLmQ3NWNiN2Y1ZjZmZTkwOGFhMzNhODdjZTNjM2IzMjg2&source=AWEME_DETAIL&video_id=v24044gl0000d129lhfog65oqjh9apc0"
              ],
              "url_prefix": null,
              "width": 576
            },
```
This is an extract with the links and where they are stored on the TikTok server.

Api:
```py
id  = "7513300401999858966" # id of any tiktok video in regular format
api = f"https://api16-normal-useast5.us.tiktokv.com/tiktok/v1/videos/detail/?aweme_ids=[{id}]" # the api that gives you all information about the video
```
