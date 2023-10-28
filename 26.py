import requests
import base64
import datetime
import re

def update_readme(repo_owner, repo_name, branch, access_token, new_content_file):
    # 构建 API 请求的 URL
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/README.md"

    # 构建请求头部，包括认证和接受的内容类型
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/vnd.github+json"
    }

    # 获取 README.md 文件的当前内容
    response = requests.get(url, headers=headers)
    response_json = response.json()

    # 提取当前文件的 SHA 值
    current_sha = response_json["sha"]

    # 从 GitHub 链接中获取新的文件内容
    raw_blob_url = "https://github.com/sangjk/fhe/raw/756c7844461f50ea4b40dd8129c3a73e602f7f9a/urls.txt"
    response = requests.get(raw_blob_url)

    if response.status_code == 200:
        # 提取文件内容
        content = response.text

        # 将 "2023-10-23 21:00" 替换为当前日期和时间
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        new_content = re.sub(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}", current_datetime, content)

        # 构建新的文件内容
        new_content_encoded = base64.b64encode(new_content.encode()).decode()

        # 构建请求体
        data = {
            "message": "Update README.md",
            "content": new_content_encoded,
            "sha": current_sha,
            "branch": branch
        }

        # 发起更新文件的请求
        response = requests.put(url, headers=headers, json=data)

        # 检查响应状态码
        if response.status_code == 200:
            print("README.md 文件已成功更新。")
        else:
            print("更新 README.md 文件时出现错误。")
            print("响应状态码:", response.status_code)
            print("响应内容:", response.json())
    else:
        print("无法获取文件内容。响应状态码:", response.status_code)

# 在调用函数时提供相应的参数
repo_owner = "sangjk"
repo_name = "fhe"
branch = "main"
access_token = "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"
new_content_file = "/Users/sangkl/PycharmProjects/pythonProject/untitled1/GitHub/urls.txt"

update_readme(repo_owner, repo_name, branch, access_token, new_content_file)

