import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import qrcode

class QRCodeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")
        self.root.geometry("500x600")
        self.root.configure(bg='#ffffff')

        # Title label
        self.title_label = tk.Label(root, text="QR Code Generator", font=('Helvetica', 18, 'bold'), bg='#ffffff')
        self.title_label.pack(pady=20)

        # URL entry frame
        self.url_frame = tk.Frame(root, bg='#ffffff')
        self.url_frame.pack(pady=10)

        self.url_label = tk.Label(self.url_frame, text="Enter URL:", bg='#ffffff', font=('Helvetica', 12))
        self.url_label.pack(side=tk.LEFT, padx=(0, 10))

        self.url_entry = tk.Entry(self.url_frame, width=40, font=('Helvetica', 12), borderwidth=2, relief="solid")
        self.url_entry.pack(side=tk.LEFT, padx=(0, 10))

        # Generate button
        self.generate_button = tk.Button(root, text="Generate QR Code", command=self.generate_qr, font=('Helvetica', 12), bg='#007bff', fg='white', relief="flat", padx=20, pady=10)
        self.generate_button.pack(pady=10)

        # QR code display frame
        self.qr_frame = tk.Frame(root, bg='#ffffff')
        self.qr_frame.pack(pady=10)

        self.qr_image_label = tk.Label(self.qr_frame, bg='#ffffff')
        self.qr_image_label.pack()

        # Save button
        self.save_button = tk.Button(root, text="Save QR Code", command=self.save_qr, font=('Helvetica', 12), bg='#28a745', fg='white', relief="flat", padx=20, pady=10, state=tk.DISABLED)
        self.save_button.pack(pady=10)

    def generate_qr(self):
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showerror("Input Error", "Please enter a URL.")
            return

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')

        # Resize the image to fit within the window
        img.thumbnail((400, 400))
        img_tk = ImageTk.PhotoImage(img)

        # Display the QR code
        self.qr_image_label.config(image=img_tk)
        self.qr_image_label.image = img_tk

        # Enable save button
        self.save_button.config(state=tk.NORMAL)

    def save_qr(self):
        if not hasattr(self, 'qr_image_label') or not self.qr_image_label.image:
            messagebox.showerror("Save Error", "No QR code to save.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if file_path:
            # Save the QR code image
            qr_img = self.qr_image_label.image._PhotoImage__photo
            qr_img.save(file_path)
            messagebox.showinfo("Success", f"QR code saved as {file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeApp(root)
    root.mainloop()
