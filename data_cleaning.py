"""
Power Appsのモデル駆動型アプリのテーブルデータをpandasのDataFrameに変換する
"""
import pandas as pd
import logger
from PowerPlatform.Dataverse.models import QueryResult


def data_cleaning(records_iter : QueryResult) -> pd.DataFrame:
    recoad_list = []
    for recoad in records_iter:
        recoad_list.append(recoad.to_dict())
    return pd.DataFrame(recoad_list)