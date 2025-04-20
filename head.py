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
