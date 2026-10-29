from PIL import Image, ImageEnhance, ImageFilter
import cv2
import numpy as np

# 1. Load your photo
img_path = "wa_image_5150271782679773689.jpg"
img = Image.open(img_path)

# 2. Enhance - Cinematic Look
# Brightness + Contrast
enhancer = ImageEnhance.Brightness(img)
img = enhancer.enhance(1.1)  # +10% brightness

enhancer = ImageEnhance.Contrast(img)
img = enhancer.enhance(1.2)   # +20% contrast

enhancer = ImageEnhance.Color(img)
img = enhancer.enhance(1.25)  # +25% color pop - purple dress ku

enhancer = ImageEnhance.Sharpness(img)
img = enhancer.enhance(1.3)   # Sharpen

# 3. Save enhanced
img.save("enhanced_cinematic.jpg")
print("Enhanced photo saved!")

# 4. For DSLR Blur Background - Advanced with OpenCV
# Face detect panni background mattum blur pannalam
def dslr_blur_effect(image_path):
    img = cv2.imread(image_path)
    
    # Simple blur for background simulation
    # Full image blur
    blurred = cv2.GaussianBlur(img, (21, 21), 0)
    
    # For real portrait mode, you need segmentation
    # Here is simple center focus (face area sharp)
    h, w = img.shape[:2]
    mask = np.zeros((h, w), dtype=np.uint8)
    cv2.circle(mask, (w//2, h//2), int(h*0.4), 255, -1)
    mask = cv2.GaussianBlur(mask, (51, 51), 0)
    mask = mask / 255.0
    
    # Combine sharp center + blurred edges
    # (You can improve this with face detection)
    result = (img * mask[:,
