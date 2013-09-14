import Image
import os

def compress(item, field, max_kb=200):
  photo = getattr(item, field)
  if photo:
    name = os.path.splitext(photo.name)[0]
    path = os.path.splitext(photo.path)[0]
    new_name = name + '.jpg'
    new_path = path + '.jpg'

    try:
      img = Image.open(photo.path)
      kb = os.stat(photo.path).st_size/1024
      if kb > max_kb:
        img.save(new_path, 'JPEG', quality=80)
        setattr(item, field, new_name)
        item.save()
        print "%s compressed from %ikb to %ikb" % (photo.name, kb, os.stat(new_path).st_size/1024)
        # Remove old file
        if new_path != photo.path:
          os.remove(photo.path)
    except IOError:
      print "Image not found %s"%photo.path
