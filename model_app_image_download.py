
"""
Power Appsのモデル駆動型アプリのテーブルデータを落としてきて表示する。
このファイルと同じディレクトリにsecret.pyを作成し、DATAVERSE_URLをstrで定義する。
"""
import warnings
import logging
import setting
from datetime import datetime
from PowerPlatform.Dataverse.client import DataverseClient
from azure.identity import InteractiveBrowserCredential
from data_cleaning import data_cleaning
from secret import DATAVERSE_URL
from export_markdown import export_markdown

# Del Worning Response mode from post.
warnings.filterwarnings(
    "ignore",
    message=".*response_mode='form_post'.*"
)
if setting.DEBUG_MODE is True:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

def download_dataverse_file(output_file_name, output_file_title, top_text):
    logging.info("Download data from Dataverse")
    credential = InteractiveBrowserCredential()
    # Dataverse環境URLを設定
    client = DataverseClient(
        DATAVERSE_URL,
        credential,
    )
    records_iter = client.records.list(
        "flash_kouji_Log",
        select=setting.SELECT_DATA,
        # {作業記録テーブルの列のスキーマ名}($select={別テーブルのカラムの理論値})
        expand=list(map(lambda x: "{}($select={})".format(x[0],x[1]), setting.EXTEND_DATA))
        )
    logging.info("Data Cleansing")
    df = data_cleaning(records_iter=records_iter)
    for extend_data in setting.EXTEND_DATA:
        df[extend_data[0]] = list(map(lambda x: x[extend_data[1]], df[extend_data[0]].values))
    if setting.DEBUG_MODE is True:
        print(df)
        df.to_csv("debug.csv")
    logging.info("Export to Markdown")
    export_markdown(
        df,
        "{}_{}.md".format(output_file_name, datetime.now().strftime("%Y%m%d-%H%M%S")),
        output_file_title,
        top_text
        )
    logging.info("Export to Markdown finish.")


if __name__ == "__main__":
    output_file_name = "アウトプットファイルタイトル"
    output_file_title = "ファイルのタイトル"
    top_text = "バージョンやら、作成者情報やら"
    download_dataverse_file(output_file_name, output_file_title, top_text)