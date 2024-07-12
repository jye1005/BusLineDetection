from glob import glob
img_list = glob('dataset/train/images/*.jpg')
val_img_list = glob('dataset/val/images/*.jpg')
test_img_list = glob('dataset/test/images/*.jpg')

with open('dataset/train.txt', 'w') as f:
    f.write('\n'.join(img_list) + '\n')

with open('dataset/test.txt', 'w') as f:
    f.write('\n'.join(test_img_list) + '\n')

with open('dataset/val.txt','w') as f:
    f.write('\n'.join(val_img_list))

