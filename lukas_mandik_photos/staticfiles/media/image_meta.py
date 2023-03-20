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
    "/Users/lukasmandik/PycharmProjects/PhotosWeb/lukas_mandik_photos/photos_web/static/media/_DSC0790.JPG",
    "/Users/lukasmandik/PycharmProjects/PhotosWeb/lukas_mandik_photos/photos_web/static/media/_DSC3824.JPG",
]
with exiftool.ExifToolHelper() as et:
    metadata = et.get_metadata(files)

    for data in metadata:
        print(data)

    print(metadata)



# from exif import Image
# with open('/Users/lukasmandik/PycharmProjects/PhotosWeb/lukas_mandik_photos/photos_web/static/media/_DSC0790.JPG', 'rb') as image_file:
#     my_image = Image(image_file)
#
# print(my_image.list_all())
# print(my_image.make)
#
# print(my_image.software)
# print(my_image.datetime)
# print(my_image.f_number)
# print(my_image.photographic_sensitivity)
# print(my_image.color_space)
# print(my_image.focal_plane_x_resolution)
# print(my_image.focal_plane_y_resolution)
# print(my_image.focal_plane_resolution_unit)
# print(my_image.focal_plane_resolution_unit)






