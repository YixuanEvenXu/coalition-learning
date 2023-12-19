runa: code/main.py
	python3 code/main.py A > logs/A.log

runb: code/main.py
	python3 code/main.py B > logs/B.log

runc: code/main.py
	python3 code/main.py C > logs/C.log

rund: code/main.py
	python3 code/main.py D > logs/D.log

rune: code/main.py
	python3 code/main.py E > logs/E.log

runall: code/main.py
	python3 code/main.py A > logs/A.log
	python3 code/main.py B > logs/B.log
	python3 code/main.py C > logs/C.log
	python3 code/main.py D > logs/D.log
	python3 code/main.py E > logs/E.log
	python3 code/main.py F > logs/F.log

plots: code/plotabc.py code/plotdef.py logs/A.log logs/B.log logs/C.log logs/D.log logs/E.log logs/F.log
	python3 code/plotabc.py A < logs/A.log
	python3 code/plotabc.py B < logs/B.log
	python3 code/plotabc.py C < logs/C.log
	python3 code/plotdef.py D < logs/D.log
	python3 code/plotdef.py E < logs/E.log
	python3 code/plotdef.py F < logs/F.log

table: code/tableabc.py logs/A.log logs/B.log logs/C.log 
	python3 code/tableabc.py A < logs/A.log
	python3 code/tableabc.py B < logs/B.log
	python3 code/tableabc.py C < logs/C.log