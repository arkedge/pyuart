#Time-stamp: <2023-06-05 17:00:34 hamada>

wheel:
	python3 setup.py bdist_wheel


clean:
	rm -rf build pyuart.egg-info dist

test.upload:
	twine upload --repository testpypi dist/*


