#Time-stamp: <2023-06-05 22:53:58 hamada>

wheel:
	python3 setup.py bdist_wheel


clean:
	rm -rf build pyuart.egg-info dist

test.deploy:
	twine upload --repository testpypi dist/*

deploy:
	twine upload --repository pypi dist/*


setup:
	pip install wheel twine 

