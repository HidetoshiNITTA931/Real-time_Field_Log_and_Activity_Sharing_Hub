"""
Markdownにエクスポートする
"""
import setting
from mdutils.mdutils import MdUtils
from convert_base64_image import convert_base64_image

def export_markdown(df, output_file, title, top_text):
    # データベースのカラムが想定通りかチェック
    _check_df_columns(df.columns)
    mdFile = MdUtils(file_name=output_file, title=title)
    mdFile.new_line(top_text)
    mdFile.new_line("\n")

    # 一行ずつ書いていく
    for index, line in df.iterrows():
        mdFile.new_line("---")
        for photo_name in [setting.CLOSE_PHOTO, setting.DISTANCE_PHOTO, setting.OTHOER_PHOTO]:
            # dataverseの画像オブジェクトは存在しない場合nanで帰ってくるのでfloat型かどうかで判定
            if type(line[photo_name]) is not float:
                if line[photo_name] is not None:
                    image_file_name = "./images/{}_{}.png".format(line[setting.KOUJI_LOG_ID], photo_name)
                    convert_base64_image(line[photo_name], image_file_name)
                    mdFile.new_paragraph('<img src={} width="150">'.format(image_file_name))
        
        mdFile.new_line("\n")
        mdFile.new_line("工事日 : " + str(line[setting.KOUJI_DATE]).split("T")[0])
        mdFile.new_line("拠点名 : " + str(line[setting.KYOTEN_MEI]))
        mdFile.new_line("工事場所 : " + str(line[setting.KOUJI_BASYO]))
        mdFile.new_line("工事カテゴリ : " + str(line[setting.SAGYO_MEI]))
        mdFile.new_line("情報 : " + str(line[setting.HOST_MEI_ETC]))
        mdFile.new_line("\n")


    #table_data = ['列1', '列2', '列3', 'データ1', 'データ2', 'データ3']
    #mdFile.new_table(columns=3, rows=2, text=table_data, text_align='center')
    mdFile.create_md_file()

def _check_df_columns(columns):
    for col in setting.SELECT_DATA:
        if col not in columns:
            raise Exception("Column isn't as expected. from dataverse columns:{}".format(columns))
    for col in setting.EXTEND_DATA:
        if col[0] not in columns:
            raise Exception("Column isn't as expected. from dataverse columns:{}".format(columns))
