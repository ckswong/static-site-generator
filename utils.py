import glob
import os
from jinja2 import Template

def get_content(path):
  return open(path).read()

def write_content(dest_path, content):
  open(dest_path, 'w+').write(content)

def build_new_placeholder():
  placeholder_content = """
  <h1>New Content!</h1>
  <p>New content...</p>
  """
  write_content('./content/new_content_page.html', placeholder_content)

def main():
  pages = []
  content_html_files = glob.glob("content/*.html")

  for html_file in content_html_files:
    file_name = os.path.basename(html_file)
    name, extension = os.path.splitext(file_name)
    title = name if name != "index" else "about"
    pages.append({
      "content_path": html_file,
      "filename": file_name,
      "title": title,
      "output": "docs/" + file_name,
    })

  template_html = open("./templates/base.html").read()
  template = Template(template_html)

  for page in pages:
    content = get_content(page["content_path"])

    complete_page = template.render(
        title= page["title"],
        content= content,
        pages= pages,
    )
    write_content( page["output"], complete_page )