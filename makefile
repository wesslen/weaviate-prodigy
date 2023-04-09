include .env

install:
	python3 -m pip install --upgrade pip
	python3 -m pip install -r requirements.txt
	python3 -m pip install --upgrade prodigy -f "https://${PRODIGY_KEY}@download.prodi.gy"

get_data:
	wget https://github.com/brmson/dataset-sts/raw/master/data/sts/sick2014/SICK_train.txt
	mkdir data
	python scripts/get_data.py SICK_train.txt data/sick-input.jsonl
	rm -rf SICK_train.txt

clean:
	rm -rf data