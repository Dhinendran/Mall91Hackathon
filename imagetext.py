from google.oauth2 import service_account
import re
import ast
import vision
credentials = service_account.Credentials. from_service_account_file("/Users/dhinendran/Desktop/Mall91/Mall91Hackathon/My First Project-2a412de5bef1.json")

def translate_en(Hindi_data):
    from google.cloud import translate
    # Instantiates a client
    translate_client = translate.Client(credentials=credentials)

    # The text to translate
    text = str(Hindi_data)
    # The target language
    target = 'en'
    # Translates some text into Russian
    translation = translate_client.translate(
        text,
        target_language=target)

    print(u'Text: {}'.format(text))
    print('Translation: {}'.format(translation['translatedText']))
    return translation['translatedText']

def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    import io
    # client = vision.ImageAnnotatorClient()
    file_data = {}

    client = vision.ImageAnnotatorClient(credentials=credentials)

    # [START vision_python_migration_text_detection]
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    # print('Texts:{}'.format(texts))
    file_data["image_text"] = []
    for text in texts:
        # print('\n"{}"'.format(text.description))
        if text.locale:
            file_data["locale"] = text.locale
        else:
            file_data["image_text"].append(text.description)
    print("list {}".format(file_data))
    if file_data["locale"] != "en":
        Trans = translate_en(file_data["image_text"])
        Trans_en= Trans.replace('&#39;','')
        file_data["image_text"] = Trans_en[1:len(Trans_en)-1].split(',')
    return file_data

result =detect_text("/Users/dhinendran/Downloads/spam/655.jpg")
# print(result)
print(" ".join(result["image_text"]))
vision.get_data(" ".join(result["image_text"]))




# def detect_safe_search(path):
#     """Detects unsafe features in the file."""
#     from google.cloud import vision
#     import io
#     client = vision.ImageAnnotatorClient(credentials=credentials)

#     with io.open(path, 'rb') as image_file:
#         content = image_file.read()

#     image = vision.types.Image(content=content)

#     response = client.safe_search_detection(image=image)
#     safe = response.safe_search_annotation

#     # Names of likelihood from google.cloud.vision.enums
#     likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
#                        'LIKELY', 'VERY_LIKELY')
#     print('Safe search:')

#     print('adult: {}'.format(likelihood_name[safe.adult]))
#     print('medical: {}'.format(likelihood_name[safe.medical]))
#     print('spoofed: {}'.format(likelihood_name[safe.spoof]))
#     print('violence: {}'.format(likelihood_name[safe.violence]))
#     print('racy: {}'.format(likelihood_name[safe.racy]))

# detect_safe_search("/Users/dhinendran/Downloads/download (1).png")
