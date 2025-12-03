#Threading Code
import threading # استدعاء مكتبة الـ Threading عشان نقدر نشغل عمليات على التوازي (Concurrency)
import time # استدعاء مكتبة الوقت، عشان نستخدم الـ sleep ونعمل تأخير وهمي

# def -> Definition: هنا بنعرف الفانكشن اللي الـ Thread الأول هينفذها
def print1():
    # threading.current_thread().name: كود بيجيب اسم الـ Thread اللي شغال دلوقتي عشان نعرف إحنا فين
    print('Start of Thread 1 :' , threading.current_thread().name)
    time.sleep(2) # الـ Thread ده هينام (يوقف شغل) لمدة ثانيتين (كأنه بيعمل عملية بتاخد وقت)
    print('End of Thread 1 :' , threading.current_thread().name)


# هنا بنعرف الفانكشن بتاعة الـ Thread التاني
def print2():
    print('Start of Thread 2 :' , threading.current_thread().name)
    time.sleep(5) # ده هينام لمدة 5 ثواني (مدة أطول من الأولاني)
    print('End of Thread 2 :' , threading.current_thread().name)


# a: هنا بنجهز (Initialize) الـ Thread الأول بس لسه مش بنشغله
# target=print1: بنحدد الفانكشن اللي هينفذها (من غير أقواس () عشان متشتغلش فوراً)
# name="thread1": بندي اسم مميز للـ Thread عشان يظهر في جملة الطباعة فوق
x = threading.Thread(target= print1, name= "thread1")

# b: بنجهز الـ Thread التاني وبنربطه بالفانكشن print2
b = threading.Thread(target= print2, name= "thread2")

# start(): دي "ساعة الصفر"، هنا الـ Threads بتبدأ تشتغل فعلياً مع بعض في نفس الوقت
x.start()
b.start()
