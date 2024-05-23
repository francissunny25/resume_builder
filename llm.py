from langchain_community.document_loaders import AsyncChromiumLoader
from langchain_community.document_transformers import BeautifulSoupTransformer
from langchain_community.document_loaders import AsyncHtmlLoader
from langchain_community.document_transformers import Html2TextTransformer


import pprint

from langchain_text_splitters import RecursiveCharacterTextSplitter
#bc:"https://www.linkedin.com/jobs/view/3791113619/"
urls = ["https://www.espn.com", "https://lilianweng.github.io/posts/2023-06-23-agent/","https://www.linkedin.com/jobs/view/3791113619/"]
loader = AsyncHtmlLoader(urls)
docs = loader.load()

html2text = Html2TextTransformer()
docs_transformed = html2text.transform_documents(docs)
# print(docs_transformed[2].page_content[1221:7000])
def extract_content(text, start_keyword, end_keyword):
    start_index = text.find(start_keyword)
    if start_index == -1:
        return "Start keyword not found"
    end_index = text.find(end_keyword, start_index)
    if end_index == -1:
        return "End keyword not found"
    return text[start_index:end_index + len(end_keyword)]

# Example: Extract content from the third document
doc_content = docs_transformed[2].page_content
extracted_content = extract_content(doc_content, 'About', 'Show less')

# Print the extracted content
print(extracted_content)