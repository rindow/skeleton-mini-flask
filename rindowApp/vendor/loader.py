import sys,os
for path in [
	'Flask-0.10.1',
	'Werkzeug-0.10.1',
	'MarkupSafe-0.23',
	'itsdangerous-0.24',
	'rindow/framework/lib',
	'rindow/cms/lib',
]:
	sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), path))
