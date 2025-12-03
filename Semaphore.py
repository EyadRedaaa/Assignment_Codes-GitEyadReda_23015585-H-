#Semaphore Code
import threading
import time
# Semaphore(1): معناها إننا عندنا مكان واحد بس متاح (دكتور واحد أو غرفة كشف واحدة)
# الـ Semaphore عامل زي "البواب" اللي بيعد الناس، لو الرقم 1 يبقى هيدخل واحد ويقفل الباب
receptionist = threading.Semaphore(1)

def Enter_examination_Room(n):
    print(f"Patient {n} Waiting For His Turn \n") # المريض وصل العيادة بس لسه مادخلش الغرفة
    # acquire(): المريض بيحاول يدخل.
    # لو الـ Semaphore قيمته 1، هيدخل وينقص القيمة لـ 0 (يقفل الباب وراه).
    # لو القيمة 0 (حد جوه)، هيفضل واقف هنا (Blocked) لحد ما اللي جوه يخرج.
    receptionist.acquire()
    print(f"Patient {n} In the Examination Room \n")  # هنا المريض دخل بالفعل
    time.sleep(2) # وقت الكشف (ثانيتين)
    print(f"Patient {n} Out the Examination Room \n")  # release(): المريض خرج، فبيزود قيمة الـ Semaphore تاني لـ 1
    receptionist.release()  # وده بيدي إشارة للي عليه الدور بره إنه يقدر يدخل دلوقتي

Patients = []
for i in range(10):     # بنعمل لوب عشان نكريت 10 مرضى
    Patient = threading.Thread(target=Enter_examination_Room , args=(i,))  # args=(i,): التعديل هنا، بعتنا الـ i (رقم المريض) عشان يطبع Patient 1, Patient 2 وهكذا
    Patients.append(Patient)
    Patient.start()
