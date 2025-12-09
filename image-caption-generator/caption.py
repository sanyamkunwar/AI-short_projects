from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration


processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")


image = Image.open("image.png")
inputs = processor(image, return_tensors="pt")


out = model.generate(**inputs)
caption = processor.decode(out[0], skip_special_tokens=True)


print("Caption:", caption)