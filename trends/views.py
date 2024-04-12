from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Keyword, Trend
import requests
from bs4 import BeautifulSoup
import datetime
from selenium import webdriver
import re
import matplotlib.pyplot as plt
import os
from io import BytesIO
import base64

def keyword(request):
    """ View to add new keywords and display all keywords. """
    if request.method == "POST":
        keyword_name = request.POST.get('keyword_name')
        if keyword_name:
            Keyword.objects.create(name=keyword_name)
        return redirect('trends:keyword')
    else:
        keywords = Keyword.objects.all()
        return render(request, 'trends/keyword.html', {'keywords': keywords})

def keyword_detail(request, pk):
    """ View to delete a specific keyword. """
    keyword = get_object_or_404(Keyword, pk=pk)
    keyword.delete()
    return redirect('trends:keyword')

def crawling(request):
    """ 저장된 키워드에 대해 크롤링을 수행하고 결과를 저장합니다. """
    keywords = Keyword.objects.all()

    for keyword in keywords:
        url = f'https://www.google.com/search?q={keyword.name}'
        #response = requests.get(url)
        driver = webdriver.Chrome()
        driver.get(url)

        html = driver.page_source

        soup = BeautifulSoup(html, 'html.parser')
        result_stats = soup.find('div', {'id': 'result-stats'})
        if result_stats:
            results_text = result_stats.text

            # 결과 텍스트에서 숫자 추출
            result_count_match = re.search(r'([0-9,]+)개', results_text)
            if result_count_match:
                result_count_str = result_count_match.group(1)
                # 쉼표 제거 후 정수로 변환
                result_count = int(result_count_str.replace(',', ''))

                if Trend.objects.filter(name=keyword.name, search_period='all').exists():
                    trend = Trend.objects.get(name=keyword.name, search_period='all')
                    trend.result = result_count
                    trend.save()
                else:
                    Trend.objects.create(
                        name=keyword.name,
                        result=result_count,
                        search_period='all',
                    )
        
        else:
            # 결과가 없는 경우 처리
            result_count = 0
            if Trend.objects.filter(name=keyword.name, search_period='all').exists():
                trend = Trend.objects.get(name=keyword.name, search_period='all')
                trend.result = result_count
                trend.save()
            else:
                Trend.objects.create(
                    name=keyword.name,
                    result=result_count,
                    search_period='all',
                )
    trends = Trend.objects.all()
    context = {
        'trends' : trends,
    }
    return render(request, 'trends/crawling.html', context)

# 그래프 처리
def export_pic():
    # BytesIO 객체를 생성하고, buffer라는 변수에 할당
    buffer = BytesIO()
    # buffer에 그래프를 png 형태로 저장
    plt.savefig(buffer, format='png')
    # buffer의 내용을 인코딩
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n','')
    buffer.close()
    return img_base64

def crawling_histogram(request):
    # 데이터 준비
    trends = Trend.objects.all()
    name = [trend.name for trend in trends]
    result = [trend.result for trend in trends]

    # 히스토그램에 데이터 입력
    plt.figure(figsize=(10, 6))
    plt.bar(name, result, label="Trend")

    # 그래프 출력 조정
    plt.title('Technology Trend Analysis')
    plt.xlabel('Keyword')
    plt.ylabel('Result')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()

    context = {
        'image': f'data:image/png;base64, {export_pic()}',
    }
    return render(request, 'trends/crawling_histogram.html', context)


def crawling_advanced(request):
    """ 저장된 키워드에 대해 크롤링을 수행하고 결과를 저장합니다. """
    keywords = Keyword.objects.all()

    for keyword in keywords:
        url = f'https://www.google.com/search?q={keyword.name}&tbs=qdr:y'
        driver = webdriver.Chrome()
        driver.get(url)

        html = driver.page_source

        soup = BeautifulSoup(html, 'html.parser')
        result_stats = soup.find('div', {'id': 'result-stats'})
        if result_stats:
            results_text = result_stats.text

            # 결과 텍스트에서 숫자 추출
            result_count_match = re.search(r'([0-9,]+)개', results_text)
            if result_count_match:
                result_count_str = result_count_match.group(1)
                # 쉼표 제거 후 정수로 변환
                result_count = int(result_count_str.replace(',', ''))

                if Trend.objects.filter(name=keyword.name, search_period='year').exists():
                    trend = Trend.objects.get(name=keyword.name, search_period='year')
                    trend.result = result_count
                    trend.save()
                else:
                    Trend.objects.create(
                        name=keyword.name,
                        result=result_count,
                        search_period='year',
                    )
        
        else:
            # 결과가 없는 경우 처리
            result_count = 0
            if Trend.objects.filter(name=keyword.name, search_period='year').exists():
                trend = Trend.objects.get(name=keyword.name, search_period='year')
                trend.result = result_count
                trend.save()
            else:
                Trend.objects.create(
                    name=keyword.name,
                    result=result_count,
                    search_period='year',
                )
    trends = Trend.objects.filter(search_period = 'year')
    name = [trend.name for trend in trends]
    result = [trend.result for trend in trends]


    # 히스토그램에 데이터 입력
    plt.figure(figsize=(10, 6))
    plt.bar(name, result, label="Trend")

    # 그래프 출력 조정
    plt.title('Technology Trend Analysis')
    plt.xlabel('Keyword')
    plt.ylabel('Result')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()

    context = {
        'image': f'data:image/png;base64, {export_pic()}',
    }


    return render(request, 'trends/crawling_advanced.html', context)