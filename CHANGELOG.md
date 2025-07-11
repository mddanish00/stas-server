# Changelog

## [0.24.0](https://github.com/mddanish00/stas-server/compare/v0.23.0...v0.24.0) (2025-06-30)


### Features

* recognise sentence that ends with comma ([95baccc](https://github.com/mddanish00/stas-server/commit/95baccce76c84239622351313194bffb5a3a816e))

## [0.23.0](https://github.com/mddanish00/stas-server/compare/v0.22.1...v0.23.0) (2025-06-17)


### Features

* update require-python max to 3.14 ([4721f9d](https://github.com/mddanish00/stas-server/commit/4721f9dc5803b5e3883876503347a450dad43ad7))
* use sentencepiece from my python-index ([4721f9d](https://github.com/mddanish00/stas-server/commit/4721f9dc5803b5e3883876503347a450dad43ad7))

## [0.22.1](https://github.com/mddanish00/stas-server/compare/v0.22.0...v0.22.1) (2025-06-15)


### Documentation

* update documentation for pipx ([92c49c2](https://github.com/mddanish00/stas-server/commit/92c49c2ebde429d7d5563353b1bd2327dea9d769))

## [0.22.0](https://github.com/mddanish00/stas-server/compare/v0.21.0...v0.22.0) (2025-06-15)


### Features

* create global config object ([83a04ca](https://github.com/mddanish00/stas-server/commit/83a04caa2896d4ca269014b5d244d70018d76d20))
* only support Python 3.12 ([c7ae466](https://github.com/mddanish00/stas-server/commit/c7ae4661d3105d2a31bb05daff5b0c598854d366))


### Bug Fixes

* fix mistake when loading config ([f80305f](https://github.com/mddanish00/stas-server/commit/f80305faba8f7afdbaf93db929852a97754fa05f))

## [0.21.0](https://github.com/mddanish00/stas-server/compare/v0.20.3...v0.21.0) (2025-04-23)


### Features

* :zap: migrate from pythonmonkey to PyICU ([a9c659e](https://github.com/mddanish00/stas-server/commit/a9c659edd714dd2f41fd5d5e07ce7d538f3a1600))


### Documentation

* :memo: update about PyICU and python-index ([a6b3e74](https://github.com/mddanish00/stas-server/commit/a6b3e74d01181aee9fa8f87eee235252e1d6bb49))

## [0.20.3](https://github.com/mddanish00/stas-server/compare/v0.20.2...v0.20.3) (2025-03-19)


### Documentation

* :memo: add Python 3.13 notice ([4a2196f](https://github.com/mddanish00/stas-server/commit/4a2196fe3f037ee085b5f5271e2de2758c12ff8c))
* change mention of rye to uv ([4a2196f](https://github.com/mddanish00/stas-server/commit/4a2196fe3f037ee085b5f5271e2de2758c12ff8c))

## [0.20.2](https://github.com/mddanish00/stas-server/compare/v0.20.1...v0.20.2) (2024-11-04)


### Bug Fixes

* **server:** correct condition for empty content check ([0580022](https://github.com/mddanish00/stas-server/commit/058002283bab9aeae24420f93c9a4ca437a0d9be))

## [0.20.1](https://github.com/mddanish00/stas-server/compare/v0.20.0...v0.20.1) (2024-11-04)


### Bug Fixes

* :loud_sound: add correct warning if batch empty received ([62f37d7](https://github.com/mddanish00/stas-server/commit/62f37d77818b1811fab269b4847e7e63aa0e9efa))

## [0.20.0](https://github.com/mddanish00/stas-server/compare/v0.19.2...v0.20.0) (2024-11-03)


### Features

* **server:** bind to all interfaces for accessibility ([c90cfcb](https://github.com/mddanish00/stas-server/commit/c90cfcba483114d11357f02cadeff3fb130444b4))

## [0.19.2](https://github.com/mddanish00/stas-server/compare/v0.19.1...v0.19.2) (2024-10-06)


### Bug Fixes

* add extra bracket and trigger for each get_original_state ([d76b2d8](https://github.com/mddanish00/stas-server/commit/d76b2d8bf42432a3449ec51f6bfef48c0513488f))

## [0.19.1](https://github.com/mddanish00/stas-server/compare/v0.19.0...v0.19.1) (2024-10-05)


### Bug Fixes

* fix some pre and post clean filters ([06c6f06](https://github.com/mddanish00/stas-server/commit/06c6f06d691611819af549202dc56b16c272cff6))

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
