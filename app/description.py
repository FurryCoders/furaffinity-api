from faapi import __version__ as faapi_version  # type:ignore

description: str = f"""
[![](https://img.shields.io/gitlab/v/tag/MatteoCampinoti94/furaffinity-api?label=version&sort=date&logo=gitlab)](https://gitlab.com/MatteoCampinoti94/furaffinity-api)
[![](https://img.shields.io/pypi/v/faapi/{faapi_version}?label=faapi&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAD5klEQVR4nJyWW2hdRRfHfzN7n3OS0HztF5u0JCWJUVo1tijV5EXTxlasFnsRn0RBUKP4VhREpUqgGgiSekPTCxJspQ95qS8m4AUtWkERC9ImYJuojTS1GlMTzznJ3nuWzO7suj0mse3AYpg9M/+11n9dZntc/tCAvSeA7+YrGtoBpI1QVwo2F3jpSMBrgbeBL4FuIOv2Lll5Ar4CeBzYnvpeA3zvaEnkObfvXw74OuDXFMgb7vvrbl0EZoAA+GwBr/9FgZVFwOkUUOTAlgHfuHXkwO182MUp62Y/TZdfYr29sN7RE6b4zQCVKY9Cd97KwZTSBUei7DEHMOtmK784JU+X8N/r7mwF3gMGgGfmC3zC4doSECtPpM5tATqB+9y6Z47zPXMwdLGA7NgB/AycBJ4EGoDXgCNasaduaXalO3ePBVSKwPdUoFUcK+v5kKcV86VuPVAHtAKbnMuTJRZavpuBXQ4wSYZAXdg/mPZAO03XAh8CeQdSSINaKy3I0v9lii893CgPtdccADbbvRsbKqSro0lqq7L27IhSNDpMnc7dPmAjUObWyRw6q/xcRuvBzhsyLasqzU/nZtYoGNRaPZvx1NebW6uOf/7KmukH11dvEeGHp7bVWQUmzf+pVPEYJ7H1Wqt4vvmaRTJ+oCVw3/tSBFuLl8kHtw3JR20bG2tyWj5Z5zXU5C42NAv2pksv7QD+ESClIIpEJqZCL+PrfGW5txPFI9YwrRn2tPru2MnphmKZNzN6qFUKE7Oc2rs2BkuKZjew04HrdOFYTSKwsq48+iMfKWOk+89i1CbCfqAJyEVGqn+fCsvLbCwLkRgBK0kMjAO1WbEBOONSNrLpFhmh84F6+rtXe30fn5XIyFGtVaczItQqpjDqHRgPZSp8p1A0e8syKioNsnHVaptXm6sBz4gYrRWHjpyTff1j6t6WqkgpzhuJW0f88IjEd7321Yt9Ve69K8JbRi5QXdoBAxcTC34XMC4SM2SGxwqqp3+MVXXl/nUrKn4TI10uSBkj4nla/bjp1v9PBL7ag+JYwuxcLTZ0SkaA+5NGphThkkrf+J7KD53On99w05JXtY6LsUOEbWFkGuurc6NmvLhc5O/WPV8PDx1dXwAviEhGBH90vKg9rSqiwdvv3P3o1Ysjw1fAPuB9BtvuDgNp9nx1IuurOMWz248u+AoFjuMuEQKtVcfZyeDMtyPTA7XVuZeblpfJVZV+fxiJGt1/yx2zhahXKXYopYZFYmYMl/iOqlTqmsPPX8/WXSfg03YNYoLJgFTtSOo81oP/fOZSvyexRVlf+cdfbIbZKAEnVfVe6W/MXwEAAP//w2SKjLOWmJcAAAAASUVORK5CYII=)](https://pypi.org/project/faapi/{faapi_version})
[![](https://img.shields.io/gitlab/pipeline-status/MatteoCampinoti94/furaffinity-api?branch=main&logo=githubactions)](https://gitlab.com/MatteoCampinoti94/furaffinity-api)
[![](https://img.shields.io/uptimerobot/ratio/m790058594-4715e1cc558179234ce66c3c?logo=heroku)](https://stats.uptimerobot.com/3vj5KUXGng)

[![](https://img.shields.io/badge/robots-json-lightblue?logo=probot)](/robots.json)
[![](https://img.shields.io/badge/Swagger%20UI-docs-85EA2D?logo=swagger)](/docs)
[![](https://img.shields.io/badge/Redoc-docs-0044D3?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAACXBIWXMAAAsTAAALEwEAmpwYAAAE7UlEQVRYw61XW6hVRRhea+0z63CSLtZLN7siQbdT2Y3Ep1lKBD1IJT1I5oNgD70ZFAQFQdRDgUgkRRH5EOJLpIhCDxqdI1F2oBlTuxwjzZNaFlkQHOn0/TPfzJq1zt5n7w0u+Pjn+s8//23+lWX4yspmqjKB5iXavt8fqkZekkeEtlnfLyxWcXNgbgcSoD4QbQ1BtCnQ7wBFQ5jK9hZAxRu7hSWYjYKO1TBjHF8IoxCggACp8HkURPcQhLfIOfm2quzvoN8Dh4BvMG9BjwInwfwE6HGBIm3hR+Bz4HUceH9yqY7TTjdtUNogwCvYdBg4hvacg3b0b+BT4AAxiTWureqxL5S2X4OexmFuL+b2YP+tXgPQTjS37eIDojodzSEqHwfeAP6lMOtrh2vaNvgC1b8IeAB4P16iso9zbZHuSXzASRgW5KrpzXcAR3ijZymAwm3F3qBif1vKWOnHE7+yK9A+RSFWR3N0N0MDwXlG2L8EOExGD3ptRbNlbSeLIe3GzPWl+JW2sxi/KdVE/9D0WlFkOA4KnzAT7nbaRcoG4EX0N6H/XCmo7CbQ53HgerQvomlXOQ1q+5GqQ3WA/KD9LbAhaOItamEZcLlvm7nE1nO1A5pZ0KsSDe3kmqiFAZKUSX1D6N1k8hpVfQvovcCddFrAoG2wztzIPSN00kcp7EY6cycb5KMpcqpuEW5yFpv3BedtOp1bE0HnzIglFH4b54YSIEtsJwnqu7KOnDeVxH5lp4GfEkxDoBms2UanvQxjf4Du8il7CAESISCAOcSw9J6v7csU6CDmp8B4Cu0pCHUQ9FtgCzWwGHv/RH9nCMeBBKC6QshdjAPOgdGeRvjNC8E0DG1IXDfQBO9xfX8BQtYLYQMsJ5OX2EeMm4eBlTgMAK1A0S+FaokU7PWXWOMiRNunqc3OAGEY0+4Ic8GH9OT7KMDHaQiqeSFpX/A83N79HL8mJLsFVF4XG6VPt6LOFWSwW9VJ6jasWYf+U2ivxZ61aK8rfV9oCMUnfSIyW2mSTqNYadsOk2LzjqiJDK7D2Cl/e3N7mtPTMEwiI0nR5h7Q8zj0LHhcSfvnKgiQOk8oJpRuvAsa46d5+yc4X9SR4doF34a89abIKzgb3hC+gp0gbFoPUN2uDWb2Cow/gvZ2bj4vTkQBizTZJJBXVLRytRysnKmMvKD/lP5VzKjVqOlWQeIGt2KBFB9/pXndJZDKSmV0jFXPD0RoT0MTP+Ow30L9oPy+d8FvMXl3Yni2n2Kfah19leXYcd46eLMkkAlJNhAKCcZ85dqOSt8lnS9JfwH+Ay9xuh2M/1gRBTPXAmiaIISc7yOHG3nxNic23Jjk9XiTtDoi81GMPYR2rIjQXtOuiFRdEZm0qGhUQ3TGcRalwuyZ+oVrFjHp7RLhYPvowKtDBuxTEUUmcLZwkNjR5fs51nvU2rw9dOj6MhDqWilUlYSiNjeHakrogv8JQQNS99FEd7EA+UzqQCXVDiAqb/8jYHyMuJR7H2OW/IC8i54CtMp1n1hEE/6271AIUetJYIZOl/4bnOD4jPL0DA77VcXIMEu9v5limN+2nDZdiv5e9Ccg2CQYTYZ/hOT/4IAbl3nMlbLWR9B+aPQT5oneb0EvIXy53qp+0uipGk9vXUNUXbNr1rcobT7J8RBfrmuiGh6qWzIaQgsXEN4J/weIP6OEPjT2HAAAAABJRU5ErkJggg==)](/redoc)

Use the Fur Affinity API badge for your projects! [![](https://furaffinity-api.herokuapp.com/badge/svg)](https://furaffinity-api.herokuapp.com/badge/svg)

_The badge is provided via [Shields.io](https://shields.io/)._
"""
