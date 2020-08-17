from bs4 import BeautifulSoup
html = """"
<HTML>

<HEAD>
<TITLE>dummy html document</TITLE>
</HEAD>

<BODY Background="http://www.microsoft.com/library/images/gifs/general/wallpaper.gif">

<h1>HTML Dummy Page</h1>
<hr>

(I acknowledge Microsoft for use of their image to illustrate the BACKGROUND attribute on the BODY tag.)
<br><br>
<br><br>

<!--Headings--><H3>Headings</H3>
<H1>Level 1 Head</H1>
<H2>Level 2 Head</H2>
<H3>Level 3 Head</H3>
<H4>Level 4 Head</H4>
<H5>Level 5 Head</H5>
<H6>Level 6 Head</H6>
<HR>

<!--Spacing--><H3>Spacing</H3>
Text in one paragraph.<P>Text in another paragraph.
<br><br>

Text before a break.<BR>text after a break.
<br><br>

<PRE>
Preformatted text:
  Indented line
    Further indented line
</PRE>
<br><br>

<BLOCKQUOTE>
A Blockquote:<br>HTML is one of three fundamental concepts on which the WWW rests.  (The other two are the HTTP protocol and the URL addressing/naming scheme.)  Consequently, it is important to understand not just how to use HTML but also its role within the web, its capabilities and limitations, and possible future directions it may take.</BLOCKQUOTE>
<br><br>

A Horizontal Rule:
<HR>
<HR>

<!--Lists--><H3>Lists</H3>
An unorderd list:
<UL>
<LI>item 1
<LI>item 1
<LI>item 1
</UL>

An ordered list:
<OL>
<LI>item 1
<LI>item 1
<LI>item 1
</OL>

A definition list:
<DL>
<DT>term 1
<DD>defn 1
<DT>term 2
<DD>defn 2
<DT>term 3
<DD>defn 3
</DL>

A nested list:
<UL>
<LI> term 1
        <UL>
        <LI>term a
        <LI>term b
        </UL>
<LI> term 2
        <UL>
        <LI>term a
        <LI>term b
        </UL>
</UL>

A menu list:
<MENU>
<LI><A HREF="">anchor 1</A>
<LI><A HREF="">anchor 2</A>
<LI><A HREF="">anchor 3</A>
</MENU>

A directory:
<DIR>
<A HREF="">anchor 1</A>
<A HREF="">anchor 2</A>
<A HREF="">anchor 3</A>
</DIR>

<HR>

<!--Fonts--><H3>Fonts</H3>
<DFN>definition font</DFN>
<br><br>
<EM>emphasis font</EM>
<br><br>
<STRONG>strong emphasis font</STRONG>
<br><br>
<CITE>citation font</CITE>
<br><br>
<KBD>keyboard font</KBD>
<br><br>
<CODE>computer code font</CODE>
<br><br>
<SAMP>sample computer output font</SAMP>
<br><br>
<ADDRESS>address font</ADDRESS>

<br><br>
<B>bold font</B>
<br><br>
<I>italics font</I>
<br><br>
<TT>typewriter font</TT>
<HR>

<!--Anchors--><H3>Anchors</H3>
<A HREF="http://www.cs.unc.edu:80/wwwc-f95/private/notes-9-5-95.html">Class notes on HTML</A>
 <br><br>

<A HREF="http://www.cs.unc.edu:80/wwwc-f95/public/guru_topics.html#potential">Anchor to a point within a file</A>
<A NAME="potential"></A>
<HR>

<!--Images--><H3>Images</H3>

<IMG SRC="http://www.cs.unc.edu/~jbs/figures/jbs.jpg">
<br><br>
<IMG ALT="Text to be displayed, if can't show image; also, aligned right." ALIGN="right" SRC="http://www.cs.unc.edu/~ladd/images/skull.gif">
<br><br><br><br>


An example of an image serving as an anchor:<br>
<A HREF="http://www.cs.unc.edu/~jbs"><IMG SRC="http://www.cs.unc.edu/~jbs/figures/jbs.jpg">jbs</A>
<br>You can click on either the picture or the "jbs" just to the (lower) right of it to follow the link.
<HR>

<!--Contact Information--><H3>Contact information</H3>
<ADDRESS>
email: <A HREF="mailto:jbs@cs.unc.edu">jbs@cs.unc.edu</A>
<BR>
url: <A HREF="http://www.cs.unc.edu/~jbs">http://www.cs.unc.edu/~jbs</a>
</ADDRESS>
<HR>

<!--Netscape extensions--><H3>Netscape extensions</H3>

<IMG ALT="" ALIGN="left" HSPACE="10" SRC="http://www.cs.unc.edu/~jbs/figures/jbs.jpg">
In this example, the image is aligned left (standard), but it is separated from the wrap-around text by 10 pixels of space.  It also uses the Break Clear All feature to separate the wrap-around text from the text that follows.
<BR CLEAR="all">
Here is the text that follows.
<br><br>

Example of Netscape HR extensions:
<HR SIZE="10" WIDTH="50%" ALIGN="center" NOSHADE>
<br><br>

Example of Netscape UL extensions:
<UL TYPE=square>
<LI> term 1
        <UL TYPE=circle>
        <LI>term a
        <LI>term b
        </UL>
<LI> term 2
        <UL TYPE=disk>
        <LI>term a
        <LI>term b
        </UL>
</UL>
<br><br>

Example of Netscape OL extensions:
<OL TYPE=1>
<LI> term 1
        <OL TYPE=A>
        <LI>term a
        <LI>term b
        </OL>
<LI> term 2
        <OL TYPE=I>
        <LI>term a
        <LI>term b
        </OL>
</OL>
<br><br>

Fonts can now be made <FONT SIZE=+3>larger</FONT>,
<FONT SIZE=-2>smaller</FONT>, and returned to normal.
<br><br>

Nobreak lets you keep <nobr>lonnnnnnnnnnnnnnnnnnnnnnnnng strings together that would, otherwise, be broken.</nobr>
<NOBR>
<br><br>

<CENTER><font size=+2><b>Text can also be centered. </b></font></CENTER>
<br><br>

Standard copyright (&COPY) and registered (&REG) symbols are available.

<HR>
<ADDRESS>
email: <A HREF="mailto:jbs@cs.unc.edu">jbs@cs.unc.edu</A>
<BR>
url: <A HREF="http://www.cs.unc.edu/~jbs">http://www.cs.unc.edu/~jbs</a>
</ADDRESS>

</BODY>

</HTML>
"""

soup = BeautifulSoup(html, 'html.parser')


#basic


#print(soup.body)
#print(soup.head)
#print(soup.head.title)


#finding


#print(soup.find('div'))
#print(soup.find_all('ul'))
#print(soup.find_all('ul')[1])

#print(soup.find(id='something'))
#print(soup.find(class_='something'))
#print(soup.find(attrs={'something':'attrname'}))


#selection


#print(soup.select('#section1')[0])//add to index//id
#print(soup.select('.section1')[0])//class


#text

#print(soup.find_all('ul')[1].get_text())


#Navigation

#print(soup.body.contents[1])//first one is line break
#.find_previous_sibling()
#.find_next_sibling()//next element in list
#.find_parent()//add parameter for what tag is required "p" for paragraph

