from unstructured.partition.html import partition_html

pagenum=0
currentid=3872081052

#url ='https://www.linkedin.com/jobs/qa-tester-jobs?original_referer=https%3A%2F%2Fwww.google.com%2F&position=1&pageNum={pagenum}&currentJobId={currentid}'
#user inputs positions and grab job ids of each page
# store ids in list
url ='https://www.linkedin.com/jobs/view/3872081052/'
elements=partition_html(url=url)
f='./out.txt'
with open(f,'w') as f:
    f.write("\n\n".join([str(el) for el in elements]))
f.close()

#convert html file to json file
