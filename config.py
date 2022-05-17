import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
"""
API_ID 11798215
API_HASH 433b9d1c8d24b23e0101cfd42ce262e8
"""

# للنشر المحلي
if os.path.exists(".env"):
    load_dotenv(".env")
# الفارات
API_ID = int(os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
