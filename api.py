import requests

def get_video_info(bvid):
    url = "https://api.bilibili.com/x/web-interface/view"
    headers = {
        'User-Agent': 'Mozilla/5.0...',
        'Referer': f'https://www.bilibili.com/video/{bvid}'
    }
    params = {
        'bvid': bvid,
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_video_url(bvid,cid):
    url = "https://api.bilibili.com/x/player/playurl"
    headers = {
        'User-Agent': 'Mozilla/5.0...',
        'Referer': f'https://www.bilibili.com/video/{cid}'
    }
    params = {
        'cid': cid,
        'bvid': bvid,
        'qn': 80,
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def download_video(video_url, title):
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Referer": "https://www.bilibili.com/"
    }
    response = requests.get(video_url, stream=True,headers=headers)
    if response.status_code == 200:
        with open(f"{title}.mp4", 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        print(f"下载完成: {title}.mp4")
    else:
        
        print("视频下载失败","错误码为：",response.status_code)


print("---------------------\n")
bvid = 'BV1JyHWe2EJw' #爱丽丝：你怎么睡得着的？
#获取视频信息
data = get_video_info(bvid)
video_data = data['data']
tiltle = video_data['title']
cid = video_data["pages"][0]["cid"]
#获取视频url
respons_video_url = get_video_url(bvid,cid)
video_url = respons_video_url['data']['durl'][0]['url']
#下载视频
download_video(video_url, tiltle)

