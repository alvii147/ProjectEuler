import re
import os

PROJECT_EULER_URL = 'https://projecteuler.net'
LOGO_URL = 'https://projecteuler.net/themes/logo_default.png'
EULER_PORTRAIT_URL = 'https://www.thoughtco.com/thmb/dh47K7WcNuQYSw3Zn1DR5YgfCZo=/1095x1095/smart/filters:no_upscale()/euler2-5baa451cc9e77c005008b61e.png'
SOLUTION_ICON_URL = 'https://cdn-icons-png.flaticon.com/512/190/190708.png'
LINK_ICON_URL = 'https://www.iconsdb.com/icons/preview/purple/link-xxl.png'

if __name__ == '__main__':
    with open('../README.md', 'w') as readme_file:
        readme_file.write('# Project Euler Problems & Solutions\n\n')
        readme_file.write(f'<img alt="Project Euler Logo" src="{LOGO_URL}" width="400"/>\n\n')
        readme_file.write(f'<img alt="Project Euler Logo" src="{EULER_PORTRAIT_URL}" width="500"/>\n\n')
        readme_file.write(f'This repository contains solutions to [Project Euler]({PROJECT_EULER_URL}) problems.\n\n')
        readme_file.write('ID | Description / Title | Solution | External Link\n')
        readme_file.write('--- | ---\n')

        for dirname in sorted(os.listdir('../')):
            match = re.search('(\d+)_(\S+)', dirname)
            if match:
                problem_id, problem_title = match.groups()
                problem_title = problem_title.replace('_', ' ')
                problem_url = PROJECT_EULER_URL + f'/problem={problem_id}'

                readme_file.write(f'{problem_id} | {problem_title} | [![Solution Icon]({SOLUTION_ICON_URL})]({dirname}) | [![Link Icon]({LINK_ICON_URL})]({problem_url})\n')