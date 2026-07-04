import io
import base64
from PIL import Image

def convert_base64_image(base64_string : str, file_name=None):
    # Base64文字列をバイナリデータに変換
    image_data = base64.b64decode(base64_string)
    # バイナリデータを画像ストリームとして読み込み
    image = Image.open(io.BytesIO(image_data))
    # 4. デフォルトの画像ビューアで表示
    # image.show()
    if file_name is not None:
        image.save(file_name)