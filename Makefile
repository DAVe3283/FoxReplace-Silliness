JSON=$(patsubst %.yaml,%.json,$(wildcard *.yaml))

%.json: %.yaml
	python transform.py < $^ > $@

all: $(JSON)

clean:
	rm -f $(JSON)
