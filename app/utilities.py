import pytesseract
import re


def get_IDs_from_img(img_path, pytesseract_path):
    # pytesseract_path = pytesseract_path + "\\tesseract"
    # pytesseract.pytesseract.tesseract_cmd = r"{}".format(pytesseract_path)
    text = pytesseract.image_to_string(img_path)
    pattern = re.search("[IDJOR]+(\w)+(\d)+<(\d)+", text)
    if pattern:
        pattern_list = pattern.group().replace("IDJOR", "").split("<")
        id = pattern_list[1]
        if id[0] != ("2" or "9"):
            id = id[1 : len(id)]
        card_id = pattern_list[0]
        return (id, card_id)
    else:
        return (None, None)
