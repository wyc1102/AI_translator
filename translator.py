import argparse
import os
import sys

from dotenv import load_dotenv
from openai import AuthenticationError, OpenAIError, OpenAI, RateLimitError

load_dotenv()

API_KEY = os.getenv("DEEPSEEK_API_KEY")
MODEL = os.getenv("DEEPSEEK_MODEL", "deepseek-v4-pro")
BASE_URL = "https://api.deepseek.com"

SYSTEM_PROMPT = (
    "You are a translation assistant. Translate the user's message: "
    "if it is Chinese, translate it into English; "
    "if it is English, translate it into Chinese."
)


def parse_args() -> str:
    parser = argparse.ArgumentParser(description="终端中英互译AI脚本")
    parser.add_argument(
        "source_message",
        nargs="+",
        help="待翻译文本",
    )
    return " ".join(parser.parse_args().source_message)


def main() -> int:
    source_message = parse_args()

    if not API_KEY:
        print("错误：未配置 DEEPSEEK_API_KEY,请先在 .env 中填入密钥", file=sys.stderr)
        return 1

    client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": source_message},
            ],
            stream=False,
            reasoning_effort="high",
            extra_body={"thinking": {"type": "enabled"}},
        )
    except AuthenticationError:
        print("error: API 密钥无效, 请检查 .env 中的 DEEPSEEK_API_KEY", file=sys.stderr)
        return 1
    except RateLimitError:
        print("error: 请求过于频繁,已被限流,请稍后再试", file=sys.stderr)
        return 1
    except OpenAIError as exc:
        print(f"error: 请求失败：{exc}", file=sys.stderr)
        return 1

    print(response.choices[0].message.content)
    return 0


if __name__ == "__main__":
    sys.exit(main())
