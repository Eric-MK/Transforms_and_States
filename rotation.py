import cairo
import os
import math

#set up surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 600)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8,0.8,0.8)
ctx.paint()


x = 250
y = 300
width = 200
height = 100

# before rotation
ctx.set_source_rgb(0,0,0)
ctx.rectangle(x,y,width, height)
ctx.set_dash([5,5])
ctx.stroke()



# applying rotation
ctx.rotate(math.pi/6)

# drawing the same rectangle after rotation
ctx.set_source_rgb(0,0.5,0.5)
ctx.rectangle(x,y,width,height)
ctx.fill()




# Save the result to a PNG file in the "output" folder
output_folder = "output_folder"

output_path = os.path.join(output_folder, "rotation.png")
surface.write_to_png(output_path)

print(f"Saved the result to: {output_path}")