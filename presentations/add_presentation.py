import os.path

from presentations import add_new_presentation
from presentations import TARGET_FOLDER_PATH

presentation_name_with_extension = "C5vmhJL5k7ad_RME8nJxmg.pptx" #example: "my_new_presentation.pptx"
delete_source = False # True for deleting source from presentations folder

add_new_presentation(
    source_path=os.path.join(os.getcwd(), presentation_name_with_extension),
    target_path=TARGET_FOLDER_PATH,
    delete_source=delete_source
)