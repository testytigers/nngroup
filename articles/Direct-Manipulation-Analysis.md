# Layered Interaction Analysis of Direct Manipulation (Jakob Nielsen) - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">25</span>

<div class="article-header">

<h1 class="article-h1">A Layered Interaction Analysis of Direct Manipulation</h1>

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

January 1, 1992

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">1992-01-01</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: A Layered Interaction Analysis of Direct Manipulation&amp;body=https://www.nngroup.com/articles/direct-manipulation-analysis/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/direct-manipulation-analysis/&amp;title=A Layered Interaction Analysis of Direct Manipulation&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/direct-manipulation-analysis/&amp;text=A Layered Interaction Analysis of Direct Manipulation&amp;via=nngroup" data-share-type="Twitter">

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

</span>The concept of direct manipulation is usually viewed as a single characteristic of a class of interaction styles. Here, direct manipulation is analyzed according to a detailed layered interaction model, showing that it has quite different effects on the dialogue on the different levels.

</div>

<div class="article-body">

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

<a class="ga-article-toc-item" href="#toc-1-introduction-1">1. Introduction</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-2-no-errors-2">2. "No Errors"</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-3-directness-and-indirectness-3">3. Directness and Indirectness</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-4-direct-mappings-4">4. Direct Mappings</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-5-conclusions-5">5. Conclusions</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-references-6">References</a>

</li>

</ul>

</div>

</div><h2 id="toc-1-introduction-1">1. Introduction</h2>

<p><a href="https://www.nngroup.com/articles/direct-manipulation/">Direct manipulation</a> (Shneiderman 1982a) has become a popular concept in the user interface field for describing a certain class of interaction styles. Initially, the term was used to characterize entire applications in a strict classification scheme where a system was seen as either having a direct manipulation interface or belonging to some other category of interfaces like natural language, menu-driven, or form fill-in. This usage lead Wixon and Good (1987) to point out the apparent paradox of having several early "canonical" direct manipulation applications make heavy use of menus and form fill-in (dialog boxes). (See Tognazzini (1989) for a discussion of the role of canonical applications in establishing consistency in new user interfaces.) Hutchins et al. (1986) provided an analysis of the concept in terms of semantic and articulatory forms of directness with respect to both execution (input) and evaluation (output) of the dialogue. This analysis was a major step towards realizing that the degree of directness in an interface should be seen as lying on a continuum.</p>

<p>In this paper, direct manipulation and other notions of dialogue directness are analyzed according to a layered interaction model. This kind of model identifies a number of levels on which an interaction takes place, using the lower levels to support the communication on the upper levels. This again means that it becomes possible to talk more precisely about directness in terms of the levels of the interaction model.</p>

<p>The Nielsen virtual protocol model (Nielsen 1986) is used for the analyses in this paper, since it is specifically intended for detailed analysis of dialogue techniques. A short summary of this model is shown in Table 1. Several other layered interaction models exist and could be used with similar results. Nielsen (1986) shows a comparison between the levels in virtual protocol model and the levels in three other popular layered models, and Taylor (1988a; 1988b) presents a general discussion of layered models.</p>

<p> </p>

<table border="1">

<caption valign="bottom"><strong>Table 1. </strong> A summary of the seven levels in the virtual protocol model (Nielsen 1986) with examples from a traditional text editor and an editor with a more modern graphical user interface.</caption>

<tbody>

<tr>

<th>Level Number</th>

<th>Name of Layer</th>

<th>Exchanged unit of Information</th>

<th>Text Example</th>

<th>GUI Example</th>

</tr>

<tr>

<td>7</td>

<td>Goal</td>

<td>Real world concepts, external to computer</td>

<td colspan="2">Remove section of my letter</td>

</tr>

<tr>

<td>6</td>

<td>Task</td>

<td>Computer-oriented objects/actions</td>

<td colspan="2">Delete 6 lines of edited text</td>

</tr>

<tr>

<td>5</td>

<td>Semantics</td>

<td>Concrete objects, specific operations</td>

<td>Delete line no 27</td>

<td>Delete selected lines</td>

</tr>

<tr>

<td>4</td>

<td>Syntax</td>

<td>Sentences (1 or 2 dimensional sequences or layouts) of tokens</td>

<td>DELETE 27</td>

<td>Click to the left of the first line; while holding down the shift-key, click to the right of last line; select CUT in menu</td>

</tr>

<tr>

<td>3</td>

<td>Lexical</td>

<td>Tokens: smallest info-carrying units</td>

<td>DELETE</td>

<td>Click at left of first line</td>

</tr>

<tr>

</tr>

<tr>

<td>2</td>

<td>Alphabetic</td>

<td>Lexemes: primitive symbols</td>

<td>D</td>

<td>Click at (345,120)</td>

</tr>

<tr>

<td>1</td>

<td>Physical</td>

<td>"Hard I/O", light, sound, movement</td>

<td>Press D-key</td>

<td>Press mouse button</td>

</tr>

</tbody>

</table>

<p>Most of the examples in this paper involve the Apple Macintosh Finder (operating system user interface). This is neither because the Finder has a badly designed user interface nor because it is the only possible example, but simply because it is so widely used that most readers should be able to try out the examples in a dynamic interaction if they want to. In some sense, the Macintosh Finder serves as the canonical example of direct manipulation interfaces in the same way as the standard Unix user interface often serves as the canonical example of command line based systems.</p>

<h2 id="toc-2-no-errors-2">2. "No Errors"</h2>

<p>It is frequently claimed that direct manipulation interfaces reduce the need for error messages and this property was one of the main advantages listed in Shneiderman's original article defining the term (Shneiderman 1982a).</p>

<p>As a matter of fact, errors frequently do occur when using direct manipulation systems but in many cases the error messages are pretty poor, maybe because the designers have believed the "no errors" claim. As an example, users of the Macintosh Finder file system interface very often get the error message "An Application could not be found for this Document." This error message succeeds in breaking almost all the standard principles for message design (Shneiderman 1982b): It uses computer-oriented terminology rather than user-oriented terminology, it is general rather than specific, and it is not constructive. So it is no surprise that I have fairly often observed users (including in one case a user with a full year's Macintosh experience) having severe problems with this error message. A more specific message would tell the user the type of the document in question and what application it is intended for. If the document was of a type that could be opened by several applications (typically plain ASCII text or a bitmapped image), the message could also be constructive and inform the user if another application was available which would allow users to work with the specified document.</p>

<p> </p>

<center>

<p><img alt="" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/30/dirman_1.gif" style="width: 176px; height: 160px;"/></p>

<p><br/>

<strong>Figure 1. </strong> Correct operation for "discard document foo" on the Macintosh: The icon representing the document file "foo" is dragged from the window containing "foo" to the Trash icon.</p>

</center>

<p>For several other examples of errors in a direct manipulation dialogue, consider the case of deleting a file in the Macintosh Finder by dragging its icon to the Trash icon. The correct operation is shown in Figure 1. It is impossible to make syntax errors in this dialogue, since any movement of the icon is legal and has some meaning.</p>

<p> </p>

<table align="center" border="0">

<tbody>

<tr>

<td><img alt="Dragging" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/30/dirman_2a.gif" style="width: 166px; height: 146px;"/></td>

<td><img alt="Dragging to the wrong pixel" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/30/dirman_2b.gif" style="width: 174px; height: 157px;"/></td>

</tr>

<tr>

<td><strong>Figure 2a. </strong><br/>

Lexical level error: "Foo" is dragged to the Backup icon instead of to the Trash icon.</td>

<td><strong>Figure 2b. </strong><br/>

Alphabetic level error: "Foo" is released at a pair of screen coordinates which are not inside the Trash icon.</td>

</tr>

</tbody>

</table>

<p>Figure 2a shows an error I have frequently made myself. The file icon is dragged to the icon representing backups, and not to the Trash icon as intended. This mistake constitutes a lexical level error since the syntax of dragging an icon on top of another icon has been correctly specified. It just happens that the second operand of the command has been given an erroneous value. Further analysis shows that the problem is due to a "capture error" (Norman 1983) because the two commands "delete file" and "backup file" start out almost identically by a gesture sweeping the file icon towards the bottom right of the screen. It happened that I had positioned by backup icon next to the Trash icon and that I used backup much more frequently than I used delete. After having observed the frequency of my error and having completed this analysis of the dialogue, my solution was simply to move the backup icon to the lower left part of the screen instead of the lower right. After this change, the gestures for backup and delete start out so differently that I have never since made the error of confusing the two commands.</p>

<p>Figure 2b shows a frequently observed error where the user has moved the document icon to a position just outside the Trash icon. Since most of the outline icon overlaps the Trash icon, the novice user may think that the Trash has been indicated as the destination for the document, but in actual fact, the cursor's "hot spot" is outside the Trash icon and therefore indicates another destination for the document. When the user lets go of the mouse button, the document will not be discarded but will be moved to a new location between the Backup and Trash icons. This is an alphabetic level error because the user is erroneously specifying a point on the screen which is outside the desired region. The experienced user may note the lack of lexical feedback since the Trash icon has not highlighted, thus indicating that it has not been specified, but this absence of feedback is unfortunately easy to miss.</p>

<p>Payne (1990) has also frequently observed users missing the Trash icon. His suggestion for a redesigned interface is to increase the feedback when users do specify the Trash icon as a destination for an icon being moved. He proposes having the outline icon disappear from the screen when it is over the Trash, thus giving a preview of the result of releasing the mouse button. This feedback action would give users information on both the syntax level ("you will have completed an entire command specification if you let go of the mouse button now") as well as the semantic level ("the action specified by this command will be to delete the document"). This increased feedback suggested by Payne might therefore alleviate the problems novice Macintosh users have been observed to have (Nielsen 1987) because of the generic nature of icon movements, since different feedback could be given depending on the chosen destination. For example, it would be possible to distinguish between the <code> move </code> operation started by dragging the document icon to a folder icon from same disk as the document and the <code> copy </code> operation started if the folder was on a different disk. Additional possibilities for enhanced feedback includes the use of sound effects to illustrate the user's actions (Gaver 1989).</p>

<p>For the specific alphabetic level error discussed here, it would probably be better, however, to redesign the lower levels of the dialogue. My suggestion would be either to allow an icon to be specified as the destination symbol for a command if there was more than 50% overlap between it and the icon being dragged, or to implement a "snap-to" attraction between destination icons and the cursor. The level of analysis presented in this paper is not sufficient to decide for sure whether one of these solutions to the icon trashing problem would be better than Payne's solution. The protocol model can only identify problems and suggest possible improvements. It would still be necessary to perform empirical tests in cases like this where there are several competing solutions.</p>

<p>In addition to the lexical and alphabetic errors discussed above, it is even possible to make physical level errors in direct manipulation interfaces. A common example is the manipulation of scrolling lists where the scrolling speed is too fast. When the program runs on a computer with the speed of the original Macintosh Plus, this scrolling works quite nicely, and the user can easily make any desired page number appear in the visible part of the list. Unfortunately, the implementation of the scrolling speed does not take variations in the computer's execution speed into account. When the program is run on the four times faster Macintosh SE/30, the list simply scrolls four times as fast as it did on the Macintosh Plus. This scrolling speed almost always make users overshoot because they hold down the mouse button too long, thus making an error on the physical level of the dialogue.</p>

<p>Finally, errors can also occur on the higher levels of the dialogue. It will often be impossible to avoid goal or task level errors, but in many cases, the computer can help the user in the case of semantic errors. As an example, consider the dialogue specifying the file to be opened by an application. In a traditional, character-based interface, this task would be realized by a command somewhat like<br/>

<code>open foo.txt </code></p>

<p>If the file foo.txt was a text file and the application required a graphics file, this command would constitute an error on the semantic level of the dialogue even though it was syntactically correct. Therefore, the user would get some kind of error message ranging from "ILLEGAL FILE" to "The file 'foo.txt' is a text file and cannot be opened since [Name-of-Application] only supports graphics files"-depending on the attention to usability engineering during the design of the application. In any case, assuming that the user actually wanted to open foo.txt in the current application, the text-based interface did allow the user to express that semantic intention. This action immediately resulted in an error message, thus indicating the user's mistake and hopefully clarifying the situation.</p>

<p>Many modern user interfaces like the Macintosh prevent the user from getting these error messages because they only allow the specification of semantically valid actions. In these systems, users open files by selecting them from a menu listing only those files that are currently legal operands for the open command. Since other files are not on the list, the user cannot click on them, and the interface avoids the "illegal file" message completely. Assume again that a user was in a graphics application and wanted to open the text file foo.txt. Often, the indirect feedback of not listing the file name in the menu will not be sufficient to make users realize their semantic error. Instead, users may conclude that the desired file must have been stored elsewhere in the file system, leading them on a major hunt through their various subdirectories.</p>

<p>Exactly this kind of problem occurred for a user who was the manager of the computer-human interaction group at the National Defence Research Center in a Western European country and was thus no novice user. He was returning to his computer after having been interrupted for slightly more than an hour because of my visit and he wanted to save his work. The Save command was grayed out, however, leading him to exclaim "Save! ... Why won't it Save? How can I get it to Save?" He tried various options without getting the computer's permission to save until he finally remembered that he had actually already saved his work when he was originally interrupted an hour earlier. This user was quite frustrated because it was impossible for him to perform his intended operation and because the computer could provide no feedback in this break-down of a protocol on the task level. An alternative design would have allowed the user to activate even the illegal Save command and would then have provided a simple feedback message somewhat like, "You have made no changes to [Name-of-File] since the last time you saved it."</p>

<p>In situations like those outlined above, having error messages may actually help the user-at least if they are worded according to established human factors principles. Taking the layered protocol view of human-computer interaction implies that negative acknowledgements (error messages) are better than the absence of communication that can easily result from a "no errors" design philosophy.</p>

<h2 id="toc-3-directness-and-indirectness-3">3. Directness and Indirectness</h2>

<p>The very term "direct manipulation" implies some kind of directness in the user interface. Again, the layered protocol analysis indicates some modifications to this supposed advantage. As a matter of fact, it is possible for a direct manipulation interface to feel very indirect to the user on some levels of the dialogue.</p>

<p>For example, setting a tabulator in one desktop publishing program requires the following series of steps:</p>

<ol>

<li>Call up the tabulator dialog box (shown in Figure 3) by using the pull-down menu or pressing a function key.</li>

<li>Since the dialog box appears independently of the text it controls, the user will have to position the dialog box until it is next to the text. Otherwise it will be very hard to compare the tab setting with the text layout. It may also be necessary to scroll the tab ruler if the text line is wider than the dialog box.</li>

<li>Actually change the tab setting by dragging the tab indicator.</li>

<li>Click OK.</li>

<li>Since the text does not reformat during step 3, the user will now have to observe the result of changing the tab setting to see whether the intended layout has been achieved. If not, it is necessary to start over with step 1.</li>

</ol>

<center>

<p><img alt="Complex GUI syntax" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/30/dirman_3.gif" style="width: 431px; height: 118px;"/></p>

<p><br/>

<strong>Figure 3. </strong> Setting the tabulator marker for the text "18 %" in an early version of the desktop publishing program ReadySetGo. The dialog box containing the tab marker can be moved and scrolled independently of the text it controls.</p>

</center>

<p>Each of these steps is actually quite direct and relies on direct manipulation interaction techniques. For example, step 2 is achieved by dragging the dialog box to the desired location, and step 3 involves grabbing the tab marker with the mouse and directly moving it to the desired new setting. In spite of this directness on the lexical level of the dialogue, the complete syntax for the operation turns out to feel very indirect.</p>

<p>Another example of indirectness is based on a complaint by a user (Westland 1988) who reviewed the upgrade of a drawing program in a user group magazine: To perform the task of drawing a rectangle filled with text in the earlier version, one could just draw the rectangle and then immediately start typing from the keyboard. The program would interpret the character input as text which was intended to go into the rectangle. In the revised version one has to first draw the rectangle, then select the "text" mode and use it to define a text region inside the rectangle, and only then type the characters. This later dialogue is more modular and conforms to the general interaction techniques used in the interface. But the user complained about the loss of directness for this frequent special case which now involves two extra steps: 1) select "text", and 2) define input region. The directness in the earlier version was achieved by having a temporal mode for special-case interpretation of keyboard input: If typing occurred as the next action immediately after the drawing of a rectangle, the text went into the rectangle.</p>

<p>Directness sometimes come at the cost of introducing additional complexity in the dialogue. For example, consider the action of pressing down the mouse button while the cursor is over the name of an icon in the Macintosh Finder and then moving the mouse while holding down the mouse button. If the icon had not previously been selected (highlighted), this action will result in moving the icon. But if the icon was the currently selected object, the same action will result in the selection of part of the icon name. A single gesture on the physical level of the dialogue thus has two different interpretations, depending on state of the interface. This modedness of the interaction is necessary to achieve two types of directness: The editing of icon names can be achieved directly by selecting part of the name and typing in a replacement text, thus achieving a direct mapping between the input and output languages for the operation. At the same time, grabbing hold of an unselected icon to move it seems to be a very frequent operation during use of the Macintosh Finder. Therefore, the requirements for precision at the physical level and alphabetical levels of the dialogue are decreased by allowing the user to achieve the lexical level effect of indicating the icon as the operand for the move operation by pointing to any location within the icon or its name.</p>

<p>A final example of directness cannot be achieved by traditional forms of direct manipulation. Assume that a user of a window system has a large and a small window and that the large window is on top, completely hiding the small window. The user now wants to bring the small window to the front and make it visible, but since it is hidden, there is no way for the user to directly manipulate the small window with the mouse. The standard way to perform this task is to first move the large window off to the side to make the small window visible. The user then grabs the small window and moves it to a third location to make room for moving the large window back to its original position. And the user can then finally move the small window back to its original location where it will now be on the top because it was the last object to be selected. This solution is obviously very indirect.</p>

<p>A faster way to solve the problem is by having a special command to bring the large window to the back, thus implicitly bringing the small window to the front. This solution involves an indirect mapping between the task level and the semantic level of the dialogue, as the user will have to realize a task expressed in terms of one object by a semantic operation expressed in terms of another object.</p>

<p>In contrast, the most direct solution to the problem would involve a menu listing all the windows and allow the user to bring a window to the front by choosing its name from the menu.</p>

<h2 id="toc-4-direct-mappings-4">4. Direct Mappings</h2>

<p>As shown in the previous section, interaction styles that are normally considered as direct manipulation can actually be quite indirect from the user's perspective, and there are also situations where directness is better achieved by alternative interaction styles such as menu listings.</p>

<p> </p>

<center>

<p><img alt="Layered communication" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/30/dirman_4.gif" style="width: 248px; height: 153px;"/></p>

<p><br/>

<strong>Figure 4. </strong> The communication principle in the layered protocol model. A communication on level <em> i </em> of the model (indicated by the gray arrow) is realized by an exchange of information on level <em> i-1 </em> . Both the user and the computer will have to translate between the two levels as indicated by the vertical arrows. The units of information exchanged at each level of the model are listed in Table 1.</p>

</center>

<p>The principle of direct mappings between dialogue levels seems to provide a better way to conceptualize directness in interactive systems. As shown in Figure 4, the layered protocol model involves several transformations between different units of information and we would want those transformations to be as direct mappings as possible to make it easy for the user to move between the levels. The idea of direct mappings is similar to the mathematical notion of isomorphisms; there is a one-to-one function between the two levels and the relationships between the units of information are the same on the two levels and are preserved by the function. For the analysis of dialogues, however, it does not seem possible to use the strict mathematical definition, so the term "direct mapping" is used in a slightly looser sense to indicate a feel of close and direct relation between two interaction levels.</p>

<p>As an example of a direct mapping, consider the operation of deleting six lines in a text editor. In a modern display editor, the user's input syntax would involve selecting the six lines and activating the delete command, utilizing a direct mapping from the user's knowledge of what lines to delete and the user's specification of those lines as an operand to the delete command. The system output would involve the removal of the selected lines from the display, thus making the mapping between the user input and the system output extremely direct following the principle of stimulus-response compatibility (John et al. 1985). In a traditional, line-oriented editor, the user input to realize this task would be something like DELETE 27-32 and the result would be an unchanged display on the syntax level even though the lines would be removed at the semantic level. This is indirect with respect to both the mappings just considered.</p>

<p>The directness of mappings is not always a clear-cut property of a dialogue element. For example, I recently designed a hypertext system (Nielsen 1990) with a front page screen depicting a book cover. This illustration served two functions in the user interface. First, it was an output language element intended to indicate that the screen was the front of a hypertext, thus making it easy for users to recognize the screen and its status when they returned to it after some period of reading. Second, the illustration was intended as the control element for getting into the hypertext proper. By clicking on the book cover as an input action, the user would "open the book" and start reading. It turned out that the illustration served the first purpose very well but failed at the second. In other words, the mapping between the lexical element of a book cover and the semantic notion of "beginning of information" was close enough to be immediately understood. But the mapping between the lexical book cover picture and the semantic notion of opening was too indirect, since a book cover suggest being pulled up, while a mouse button is pushed down during a click. Therefore, the physical level action needed to realize the lexical level element of activating the book illustration interfered with its interpretation as part of the input language. This example shows that we still do not know enough about user interface design to rely on a purely mathematical definition of isomorphisms between the levels of the dialogue.</p>

<p>Even though the directness of a mapping cannot be measured exactly, the concept of direct mappings can still be used to gain a better understanding of several forms of directness in user interfaces. In the rest of this section, direct mappings are used as a unifying principle in the discussion of direct manipulation, transparency, WYSIWYG, immediate command specification, articulatory directness, and computational appliances.</p>

<h3>Direct Manipulation</h3>

<p>Direct manipulation may be defined as a direct mapping between the semantic level of the dialogue and the syntactic level. The syntax of operations should correspond to a metaphor of the semantic change in the data and the screen representation of objects should mirror their internal state. The classic example is the file deletion shown in Figure 1. Moving an icon around on the screen corresponds to moving the file in the file system. When the icon is dropped into the Trash icon, the file icon disappears, and (in some implementations) the Trash icon changes to look stuffed.</p>

<p>According to the direct mapping view, direct manipulation is not just related to the dialogue's input language. The output language is also of interest for determining the degree of directness in the mapping between the semantic and the syntactic level of the dialogue. For example, consider a multi-font text editor where the user is about to type some text to be inserted at a point between two existing characters, say, A and B. In many systems, this system state would look something like A|B where the vertical bar | is a blinking insertion cursor. When the user starts typing, the font of the new text could be that of A, that of B, that of the previous text between A and B (if the user had just removed some such text), or it could even be something altogether different (if the user had just issued some font changing command). Most text editors provide no visible indication of this semantic state, leaving the user to guess. In most cases, this lack of information does not matter since A, B, and the new text will all have the same font. Otherwise, the user will have to start typing to learn what font will be used, leading to a small degree of indirectness: There is no way to "directly manipulate" (or learn) the font state at the insertion mark since it represents an empty object.</p>

<h3>Transparency</h3>

<p>Transparency (Maass 1983) is a direct mapping between goal level and the semantic level. What you want to do and what you can do corresponds, and it is not necessary to think about transforming real world objects and operations to computer-oriented objects and actions. The term itself suggests the "disappearance" of the computer-oriented concepts in the dialogue.</p>

<p>A typical example of the lack of transparency is the complicated installation procedures involved in transferring certain large applications from the floppy disks on which they are sold to the user's hard disk. The user's goal is to move the application to the hard disk and to run it, but it is sometimes necessary for the user to follow long and complicated instructions on how to establish various subdirectories and to copy files from the floppies in a specific order. These computer-oriented concepts and actions are completely unnecessary from the user's goal perspective.</p>

<h3>WYSIWYG</h3>

<p>To achieve WYSIWYG (what you see is what you get), there should be a direct mapping between the goal state (what you want) and the syntax level (what you see). Remember that the syntax level contains the two-dimensional layout of the dialogue elements on the screen. In a WYSIWYG interface, the screen representation of objects mirrors the real world, and the syntax of operations correspond to the desired real world action.</p>

<p>As an example, most mouse-based interfaces have a two-cursor problem (Brooks 1988) where one cursor is used to point and another cursor indicates where text input will appear. Users often confuse these two cursors because of the lack of WYSIWYG in the interface. The pointing cursor that tracks the user's mouse movements is the user's focus of attention ("what you see") in the syntax, but the input ("what you get") changes the output product according to the location of the insertion mark. One possible solution to the two-cursor problem is to follow a strict WYSIWYG interpretation of a single cursor where input appears wherever the pointer happens to be when the user hits the keyboard (Akscyn et al. 1988).</p>

<p>Changing the headers in one early graphical-interface word processor required the user to open a special window for the header. The actual editing followed direct manipulation principles as defined here since there was a direct mapping between the syntax for changing the header and the semantic change in the stored header information. But the interaction technique was not WYSIWYG since the user could not easily translate between the syntax for changing the header and the goal of making the header look a specific way in relation to the rest of the page. For a true WYSIWYG editing of headers, it becomes necessary to make them editable in the main window together with the main sequence of text in the file.</p>

<h3>Immediate Command Specification</h3>

<p>Immediate command specification involves a direct mapping between the syntactic level and the alphabetic level to allow users to package an entire command in a single, atomic input action. Typical examples are function keys in traditional interfaces and the double click shortcuts in many graphical user interfaces. It is also possible to allow the individual user to build "buttons" (MacLean et al. 1990) that run a complex sequence of operations when they are activated.</p>

<p> </p>

<center>

<p><img alt="Change bar dialog box" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/30/dirman_5.gif" style="width: 193px; height: 151px;"/></p>

<p><br/>

<strong>Figure 5. </strong> Interface control for specifying borders surrounding the text in a word processor. Here, the user has specified that a wide bar is to appear in the left margin.</p>

</center>

<p>Figure 5 shows a control for specifying text borders in a word processor with a graphical user interface. This interface has both direct manipulation, WYSIWYG, and transparency aspects. The WYSIWYG property comes from the direct correspondance between the position of the borders on the miniature page and their position on the screen and the final printout. The syntax for placing the border lines on the miniature uses a direct manipulation technique corresponding directly to the semantics: Clicking first on the fat line in the palette and then on the left margin of the miniature page. Finally, the semantics of having a wide bar in the left margin correspond directly to the goal of getting a fat line in the margin because the interface has been simplified</p>

<p>A user who often wanted a wide bar to appear in the left margin could construct a button (perhaps labelled "Make Change Bar") that would have the same effect as calling up the control in Figure 5 and modifying it as shown. This hypothetical interface would be an immediate command specification. As this example shows, macros or other user-constructed customizations will often be necessary for immediate command specification unless the interface designer has conducted a very detailed task analysis.</p>

<h3>Articulatory Directness</h3>

<p>Articulatory directness involves a direct mapping between the alphabetic level and the physical level to ensure that the primitive input actions correspond to the user's physical actions. The classic example is the input unit of moving the cursor to a specific set of screen coordinates, (x,y). The highest articulatory directness is achieved by touching a touch screen at (x,y) since there is practically no transformation between the two levels. A slight degree of indirectness is involved in using a mouse since it is not moved in the same plane as the screen coordinates being specified. Even so, moving the mouse still has higher articulatory directness than combining a set of activations of the arrow keys.</p>

<p>In many visual interfaces, input actions sometimes involve not just the specification of a single point but the specification of a curve. When the curve is used to drag an icon, the mouse has a higher articulatory directness than a stylus, whereas the stylus has a higher articular directness than the mouse when it comes to handwriting input because of the different requirements for the preciseness of the curve.</p>

<h3>Computational Appliances</h3>

<p>The computational appliance principle involves a direct mapping all the way from the goal level to the physical level. The computer as tool, where you do not really "interact" with the computer as such-you just do your work. The computational appliance idea is really to achieve the ultimate directness.</p>

<p>An example of a measurement of the extent to which a computer served as a computational appliance, is the study by Haas (1989) of users revising a text either in a computer editor or using pen and paper. She had test subjects think aloud while they edited the text and she then counted the proportion of their utterances referring to the editing medium instead of the writing task. In the pen and paper condition, only 3% of the utterances referred to the medium, while 14% of the utterances in the computer condition did so. In the ideal case, users would be able to focus completely on their primary task and just deal directly with it without having to think about the computer at all. Haas' study indicates that we still have some way to go to achieve this goal.</p>

<p>In the computational appliance mapping, there is a direct connection between the user's input and the achieved goal, and the computer's output is interpreted as a signal for the real world goal state instead of signs or symbols of the computer's state (Rasmussen 1983). With current computers, the computational appliance mapping is of course easiest to achieve for text editing where the input and output equipment on modern workstations almost completely match the goal of producing sheets of paper with letters on them.</p>

<h2 id="toc-5-conclusions-5">5. Conclusions</h2>

<p>Analyzing the concept of direct manipulation according to a detailed layered interaction model indicates several modifications to a simplistic view-especially with respect to error situations where usability often is better served by explicit error handling. Furthermore, it seems that a more general notion of directness is more relevant for usability than the traditional concept of direct manipulation, since some direct manipulation designs can feel very indirect. The direct mapping principle presented here accounts for several other common interaction concepts such as WYSIWYG in addition to direct manipulation.</p>

<p> </p>

<center>

<p><img alt="Layered communication" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/30/dirman_6.gif" style="width: 310px; height: 327px;"/><br/>

<strong>Figure 6. </strong> Summary of the direct mappings discussed in section 4. For simplicity, the figure only shows those interaction levels actually involved in these mappings, but similar mappings could be defined between the rest of the interaction levels.</p>

</center>

<p>Summary of the direct mappings discussed in section 4. For simplicity, the figure only shows those interaction levels actually involved in these mappings, but similar mappings could be defined between the rest of the interaction levels. Previous work has shown that experienced users find the concept of "user friendliness" more closely related to whether an application is pleasant to work with than to whether it is easy to learn (Nielsen 1989). Even though it is not really known what makes an interface pleasant, it is likely that the various forms of directness contribute to pleasantness. Another likely contributing factor is good-looking graphic design. Further research is required to address this issue.</p>

<h3>Acknowledgements</h3>

<p>The author would like to thank Saul Greenberg, Robert Jacob, and John Schnizlein for helpful comments on earlier versions of the manuscript.</p>

<h2 id="toc-references-6">References</h2>

<ol>

<li>Akscyn, R., McCracken, D., and Yoder, E. (1988). KMS: A distributed hypermedia system for managing knowledge in organizations. Communications of the ACM 31, 820-835.</li>

<li>Brooks, F.P., Jr. (1988). Grasping reality through illusion-Interactive graphics serving science. Proceedings ACM CHI'88 (Washington, DC, 15-19 May), 1-11.</li>

<li>Gaver, W.W. (1989). The SonicFinder: An interface that uses auditory icons. Human-Computer Interaction, 4, 67-94.</li>

<li>Haas, C. (1989). Does the medium make a difference? Two studies of writing with pen and paper and with computers. Human-Computer Interaction, 4, 149-169.</li>

<li>Hutchins, E.L., Hollan, J.D., and Norman, D.A. (1986). Direct manipulation interfaces. In: D.A. Norman and S.W. Draper (eds.): User Centered System Design: New Perspectives on Human-Computer Interaction, Hillsdale, NJ: Lawrence Erlbaum Associates, 87-124.</li>

<li>John, B.E., Rosenbloom, P.S., and Newell, A. (1985). A theory of stimulus-response compatibility applied to human-computer interaction, Proceedings ACM CHI'85 (San Francisco, CA, 14-18 April), 213-219.</li>

<li>Maass, S. (1983). Why systems transparency? In: T.R. Green, S.J. Payne, and G.C. van der Veer (eds.): The Psychology of Computer Use. London: Academic Press, 19-28.</li>

<li>MacLean, A., Carter, K., Lovstrand, L., and Moran, T. (1990). User-tailorable systems: Pressing the issues with buttons. Proceedings ACM CHI'90 (Seattle, WA, 1-5 April), 175-182.</li>

<li>Nielsen, J. (1986). A virtual protocol model for computer-human interaction. International Journal of Man-Machine Studies, 24, 301-312.</li>

<li>Nielsen, J. (1987). A user interface case study of the Macintosh. In: G. Salvendy (ed.): Cognitive Engineering in the Design of Human-Computer Interaction and Expert Systems. Amsterdam: Elsevier Science Publishers, 241-248.</li>

<li>Nielsen, J. (1989). What do users really want? International Journal of Human-Computer Interaction, 1, 137-147.</li>

<li>Nielsen, J. (1990). The art of navigating through hypertext. Communications of the ACM, 33, 296-310.</li>

<li>Norman, D.A. (1983). Design rules based on analyses of human error. Communications of the ACM, 26, 254-258.</li>

<li>Payne, S.J. (1990). Looking HCI in the I. Proceedings IFIP INTERACT'90 Conf. (Cambridge, U.K., 27-31 August), 185-192.</li>

<li>Rasmussen, J. (1983). Skills, rules, and knowledge: Signals, signs, and symbols, and other distinctions in human performance models. IEEE Transactions on Systems, Man, and Cybernetics, 13, 257-264.</li>

<li>Shneiderman, B. (1982a). The future of interactive systems and the emergence of direct manipulation. Behaviour and Information Technology, 1, 237-256.</li>

<li>Shneiderman (1982b). Designing computer systems messages. Communications of the ACM, 25, 610-611.</li>

<li>Taylor, M.M. (1988a). Layered protocols for computer-human dialogue I: Principles. International Journal of Man-Machine Studies, 28, 175-218.</li>

<li>Taylor, M.M. (1988b). Layered protocols for computer-human dialogue II: Some practical issues. International Journal of Man-Machine Studies, 28, 219-257.</li>

<li>Tognazzini, B. (1989). Achieving consistency for the Macintosh. In: J. Nielsen (ed.): Coordinating User Interfaces for Consistency, San Diego, CA: Academic Press, 57-73.</li>

<li>Westland, M.J. (1988). 10 steps forward, 2 steps back, The Active Window (Boston Computer Society), 5 (August), 36-40.</li>

<li>Wixon, D. and Good, M. (1987). Interface style and eclecticism: Moving beyond categorical approaches. Proceedings Human Factors Society 31st Annual Meeting, 571-575.</li>

</ol>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Application Design for Web and Desktop" href="/courses/application-ux/?lm=direct-manipulation-analysis&amp;pt=article">

<h4 class="title heading-small">Application Design for Web and Desktop</h4>

<p id="application-design-for-web-and-desktop" class="description body-small">

Components, design patterns, workflows, and ways of interacting with complex data

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">direct manipulation,Application Design,Human Computer Interaction</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Application Design</span>

<a class="ga-article-related-topic" href="/topic/applications/">Application Design</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/human-computer-interaction/">Human Computer Interaction</a>

</li>

</ul>

</div>

</div>

</div>

</div>