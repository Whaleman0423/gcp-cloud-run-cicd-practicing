# from flask import Flask
import pytest

# 將 app 從 app.py 導入
from app import app

def test_hello():
    # 創建一個測試客戶端
    with app.test_client() as client:
        # 使用客戶端發送請求
        rv = client.get('/')
        assert rv.status_code == 200
        assert rv.data.decode("utf-8") == "Hello, World!"
