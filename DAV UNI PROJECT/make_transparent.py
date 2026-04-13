from PIL import Image

def make_transparent(img_path, out_path, tolerance=240):
    img = Image.open(img_path).convert("RGBA")
    data = img.getdata()
    
    new_data = []
    for item in data:
        # Check if the pixel is close to white
        # item is (R, G, B, A)
        if item[0] > tolerance and item[1] > tolerance and item[2] > tolerance:
            # Calculate alpha based on how close to pure white it is (for smooth edges)
            # 255 -> alpha 0. tolerance -> alpha 255.
            # Simplified: just make entirely transparent if close to white
            new_data.append((255, 255, 255, 0))
        else:
            # To handle anti-aliasing edges better, we could blend, but simple threshold works ok
            # Actually let's blend the alpha so edges are smooth.
            # Let brightness be average of RGB. Max brightness is 255.
            brightness = (item[0] + item[1] + item[2]) / 3.0
            if brightness > tolerance:
                # scale alpha
                alpha = int(255 - ((brightness - tolerance) / (255 - tolerance) * 255))
                # For dark text on white, making it transparent and keeping original color means
                # the edge pixels will still have some white mixed in. 
                # Better approach: 
                new_data.append((item[0], item[1], item[2], alpha))
            else:
                new_data.append(item)
            
    img.putdata(new_data)
    img.save(out_path, "PNG")

if __name__ == "__main__":
    make_transparent(r"C:\Users\ACER\.gemini\antigravity\brain\431523c4-b87b-47f5-a95c-a32421d298a3\vistra_logo_v5_white_1775886199908.png", r"d:\DAV UNI PROJECT\vistra_logo.png")
