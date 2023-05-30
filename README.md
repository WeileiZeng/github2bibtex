# github2bibtex
Convert github repo to a bibtex item

- save repo names or links in each line of `repos.txt`
- run `python3 github2bibtex.py`
- see results in stdout as well as in `repos.bib`


sample `repos.txt`
```
https://github.com/WeileiZeng/github2bibtex
Daisyforest/SWQsim
```






sample `repos.bib`
```
@misc{WeileiZeng2023github2bibtex
  author=WeileiZeng,
  title=github2bibtex,
  year=2023,
  url=https://github.com/WeileiZeng/github2bibtex,
}
@misc{Daisyforest2023SWQsim
  author=Daisyforest,
  title=SWQsim,
  year=2023,
  url=https://github.com/Daisyforest/SWQsim,
}
```
