from django.http import HttpResponse
from django.shortcuts import render, redirect
from shareRes.models import *       # shareRes에 오류줄이 생길 수도 있는데, 무시하면 된다.
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Create your views here.


def sendEmail(request) :
    checked_res_list = request.POST.getlist('checks')
    inputReceiver = request.POST['inputReceiver']
    inputTitle = request.POST['inputTitle']
    inputContent = request.POST['inputContent']

    mail_html = "<html><body>"
    mail_html += "<h1>맛집 공유</h1>"
    mail_html += "<p>" + inputContent + "<br>"
    mail_html += "발신자님께서 공유하신 맛집은 다음과 같습니다.</p>"

    for checked_res_id in checked_res_list :
        restaurant = Restaurant.objects.get(id = checked_res_id)        # Restaurant에 오류빨간줄이 생길 수도 있는데, 무시하면 된다.
        mail_html += "<h2>" + restaurant.restaurant_name + "</h3>"
        mail_html += "<h4>* 관련 링크</h4>" + "<p>" + restaurant.restaurant_link + "</p><br>"
        mail_html += "<h4>* 상세 내용</h4>" + "<p>" + restaurant.restaurant_content + "</p><br>"
        mail_html += "<h4>* 관련 키워드</h4>" + "<p>" + restaurant.restaurant_keyword + "</p><br>"
        mail_html += "<br>"
        mail_html += "<body><html>"

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("Write your gmail address!", "Write your gmail password!")     # 자기 자신의 구글 이메일 및 비밀번호 기입

    msg = MIMEMultipart('alternative')
    msg['Subject'] = inputTitle
    msg['From'] = "Write your gmail address!"       # 자기 자신의 구글 이메일 기입
    msg['To'] = inputReceiver
    mail_html = MIMEText(mail_html, 'html')
    msg.attach(mail_html)

    print(msg['To'], type(msg['To']))
    server.sendmail(msg['From'], msg['To'].split(','), msg.as_string())
    server.quit()

    return redirect('index')

