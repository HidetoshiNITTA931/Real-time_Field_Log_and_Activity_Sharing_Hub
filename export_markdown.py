"""
Markdownにエクスポートする
"""
from mdutils.mdutils import MdUtils
from convert_base64_image import convert_base64_image

def export_markdown(df, output_file, title, top_text):
    mdFile = MdUtils(file_name=output_file, title=title)
    mdFile.new_line(top_text)
    mdFile.new_line("\n")

    mdFile.new_line("---")
    convert_base64_image(df["flash_close_photo"][0], "./images/temp1.png")
    convert_base64_image(df["flash_distance_photo"][0], "./images/temp2.png")
    mdFile.new_paragraph('<img src="./images/temp1.png" width="150">')
    mdFile.new_paragraph('<img src="./images/temp2.png" width="150">')
    mdFile.new_line("\n")
    mdFile.new_line("拠点名 : " + df["flash_field"][0])
    mdFile.new_line("工事場所 : " + df["flash_place"][0])
    #table_data = ['列1', '列2', '列3', 'データ1', 'データ2', 'データ3']
    #mdFile.new_table(columns=3, rows=2, text=table_data, text_align='center')
    mdFile.create_md_file()
    