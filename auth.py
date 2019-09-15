from watson_developer_cloud import VisualRecognitionV3

import json

visual_recognition = VisualRecognitionV3(
    version='2018-03-19',
    iam_apikey='yxu1EPLR_Ry65MXOkWItzzA4VSDhghPSKLt07UIxAD8F'
)

with open('./banana1.jpg', 'rb') as images_file:
    classes = visual_recognition.classify(
        images_file,
        threshold='0.6',
	classifier_ids='DefaultCustomModel_793529682').get_result()
print(json.dumps(classes, indent=2))