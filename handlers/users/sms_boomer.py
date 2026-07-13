import requests
import time

from aiogram.types import Message
from fake_useragent import UserAgent

proxy_url = f"http://vsg9A6pT8wouSwG:IPX4a6cVD5nfO2o@proxy-us.proxy-cheap.com:5959"
proxies = {"http": proxy_url, "https": proxy_url}


def check_proxy():
    try:
        response = requests.get("https://api.ipify.org", proxies=proxies, timeout=10)
        return True, response.text
    except Exception:
        return False, None


async def send_sms(phone, formatted_phone,message):
    print(f"DEBUG: message turi: {type(message)}")  # Konsolda nima chiqayotganini qarang
    print(f"DEBUG: message qiymati: {message}")
    is_proxy_ok, current_ip = check_proxy()
    if not is_proxy_ok:
        await message.answer("-> Proksi ulanmadi, SMS yuborish bekor qilindi.")
        return False

    ua = UserAgent()
    url = "https://api.100k.uz/api/auth/sms-login"
    payload = {"phone": phone, "formatted_phone": formatted_phone}
    headers = {
        "User-Agent": ua.random,
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(url, json=payload, headers=headers, proxies=proxies, timeout=15)
        if response.status_code == 200:
            await message.answer(f" SMS yuborildi! (IP: {current_ip})")
            return True
        elif response.status_code == 403:
            await message.answer(f"Status 403: IP bloklandi (IP: {current_ip})")
            return False
        else:
            await message.answer(f" Xatolik kodi: {response.status_code}")
            return False
    except Exception as e:
        await message.answer(f" Ulanish xatosi: {e}")
        return False


