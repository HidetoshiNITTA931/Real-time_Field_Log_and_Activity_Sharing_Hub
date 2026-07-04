"""
デバッグモード
"""
DEBUG_MODE = False

"""
テーブルデータの名前定義
"""
#### 作業記録テーブル ####
# 工事名(PJ名)
KOUJI_MEI = "flash_project"
KOUJI_MEI_RIRON = "flash_name"
# 拠点名
KYOTEN_MEI = "flash_field"
KYOTEN_MEI_RIRON = "flash_name"
# 拠点内の工事場所
KOUJI_BASYO = "flash_place"
# 作業カテゴリ
SAKYO_MEI = "flash_categories"
# ホスト名など
HOST_MEI_ETC = "flash_something_info"
# 工事実施日
KOUJI_DATE = "flash_done_date"
# 寄りの写真
CLOSE_PHOTO = "flash_close_photo"
# 引きの写真
DISTANCE_PHOTO = "flash_distance_photo"
# その他の写真
OTHOER_PHOTO = "flash_othoer_photo"

"""
取得データの定義
"""
SELECT_DATA = [
    KOUJI_BASYO,
    SAKYO_MEI,
    HOST_MEI_ETC,
    KOUJI_DATE,
    CLOSE_PHOTO,
    DISTANCE_PHOTO,
    OTHOER_PHOTO,
]
EXTEND_DATA = [
    # 作業記録テーブルのスキーマ名、別テーブルのカラムの理論値
    [KOUJI_MEI, KOUJI_MEI_RIRON],
    [KYOTEN_MEI, KYOTEN_MEI_RIRON]
]