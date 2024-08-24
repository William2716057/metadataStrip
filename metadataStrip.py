from PIL import Image

#function
def remove_metadata(input_path, output_path):
    #open image file
    with Image.open(input_path) as img:
        #convert image to remove existing metadata
        img_no_metadata = Image.new(img.mode, img.size)
        img_no_metadata.putdata(list(img.getdata()))
        
        #Save new image without metadata
        img_no_metadata.save(output_path)
        
input_image = 'sample.jpg'
output_image ='stripped.jpg'

#call function
remove_metadata(input_image, output_image)
print("Metada stripped and saved as {output_image}")

