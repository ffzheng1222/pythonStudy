#!/usr/bin/env python
# -*- coding: utf-8 -*


import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


def arrange_github_data(resp_dicts):
    print("Total repositories: ", resp_dicts['total_count'])

    repo_dicts = resp_dicts['items']
    print("Repositories returned: ", len(repo_dicts))

    # repo_dict = repo_dicts[0]
    # print("\n Keys: ", len(repo_dict))
    # for key in sorted(repo_dict.keys()):
    #     print(key)

    # print("\nSelected information about each repository:")
    # for repo_dict in repo_dicts:
    #     print('\nName: ', repo_dict['name'])
    #     print('Owner: ', repo_dict['owner']['login'])
    #     print('Start: ', repo_dict['stargazers_count'])
    #     print('Repository: ', repo_dict['html_url'])
    #     print('Description: ', repo_dict['description'])

    names, plot_dicts = [], []
    for repo_dict in repo_dicts:
        names.append(repo_dict['name'])

        plot_dict = {
            'value': repo_dict['stargazers_count'],
            'label': str(repo_dict['description']),
            'xylina': repo_dict['html_url'],
        }
        plot_dicts.append(plot_dict)

    my_style = LS('#333366', base_style=LCS)

    my_config = pygal.Config()
    my_config.x_label_rotation = 45
    my_config.show_legend = False
    my_config.title_font_size = 24
    my_config.label_font_size = 14
    my_config.margin_label_font_size = 18
    my_config.truncate_label = 15
    my_config.show_y_guides = False
    my_config.width = 1000

    chart = pygal.Bar(my_config, style=my_style)
    chart.title = 'Most-Starred python Project on GitHub'
    chart.x_labels = names

    chart.add('', plot_dicts)
    chart.render_to_file('python_repos.svg')


def get_github_data():
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

    r = requests.get(url)
    print("Status Code: ", r.status_code)

    response_dicts = r.json()
    print(response_dicts.keys())

    # 整理cong Github 上获取的数据
    arrange_github_data(response_dicts)


def main():
    get_github_data()


#### main program ###
if __name__ == '__main__':
    main()
