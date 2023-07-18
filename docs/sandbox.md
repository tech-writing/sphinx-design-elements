# Sandbox

Those commands will get you started with a sandboxed development environment.
After invoking `poe check`, and observing the software tests succeed, you
should be ready to start hacking.

```shell
git clone https://github.com/panodata/sphinx-design-elements
cd sphinx-design-elements
python3 -m venv .venv
source .venv/bin/activate
pip install --editable=.[develop,docs,test]
poe check
```
