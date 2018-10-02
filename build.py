print('build started')

template_top = open('./templates/top.html').read()
template_header = open('./templates/header.html').read()
template_bottom = open('./templates/bottom.html').read()

pages = ['index', 'blog', 'contact', 'projects']

for page in pages:
  content_path = './content/' + page + '.html'
  output_path = './docs/' + page + '.html'
  combined_html = template_top + template_header + open(content_path).read() + template_bottom
  open(output_path, 'w+').write(combined_html)

print('build complete')