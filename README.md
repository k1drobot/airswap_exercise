airswap_exercise
=============================

airswap_exercise

Author
------
* Brandon Ng


pip install package

``` pip install -e . 
cmd to run 
 airswap 
  	-v add debugging

 calculate_mean 
 	-s symbol (default = ETHBTC)
	-d length of mean sample (default = 60)

 ex. airswap -v calculate_mean -d 60 -s ETHBTC 

 Tests
 ------
py.test --cov-report xml --cov=. tests/

 ```
