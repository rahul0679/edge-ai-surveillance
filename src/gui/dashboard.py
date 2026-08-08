import tkinter as tk
from tkinter import ttk, messagebox
import os

import cv2
from PIL import Image, ImageTk

from src.camera.camera import Camera
from src.detection.detector import Detector
from src.utils.database import fetch_all_detections


class Dashboard(tk.Tk):

    def __init__(self):
        super().__init__()

        # ==========================================
        # WINDOW
        # ==========================================

        self.title("ThirdEye AI Cam")
        self.geometry("1100x750")
        self.minsize(900, 650)
        self.configure(bg="#1e1e1e")

        self.camera = Camera()
        self.running = False
        self.detector = Detector()

        # ==========================================
        # TITLE
        # ==========================================

        title = tk.Label(
            self,
            text="ThirdEye AI Cam",
            font=("Arial", 26, "bold"),
            fg="white",
            bg="#1e1e1e"
        )

        title.pack(pady=(20, 10))

        # ==========================================
        # MAIN AREA
        # ==========================================

        main_frame = tk.Frame(
            self,
            bg="#1e1e1e"
        )

        main_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        # ==========================================
        # CAMERA AREA
        # ==========================================

        camera_container = tk.Frame(
            main_frame,
            bg="#111111"
        )

        camera_container.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 15)
        )

        camera_title = tk.Label(
            camera_container,
            text="LIVE CAMERA",
            font=("Arial", 14, "bold"),
            fg="white",
            bg="#111111"
        )

        camera_title.pack(pady=10)

        self.camera_label = tk.Label(
            camera_container,
            text="Camera is stopped\n\nClick 'Start Camera'",
            font=("Arial", 18),
            fg="#aaaaaa",
            bg="black"
        )

        self.camera_label.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(0, 15)
        )

        # ==========================================
        # RIGHT PANEL
        # ==========================================

        right_panel = tk.Frame(
            main_frame,
            bg="#2b2b2b",
            width=260
        )

        right_panel.pack(
            side="right",
            fill="y"
        )

        right_panel.pack_propagate(False)

        # Status heading

        tk.Label(
            right_panel,
            text="SYSTEM STATUS",
            font=("Arial", 15, "bold"),
            fg="white",
            bg="#2b2b2b"
        ).pack(pady=(25, 10))

        # Status

        self.status_label = tk.Label(
            right_panel,
            text="● Camera Stopped",
            font=("Arial", 13),
            fg="#ff5555",
            bg="#2b2b2b"
        )

        self.status_label.pack(pady=10)

        # Separator

        tk.Frame(
            right_panel,
            height=1,
            bg="#555555"
        ).pack(
            fill="x",
            padx=20,
            pady=20
        )

        # FPS

        self.fps_label = tk.Label(
            right_panel,
            text="FPS\n0",
            font=("Arial", 14, "bold"),
            fg="cyan",
            bg="#2b2b2b"
        )

        self.fps_label.pack(pady=10)

        # Threats

        self.threat_label = tk.Label(
            right_panel,
            text="THREATS\n0",
            font=("Arial", 14, "bold"),
            fg="white",
            bg="#2b2b2b"
        )

        self.threat_label.pack(pady=10)

        # ==========================================
        # BUTTON AREA
        # ==========================================

        button_frame = tk.Frame(
            self,
            bg="#1e1e1e"
        )

        button_frame.pack(
            fill="x",
            pady=(5, 20)
        )

        # Start

        self.start_button = tk.Button(
            button_frame,
            text="START CAMERA",
            font=("Arial", 11, "bold"),
            width=18,
            height=2,
            command=self.start_camera
        )

        self.start_button.pack(
            side="left",
            padx=10,
            expand=True
        )

        # Stop

        self.stop_button = tk.Button(
            button_frame,
            text="STOP CAMERA",
            font=("Arial", 11, "bold"),
            width=18,
            height=2,
            command=self.stop_camera
        )

        self.stop_button.pack(
            side="left",
            padx=10,
            expand=True
        )

        # History

        self.history_button = tk.Button(
            button_frame,
            text="DETECTION HISTORY",
            font=("Arial", 11, "bold"),
            width=18,
            height=2,
            command=self.show_history
        )

        self.history_button.pack(
            side="left",
            padx=10,
            expand=True
        )

        # Exit

        self.exit_button = tk.Button(
            button_frame,
            text="EXIT",
            font=("Arial", 11, "bold"),
            width=18,
            height=2,
            command=self.close
        )

        self.exit_button.pack(
            side="left",
            padx=10,
            expand=True
        )

        # ==========================================
        # WINDOW CLOSE
        # ==========================================

        self.protocol(
            "WM_DELETE_WINDOW",
            self.close
        )

    # ==========================================
    # START CAMERA
    # ==========================================

    def start_camera(self):

        if self.running:
            return

        print("Starting camera...")

        if not self.camera.start():

            print("Camera could not be opened.")

            self.status_label.config(
                text="● Camera Error",
                fg="#ff3333"
            )

            messagebox.showerror(
                "Camera Error",
                "Could not open webcam.\n\n"
                "Check that your camera is connected "
                "and not being used by another application."
            )

            return

        print("Camera started successfully.")

        self.running = True

        self.status_label.config(
            text="● Camera Running",
            fg="#00ff66"
        )

        self.update_frame()

    # ==========================================
    # UPDATE CAMERA FRAME
    # ==========================================

    def update_frame(self):

        if not self.running:
            return

        ret, frame = self.camera.read()

        if ret:

            # ==============================
            # YOLO DETECTION
            # ==============================

            frame, fps, threats, latest = self.detector.detect(frame)

            # ==============================
            # UPDATE INFORMATION
            # ==============================

            self.fps_label.config(
                text=f"FPS\n{fps}"
            )

            self.threat_label.config(
                text=f"THREATS\n{threats}"
            )

            # ==============================
            # THREAT STATUS
            # ==============================

            if latest:

                self.status_label.config(
                    text=f"⚠ {latest.upper()} DETECTED",
                    fg="#ff3333"
                )

            else:

                self.status_label.config(
                    text="● Monitoring",
                    fg="#00ff66"
                )

            # ==============================
            # CAMERA DISPLAY
            # ==============================

            frame = cv2.cvtColor(
                frame,
                cv2.COLOR_BGR2RGB
            )

            image = Image.fromarray(frame)

            image.thumbnail((760, 520))

            photo = ImageTk.PhotoImage(image)

            self.camera_label.config(
                image=photo,
                text=""
            )

            # IMPORTANT: Keep reference alive
            self.camera_label.image = photo

        else:

            self.status_label.config(
                text="● Camera Read Error",
                fg="#ff3333"
            )

        # Continue loop
        self.after(
            15,
            self.update_frame
        )

    # ==========================================
    # STOP CAMERA
    # ==========================================

    def stop_camera(self):

        print("Stopping camera...")

        self.running = False

        self.camera.stop()

        self.camera_label.config(
            image="",
            text="Camera is stopped\n\nClick 'Start Camera'"
        )

        self.camera_label.image = None

        self.status_label.config(
            text="● Camera Stopped",
            fg="#ff5555"
        )

        self.fps_label.config(
            text="FPS\n0"
        )

        self.threat_label.config(
            text="THREATS\n0"
        )

    # ==========================================
    # DETECTION HISTORY
    # ==========================================

    def show_history(self):

        history_window = tk.Toplevel(self)

        history_window.title(
            "Detection History - ThirdEye AI Cam"
        )

        history_window.geometry("850x500")

        history_window.configure(
            bg="#1e1e1e"
        )

        # Title
        tk.Label(
            history_window,
            text="Detection History",
            font=("Arial", 20, "bold"),
            fg="white",
            bg="#1e1e1e"
        ).pack(pady=15)

        # Table container
        table_frame = tk.Frame(
            history_window,
            bg="#1e1e1e"
        )

        table_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        columns = (
            "ID",
            "Timestamp",
            "Object",
            "Confidence",
            "Snapshot"
        )

        tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        tree.heading("ID", text="ID")
        tree.heading("Timestamp", text="Timestamp")
        tree.heading("Object", text="Object")
        tree.heading("Confidence", text="Confidence")
        tree.heading("Snapshot", text="Snapshot")

        tree.column(
            "ID",
            width=50,
            anchor="center"
        )

        tree.column(
            "Timestamp",
            width=180,
            anchor="center"
        )

        tree.column(
            "Object",
            width=100,
            anchor="center"
        )

        tree.column(
            "Confidence",
            width=100,
            anchor="center"
        )

        tree.column(
            "Snapshot",
            width=300
        )

        tree.pack(
            side="left",
            fill="both",
            expand=True
        )

        # Scrollbar
        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=tree.yview
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        tree.configure(
            yscrollcommand=scrollbar.set
        )
        
                # ==================================
        # Open Snapshot on Double Click
        # ==================================

        def open_snapshot(event):

            selected = tree.selection()

            if not selected:
                return

            item = tree.item(selected[0])

            values = item["values"]

            if len(values) < 5:
                return

            snapshot_path = values[4]

            print("Opening snapshot:", snapshot_path)

            if not os.path.exists(snapshot_path):

                messagebox.showerror(
                    "Snapshot Not Found",
                    f"Snapshot file not found:\n\n{snapshot_path}"
                )

                return

            try:

                image = Image.open(snapshot_path)

                image.thumbnail((800, 600))

                viewer = tk.Toplevel(history_window)

                viewer.title(
                    "Snapshot - ThirdEye AI Cam"
                )

                viewer.configure(
                    bg="#1e1e1e"
                )

                photo = ImageTk.PhotoImage(image)

                image_label = tk.Label(
                    viewer,
                    image=photo,
                    bg="#1e1e1e"
                )

                image_label.image = photo

                image_label.pack(
                    padx=20,
                    pady=20
                )

            except Exception as e:

                messagebox.showerror(
                    "Error",
                    f"Could not open snapshot:\n\n{e}"
                )

        tree.bind(
            "<Double-1>",
            open_snapshot
        )

        # ==================================
        # Load Database
        # ==================================

        try:
            rows = fetch_all_detections()

            for row in rows:
                tree.insert(
                    "",
                    "end",
                    values=(
                        row[0],
                        row[1],
                        row[2].capitalize() if row[2] else "",
                        f"{row[3] * 100:.1f}%" if isinstance(row[3], (int, float)) else row[3],
                        row[4]
                    )
                )

        except Exception as e:
            print("History Error:", e)

        # ==================================
        # Close Button
        # ==================================

        tk.Button(
            history_window,
            text="Close",
            width=15,
            command=history_window.destroy
        ).pack(pady=15)

    # ==========================================
    # CLOSE APPLICATION
    # ==========================================

    def close(self):

        print("Closing ThirdEye AI Cam...")

        self.running = False

        self.camera.stop()

        self.destroy()


# ==============================================
# TEST
# ==============================================

if __name__ == "__main__":

    app = Dashboard()

    app.mainloop()