import win32com.client
import os
import shutil
from typing import Optional

def add_new_presentation(source_path: str, target_path: str, delete_source: Optional[bool]=False):
    presentation_name = os.path.split(source_path)[1]
    name_without_expansion = presentation_name[:presentation_name.rfind(".")]
    Application = win32com.client.Dispatch("PowerPoint.Application")
    Presentation = Application.Presentations.Open(source_path)
    for slide_number in range(len(Presentation.Slides)):
        Presentation.Slides[slide_number].Export(
            os.path.join(target_path, name_without_expansion+"_" + "{x:03}".format(x=slide_number + 1) + ".jpg"),
            "JPG"
        )
    shutil.copy(source_path, target_path)
    if delete_source:
        os.remove(source_path)
    Application.Quit()


def remove_presentation(source_path: str, target_path: str, delete_source: Optional[bool]=False):
    presentation_name = os.path.split(source_path)[1]
    name_without_expansion = presentation_name[:presentation_name.rfind(".")]
    Application = win32com.client.Dispatch("PowerPoint.Application")
    Presentation = Application.Presentations.Open(source_path)
    for slide_number in range(len(Presentation.Slides)):
        os.remove(os.path.join(target_path, name_without_expansion + "_" + "{x:03}".format(x=slide_number + 1) + ".jpg"))
    os.remove(os.path.join(target_path, presentation_name))
    if delete_source:
        os.remove(source_path)
    Application.Quit()
