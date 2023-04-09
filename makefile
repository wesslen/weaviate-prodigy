include .env

install:
	python3 -m pip install --upgrade pip
	python3 -m pip install -r requirements.txt
	python3 -m pip install --upgrade prodigy -f "https://${PRODIGY_KEY}@download.prodi.gy"

get_data:
	wget https://github.com/brmson/dataset-sts/raw/master/data/sts/sick2014/SICK_train.txt
	wget https://github.com/brmson/dataset-sts/raw/master/data/sts/sick2014/SICK_trial.txt
	mkdir data
	python3 scripts/get_data.py SICK_train.txt data/sick-train.jsonl
	python3 scripts/get_data.py SICK_trial.txt data/sick-test.jsonl
	rm -r SICK_train.txt
	rm -r SICK_trial.txt

clean:
	rm -rf data