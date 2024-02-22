from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas

from lib import image_service


def get_image_size() -> int:
    return 531  # This image size results in almost exactly 1MB per page


def create_pdf(name: str, pages: int):
    img_size = get_image_size()
    c = canvas.Canvas(name, pagesize=(1000, 1000))

    for p in range(pages):
        c.drawString(500, 950, f"Page: {p + 1}")
        img = image_service.color_noise_image(img_size)
        c.drawImage(ImageReader(img), 200, 200)
        c.showPage()
    c.save()
