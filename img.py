from PIL import Image
import imgfunc
import sys


def usage():
  print "Usage: \n \n"
	print "python img.py currentImg.ext afterImg.ext reverse_miroir_neg\n",
	print "currentImg.ext: l'image avant retouche\n",
	print "afterImg.ext: l'image cree apres retouche\n",
	print "_ : separateur pour appliquer plusieurs fonctions\n",
	print "Fonctions disponibles :\n",
	print "miroir\n",
	print "reverse\n",
	print "neg\n",
	print "seuillage\n",
	print "seuillageINT, où INT est un entier positif, par ex 60"
	print "grisage\n",

def cmdline(argv):
	if "-h" in argv:
		usage()
	else:
		img = Image.open(argv[1])

		pixels = img.load()

		img2 = Image.new('RGB', img.size)

		pixels2 = img2.load()
		img2.save(argv[2], img.format)
		imgfunc.initialize(pixels, pixels2, img.size)

		for func in argv[3].split("_"):
			img2 = Image.open(argv[2])
			pixels3 = img2.load()
			#pixels3 = pixels2
			if func == "miroir":
				imgfunc.miroir(pixels2, pixels3, img.size)
			elif func == "neg":
				imgfunc.neg(pixels2, pixels3, img.size)
			elif func == "reverse":
				imgfunc.reverse(pixels2, pixels3, img.size)
			elif "seuillage" in func:
				if func[len("seuillage"):].isdigit():
					imgfunc.seuillage(pixels2, pixels3, img.size, int(func[len("seuillage"):]))
				elif func == "seuillage":
					imgfunc.seuillage(pixels2, pixels3, img.size)
			elif func == "grisage":
				imgfunc.to_gris(pixels2, pixels3, img.size)
			else:
				print "Error, use -h",
				sys.exit()
			img2.save(argv[2], img.format)
			pixels2 = pixels3

cmdline(sys.argv)
