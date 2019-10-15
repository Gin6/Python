# coding=gbk
from PIL import Image
from scipy.ndimage import filters
import numpy as np

im1=Image.open("C:/Users/Gin/Pictures/Wallpaper.jpg")
a = np.array(Image.open('C:/Users/Gin/Pictures/Wallpaper.jpg').convert('L')).astype('float')

gamma=0.5
a=255*(a/255)**gamma

# �Ҷȱ任
depth = 10.                         # (0-100)
grad = np.gradient(a)               #ȡͼ��Ҷȵ��ݶ�ֵ
grad_x, grad_y = grad               #�ֱ�ȡ����ͼ���ݶ�ֵ
grad_x = grad_x*depth/100.
grad_y = grad_y*depth/100.
A = np.sqrt(grad_x**2 + grad_y**2 + 1.)#�����൱�� grad_z=1.0

uni_x = grad_x/A
uni_y = grad_y/A
uni_z = 1./A
vec_el = np.pi/2.2  # ��Դ�ĸ��ӽǶȣ�����ͼƬ����ģ�������ֵ
vec_az = np.pi/4.  # ��Դ�ķ�λ�Ƕȣ�����ͼƬ����ģ�������ֵ
dx = np.cos(vec_el)*np.cos(vec_az)  #��Դ��x �� ��λ���� ��Ӱ��
dy = np.cos(vec_el)*np.sin(vec_az)  #��Դ��y �� ��λ���� ��Ӱ��
dz = np.sin(vec_el)                 #��Դ��z �� ��λ���� ��Ӱ��
b = 255*(dx*uni_x + dy*uni_y + dz*uni_z)    #��Դ��һ��
b = b.clip(0,255)#Ϊ��������Խ�磬�����ɵĻҶ�ֵ�ü���0�\255����
im = Image.fromarray(b.astype('uint8'))     #�ع�ͼ��

# �����ߴ����ת
im=im.resize((1920,1080))
im=im.rotate(180)

# ���ƺ�ճ��ͼ������
box = (100,100,400,400)
region = im.crop(box)
region = region.transpose(Image.ROTATE_180)
im.paste(region,box)

# ͼ��ģ��
im = filters.gaussian_filter(im,5)

im.save('C:/Users/Gin/Pictures/Wallpaper-1.jpg')
im.show()