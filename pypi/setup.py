from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))


with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyuart', # パッケージ名(プロジェクト名)
    packages=['pyuart'], # パッケージ内(プロジェクト内)のパッケージ名をリスト形式で指定

    version='0.0.1', # バージョン

    license='MIT', # ライセンス

    install_requires=['pyserial'], # pip installする際に同時にインストールされるパッケージ名をリスト形式で指定

    author='Tsuyoshi Hamada', # パッケージ作者の名前
    author_email='hamada@arkedgespace.com', # パッケージ作者の連絡先メールアドレス

    url='https://github.com/arkedge/pyuart', # パッケージに関連するサイトのURL(GitHubなど)

    description='a simple UART library for python3', # パッケージの簡単な説明
    long_description='pyuart', # PyPIに'Project description'として表示されるパッケージの説明文
    long_description_content_type='text/markdown', # long_descriptionの形式を'text/plain', 'text/x-rst', 'text/markdown'のいずれかから指定
    keywords='pyuart uart', # PyPIでの検索用キーワードをスペース区切りで指定

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
    ], # パッケージ(プロジェクト)の分類。https://pypi.org/classifiers/に掲載されているものを指定可能。
)
