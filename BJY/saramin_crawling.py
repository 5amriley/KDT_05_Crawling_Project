from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import collections
collections.Callable = collections.abc.Callable
import pandas as pd

base = 'https://www.saramin.co.kr'

driver = webdriver.Chrome()
driver2 = webdriver.Chrome()

cname_list = []
href_list = []
work_years_list = []

for i in range(1, 43):  # 1 ~ 42
    #example = 'https://www.saramin.co.kr/zf_user/jobs/list/job-category?page=1&cat_kewd=110%2C105%2C106%2C107%2C108%2C109%2C116&search_optional_item=n&search_done=y&panel_count=y&preview=y&isAjaxRequest=0&page_count=50&sort=RL&type=job-category&is_param=1&isSearchResultEmpty=1&isSectionHome=0&searchParamCount=1&tab=job-category#searchTitle'
    url1 = 'https://www.saramin.co.kr/zf_user/jobs/list/job-category?page=' + str(i) + \
               '&cat_kewd=110%2C105%2C106%2C107%2C108%2C109%2C116&search_optional_item=n&search_done=y&panel_count=y&preview=y&isAjaxRequest=0&page_count=50&sort=RL&type=job-category&is_param=1&isSearchResultEmpty=1&isSectionHome=0&searchParamCount=1&tab=job-category#searchTitle'
    driver.get(url1)
    driver.implicitly_wait(5)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # print(html)

    a_company = soup.select('div.list_item > div.box_item > div.col > a.str_tit')

    for a in a_company:
        a_href = a['href']
        url2 = base + a_href
        cname = a.text.strip()
        # print(url2)

        driver2.get(url2)
        driver2.implicitly_wait(5)

        html2 = driver2.page_source
        soup2 = BeautifulSoup(html2, 'lxml')

        p = soup2.select('#content > div > div.main_content.cont_recruit > section > div > div > div > ol > li > p')
        top_area = []   # 채용 직무별 순위 저장 (1위 ~ 4위)
        cnt = 0
        for pp in p:
            # 채용 직무별 순위 저장 (1위 ~ 4위)
            if cnt == 0:
                top_area.append(pp.select_one('strong').text.strip())
            else:
                top_area.append(pp.text.strip())
            cnt += 1
        # print(top_area)

        if (cname not in cname_list) and ('IT개발·데이터' in top_area):
            cname_list.append(cname)
            href_list.append(url2)

            # '기업소개' 창으로 이동
            intro_button = driver2.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div/nav/ul/li[1]/button')
            driver2.execute_script('arguments[0].click();', intro_button)   # '기업소개' 버튼 클릭

            html2 = driver2.page_source
            soup2 = BeautifulSoup(html2, 'lxml')

            # '근속 연수' 탐색
            work_years_h3 = soup2.select('#content > div > div.main_content.cont_introduce > section > div > div > div.box_chart.wide > h3')
            # print(cname, "있음" if work_years_h3 else "없음")
            # print(work_years_h3)
            if work_years_h3:   # 근속 연수 정보 있을 시
                work_year = work_years_h3[0].parent.select_one('div > p > strong').text
                work_years_list.append(float(work_year))
            else:   # 근속 연수 정보 없을 시
                work_years_list.append(0)   # 0 저장
        # print(cname)
    print(f'page {i} 완료')
print('-'*70)

print(f'전체 IT기업 리스트 : {cname_list}')
print('-'*70)

print(f'전체 IT기업 리스트 길이 : {len(cname_list)}')
print(f'href 리스트 길이 : {len(href_list)}')
print(f'work_years 리스트 길이 : {len(work_years_list)}')

driver2.close()
driver2.quit()

driver.close()
driver.quit()

# 데이터프레임 생성
saraminDF = pd.DataFrame({'IT기업': cname_list, '근속년수': work_years_list, '사람인 채용정보 링크': href_list})

# 데이터프레임 csv 파일로 저장
filename = 'saramin_it_data_companies.csv'
saraminDF.to_csv(filename, encoding='utf-8', index=False)
print('데이터프레임 저장 완료')
