# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel

from flask import Flask, render_template, request, redirect

app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 150

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

def setSolidColor(r,g,b,index):
    print("setSolidColor")
    print(index)
    if type(index) == int:
        print("t1")
        if index == -1:
            print("t2.0",index)
            pixels.fill((r,g,b))
            pixels.show()
        else:
            print("t2.1",index)
            pixels[index] = (r,g,b)
            pixels.show()
    elif len(index)>1:
        for pixel in index:
            pixels[pixel] = (r,g,b)
            pixels.show()
    else:
        print("third arg must be: -1 (for all pixels), a pixel number or a list (eg.: [1,2,3,4])")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/set-color", methods=["POST"])
def setColor():
    req =  request.form.to_dict()
    red = req['red']
    green = req['green']
    blue = req['blue']
    px = req['pixel']
    print(red,green,blue,px)
    setSolidColor(int(red),int(green),int(blue),int(px))
    return redirect("/", code=302)
    
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="5002")


# # Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# # NeoPixels must be connected to D10, D12, D18 or D21 to work.
# pixel_pin = board.D18

# # The number of NeoPixels
# num_pixels = 150

# # The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# # For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
# ORDER = neopixel.GRB

# pixels = neopixel.NeoPixel(
#     pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
# )


# def wheel(pos):
#     # Input a value 0 to 255 to get a color value.
#     # The colours are a transition r - g - b - back to r.
#     if pos < 0 or pos > 255:
#         r = g = b = 0
#     elif pos < 85:
#         r = int(pos * 3)
#         g = int(255 - pos * 3)
#         b = 0
#     elif pos < 170:
#         pos -= 85
#         r = int(255 - pos * 3)
#         g = 0
#         b = int(pos * 3)
#     else:
#         pos -= 170
#         r = 0
#         g = int(pos * 3)
#         b = int(255 - pos * 3)
#     return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)


# def rainbow_cycle(wait):
#     for j in range(255):
#         for i in range(num_pixels):
#             pixel_index = (i * 256 // num_pixels) + j
#             pixels[i] = wheel(pixel_index & 255)
#             print(pixel_index, wheel(pixel_index & 255))
#         pixels.show()
#         time.sleep(wait)

# # pixels[0] = (255, 0, 0)
# # pixels[1] = (0, 255, 0)
# # pixels[2] = (0, 0, 255)

# minBrightness = 10
# maxBrightness = 255

# def setLightsToBrightness(x):
#   if x<0:
#       x=0
#   if x>255:
#       x=255
#   red_pulse = (x,0,0)
#   print(red_pulse)
#   setSolidColor(red_pulse[0],red_pulse[1],red_pulse[2],-1)
# #   time.sleep(0.0001)

# def setSolidColor(r,g,b,index):
#     if type(index) == int:
#         if index == -1:
#             pixels.fill((r,g,b))
#             pixels.show()
#         else:
#             pixels[pixel] = (r,g,b)
#             pixels.show()
#     elif len(index)>1:
#         for pixel in index:
#             pixels[pixel] = (r,g,b)
#             pixels.show()
#     else:
#         print("third arg must be: -1 (for all pixels), a pixel number or a list (eg.: [1,2,3,4])")

# brightness = 80
# brightnessFlag = False


# while True:
#     setLightsToBrightness(brightness)
#     if brightnessFlag == False:
#         brightness += 5
#     else:
#         brightness -= 5
#     if brightness >= maxBrightness:
#         brightnessFlag = True
#     if brightness <= minBrightness:
#         brightnessFlag = False
#     time.sleep(0.005)

