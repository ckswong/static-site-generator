print('build started')

pages = [
  {
    "filename": "content/index.html",
    "output": "docs/index.html",
    "title": "Home",
    "link_path": "./index.html",
  }, {
    "filename": "content/blog.html",
    "output": "docs/blog.html",
    "title": "Blog",
    "link_path": "./blog.html",
  }, {
    "filename": "content/contact.html",
    "output": "docs/contact.html",
    "title": "Contact",
    "link_path": "./contact.html",
  }, {
    "filename": "content/projects.html",
    "output": "docs/projects.html",
    "title": "Projects",
    "link_path": "./projects.html",
  },
]

def get_content(path):
  return open(path).read()

def write_content(dest_path, content):
  open(dest_path, 'w+').write(content)

def build_nav_links(current_page, pages, template):
  nav_links = []
  for page in pages:
    is_active_class = "active" if current_page["title"] == page["title"] else ""
    list_item = template.format(is_active_class = is_active_class, path = page["link_path"], title= page["title"])
    nav_links.append(list_item)
  return ("\n").join(nav_links)
  

def main():
  base = get_content("templates/base.html")
  nav_list_item_template = get_content("templates/nav_link.html")
  for page in pages:
    content = get_content(page["filename"])
    nav_links = build_nav_links( page, pages, nav_list_item_template )
    complete_page = base.format( content= content, links= nav_links, title= page["title"] )
    write_content( page["output"], complete_page )

if __name__ == "__main__":
  main()

print('build complete')