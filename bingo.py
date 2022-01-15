import random
from re import T
from reportlab.pdfgen.canvas import Canvas

contents = ['"wyld"',"Leon versteht\nnicht, was Valle\nsagt",
            "*Grillenzirpen*","stockendes\nIntro","Valle redet\n5min durch",
            '"das`n\nSchnapper"','"ja nice"',"jemand\ngoogelt\netwas",
            "Valle bleibt\nkonsequent\nbeim Thema",'häufiges\n"äh"',
            "Gespräch\nüber\nUni","Valle macht\nsich über\njemanden\nlustig",
            "Idee für\nzukünftigen\nPodcast","insider-\nJoke",'"das schneiden\nwir später\nraus"',
            "gegenseitiges\nUnterbrechen","Gespräch\nüber\nCorona","Selbstdisse",'"Worüber haben\nwir nochmal\ngeredet?"',
            "Bemerkung zur\nAudienzgröße","Tastatur-\ngeräusche","Referenz\nan\nJohnny",'"ich stimme\nvoll zu"',"Valle\nbeleidigt\njemanden",
            "Valle macht\nschlechten\nWortwitz","Valle weiß\nkomische\nFakten","Valle ist\nschüchtern und\nsagt fast\nnichts",
            "Leon redet\nmit\nDialekt","Leon\nstottert","das das\nregt mich\nsowieso am\nmeisten auf",
            "ich hab\nmir\nletztens ...\nangeschaut","Leon redet\n5min durch",'Leon sagt\nmindestens 10x\n"sowieso"']

def contents_order():
    """returns contents in a random order"""
    global contents
    ret = []
    while len(contents) > 0:
        index = random.randint(0,(len(contents)-1))
        ret.append(contents[index])
        contents.pop(index)

    ret.insert(len(contents)-13,"Leon & Valle\nPodcast\nBingo!")

    if(len(ret) < 25):
        while (len(ret)<25):
            ret.append("")

    return ret

def inch_to_canvas(value,x):
    """returns the cm value in the correct needed value for canvas"""
    value = value*72
    if(x == False):
        value = 11.7*72-value

    return value



def create_pdf():
    """creates the pdf file"""
    canvas = Canvas("bingo.pdf")
    canvas.setFont("Helvetica-Oblique",10)
    x1 = inch_to_canvas(1,True)
    y1 = inch_to_canvas(1,False)
    x2 = inch_to_canvas(7.26,True)
    y2 = y1
    canvas.line(x1,y1,x2,y2)
    val = inch_to_canvas(1.252,True)
    for i in range(5):
        #print(y1)
        y1 = y1-val
        y2 = y1
        canvas.line(x1,y1,x2,y2)
    y1 = inch_to_canvas(1,False)
    x2 = x1
    canvas.line(x1,y1,x2,y2)
    for i in range(5):
        x1 = x1+val
        x2 = x1
        canvas.line(x1,y1,x2,y2)

    content = contents_order()

    y1 = inch_to_canvas(1.636,False)
    x_val = inch_to_canvas(1.626,True)
    x1 = x_val
    j = len(content)-2
    text_size = 12
    for k in range(5):
        for i in range(5):
            #print(len(content))
            #canvas.drawCentredString(x1,y1,content[j])
            """text = canvas.beginText()
            text.setTextOrigin(x1,y1)
            text.setFont("Helvetica-Oblique",10)
            text.setFillColorRGB(0,0,0)"""
            if(k==2 and i==2):
                canvas.setFont("Helvetica-Bold",14)
                text_size = 16
                canvas.setFillColorRGB(89, 0, 92)
                y1 = y1-6
            parts = content[j].split("\n")
            num_parts = len(parts)
            size = num_parts * text_size
            steps = 0.5 * (num_parts-1)
            d=0
            if(steps==0):
                canvas.drawCentredString(x1,y1,parts[0])
            else:
                for n in range(int(-steps*2),int((steps+0.5)*2),2):
                    #text.textLine(parts[n])
                    canvas.drawCentredString(x1,y1-((n/2)*text_size),parts[d])
                    d+=1
            #canvas.drawText(text)
            content.pop(j)
            #print(content)
            x1 = x1+val
            j-=1

            if(k==2 and i==2):
                canvas.setFont("Helvetica-Oblique",10)
                text_size = 12
                canvas.setFillColorRGB(0, 0, 0)
                y1 = y1 +6

        x1 = x_val
        y1 = y1-val

    canvas.save()

if __name__ == "__main__":
    create_pdf()