import os
directory = os.path.expanduser('/home/pi/Desktop/switch/switch-working/test-files/')

from bs4 import BeautifulSoup


for file in os.listdir(directory):
    # this will return a tuple of root and extension
    split_tup = os.path.splitext(file)

    # extract the file name and extension
    file_name = split_tup[0]
    file_extension = split_tup[1]

    #only rewrite html files - skips Mac system files, etc.
    if file_extension in ('.html', '.htm'):
        doc=open(os.path.join(directory,file),'rb')
        soup=BeautifulSoup(doc,'lxml', from_encoding="windows-1252")
        #get article content
        article = soup.find(class_='DBoutput')
        special = soup.find(class_='specialObjs')
        images = soup.find_all("img")
        image1 = images[0]
        image2 = images[1]
        image3 = images[2]
        #write to new html
        output="""
        <html>
            <head>
            <meta http=equiv="Content-Type" content="text/html;charset="utf-8" />
            <link href="../../categories/global_files/switch.css" rel="stylesheet" type="text/css">
            <style>
                #issueImage img {{margin-right:1px;}}
                B.et4 {{}}
                a:link {{color:#222222;}}
                td.quote {{color:#222222;}}
                td.specialObjs p, td.specialObjs a {{color:#bbbbbb;}}
            </style>
            </head>
            <body>
            <div id="header">
            <div id="switchLogo" style="float:left; width:200px; text-align:right; padding-top:16px; margin-right:5px;">
            {firstImage}
            </div>
            <div id="issues" style="float:left;background: #999999; padding:44px 0px 5px 5px; width:495px; margin-bottom:4px;">
            <b class="light">
				<a href="front.php.html">all</a>
				<a href="front.php_cat%3d5.html">#1</a>
				<a href="front.php_cat%3d6.html">#2</a>
				<a href="front.php_cat%3d7.html">#3</a>
				<a href="front.php_cat%3d8.html">#4</a>
				<a href="front.php_cat%3d9.html">#5</a>
				<a href="front.php_cat%3d10.html">#6</a>
				<a href="front.php_cat%3d11.html">#7</a>
				<a href="front.php_cat%3d12.html">#8</a>
				<a href="front.php_cat%3d13.html">#9</a>
				<a href="front.php_cat%3d14.html">#10</a>
				<a href="front.php_cat%3d15.html">#11</a>
				<a href="front.php_cat%3d16.html">#12</a>
				<a href="front.php_cat%3d17.html">#13</a>
				<a href="front.php_cat%3d18.html">#14</a>
				<a href="front.php_cat%3d19.html">#15</a>
				<a href="front.php_cat%3d20.html">#16</a>
				<a href="front.php_cat%3d21.html">#17</a>
				<a href="front.php_cat%3d44.html">#18</a>
				</b>
            </div>
            <div id="plus" style="float:right; background: #CCCCCC; padding:4px 8px 3px 0px;">
            <p>+ +</p>
            <p>+ +</p>
            </div>
            </div>
            <div id="issueImage" style="background-color:#444444; clear:both; height:200px;">
            {secondImage}
            {thirdImage}
            </div>
            <div id="article" style="background-color:#444444; display: inline-block; width: 100%;">
            <div id="sidebar" style="width:200px; float:left; margin-right:5px;">
            <table>
            <tr>
            {specialObjects}
            </tr>
            </table>
            </div>
            <div id="content" style="width:500px; float:left;">
            <table>
            {content}
            </table>
            </div>
            </div>
            <div id="footerOuter" background:#FFFFFF;>
            <div id="footerSidebar" style="background:#444444; width:205px; height:66px; float:left;">
            </div>
            <div class="switchAbout" style="background:#999999; border-top:white 4px solid; padding:44px 5px 5px; width:490px; float:left;"">
				<a href="front.php_artc%3d89.html">about</a> |
				<a href="front.php_artc%3d96.html">contact</a> |
				<a href="front.php_artc%3d292.html">credits</a> |
				<a href="subscribe.php.html">subscribe</a>
            </div>
            <div id="footerRight" style="float:right;background: #CCCCCC; width:30px; height:66px;">
            </div>
            </body>
            </html>
            """.format(firstImage=image1, secondImage=image2, thirdImage=image3, specialObjects=special, content=article)

        #accesssibility changes - make changes here where inline styles and other issues make CSS difficult
        output=output.replace('bgcolor="#666666"','bgcolor="#888888"')
        #write to new file
        newFilename = file
        htmlFile= open(newFilename,"w")
        htmlFile.write(output)
        htmlFile.close()
