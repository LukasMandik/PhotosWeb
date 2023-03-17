import os
# from PIL import Image
# from PIL.ExifTags import TAGS
#
# image_file = '_DSC0790.JPG'
# image = Image.open(image_file)
#
# exif = {}
#
# for tag, value in image._getexif().items():
#     if tag in TAGS:
#         exif[TAGS[tag]] = value
#
# print(exif)

import exiftool

files = [
    "/Users/lukasmandik/PycharmProjects/PhotosWeb/lukas_mandik_photos/photos_web/static/media/AC571185-1C2B-4BE6-B108-6096F0685529_1_102_o.jpeg",
    "/Users/lukasmandik/PycharmProjects/PhotosWeb/lukas_mandik_photos/photos_web/static/media/_DSC3820.JPG",
    "/Users/lukasmandik/PycharmProjects/PhotosWeb/lukas_mandik_photos/photos_web/static/media/_DSC3824.JPG",
]
with exiftool.ExifToolHelper() as et:
    metadata = et.get_metadata(files)

    for data in metadata:
        print(data)

    print(metadata)

