from unstructured.partition.html import partition_html
import json

job_dict = dict()
'''
test_path="children[2].children[3].children[17].children[9].children[1].children[7].children[1].children[1].children[1].children[1].attrs.href"
test_path="children[2].children[3].children[17].children[9].children[1].children[7].children[1].children[3].children[1].children[1].attrs.href"
test_child=test_path.replace('children',"['children']")
py=test_child.replace('.','') 
print(py) 
'''
with open('./job1.json','r') as file:
    jobs_data=json.load(file)
file.close()

jl=1
for i in range(25):
    job_dict[str(i)]={}
    #job_dict[str(i)]['job_id']=jobs_data['children'][2]['children'][3]['children'][17]['children'][9]['children'][1]['children'][7]['children'][1]['children'][jl]['children'][1]['children'][1]['attrs']['href']
    p=str(jobs_data['children'][2]['children'][3]['children'][17]['children'][9]['children'][1]['children'][7]['children'][1]['children'][jl]['children'][1]['children'][1]['attrs']['href'])
    refId=p.index('refId')
    job_dict[str(i)]['id']=p[refId-11:refId-1]
    jl+=2
#find location of jd (scrape) for each job and add to dict


print(job_dict['0']['id'])
texts=[]
parent='https://www.linkedin.com/jobs/view/'
#3x=25
for i in range(25):
    elements=partition_html(url=parent+job_dict[str(i)]['id'])
    text=("\n\n".join([str(el) for el in elements]))
    job_dict[str(i)]['jd']=text
#workaround: use a directory to store text files 
#read each file and store into json object

json_data=[]
for i in range(len(job_dict)):
    json_data.append(job_dict[str(i)])
with open('./jobs.json','w') as file:
    json.dump(json_data,file,indent=4)
    
print(len(job_dict))

  

file.close()

#convert html file to json file
# Send a GET request to the URL
