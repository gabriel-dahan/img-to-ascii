from PIL import Image
import numpy as np
from typing import Optional

class Img(object):

    def __init__(self, path: str):
        self.path = path
        self.image = Image.open(path).convert('L')
        self.chars_70 = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`\'. '
        self.chars_10 = '@%#*+=-:. '

    def _get_grayscale(self, img): 
        im = np.array(img)
        w, h = im.shape
        return np.average(im.reshape(w * h))

    def to_ascii(self, more_detail: Optional[bool] = False, scale: Optional[float] = 0.43, cols: Optional[int] = 80, out_file: Optional[str] = False):
        print('Generating ASCII art...') 
        W, H = self.image.size[0], self.image.size[1]

        w = W / cols
        h = w / scale
        rows = int(H / h)
        
        if cols > W or rows > H: 
            print("Image too small for specified cols !")
            exit(0)

        aimg = []
        for j in range(rows):
            y1 = int(j * h)
            y2 = int((j + 1) * h)

            if j == rows - 1: 
                y2 = H

            aimg.append("") 
    
            for i in range(cols): 
                x1 = int(i* w) 
                x2 = int((i + 1) * w) 

                if i == cols - 1: 
                    x2 = W 

                img = self.image.crop((x1, y1, x2, y2)) 
                avg = int(self._get_grayscale(img)) 

                if more_detail: 
                    gs_val = self.chars_70[int((avg * 69) / 255)] 
                else: 
                    gs_val = self.chars_10[int((avg * 9) / 255)] 

                aimg[j] += gs_val

        if out_file:
            f = open(out_file, 'w')
            for row in aimg:
                f.write(row + '\n')
            f.close()

        return aimg 

if __name__ == '__main__':
    print(Img('img.jpg').to_ascii(out_file = 'ascii.txt'))