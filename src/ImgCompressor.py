from PIL import Image
import os

# exemplo de imagem
imagem_path = "typescritp.jpg"


def imagemCompressor(input_path, max_width=None, max_height=None, quality=85):
    output_dir = "Image/"
    output_path = os.path.join(output_dir, imagem_path)
    try:
        with Image.open(input_path) as img:
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")

            if max_width or max_height:
                img.thumbnail((max_width, max_height))

            img.save(output_path, "JPEG", quality=quality)

    except Exception as e:
        print(f"Erro ao abrir imagem: {e}")


if __name__ == "__main__":
    imagemCompressor(
        imagem_path,
        max_width=800,
        max_height=600,
    )
