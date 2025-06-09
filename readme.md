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
"video": {
        "CoverTsp": 10.69257641921397,
        "ai_dynamic_cover": {
          "height": 720,
          "uri": "tos-no1a-p-0037-no/oglKeAGi6NCLdLj6QfnVXAIIAIfJFTXQAAkTIw",
          "url_list": [
            "https://p16-common-sign-no.tiktokcdn-us.com/tos-no1a-p-0037-no/oglKeAGi6NCLdLj6QfnVXAIIAIfJFTXQAAkTIw~tplv-tiktokx-origin.image?dr=9636&refresh_token=de702eb4&x-expires=1749582000&x-signature=lgToHMxJ3ZQHJZl13HwMh7bVegM%3D&t=4d5b0474&ps=13740610&shp=d05b14bd&shcp=34ff8df6&idc=useast5&s=AWEME_DETAIL",
            "https://p19-common-sign-no.tiktokcdn-us.com/tos-no1a-p-0037-no/oglKeAGi6NCLdLj6QfnVXAIIAIfJFTXQAAkTIw~tplv-tiktokx-origin.image?dr=9636&refresh_token=b149c895&x-expires=1749582000&x-signature=F8w47UH4OOoUe3vFKMs%2Flwy%2BJx0%3D&t=4d5b0474&ps=13740610&shp=d05b14bd&shcp=34ff8df6&idc=useast5&s=AWEME_DETAIL",
            "https://p16-common-sign-no.tiktokcdn-us.com/tos-no1a-p-0037-no/oglKeAGi6NCLdLj6QfnVXAIIAIfJFTXQAAkTIw~tplv-tiktokx-origin.jpeg?dr=9636&refresh_token=61c4315f&x-expires=1749582000&x-signature=kT7Ywf96GYA7%2BbN9%2FJZEWt8AffQ%3D&t=4d5b0474&ps=13740610&shp=d05b14bd&shcp=34ff8df6&idc=useast5&s=AWEME_DETAIL"
          ],
          "url_prefix": null,
          "width": 720
        }
```
This is an extract with the links and where they are stored on the TikTok server.
