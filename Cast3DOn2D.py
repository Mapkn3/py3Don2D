from PIL import Image, ImageDraw

class Cast3DOn2D:
    def __init__(self, img_width, img_height, zx, zy):
        self.set_scale_z(zx, zy)
        self.set_o(img_width / 2, img_height / 2)
        self.img_width = img_width
        self.img_height = img_height
        self.img = Image.new('RGBA', (img_width, img_height), (255,255,255,0))
        self.draw = ImageDraw.Draw(self.img)

    def set_o(self, x, y):
        self.ox = x
        self.oy = y

    def set_scale_z(self, zx, zy):
        self.zx = zx
        self.zy = zy
    
    def show_img(self):
        self.img.show()

    def save_img(self, path):
        img.save(path, 'png')

    def draw_line(self, xyz):
        #xyz = [(x0,y0,z0), (x1,y1,z1), (x2,y2,z2), ...]
        xy = [(self.ox+i[0]-self.zx*i[2], self.img_height-(self.oy+i[1]-self.zy*i[2])) for i in xyz[1:]]
        self.draw.line(xy, fill=xyz[0])

    def draw_lines(self, *xyzs):
        for xyz in xyzs:
            self.draw_line(xyz)


caster = Cast3DOn2D(1024, 1024, 1, 1)
w = 80
h = 100
d = 50
caster.draw_lines([0,(0,0,0),(w,0,0),(w,h,0),(0,h,0),(0,0,0)],
                  [0,(0,0,d),(w,0,d),(w,h,d),(0,h,d),(0,0,d)],
                  [0,(0,0,0),(0,0,d)],
                  [0,(w,0,0),(w,0,d)],
                  [0,(w,h,0),(w,h,d)],
                  [0,(0,h,0),(0,h,d)])
caster.set_o(256, 256)
caster.set_scale_z(0.5, 1)
caster.draw_lines([0,(0,0,0),(w,0,0),(w,h,0),(0,h,0),(0,0,0)],
                  [0,(0,0,d),(w,0,d),(w,h,d),(0,h,d),(0,0,d)],
                  [0,(0,0,0),(0,0,d)],
                  [0,(w,0,0),(w,0,d)],
                  [0,(w,h,0),(w,h,d)],
                  [0,(0,h,0),(0,h,d)])
caster.show_img()
