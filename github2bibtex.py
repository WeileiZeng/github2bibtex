#!python3
template="""
@misc{_id_
  author={_author_},
  title={_title_},
  year={2023},
  url={_url_},
}
"""

template="""@misc{{{}
  author={},
  title={},
  year={},
  url={},
}}"""

year=2023

def repo2bib(identifier:str):
    info = identifier[:-1].split('/')
    author=info[-2]
    title=info[-1]
#    print("author:{}, title:{}".format(author,title))
    id="{}{}{}".format(author, year, title)
    url="https://github.com/{}/{}".format(author,title)
    return template.format(id, author, title, year, url)


def main():
    filename = 'repos.txt'
    bibs=[]
    with open(filename, 'r') as f:
        repos = f.readlines()
#        print(repos)
        for repo in repos:
#            print(repo)
            bibs.append(repo2bib(repo))
    filename= 'repos.bib'
    with open(filename,'w') as f:
        for b in bibs:
            print(b)
            f.write(b+'\n')
    print('The outputs have been wrote into {}'.format(filename))


if __name__=="__main__":
    main()
