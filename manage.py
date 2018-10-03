from utils import main, build_new_placeholder
import sys

usage_message = """Usage:
Rebuild site:    python manage.py build
Create new page: python manage.py new
"""

if __name__ == "__main__":
  if len(sys.argv) > 1:
    command = sys.argv[1]
    if command == "build":
      print('build started')
      main()
      print('build complete')
    elif command == "new":
      build_new_placeholder()
      print('new template created')
  else:
      print(usage_message)
