import cv2
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import datetime
import os


class VideoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lab 7 - Videostream cu filtre (Varianta 2)")

        self.cap = None
        self.running = False  # flag pentru Start/Stop
        self.current_filter = tk.StringVar(value="normal")
        self.frame_count = 0
        self.last_frame = None  

        # INTERFAȚĂ 

        # Zonă video
        self.video_label = tk.Label(self.root, text="Videostream-ul va apărea aici", bg="black", fg="white")
        self.video_label.pack(padx=10, pady=10)

        # Frame pentru butoane
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(padx=10, pady=5)

        self.start_button = tk.Button(buttons_frame, text="Start", width=12, command=self.start_video)
        self.start_button.grid(row=0, column=0, padx=5)

        self.stop_button = tk.Button(buttons_frame, text="Stop", width=12, command=self.stop_video, state=tk.DISABLED)
        self.stop_button.grid(row=0, column=1, padx=5)

        self.capture_button = tk.Button(buttons_frame, text="Captură imagine", width=15, command=self.capture_image, state=tk.DISABLED)
        self.capture_button.grid(row=0, column=2, padx=5)

        # Selectare filtru
        filter_frame = tk.LabelFrame(self.root, text="Filtru imagine")
        filter_frame.pack(padx=10, pady=5, fill="x")

        ttk.Radiobutton(filter_frame, text="Normal", value="normal", variable=self.current_filter).pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(filter_frame, text="Grayscale", value="gray", variable=self.current_filter).pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(filter_frame, text="Edge detection", value="edge", variable=self.current_filter).pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(filter_frame, text="Blur", value="blur", variable=self.current_filter).pack(side=tk.LEFT, padx=5)

        # dimensiune cadre + număr de cadre
        self.info_label = tk.Label(self.root, text="Rezoluție: N/A | Cadre procesate: 0")
        self.info_label.pack(padx=10, pady=5)

        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)


    def start_video(self):
        """Pornește capturarea de la camera web."""
        if self.cap is None:
            self.cap = cv2.VideoCapture(0)
            if not self.cap.isOpened():
                messagebox.showerror("Eroare", "Nu s-a putut deschide camera web.")
                self.cap = None
                return

        self.running = True
        self.frame_count = 0
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.capture_button.config(state=tk.NORMAL)

        self.update_frame()

    def stop_video(self):
        self.running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.capture_button.config(state=tk.DISABLED)

    def apply_filter(self, frame):
        filt = self.current_filter.get()

        if filt == "gray":
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
        elif filt == "edge":
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray, 100, 200)
            frame = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        elif filt == "blur":
            frame = cv2.GaussianBlur(frame, (15, 15), 0)

        return frame

    def update_frame(self):
        if not self.running or self.cap is None:
            return

        ret, frame = self.cap.read()
        if not ret:
            print("Nu s-a putut citi cadrul de la cameră.")
            self.stop_video()
            return

        # salvăm ultimul frame 
        frame = self.apply_filter(frame)
        self.last_frame = frame.copy()

        self.frame_count += 1

        # Obținem dimensiunile
        height, width, _ = frame.shape

    
        self.info_label.config(text=f"Rezoluție: {width} x {height} | Cadre procesate: {self.frame_count}")

        # Convertim imaginea din BGR (OpenCV) în RGB (PIL/Tkinter)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame_rgb)
        imgtk = ImageTk.PhotoImage(image=img)

        # Afișăm în Label
        self.video_label.imgtk = imgtk  
        self.video_label.configure(image=imgtk)

        self.root.after(15, self.update_frame)  

    def capture_image(self):
        if self.last_frame is None:
            messagebox.showwarning("Atenție", "Nu există niciun cadru de salvat.")
            return

        if not os.path.exists("capturi"):
            os.makedirs("capturi")

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"capturi/snapshot_{timestamp}.png"

        cv2.imwrite(filename, self.last_frame)
        messagebox.showinfo("Captură salvată", f"Imaginea a fost salvată ca:\n{filename}")

    def on_closing(self):
        self.running = False
        if self.cap is not None:
            self.cap.release()
        self.root.destroy()


def main():
    root = tk.Tk()
    app = VideoApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()