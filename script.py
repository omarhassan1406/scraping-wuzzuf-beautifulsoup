#script to find the company name and jop title and the experince in wuzzuf for data science jops for the first 20 pages


from bs4 import BeautifulSoup
import requests

num = 0
company_names = []
experinces = []
titles = []
info = []
while(num != 400):
    html_text = requests.get('https://wuzzuf.net/a/Data-Science-Jobs-in-Egypt?start='+str(num)).text
    soup = BeautifulSoup(html_text , 'lxml')
    
    block_name = soup.find_all('span' , class_ = 'company-name')
    
    
    for block in block_name:
        if (block.find('span') == None):
            company_names.append(block.text)
        else:
            block_name2 = block.find('span').text
            company_names.append(block_name2)
    
    
    
    block_details = soup.find_all('div' , class_ = 'job-details')
    
    
    for block in block_details:
        if (block.find_all('span') == None):
            experinces.append(block.text.strip())
        else:
            block_details2 = block.find_all('span')
            experinces.append(block_details2[1].text.strip())
    
    
    block_title = soup.find_all('h2' , class_ = 'job-title')
    
    for block in block_title:
        titles.append(block.find('span').text)
        more_info = block.a['href']
        info.append(more_info)
    
    
    
    j=0
    for i in company_names:
        if (i != 'Confidential'):
            print(f'''
              company name : {i}
              experinces : {experinces[j]}
              jop title : {titles[j]}
              more info : {info[j]}
              ''')
        j+=1
        
              
    num += 20