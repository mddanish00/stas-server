# Changelog

## [0.19.0](https://github.com/mddanish00/stas-server/compare/v0.18.1...v0.19.0) (2024-10-05)


### Features

* update Japanese regex to use Unicode blocks ([88272b4](https://github.com/mddanish00/stas-server/commit/88272b41c19a49260e375e73a3c81db4f0b51d23))


### Bug Fixes

* ambiguous variable name ([e0f430c](https://github.com/mddanish00/stas-server/commit/e0f430c574e5464be6fcc082ee9baccfe8071e73))
* disable strip_bracket on post_clean ([9190a04](https://github.com/mddanish00/stas-server/commit/9190a042a8ffaec5dec17f10c6098fefcf441ebb))
* some newlines not interpreted correctly ([1364b9e](https://github.com/mddanish00/stas-server/commit/1364b9e3ce22cbc7410408ba04da975937a69d98))

## [0.18.1](https://github.com/mddanish00/stas-server/compare/v0.18.0...v0.18.1) (2024-09-22)


### Bug Fixes

* remove print statement from lru_cache_ext function ([f919605](https://github.com/mddanish00/stas-server/commit/f91960511320414080b3f186dc86fbfc12497ad4))

## [0.18.0](https://github.com/mddanish00/stas-server/compare/v0.17.1...v0.18.0) (2024-09-18)


### Features

* models dir support ([383a961](https://github.com/mddanish00/stas-server/commit/383a96120a7cd2e20d55f4a9d670787fa72c5ffa))

## [0.17.1](https://github.com/mddanish00/stas-server/compare/v0.17.0...v0.17.1) (2024-09-17)


### Bug Fixes

* fix not properly pass args and kwargs when cache disabled ([539a501](https://github.com/mddanish00/stas-server/commit/539a50160b3de1c7bb9040f21d60375992d7f5ff))

## [0.17.0](https://github.com/mddanish00/stas-server/compare/v0.16.0...v0.17.0) (2024-09-14)


### Features

* add support of optionally disable cache ([dd24918](https://github.com/mddanish00/stas-server/commit/dd249187c32f47391c9f5a56efd9ef13ad960181))


### Bug Fixes

* split_list_by_condition not used properly for filtering non-Japanese ([b6fa91e](https://github.com/mddanish00/stas-server/commit/b6fa91e41c2e38d2683a4a6cf1af299ca38a7181))

## [0.16.0](https://github.com/mddanish00/stas-server/compare/v0.15.0...v0.16.0) (2024-09-14)


### Features

* add lru_cache_ext to util ([c942938](https://github.com/mddanish00/stas-server/commit/c942938a5ea6b09f03522a73106848c4d3a39cc5))
* apply lru_cache_ext to split_jp ([f854889](https://github.com/mddanish00/stas-server/commit/f8548893c5044d3add64a56a1e77dd28b2e80710))


### Bug Fixes

* unhashable error when cache applied ([9e213fd](https://github.com/mddanish00/stas-server/commit/9e213fd144dc448de4addcfffb145fc3c14ff479))


### Documentation

* update docs ([a9600b2](https://github.com/mddanish00/stas-server/commit/a9600b298c789ecdbb4cac74abb47e7cf9a69f96))

## [0.15.0](https://github.com/mddanish00/stas-server/compare/v0.14.2...v0.15.0) (2024-09-13)


### Features

* add cache to core_translator ([6c1f534](https://github.com/mddanish00/stas-server/commit/6c1f5343a7568c53b9d5cad65da6908d0e728721))
* properly set correct options for cpu and cuda ([a601859](https://github.com/mddanish00/stas-server/commit/a6018590924889c67c799672c12eecce24bad124))
* set new descriptive help message ([93d42c4](https://github.com/mddanish00/stas-server/commit/93d42c4b7eeab79e7ca5c078faab12f29baea8b3))


### Documentation

* update docs ([b540383](https://github.com/mddanish00/stas-server/commit/b540383d3e934ac80f178cce9d40d711cd94057c))

## [0.14.2](https://github.com/mddanish00/stas-server/compare/v0.14.1...v0.14.2) (2024-09-09)


### Documentation

* update README.md ([1e47610](https://github.com/mddanish00/stas-server/commit/1e476105981611b62da8e6c41640c8e4af78deb8))

## [0.14.1](https://github.com/mddanish00/stas-server/compare/v0.14.0...v0.14.1) (2024-09-09)


### Bug Fixes

* remove stas-config script ([6263236](https://github.com/mddanish00/stas-server/commit/6263236d7fd69caa6d446e75b0cfbd4a226c452e))

## [0.14.0](https://github.com/mddanish00/stas-server/compare/v0.13.1...v0.14.0) (2024-09-09)


### Features

* remove config and stas-config ([61818ca](https://github.com/mddanish00/stas-server/commit/61818cad3834ab2f54cd32a70ed7ee73695c7b35))


### Bug Fixes

* add default on ct2_dir option ([6073139](https://github.com/mddanish00/stas-server/commit/6073139149a28f3261f518860c006a426167feed))

## [0.13.1](https://github.com/mddanish00/stas-server/compare/v0.13.0...v0.13.1) (2024-09-01)


### Bug Fixes

* specify correct directory for wheel build ([01d10bd](https://github.com/mddanish00/stas-server/commit/01d10bd04b51470ede3f62577092b0d8740d3ab2))

## 0.13.0 (2024-09-01)


### Bug Fixes

* remove src and put module on root directory ([751d41f](https://github.com/mddanish00/stas-server/commit/751d41f662f737970def78953ce51f5240da4021))


### Miscellaneous Chores

* release 0.13.0 ([3aab13c](https://github.com/mddanish00/stas-server/commit/3aab13c478c0dec8b7c49415b83da3907692c5c4))
