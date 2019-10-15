# coding=gbk
from PIL import Image
from scipy.ndimage import filters
import numpy as np

im1=Image.open("C:/Users/Gin/Pictures/Wallpaper.jpg")
a = np.array(Image.open('C:/Users/Gin/Pictures/Wallpaper.jpg').convert('L')).astype('float')

gamma=0.5
a=255*(a/255)**gamma

# 灰度变换
depth = 10.                         # (0-100)
grad = np.gradient(a)               #取图像灰度的梯度值
grad_x, grad_y = grad               #分别取横纵图像梯度值
grad_x = grad_x*depth/100.
grad_y = grad_y*depth/100.
A = np.sqrt(grad_x**2 + grad_y**2 + 1.)#这里相当于 grad_z=1.0

uni_x = grad_x/A
uni_y = grad_y/A
uni_z = 1./A
vec_el = np.pi/2.2  # 光源的俯视角度（根据图片假设的），弧度值
vec_az = np.pi/4.  # 光源的方位角度（根据图片假设的），弧度值
dx = np.cos(vec_el)*np.cos(vec_az)  #光源对x 轴 单位长度 的影响
dy = np.cos(vec_el)*np.sin(vec_az)  #光源对y 轴 单位长度 的影响
dz = np.sin(vec_el)                 #光源对z 轴 单位长度 的影响
b = 255*(dx*uni_x + dy*uni_y + dz*uni_z)    #光源归一化
b = b.clip(0,255)#为避免数据越界，将生成的灰度值裁剪至0‐255区间
im = Image.fromarray(b.astype('uint8'))     #重构图像

# 调整尺寸和旋转
im=im.resize((1920,1080))
im=im.rotate(180)

# 复制和粘贴图像区域
box = (100,100,400,400)
region = im.crop(box)
region = region.transpose(Image.ROTATE_180)
im.paste(region,box)

# 图像模糊
im = filters.gaussian_filter(im,5)

im.save('C:/Users/Gin/Pictures/Wallpaper-1.jpg')
im.show()