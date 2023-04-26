import tkinter
import face_recognition
import cv2
import numpy as np
import time
from tkinter import *
from tkinter import messagebox


video_capture = cv2.VideoCapture(0)


user_image = face_recognition.load_image_file("user.jpg")
user_face_encoding = face_recognition.face_encodings(user_image)[0]



known_face_encodings = [
    user_face_encoding
]
known_face_names = [
    "Vlad"
]


face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
end = time.time()+3
def parol():
    file = open('PASSWORD.txt', encoding='utf-8')
    pas = file.read(10)

    def btn_click():
        k = ent.get()
        if k == pas:
            messagebox.showinfo(title="Успех", message="Верный пароль")
            quit()
        else:
            messagebox.showwarning(title="Ошибка", message="Неправильный пароль")

    def exits():
        if ent.get() != pas:
            messagebox.showwarning(title="Ошибка", message="Неправильный пароль")

    root = Tk()
    root.attributes('-fullscreen', True)
    root.protocol('WM_DELETE_WINDOW', exits)
    root['bg'] = 'red'
    root.call('wm', 'attributes', '.', '-topmost', '1')

    Label(root, text="ЛИЦО НЕ РАСПОЗНАНО", font='Arial 25', bg='red', fg='white').pack()
    Label(root, text="ВВЕДИТЕ ПАРОЛЬ", font='Arial 28', bg='red', fg='white').pack()

    ent = Entry(root, text='', font='Arial 25', width=17)
    ent.pack()

    Button(root, text="ВВЕСТИ", width=16, font="Arial 25", bg='purple', fg='white', command=btn_click).pack()
    root.mainloop()
while time.time() < end:

    ret, frame = video_capture.read()


    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)


    rgb_small_frame = small_frame[:, :, ::-1]


    if process_this_frame:

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:

            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            if matches[0] == True:
                quit()
            else:
                parol()


    process_this_frame = not process_this_frame
    cv2.namedWindow('Video', cv2.WINDOW_KEEPRATIO)
    cv2.imshow('Video', frame)
    cv2.resizeWindow('Video', 1900, 1500)



    if cv2.waitKey(1) & 0xFF == ord('q'):
        parol()
parol()
video_capture.release()
cv2.destroyAllWindows()