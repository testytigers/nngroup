# Theory of Hypertext Systems: Article by Jakob Nielsen - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">26</span>

<div class="article-header">

<h1 class="article-h1">Architectural Component of Hypertext Systems</h1>

<div class="article-authors">

<span id="gaDataAuthors" class="ga-data-layer" aria-hidden="true">Jakob Nielsen</span>

<div class="author-tile multiple body-small">

<div class="author-photos">

<img height="64" width="64" class="author-photo fluid" src="https://media.nngroup.com/media/people/photos/Jakob-Nielsen-tie-800x800.jpg.256x256_q75_autocrop_crop-smart_upscale.jpg" alt="">

</div>

<div class="author-meta">

<span class="authors-list"><a class="ga-article-author" href="/articles/author/jakob-nielsen/">

Jakob Nielsen</a></span>

<p class="publication-date">

January 1, 1995

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">1995-01-01</span>

</p>

</div>

</div>

</div>

<div class="article-share">

<a class="article-share-title ga-share" href="#">

<span class="article-share-icon"></span>

<p class="article-share-label body-medium">Share</p>

</a>

<div class="share-links tooltip">

<div class="tip-arrow"></div>

<ul>

<li class="body-medium">

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Architectural Component of Hypertext Systems&amp;body=https://www.nngroup.com/articles/architectural-component-hypertext-systems/" data-share-type="Email">

<svg

width="24"

viewbox="0 0 24 24"

fill="none"

xmlns="http://www.w3.org/2000/svg"

class="icon"

>

<rect x="2.375" y="5" width="19.25" height="14" rx="0.65625" stroke="currentColor" stroke-width="1.3125"/>

<path d="M21.625 6.75L12.4156 14.285C12.1738 14.4828 11.8262 14.4828 11.5844 14.285L2.375 6.75" stroke="currentColor" stroke-width="1.3125"/>

</svg>Email article

</a>

</li>

<li class="body-medium">

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/architectural-component-hypertext-systems/&amp;title=Architectural Component of Hypertext Systems&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/architectural-component-hypertext-systems/&amp;text=Architectural Component of Hypertext Systems&amp;via=nngroup" data-share-type="Twitter">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-x" />

</svg>

Share on Twitter

</a>

</li>

</ul>

</div>

</div>

</div>

<div class="article-container">

<div class="article-content">

<div class="article-summary article-heading-small-light">

<span class="article-summary-label">

Summary:&nbsp;

</span>Hypertext systems include a Presentation level, a Hypertext Abstract Machine (HAM) level, and a Database level. The following sections describe each of the levels in further detail, starting at the bottom.

</div>

<div class="article-body">

<p><em>This is chapter 5 from Jakob Nielsen's book <a href="/books/multimedia-and-hypertext/"> Multimedia and Hypertext: The Internet and Beyond</a>, Morgan Kaufmann Publishers, 1995. (For full literature references, please see the bibliography in the book.)</em></p>

<p>In theory one can distinguish three levels of a hypertext system [Campbell and Goodman 1988]:</p>

<ul>

<li>Presentation level: user interface</li>

<li>Hypertext Abstract Machine (HAM) level: nodes and links</li>

<li>Database level: storage, shared data, and network access</li>

</ul>

<p>Actually, very few current hypertext systems follow this model in their internal structure; most are a more or less confused mix of features. Even so, the model shows interesting directions for the future and is important for standardization work. The following sections describe each of the levels in further detail, starting at the bottom.</p>

<h3>The Database Level</h3>

<p>The database level is at the bottom of the three-level model and deals with all the traditional issues of information storage that do not really have anything specifically to do with hypertext. It is necessary to store large amounts of information on various computer storage devices like hard disks, optical disks, etc., and it may be necessary to keep some of the information stored on remote servers accessed through a network. No matter how the information is stored it should be possible to retrieve a specified small chunk of it in a very short time. This sounds very much like a specification for a database, which is what it is.</p>

<p>Furthermore, the database level should handle other traditional database issues, like multiuser access to the information, and various security considerations, including backup. Ultimately it will be the database level's responsibility to enforce the access controls which may be defined at the upper levels of the architecture.</p>

<p>As far as the database level is concerned, the hypertext nodes and links are just data objects with no particular meaning. Each of them forms a unit that only one user can modify at the same time and that takes up so many bits of storage space. In real life, it may be advantageous for the database level to know a little bit more about its data objects in order to enable it to manage its storage space most efficiently and provide faster response. But in any case the hypertext field would do well in taking advantage of the extensive work and experience in the traditional database field for the design and implementation of the database level.</p>

<h3>The Hypertext Abstract Machine (HAM) Level</h3>

<p>The HAM sits in the middle of the sandwich between the database and user interface levels. This center is where the hypertext system determines the basic nature of its nodes and links and where it maintains the relation among them. See the discussion below about the range of design choices regarding nodes and links. The HAM would have knowledge of the form of the nodes and links and would know what attributes were related to each. For example, a node might have an "owner" attribute that specified the user who created it and who has to authorize updates, or it could have a version number. Links might be typed as in NoteCards, or they might be plain pointers as in Guide.</p>

<p>The HAM is the best candidate for standardization of import-export formats for hypertexts, since the database level has to be heavily machine dependent in its storage format and the user interface level is highly different from one hypertext system to the next. This leaves only the HAM, and since we do need the ability to transfer information from one hypertext system to the other, we have to come up with an interchange format at this level. One current example of a HAM-level standard is HyTime (the ISO standard for <em> hy </em> permedia/ <em> time </em> -based document structuring) [Newcomb et al. 1991; DeRose and Durand 1994].</p>

<p>Interchanging hypertexts is more difficult than simply interchanging the component data in the nodes, even though there are also problems with the less standardized data formats for non-ASCII information like graphics and video clips. The problem is that hypertext interchange also requires the transfer of linking information. It should be possible to transfer the basic links (i.e., the "A points to B" type information), but large parts of the linking information may be lost.</p>

<p><img alt="Screenshot of one-to-many links" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/31/dickens_crossroads_interleaf.gif" style="width: 617px; height: 481px;"/><br/>

<strong>Figure 5.1. </strong> <em> So-called crossroads document used to represent one-to-many links in the WorldView version of the Dickens Web. Copyright © 1992–94 by Paul Kahn, George P. Landow, and Brown University, reprinted by permission. </em></p>

<p>For example, some hypertext systems like Intermedia have links that point to specific text strings in the destination node, whereas other systems like Hyperties only point to the destination node as a complete entity. A transfer of a hypertext from Intermedia to Hyperties would therefore lose important aspects of the linking information but should still be possible in principle. If we were to transfer a hypertext structure from Hyperties to Intermedia there would be no way to come up with a sensible substring for the destination anchor because the Hyperties author would not have considered that option when writing the hypertext. We would probably have to come up with a dummy anchor in the beginning of the destination node just to keep the Intermedia system happy. Of course if the transfer had been from Intermedia to Guide (which does have anchored link destinations), then we would want the transfer to keep the information about the destination substring so that it could be highlighted on arrival. The difficulty is that we would like to achieve both of these results with a single interchange format.</p>

<p>Kahn and Landow [1992] report on their experience in transferring the <cite> Dickens Web </cite> (a hypertext about Charles Dickens) from Intermedia where it was originally developed to two other hypertext systems: Eastgate System's Storyspace and Interleaf's WorldView. One of the major problems was that the "fat" one-to-many links in Intermedia could not be transferred to WorldView since it only had traditional one-to-one hypertext links. As an alternative, Kahn and Landow came up with "crossroads" documents like the one shown in Figure 5.1.</p>

<p>A crossroads documents serves as a waystation between the original departure anchor and the original destination anchors. The original link is replaced by a link from the departure anchor to the crossroads document as well as however many links it take to connect the crossroads document to all the original destination anchors. This example shows how awkward it can be to move hypertexts between systems if they do not share fundamental concepts as to the structure of the hypertext.</p>

<p>Work on the definition of hypertext interchange formats was initially started through informal meetings of the so-called Dexter Group, consisting of many of the designers of the early hypertext systems. (The Dexter Group is named after the inn in New Hampshire where it had its first meeting. The two meetings that resulted in the reference model were organized by Jan Walker and John Leggett and funded primarily by Digital Equipment Corporation and Texas A&amp;M University.) Since the hypertext standardization workshop in January 1990, work on hypertext reference models has continued through more formal activities at the U.S. National Institute of Standards and Technology.</p>

<p>This work has resulted in more detailed architectural models than the simple three-level model discussed here [Halasz and Schwartz 1990, 1994; Grønbæk and Trigg 1992, 1994] and also in some preliminary success in transferring hypertext information from NoteCards to HyperCard. Both NoteCards and HyperCard are frame-based hypertext engines, where the information is displayed on fixed cards. It would presumably be harder to transfer between hypertext systems with different architectures, such as, for example, a transfer from a window-based system like Guide with its long scrolling texts to a frame-based system. See the discussion of frame-based vs. window-based hypertext in the following section on Nodes. Figure 5.2 shows the relation between the Dexter model and the model used in this book.</p>

<p><img alt="Comparing two abstract models of the architectures of hypertext systems" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/31/hypertext_abstract_machine_model_model.png" style="width: 612px; height: 399px;"/><br/>

<strong>Figure 5.2. </strong> <em> Comparing the Dexter reference model to the three-level model proposed by Campbell and Goodman [1988] and used in this book. There are some terminology differences, such as the use of the word "storage" in the Dexter model to refer to the representation of the abstract hypertext network, but otherwise the main difference is the explicit discussion in the Dexter model of the interfaces between the levels, especially with respect to anchors. </em></p>

<h3>The User Interface Level</h3>

<p>The user interface deals with the presentation of the information in the HAM, including such issues as what commands should be made available to the user, how to show nodes and links, and whether to include overview diagrams or not.</p>

<p>Let us assume that the HAM level of a hypertext defines the links as being typed. The user interface level might decide not to display that information at all to some novice users and to make typing information available only in an authoring mode. The very distinction between reading and writing is one of the basic user interface issues.</p>

<p>Let us now assume that the user interface level does want to display the link typing to the user. It might want to do so by changing the shape of the cursor, as Guide does (see Figure 3.8), or by having a special notation for various forms for anchors. It could also decide to display typing information in an overview diagram. If it had a color display available, it might choose to show each link type in a different color, whereas on a monochrome display it would have to use different representations, such as different line patterns (like NoteCards), small icons (like CM/1, see Figure 4.3), or by using words to label the lines.</p>

<p>Actually, this decision cannot be made at the user interface level in isolation without considering the likely form of the data in the HAM. If the hypertext will have only a few link types, then colors or line patterns are suitable choices, but human ability to understand and distinguish such an encoding is limited to about seven different values. Icons could support hypertexts with somewhat more link types, but a hypertext with hundreds of link types would probably require the use of the type names in the interface.</p>

<div class="table-of-contents">

<div class="content">

<div class="header">

<div class="toc-header">

<h2 class="toc-title article-heading-small">

In This Article:

</h2>

<span class="expand-icon"></span>

</div>

<a class="current-element" href="#"></a>

</div>

<ul class="toc-items">

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-nodes-1">Nodes</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-links-2">Links</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-hypertext-engines-3">Hypertext Engines</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-open-hypertext-4">Open Hypertext</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-integrating-hypertext-ideas-into-other-environments-5">Integrating Hypertext Ideas into Other Environments</a>

</li>

</ul>

</div>

</div><h2 id="toc-nodes-1">Nodes</h2>

<p>Nodes are the fundamental unit of hypertext, but there is no agreement as to what really constitutes a "node." The main distinction is between frame-based systems and window-based systems.</p>

<p>Frames take up a specific amount of space on the computer screen no matter how much information they contain. Typical examples are the KMS frames and the HyperCard cards. Often the size of the frame is defined as the size of the computer screen, but that determination may not hold in all systems. Since the frame has a fixed size, the user may have to split a given amount of information over several frames if it cannot fit into one. The advantage of frames is that all user navigation takes place using whatever hypertext mechanisms are provided by the system.</p>

<p>In contrast, window-based systems require the user to use a scrolling mechanism in addition to the hypertext mechanisms to get the desired part of the node to show in the window. Because the system can display only a (potentially small) part of the node through the window at any given time, the node may be as large as needed, and the need for potential unnatural distribution of text over several nodes is eliminated. Guide and Intermedia are typical window-based systems.</p>

<p>A great disadvantage of window-based hypertexts is that the hypertext designer has no control over how the node will appear when the user reads it since it can be scrolled in many ways. The advantage is that windows may be of different size depending on the importance and nature of information they hold. One can imagine a window-based system that did away with scrolling and thus kept most of the advantages of both display formats.</p>

<p>The real world is not quite as simple as the clear distinction between frames and windows. HyperCard is mostly frame-based but includes the possibility for having scrolling text fields as part of a card. Hyperties uses a full-screen display without scrolling but instead requires the user to page back and forth through a sequence of screens in case the node is too big to fit on a single screen.</p>

<p>Most current hypertext systems provide fixed information in the nodes as written by the original author. In computational hypertext systems like KMS and HyperCard (with an embedded programming language) or NoteCards (with an interface to a programming language), it is possible to have computed nodes generated for the reader by the system. An example is a node with the current weather forecast retrieved from an online service like the American Prodigy or the French Minitel. Computing a node on the fly by executing a program obviously involves the risk of Trojan horses leading to virus infection or other problems. The problem is minimized when the program is executed on a remote server that is restricted to transmitting the resulting data to the user's computer. If the code has to execute on the user's computer precautions will need to be taken in the form of virus scanners. There are also efforts under way for constructing safe programming languages that can be interpreted inside a protective shell that ensures that no permanent damage can be done to the user's system.</p>

<p>If one has a certain amount of information to communicate, one issue is whether it should be split into many small nodes or kept in a rather small number of larger nodes. Kreitzberg and Shneiderman [1988] report on a small experiment to investigate this issue, wherein they split the same text into either 46 articles of between 4 and 83 lines or 5 articles of between 104 to 150 lines in Hyperties. The result was that users could answer questions significantly faster in the information base with many small nodes (125 sec. vs. 178 sec. per answer). One reason for this result is probably that Hyperties is one of the hypertext systems that links to the beginning of an article and not to the location within an article where the information of interest for the departure point is located. Because of this feature, Hyperties is most easily operated with small, focused nodes dealing with precisely one issue so that there can be no doubt about what part of the node a link points to.</p>

<h2 id="toc-links-2">Links</h2>

<p>Links are the other fundamental unit of hypertext besides nodes. Links are almost always anchored at their departure point to provide the user with some explicit object to activate in order to follow the link. The result of activating the anchor is to follow the link to its destination node. Most often, this anchoring takes the form of "embedded menus" where part of the primary text or graphics does double duty as being both information in itself and being the link anchor. It is also possible to have the hypertext anchors listed as separate menus, but that somehow seems to reduce the "hypertext feel" of a design, and a study by Vora et al. [1994] found that users performed 26% faster when the anchors were part of the main text.</p>

<p>Most links are explicit in the sense that they have been defined by somebody as connecting the departure node with the destination node. Some systems also provide <em> implicit </em> links, which are not defined as such but follow from various properties of the information. A classic example of implicit links is the automatic glossary lookup possible in Intermedia (see Figure 4.15). The InterLex server provides a link from any word in any Intermedia document to the definition of that word in the dictionary, but it would obviously be ridiculous to have to store all these links explicitly. Only when the user requests the definition of a word does the system need to find the destination for the link.</p>

<p>The StrathTutor system [Kibby and Mayes 1989] provided another kind of implicit link. The hypertext author was not expected to provide links between nodes but was instead asked to define a set of relevant attributes for each node and for areas of interest in the node. These attributes were keywords taken from a predefined restricted vocabulary. The areas of interest were called "hotspots" and served a purpose similar to anchors in other hypertext systems. When the user activated a hotspot, the system would view the user's interests as being defined by the combination of the attributes (keywords) from the current node and the selected hotspot. StrathTutor therefore linked to a new node having the highest overlap between its own attributes and this set of attributes. Kibby and Mayes claimed that this form for distributed specification of hypertext connections was the only way one could manage the authoring of really big hypertexts.</p>

<p>The StrathTutor links were an example of computed links determined by the system while the reader is reading, instead of being statically determined in advance by the author. Another example of computed links is a link from a tourist guide like <cite> Glasgow Online </cite> to the train schedule, where the system could link to the listing for the next train out of Glasgow for each destination.</p>

<p>A hypertext link has two ends. Even if a link is not bidirectional there may still be a need to anchor it explicitly at the destination node. Most frame-based hypertext systems only have links that point to an entire node, but when the destination is large, it is an advantage for the user to have the system point out the relevant information more precisely. See for example how the Drexel Disk highlights Building 53 because the user jumped to the campus map in Figure 1.3 from a description of the repair facility (which is located in that building).</p>

<p>In general, a hypertext design should tell the user why the destination for a link was an interesting place to jump to by relating it to the point of departure and following a set of conventions for the "rhetoric of arrival" [Landow 1989a].</p>

<p>Given that the hypertext is based on explicit links, the next issue is whether or not to make the anchors especially prominent on the screen compared with the rest of the node. In a sparse hypertext, where maybe less than 10% of the information serves as anchors, it is probably a good idea to visually emphasize the anchors. This is just a special case of the general user interface guideline of letting the user know what options are available in a dialogue. In a rich hypertext, where almost everything is linked to something, the best advice would be to remove any special emphasis on the anchors. After all, if everything is highlighted, then nothing is really highlighted anyway.</p>

<p>It is possible to use the Guide method of providing feedback by changing the shape of the cursor when it is over an anchor (see Figure 3.8). But that method should still be supplemented with some visual indication of the location of the anchors since users will otherwise be reduced to playing mine sweeper with the mouse to discover the active areas of the screen.</p>

<p>Unfortunately the highlighting of anchors conflicts with the use of emphasis in the running text. Traditionally writers have used typographical notation like <i> italics </i> or <b> boldfaced </b> type to indicate various forms for emphasis or special purpose text like quotations, and we would like to keep these capabilities for hypertext authors. But many current hypertext systems use the same or similar notation to indicate hypertext anchors also. This can unfortunately be very confusing to users unless the author has used a style guide to provide consistent notation for anchors and running emphasis. One solution to this problem may be the invention of special typographical cues for hypertext links [Evenson et al. 1989] and the gradual emergence of conventions for hypertext notation.</p>

<p>Most current hypertext systems have plain links, which are just connections between two nodes (and possibly anchors). The advantage of that approach is of course the simplicity of both authoring and reading. There is nothing to do with links except to follow them, and that one action can be achieved by a click of the mouse.</p>

<p>Alternatively, a link can be tagged with keywords or semantic attributes such as the name of the creator or the date it was created. These tags allow one to reduce the complexity of a hypertext through filter queries like, "Show all links created after March 23, 1995" or "Hide all links by so-and-so" (if we think that that person's contributions are rubbish).</p>

<p>Links can also be typed to distinguish among different forms of relationship between nodes. Trigg [1983] presents a very elaborate taxonomy of 75 different link types, including abstraction, example, formalization, application, rewrite, simplification, refutation, support, and data.</p>

<p>In addition to the standard links connecting two nodes, some hypertext systems also have "super-links" to connect a larger number of nodes. There are several possibilities for dealing with having a single i.Anchors:Multiple destinations;anchor connected to several destinations. The two simplest options are either to show a menu of the links or to go to all the destinations at the same time. Intermedia uses the menu option and allows users to choose only a single destination. This approach requires good names for the links or destination nodes in order for users to be able to understand their options. Some users of NoteCards have implemented a "fat link" type that opens windows on the screen for all the destination nodes.</p>

<p>The alternative way to deal with multiple destinations would be to have the system choose for the user in some way. The choice could be based on the system's model of the user's needs or some other estimate of the best destination, or it could simply be random, as in the example discussed towards the end of Chapter 2.</p>

<p><img alt="Screenshot from CD-ROM" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/31/kon-tiki.png" style="width: 649px; height: 486px;"/><br/>

<strong>Figure 5.3. </strong> <em> The Kon-Tiki system generates a video footnote by zooming the large video image to an icon. Copyright © 1993 by The Kon-Tiki Museum, reprinted by permission. </em></p>

<p>Link anchors present special problems for layered hypertext architectures like the model presented in the beginning of this chapter. In principle, links belong at the hypertext abstract machine level, but the location of the anchor in the node is dependent on the storage structure for the node media. In a text-only node, an anchor position can be described as a substring ("characters 25–37"), whereas an anchor in a film clip needs both substring information ("film frames 517–724") and a graphic location ("the rectangle [(10,10);(20,20)]"). Some dynamic anchors may be even harder to specify: Try encoding the anchors in a video of a football game to allow the user to click on a player at any time to link to that player's name and statistics. Therefore the actual anchoring of the link cannot be handled by the hypertext abstract machine. The solution in the Dexter model [Halasz and Schwartz 1990] is to define an explicit interface between the hypertext abstract machine (called "storage layer" in their model) and the database level (called "within-component layer" in their model) as shown in Figure 5.2. Anchors become indirect pointers and the anchoring interface provides a translation between anchor identifiers in the hypertext abstract machine and actual anchor values in the node data.</p>

<p>Gunnar Liestøl and Per Siljubergsåsen have designed a user interface for the Kon-Tiki Museum in Norway that uses an interesting way of indicating links in video materials [Liestøl 1994]. The museum has large amounts of films recorded in connection with Thor Heyerdahl's expeditions, and the design challenge was how to represent the links between the video clips and other information such as text, maps, and photographs.</p>

<p>To get a device pointing out of a video sequence, the designers borrowed a convention from the Macintosh user interface guidelines (Michael Arent [Vertelney et al. 1990] uses the term "interface slang" for this approach to borrowing elements of an established interaction vocabulary for other, though related, uses.): when documents are opened or closed on the Mac, the relationship between the document and the icon representing it is visualized by an animated rectangle zooming between the two positions. Similarly, the main video area in the Kon-Tiki system "throws off" miniature pictures that zoom down from the video to rest on the screen as "video footnotes" that can be clicked for further information about that part of the video.</p>

<h3>Annotations</h3>

<p>A special link type is the annotation link to a small, additional amount of information. The reading of an annotation typically takes the form of a temporary excursion from the primary material to which the reader returns after having finished with the annotation. Annotations are quite similar to footnotes in traditional text and can be implemented, for instance, as Guide pop-up windows that disappear as soon as the user releases the mouse button. Alternatively, as shown in Figure 5.4, annotations can be floating "stickies" (almost always shown in yellow windoids in homage to 3M's Post-It notes [Lucas and Schneider 1994; Scott 1994]), or they can be accessed through an icon.</p>

<p><img alt="Sticky-note annotation from DEC system." loading="lazy" src="//media.nngroup.com/media/editor/2012/10/31/dec_sticky_note.png" style="width: 640px; height: 481px;"/><br/>

<strong>Figure 5.4. </strong> <em> Use of sticky-notes to represent annotations. To add an annotation, the user tears off a sticky-note from the pile to the right and places it on the object that needs a comment. Every time this object is displayed in the future, the sticky-note will be there (until the user removes it). Copyright © 1994 by J. Ray Scott, Digital Equipment Corporation, reprinted by permission. </em></p>

<p>Hypertext writers can use annotations in the same way they would use footnotes in traditional text with the exception that hypertext annotations are less intrusive because they are not shown unless the reader asks for them. The most interesting use of annotations in hypertext is for the readers, however. Many hypertext systems allow readers to add new links to the primary material even if they do not always allow the reader to change the original nodes and links, and readers can use these facilities to customize the information space to their own needs. For example, readers of a hypertext medical handbook [Frisse 1988a] might want to supplement the generic description of a drug in the handbook with an annotation stating the brand name normally prescribed at their hospital.</p>

<p><img alt="Screenshot of InterNote annotation service" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/31/internote.gif" style="width: 598px; height: 491px;"/><br/>

<strong>Figure 5.5. </strong> <em> The InterNote service within IRIS Intermedia provides a quick facility for annotating documents of any type. The top frame of the note window (right) contains the annotator's suggestion of a change in wording. The bottom frame explains the reason for the suggestion. The author of the "Microtubules Introduction" document may now choose to incorporate the change by selecting the marker at either end of the link that connects the note to the document and choosing the "Incorporate Annotation" command. © 1989 by Brown University, reprinted with permission. </em></p>

<p>One system that does provide an annotation facility is Intermedia, as shown in Figure 5.5. Other systems like Hyperties do not allow readers to annotate but reserve all options to change the information space for the authors. In the case of Hyperties, one reason for refusing readers the right to add information is that the system was originally designed for museum information systems where one may in fact not want random users to alter the content of the hypertext. Another reason was the desire for an extremely simple user interface to Hyperties: Having a smaller number of options available to the user means that there is less to learn.</p>

<p>Finally, users can annotate a hypertext by adding various forms of highlighting [Nielsen 1986], such as the use of various colors to emphasize text of special importance to a particular user [Irler and Barbieri 1990]. One product that supports highlighting is Folio. Even though individualized highlighting does not really constitute a form of link, information gathered from highlighting (possibly from multiple users) can be used in filtering the hypertext to show only important information or to search the hypertext for nodes that had previously been highlighted.</p>

<h2 id="toc-hypertext-engines-3">Hypertext Engines</h2>

<p>Many hypertext systems are really hypertext engines that can display many different hypertext documents. Other hypertext systems are built specifically to display a single document and can therefore provide a much richer interaction with respect to the content of that particular document.</p>

<p>Besides the obvious advantage of not having to program a new application, the use of hypertext engines also has the advantage that they provide a user interface common to many documents. Users who already know how to use Guide, for example, can immediately start to read the next Guide document without any training.</p>

<p>Some hypertext systems like Guide and Hyperties are truly plain engines. The author just pours text into them and they take care of everything else. For example, a pop-up window in Guide always appears in the top right corner of the screen. The author does not have to make any user interface decisions except for a few low-level formatting details such as where to break paragraphs. Considering that most people are poor user interface designers, this may well be an advantage.</p>

<p>Other hypertext engines allow the hypertext designer to customize the user interface to a document within a certain framework. HyperCard is a prime example of such a system since it allows the designer to move fields around and add all sorts of background graphics. Even so, the designer is constrained by the basic HyperCard framework of being a frame-based system with a fixed size monochrome card. There are certain user interface facilities available in a kind of construction kit for the designer, but it is not possible to add new interaction techniques.</p>

<p>Actually it is possible to extend the framework of HyperCard, but only by leaving its built-in HyperTalk programming language behind and programming so-called external commands (XCMDs) in a traditional programming language like C. NoteCards is extensible because it is integrated with InterLisp, but it also provides several simpler possibilities for hypertext designers to customize their interfaces to the needs of their individual documents [Trigg et al. 1987].</p>

<p>HyperCard not only allows hypertext authors to customize the user interface of their hypertext documents, it requires them to do so. HyperCard has no default document design but in principle presents the author with a blank screen where it is necessary to define the placement of text fields before anything can be written.</p>

<p>Finally, some hypertext documents are implemented as specialized applications. These include the Drexel Disk (see Figure 1.3) and Palenque (see Chapter 4). These specialized applications can achieve an exact match between the hypertext system and the needs of the document. For example, for the children exploring the Mexican jungle, Palenque has special features in the form of a filmed television personality who pops up from time to time to introduce new discoveries. The designers of Palenque added this guide character to the interface after having interviewed children about how they would like to explore Maya ruins in the Mexican jungle. And they certainly did not want to do so alone.</p>

<h2 id="toc-open-hypertext-4">Open Hypertext</h2>

<p>Most hypertext researchers work with systems that are specifically designed as hypertext systems. Most <em> users </em> , on the other hand, work with systems that assist them in performing all kinds of tasks, from simple spreadsheet calculations to complex domain-specific work like analysis of seismic data from oil exploration sites. The conflict between these two perspectives on the world will definitely never be resolved by having the majority of users convert to using a hypertext tool and give up on their other software tools. A more promising approach is called open hypertext and is aimed at integrating hypertext capabilities with the rest of the user's software environment. The key notion is to let each application work with the data it is optimized for and have some way for the applications to communicate with a shared hypertext mechanism that handles the links across applications (and possibly even within applications).</p>

<p>Engelbart [1990] defines three levels of interoperability for open hypertext: interoperability in an individual's information space (e.g., linking from a phone list to a set of notes), interoperability in a group's information space (e.g., from one person's file space to a colleague's), and interoperability across groups (e.g., linking from the marketing organization to the manufacturing or product development organizations). The latter case is an example of interoperability across knowledge domains since the different groups are likely to use very different applications for their specialized work.</p>

<p>This section will mostly concern the first level of interoperability: the ability to link between information objects in different applications. The remaining two levels are in the nature of computer-supported cooperative work and involve networking and groupware software to a larger extent than they involve hypertext as such. Interoperability across group and companies can partly be supported by the World Wide Web and other Internet mechanisms discussed further in Chapter 7.</p>

<p>The typical method for supplying open hypertext is to remove the hypertext level from the applications and provide a single hypertext service for everything on the user's computer. The hypertext service will need to keep track of what information is moved where, and it can then communicate with the applications using message passing to indicate, for example, that they should open a certain document and scroll it to a certain location. The link information is typically stored in a database that is separate from the primary documents and is maintained by the hypertext service rather than the user's applications. The reasons for this separation is that the link information may exist in formats that are incompatible with some of the applications and that one does not want the user to have to see these internal data structures.</p>

<p>The Microcosm project [Davis et al. 1992, 1994; Hill and Hall 1994] defined three degrees of application-support for open hypertext: fully aware, partly aware, and unaware applications, where the term "aware" refers to the extent to which the application knows about hypertext and the possibility of links between its data and other applications. Figure 5.6 shows fully Microcosm-aware applications and the way Microcosm supports links between, say, a graphics application and a word processor. When a fully aware application opens a document, it sends a message to Microcosm to find out whether the document contains any links, and if so, it can display the anchors as buttons and make the user interface more appealing and intuitive to use. When the user activates an anchor, the fully aware application will know that a hypertext link should be followed, and it can ask the Microcosm service to do so. As the user edits the information in the source document, a fully aware application can inform Microcosm if link anchors have been added, moved, or deleted, and Microcosm can thus get the necessary information to maintain the link database.</p>

<p><img alt="Screenshot of Microcosm viewers" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/31/fully_aware_microcosm.png" style="width: 781px; height: 448px;"/><br/>

<strong>Figure 5.6. </strong> <em> Fully aware Microcosm viewers. The image viewer shows part of a city map with super-imposed "buttons" on top of the bitmap data for display purposes. The text viewer is based on RTF (rich text format). These viewers have been launched as a result of the user selecting items from the available links box, which is showing links available from the source anchor "Abbey Green." Copyright © 1994 by the Microcosm Group, University of Southampton, U.K., reprinted by permission. </em></p>

<p>The main problem with fully aware applications is that they have to be customized for the particular open hypertext model employed by the user. In this case, Microcosm was used, but several other open hypertext systems exist (and more can be expected in the future), so it is not realistic to expect all applications to be modified to work with all hypertext services.</p>

<p><img alt="Screenshot of Microcosm in Microsoft Calendar" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/31/microcosm_overlay.png" style="width: 426px; height: 277px;"/><br/>

<strong>Figure 5.7. </strong> <em> The Microcosm Universal Viewer running on top of the Microsoft Calendar program which is completely unaware of Microcosm. The Universal Viewer acts as a shim between Microcosm and unaware applications, displaying the menus and any relevant buttons on the application's title bar, and allows the user to make selections within the application for making or following links. Copyright © 1994 by the Microcosm Group, University of Southampton, U.K., reprinted by permission. </em></p>

<p>Partly aware viewers are those that have some kind of programmability that allows them to be extended with an action menu with the commands needed to interact with the hypertext service. Many popular applications, including Microsoft Word and most spreadsheet packages, come with a scripting facility (e.g., Visual Basic) that can be used for this purpose. The partly aware viewers typically do not allow anchors to be marked as buttons since they control their own user interface and the way they want to show their data on the screen. Thus, users are relegated to selecting objects in the application using its normal selection mechanism and then issuing hypertext commands such as "Follow Link" from the Microcosm menu.</p>

<p>In an unaware application, the hypertext commands cannot even be represented as menu commands but must be supplied through a modification of the window system or some other level of the underlying operating system. Figure 5.7 shows how the Microcosm Universal Viewer can attach itself to the title bar of a window and thus be accessed in the context of the application running in that window even though the application knows nothing about Microcosm. When the Microcosm service is activated through the menu on the titlebar, it reads the current selection in the window and compares it with its database of anchors or other hypertext objects, after which Microcosm can take the appropriate action (e.g., open another window with the destination of a link, even if that destination is in another application).</p>

<p>Applications that are partly aware or unaware of the hypertext service will not know to inform the hypertext service as the user edits information that may contain hypertext links. Therefore, the hypertext service will need some other mechanism to update its link database to ensure link integrity. This problem cannot be solved fully in all cases since users may have modified the document too much to allow the hypertext anchors to be located. Remember that the document itself is typically not allowed to contain any anchor markup in order to keep it compatible with the original application datastructures. The typical solution to the problem of the moving anchors is to remember the location of the anchor before the document was edited and then to search for a location as close as possible with the same text (or other data) as the anchor. Of course, if the user edited the anchor itself or if it was moved too much, then this approach will fail.</p>

<h2 id="toc-integrating-hypertext-ideas-into-other-environments-5">Integrating Hypertext Ideas into Other Environments</h2>

<p>A final architectural observation is that hypertext does not really need to involve a full-fledged set of features. It is possible to utilize a smaller number of ideas from hypertext and integrate them into other computer systems without making them full hypertext systems [Frisse and Cousins 1992].</p>

<p><img alt="Screenshot of HyperView menu" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/31/hyperview_pulldown_menu.png" style="width: 494px; height: 193px;"/><br/>

<strong>Figure 5.8. </strong> <em> A HyperView pop-up menu from the statistics program Data Desk Professional. The user is looking at a table containing an analysis of variance and has indicated a special interest in one of the variables. The pop-up menu now allows the user to open windows with additional statistical analyses and graphs that are especially relevant given this context. </em></p>

<p>For example, the statistics package Data Desk Professional from Odesta has a facility called HyperView which is shown in Figure 5.8. HyperViews allow the user direct access from one statistical analysis to a small number of other analyses that are relevant given the user's current context. Based on its knowledge of statistics, the program "knows" what other statistical analyses people normally want if they have an interest in the selected variable in the context given by the existing table.</p>

<p>The result of making a choice from the menu in Figure 5.8 is to jump to a new window containing the desired analysis or graph. Of course the system has to calculate the content of that window first so the real result is just to activate the statistics package with a given command and a given set of parameters. But to the user it <em> feels </em> like a hypertext-like navigation between connected windows. It is also a great practical advantage of the HyperView facility that it reduces the need for the user to find the correct command among the large set of statistical analyses available in the program and that it automatically specifies the correct parameters.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Emerging Patterns in Interface Design" href="/courses/emerging-patterns-interface-design/?lm=architectural-component-hypertext-systems&amp;pt=article">

<h4 class="title heading-small">Emerging Patterns in Interface Design</h4>

<p id="emerging-patterns-in-interface-design" class="description body-small">

Trending UX patterns and their impact on the total user experience

</p>

<div class="ux-specialties">

<div class="ux-specialty-item">

<svg width="16" height="16" viewBox="0 0 21 21" aria-hidden="true">

<use href="#icon-interaction" />

</svg>

<p class="ux-specialty interaction-design">Interaction</p>

</div>

</div>

</a>

</li>

</ul>

</div>

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">hypertext,Navigation,new technologies</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Navigation</span>

<a class="ga-article-related-topic" href="/topic/navigation/">Navigation</a>

</li>

</ul>

</div>

</div>

</div>

</div>