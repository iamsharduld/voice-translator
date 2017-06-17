import textTospeech

from translate import Translator
def translator(x):
	#print "Language Name	Code	Language Name	Language Code\nAfrikaans	af	Irish		ga\nAlbanian	sq	Italian		it\nArabic		ar	Japanese	ja\nAzerbaijani	az	Kannada		kn\nBasque		eu	Korean		ko\nBengali		bn	Latin		la\nBelarusian	be	Latvian		lv\nBulgarian	bg	Lithuanian	lt\nCatalan		ca	Macedonian	mk\nCroatian	hr	Norwegian	no\nCzech		cs	Persian		fa\nDanish		da	Polish		pl\nDutch		nl	Portuguese	pt\nEnglish		en	Romanian	ro\nEsperanto	eo	Russian		ru\nEstonian	et	Serbian		sr\nFilipino	tl	Slovak		sk\nFinnish		fi	Slovenian	sl\nFrench		fr	Spanish		es\nGalician	gl	Swahili		sw\nGeorgian	ka	Swedish		sv\nGerman		de	Tamil		ta\nGreek		el	Telugu		te\nGujarati	gu	Thai		th\nHaitian Creole	ht	Turkish		tr\nHebrew		iw	Ukrainian	uk\nHindi		hi	Urdu		ur\nHungarian	hu	Vietnamese	vi\nIcelandic	is	Welsh		cy\nIndonesian	id	Yiddish		yi"
	#print "Enter the code of the language From which you want to translate"
	source = "en"
	#print "Enter the code of the language To which you want to translate"
	dest = "de"
	translator= Translator(from_lang=source,to_lang=dest)
	#istring = raw_input()
	translation = translator.translate(x)

	print translation
	return translation


