import cairo
import os

#set up surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 600)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8,0.8,0.8)
ctx.paint()

# rectangle blue
ctx.set_source_rgb(0,0,0.5)
ctx.translate(200, 300)
ctx.rectangle(-100, -100, 200, 200)
ctx.fill()

# rectangle green
ctx.set_source_rgb(0,0,0.5)
ctx.translate(200, 100)
ctx.rectangle(-100, -100, 200, 200)
ctx.fill()

# Save the result to a PNG file in the "output" folder
output_folder = "output_folder"

output_path = os.path.join(output_folder, "translation.png")
surface.write_to_png(output_path)

print(f"Saved the result to: {output_path}")