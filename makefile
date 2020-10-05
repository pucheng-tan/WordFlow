######################## \
Make file to build python project env \
run 'make' to install dependencies \
make sure that you have pip and virtualenv installed \
for any more questions, ask Cameron \

# after running make, use source /env/bin/activate or . \env\Scripts\activate
# to start venv
# when finished in venv, use 'deactivate'

#note: does not currently support linux 

# please make clean before pushing to main branch :)




NAME = $(shell uname)

.PHONY: all req

ifeq ($(NAME),Darwin)



all: env req

env: 
	python3 -m venv env

req: requirements.txt
	#this dot is equal to saying source
	. env/bin/activate

	env/bin/pip3 install -r requirements.txt
	

	
clean:
	rm -rf env

else
	
all: env req

env:
	py -m venv env

req: requirements.txt
	. env/Scripts/activate
	env\bin\pip3 install -r requirements.txt

clean:
	rm -rf env
	
	
endif
