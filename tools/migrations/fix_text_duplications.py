# made sense at the time of: bf7edef8884d1a23bb485c2b45b1d4815c4c1297
# there was no unique constraint on the text at the time
# the db ended with quite a bit of duplicated texts
from collections import defaultdict
data = defaultdict(set)
from zeeguu.model import Text, Bookmark
import zeeguu

texts = zeeguu.db.session.query(Text).all()

for a in texts:
    data[a.content.strip()].add(a)


for content, _texts in data.items():
    #print (str(len(_texts)))
    if len(_texts)<=1:
        continue

    texts = list(_texts)
    first_text = texts[0]
    print ("found dupe with text : "  + str(texts[0].content))
    print ("the first text is: "  + str(texts[0].id))
    print ("the rest are: " + str(texts[1:]))

    #input("Press Enter to remove ...")

    for text in texts[1:]:
        bookmarks = zeeguu.db.session.query(Bookmark).filter_by(text=text).all()
        for bookmark in bookmarks:
            print ("got bookmark {0} that points to text {1} ".format(bookmark.id, text.id))
            print ("will rewire it to point to " + str(first_text.id))
            bookmark.text = first_text
            zeeguu.db.session.add(bookmark)
        print("text {0} should be deleted now".format(text.id))
        zeeguu.db.session.delete(text)
        zeeguu.db.session.commit()

    print ("dupe removed ")
