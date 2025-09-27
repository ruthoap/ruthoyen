SITE_DIR = _site

.PHONY: serve build clean setup

default: serve

# Gemfile が無ければ作成
Gemfile:
	echo 'source "https://rubygems.org"' > Gemfile
	echo 'gem "jekyll", "~> 3.10"' >> Gemfile

# Gemfile.lock は bundle install で生成
Gemfile.lock: Gemfile
	bundle install

# 開発環境セットアップ
setup: Gemfile.lock

# サーバ起動 (ローカル確認用)
serve: Gemfile.lock
	bundle exec jekyll serve --livereload --host 0.0.0.0

# 静的ファイル生成
build: Gemfile.lock
	bundle exec jekyll build

# 出力を削除
clean:
	rm -rf $(SITE_DIR)
