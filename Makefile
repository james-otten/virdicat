PostZip = virdicat-post.zip
GetZip = virdicat-get.zip
DB = virdicatdb.py
GetDir = virdicat-get
PostDir = virdicat-post
ZIPARGS = -9 -r

all: clean virdicat-get virdicat-post

virdicat-get: virdicat-db
	cp $(DB) $(GetDir)/$(DB)
	pip install praw -t $(GetDir)
	cd $(GetDir) ; zip $(ZIPARGS) ../$(GetZip) * ; cd ..

virdicat-post: virdicat-db
	cp $(DB) $(PostDir)/$(DB)
	pip install python-twitter -t $(PostDir)
	cd $(PostDir) ; zip $(ZIPARGS) ../$(PostZip) * ; cd ..

virdicat-db: $(DB)

clean:
	rm -rf $(PostZip)
	rm -rf $(GetZip)
	find . -type f -name "*.pyc" -exec rm -rf {} \;
