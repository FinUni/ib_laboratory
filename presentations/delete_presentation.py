import os.path

from presentations import remove_presentation
from presentations import TARGET_FOLDER_PATH

presentation_name_with_extension = "zai.pptx" #example: "my_new_presentation.pptx"
delete_source = False # True for deleting source from presentations folder

remove_presentation(
    source_path=os.path.join(os.getcwd(), presentation_name_with_extension),
    target_path=TARGET_FOLDER_PATH,
    delete_source=delete_source
)