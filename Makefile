JSON=$(patsubst %.yaml,%.json,$(wildcard *.yaml))

%.json: %.yaml
	python -c 'import sys, yaml, json; json.dump(yaml.load(sys.stdin), sys.stdout, indent=2)' < $^ > $@

all: $(JSON)

clean:
	rm -f $(JSON)
