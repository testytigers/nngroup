# Navigating Information Spaces: Article by Jakob Nielsen - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">32</span>

<div class="article-header">

<h1 class="article-h1">Navigating Large Information Spaces</h1>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Navigating Large Information Spaces&amp;body=https://www.nngroup.com/articles/navigating-large-information-spaces/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/navigating-large-information-spaces/&amp;title=Navigating Large Information Spaces&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/navigating-large-information-spaces/&amp;text=Navigating Large Information Spaces&amp;via=nngroup" data-share-type="Twitter">

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

</span>A variety of navigation elements can be employed to help users avoid getting &quot;lost&quot; in digital environments. This chapter provides and overview of different navigation structures  including history lists, bookmarks, overview diagrams, and navigational dimensions and metaphors.

</div>

<div class="article-body">

<div><em>This is chapter 9 from Jakob Nielsen's book <a href="http://www.nngroup.com/books/multimedia-and-hypertext/"> Multimedia and Hypertext: The Internet and Beyond</a>, Morgan Kaufmann Publishers, 1995. (For full literature references, please see the bibliography in the book.)</em></div>

<div> </div>

<p>When users move around a large information space as much as they do in hypertext, there is a real risk that they may become disoriented or have trouble finding the information they need. To investigate this phenomenon, we conducted a field study where users were allowed to read a Guide document at their own pace [Nielsen and Lyngbæk 1990].</p>

<p>Even in this small document, which could be read in one hour, users experienced the "lost in hyperspace" phenomenon as exemplified by the following user comment: "I soon realized that if I did not read something when I stumbled across it, then I would not be able to find it later." Of the respondents, 56% agreed fully or partly with the statement, "When reading the report, I was often confused about 'where I was.'"</p>

<p>Users also had problems using the inverse operations of the Guide hypertext buttons to return to their previous system states, as can be seen from the 44% agreement with the statement, "When reading the report, I was often confused about 'how to get back to where I came from.'" One reason for the confusion felt by many users is probably that Guide uses different backtrack mechanisms depending on which type of "button" (link mechanism) was used originally. Several users complained that Guide does not reestablish a completely identical screen layout when returning to a previous state after a backtrack operation. This change makes it more difficult to recognize the location one has returned to and thus complicates the understanding of the navigational dimensions of the hyperspace.</p>

<p>There are several possible solutions to the navigation problem. The most simple from the user's perspective may be to remove the requirement for navigation by providing guided tours [Trigg 1988] through the hypertext somewhat like the original "trails" suggested by Vannevar Bush in 1945. A guided tour may be thought of as a "superlink" that connects a string of nodes instead of just two nodes. As long as users stay on the guided tour, they can just issue a "next node" command to see more relevant information. The Perseus system (see Figures 4.16 and 4.17) have a "path" icon for use in moving back or forth along the selected guided tour. The system also provides the path editor shown in Figure 9.1 listing the names of all the nodes in a path and allowing users to add new nodes or remove or rearrange the existing nodes. Path navigation may be done manually by the user, or the system may automatically forward to the next node on the path after a specified wait [Zellweger 1989]</p>

<p><img alt="Screenshot of path editor" height="346" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/31/perseus_path_editor.png" width="482"/><br/>

<strong>Figure 9.1. </strong> <em> The path editor in Perseus. Each icon (called a "footprint") is a reference to a node in the hypertext. Copyright © 1989 by the President and Fellows of Harvard University and the Annenberg/CPB Project, reprinted with permission. </em></p>

<p>Guided tours can be used to introduce new readers to the general concepts of a hypertext, and one can also provide several different guided tours for various special-interest readers. The advantage of hypertext guided tours compared to tourist guided tours is that the hypertext reader can leave the guided tour at any spot and continue browsing along any other links that seem interesting. When the reader wants to get back on the tour, it suffices to issue a single command to be taken back to the point where the tour was suspended. The "guide" will be waiting as long as it takes.</p>

<p>Guided tours are nice, but they really bring us back full circle to the sequential linear form of information. Even though guided tours provide the option of side trips, they cannot serve as the only navigation facility since the true purpose of hypertext is to provide an open exploratory information space for the user.</p>

<h3>Backtrack</h3>

<p>Probably the most important navigation facility is the backtrack, which takes the user back to the previous node. Almost all hypertext systems provide some form for backtrack but not always very consistently, and we found in the Guide study mentioned above that inconsistency in backtracking could give users trouble. The great advantage of backtrack is that it serves as a lifeline for the user who can do anything in the hypertext and still be certain to be able to get back to familiar territory by using the backtrack. Since backtrack is essential for building the user's confidence it needs to fulfill two requirements: It should always be available, and it should always be activated in the same way. Furthermore, it should in principle be possible for the user to backtrack enough steps to be returned all the way to the very first introduction node. Even though much of the functionality of backtrack can be achieved by a hypertext design where the user can see the previous nodes (e.g., in a table of contents), there are great benefits to being able to go back without having to spend time on figuring out how to do so [Vargo et al. 1992].</p>

<p>Electronic Art's multimedia version of <cite> Peter Pan </cite> includes a special form of backtrack in the form of a replay option accessed through an hourglass icon. This interactive fiction is aimed at 3-8 year old children who often like to repeat the same actions over again, and clicks on the replay icon will move back in the story to allow the child to reexperience fun animations or other special scenes.</p>

<p>Alternatively, a child can use the hypermedia aspects of the system during replay to see what would happen if he or she chose an alternative course of action at a branching point in the story.</p>

<p><img alt="Five models for the 'Back' feature in hypertext navigation" height="540" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/31/hypertext_backtrack_model.png" width="744"/><br/>

<strong>Figure 9.2. </strong> <em> Various backtrack models. Sequence 1 represents the user's initial navigation and sequences 2-5 represent possible backtrack movement. Sequence 6 shows a more complicated example of sequence 2. </em></p>

<p>Backtrack is conceptually very simple: the user clicks on a button and is returned to the previous node. The problem arises when the user backtracks more than once and when the user has visited certain nodes more than once. Sequence 1 in Figure 9.2 shows an example of a navigation sequence where the user has started in node <strong> A </strong> , moved to node <strong> B </strong> and <strong> C </strong> , then revisited node <strong> B </strong> , and finally moved on from <strong> B </strong> to <strong> D </strong> . The simplest backtrack model is chronological backtrack as shown in sequence 2, where all the nodes are visited again in the opposite order.</p>

<p>The main problem with chronological backtrack is that it is inefficient for the users to spend time on revisiting the same node multiple times just because they originally went through it several times. In our example in Figure 9.2, node <strong> B </strong> is the only one to be revisited, but users often move back and forth between a few nodes several times before deciding to backtrack out, and chronological backtrack would involve too many visits to the same nodes. To avoid this problem, several alternative backtrack models have been proposed.</p>

<p>My favorite backtrack model is the single-revisit backtrack shown in sequence 3 in Figure 9.2. Single-revisit backtrack works like chronological backtrack, but the computer keeps track of what nodes have already been revisited during the current backtrack sequence and does not show them a second time. A backtrack sequence is a sequence of user navigation actions that includes nothing but backtrack commands (and possibly local movement within the current node in systems with features like panning or scrolling). As soon as the user navigates to another node using any command other than backtrack, the backtrack sequence is interrupted. There are two ways of dealing with interrupted backtrack sequences. My preference is to reset the backtrack sequence and start a new one the next time the user initiates a backtrack command. I will call this approach simple single-revisit backtrack. The alternative, strict single-revisit backtrack, is to have the system remember the backtrack sequence and continue to add to it the next time the user backtracks. Unfortunately, strict single-revisit backtrack involves a further complication since it is necessary to remove the current node from the remembered backtrack sequence at the time when the user interrupts the backtrack sequence. Otherwise, users would not be able to revisit this node, and backtracking from node <strong> E </strong> in sequence 6 in Figure 9.2. would take the user directly to node <strong> A </strong> without stopping at node <strong> C </strong> .)</p>

<p>Sequence 6 in Figure 9.2 shows an example of an interrupted backtrack sequence. The user first moves <strong> ABCBD </strong> and then backtracks to node <strong> C </strong> . At this time, the backtrack sequence contains nodes <strong> D </strong> , <strong> B </strong> , and <strong> C </strong> , and a subsequent backtrack command would have moved the user back to node <strong> A </strong> (as shown in sequence 3) since the single-revisit backtrack model will skip the first occurrence of node <strong> B </strong> . In sequence 6 the user has chosen to move from <strong> C </strong> to <strong> E </strong> , however, thus interrupting the current backtrack sequence. When the user issues a backtrack command from node <strong> E </strong> , the system will first move back to node <strong> C </strong> . A second backtrack command will move to node <strong> B </strong> in the simple single-revisit backtrack model (as shown in sequence 6 in Figure 9.2) and all the way to node <strong> A </strong> in the strict single-revisit backtrack model.</p>

<p>First-visit backtrack (sequence 4 in Figure 9.2) is related to single-revisit backtrack but probably harder to understand and less useful for most applications. In both cases, each node is only revisited once, but nodes that have been visited multiple times are treated differently. In first-visit backtrack, only the first visit to a node is considered a backtrack candidate, whereas in single-revisit backtrack it is the last visit to a node that is the backtrack candidate.</p>

<p>Detour-removing backtrack (sequence 5 in Figure 9.2) was suggested by Bieber and Wan [1994] as a way to avoid backtracking through nodes that were visited by mistake. The notion is to detect when the user has been on a detour through hyperspace and returns to a main navigation sequence. The detour can then be eliminated from any subsequent backtrack. In Figure 9.2, the user's movement from B to C and back to B would suggest that the visit to C was a mistake and should be treated as a detour. The difficulty in detour-removing backtrack is obviously to detect the detours and there is currently no empirical evidence to suggest that this is possible in the general case.</p>

<p>The backtrack models so far are all identical with respect to the required user action: the user simply clicks on the "go back" button. The button may be generic, or it may include the name of the node to which the user will be returned. This latter approach is taken in General Magic's Magic Cap interface [Knaster 1994] where the name of the previous location is consistently listed in the upper right corner of the screen (e.g., <img alt="Picture of a pointing hand" height="15" loading="lazy" src="//media.nngroup.com/media/editor/2012/12/14/hand.gif" width="31"/> <strong> Hallway</strong>). A more advanced, but also more complicated, option is to offer parameterized backtrack [Garzotto et al. 1995] where the user can specify some condition and backtrack to the most recently visited node for which the condition holds. In hypertext systems with typed nodes, the most common use of parameterized backtrack is to backtrack to nodes of a certain type. For example, in a banking system, the user might want to backtrack to the last time a "customer" node was visited.</p>

<h3>History Lists</h3>

<p>Some hypertext systems provide more general history mechanisms than the simple backtrack. For example, some systems have history lists like Figure 9.3 to allow users direct access to any previously visited node. Figure 9.3 shows a best-case user interface for a history list where it is possible to combine pictures and text for each object. A combination of the two is to be preferred because the two media complement each other (see, for example, the two different meanings of the word "paint" in Figure 9.3) and make it easier for users to understand the meaning of each element in the list [Egido and Patterson 1988]. The two obvious alternatives for history lists are text alone (often the node name, as shown in Figure 2.10) or pictures alone (shown in Figure 9.5). The choice between the two will depend on the visual nature of the content of the nodes, since pictures only make sense if they are sufficiently distinct and characteristic to be recognized quickly. Finally, it is of course possible to use some other representation like the miniatures shown in Figure 9.4.</p>

<p><img alt="history list" height="448" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/31/history_list.png" width="642"/><br/>

<strong>Figure 9.3. </strong> <em> The history list in My First Incredible, Amazing Dictionary (a children's dictionary). The system shows the ten most recently visited nodes and allows the user to return directly to any one of them. Note that even though the dialog box is called "Backtrack," it is actually a history list in the terminology used in this book. Copyright © 1994 by Dorling Kindersley, reprinted by permission. </em></p>

<p>Since users are most likely to want to return to nodes they have visited relatively recently, it is possible to display the top part of the history list as a "visual cache" like Figure 9.4 where a small number of nodes are kept permanently visible on the primary display. The design in Figure 9.4 represents the nodes by miniatures [Nielsen 1990f] of their graphic layout, but it is also possible to use icons or just the names of the nodes. Compare with Figure 9.5 to see how much better miniatures work when representing graphical nodes than the mostly text-oriented nodes in Figure 9.4. When the visual cache is shown as a horizontal list it is also sometimes referred to as a "visit shelf" because it stores the places that have been visited recently.</p>

<p><img alt="History of thumbnails that form a visual cache of recently seen pages" height="335" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/31/thumbnail_navigation.png" width="513"/><br/>

<strong>Figure 9.4. </strong> <em> A "visual cache" of thumbnail miniatures of the five most recently visited nodes. From a prototype window-oriented videotex system designed in my group at the Technical University of Denmark in 1989 (implementation by Flemming Jensen). </em></p>

<h3>Bookmarks</h3>

<p>Hypergate and some other systems allow users to define bookmarks at nodes they might want to return to later. The difference between bookmarks and history lists is that a node gets put on the bookmark list only if the user believes that there might be a later need to return to it. This condition means that the bookmark list is smaller and more manageable, but it also means that it will not include everything of relevance. It frequently happens that you do not classify something as relevant until a later time, when its connection with something else suddenly becomes apparent. Then it is nice to be able to find it on the history list, which the system has automatically been keeping for you.</p>

<p><img alt="Miniatures of salient items from previously visited screens used for backtrack navigation" height="602" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/31/miniatures_navigation.png" width="794"/><br/>

<strong>Figure 9.5. </strong> <em> Museum information system from the National Museum of Denmark. Users can navigate back to the eight most recently visited nodes by touching the miniatures at the bottom of the screen. Note that the miniatures do not represent the entire screen but only the photograph of the artifact, making them easier to recognize. Miniatures of illustrations instead of the full screens are sometimes referred to as a comic book interface [Lesk 1991]. Buttons link to information about the use and origin of the artifact and to a diagram showing where the object is exhibited in the room, thus providing a simple kind of augmented reality [Wanning 1993]. Copyright © 1994 by the National Museum of Denmark, reprinted by permission. </em></p>

<p>When the user defines a bookmark, the system may put the node's name on the bookmark list, or it may prompt the user for a small text to remember the node by. Bookmarks are more useful in hypertexts than in regular books because it is possible to use more of them. It is easy for a user to scan a menu of twenty node names that have been marked, whereas the same number of physical bookmarks in a book would be a complete mess to handle.</p>

<p>A special kind of bookmark would allow a user to resume the session with a hypertext system after an interruption and keep the state of the hypertext unchanged. A "smart bookmark" might even show some additional context to reorient the reader in the information space.</p>

<p>The Symbolics Document Examiner offers a special feature where users can build a list of references to nodes that they might want to remember to look at later. These references might be picked up from links in previously visited nodes and thus alleviate the problem of only being able to navigate to one new node at a time in most hypertext systems. This feature is called a bookmark list but might more appropriately be called a "shopping list."</p>

<p>Bookmarks have classically been seen as list elements in a bookmark list. The main advantage of this approach is that a single centralized bookmark list makes it easy for the user to determine how to get to the bookmarks (just open the list with the single command dedicated to that purpose) and how determine what bookmarks exist (just scan the list). A variant of this approach is used in the Netscape WWW browser (a variant of Mosaic). Users tend to collect a very large number of bookmarks pointing to WWW pages because of the difficulty of finding locations on the Web (due to the lack of overview diagrams or other navigational aids). These bookmark collections are normally referred to as hotlists, and it is quite common for WWW hotlists to contain 50 or more items. In order to manage these large lists, Netscape uses a hierarchical bookmark list, where the user can add dividers and a nested set of named categories. Users can then add new bookmarks to the general list, or they can place them in the appropriate category.</p>

<p>Bookmarks can also be seen as objects in their own right, meaning that they can have an existence outside the bookmark list. The advantage of this approach is obviously the added flexibility to move bookmarks around and to build different kinds of collections of bookmarks for different purposes. The downside is that the added features complicate the user interface and make it less clear what bookmarks exist in the system. Object-oriented bookmarks are used in General Magic's Magic Cap user interface. When the user defines a bookmark, it is visualized with a paper clip icon (a fairly common icon for bookmarks). The user can peel off copies of the bookmark icon and drag them to other places in the interface from which they act as links to the bookmarked page.</p>

<p><img alt="Visualization of a navigation hierarchy with viewport onto current location" height="436" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/31/ia_tree_overview.png" width="322"/><br/>

<strong>Figure 9.6. </strong> <em> The navigator overview window from the SGI Topic/Task Navigator (see Figure 9.21). The rectangular "viewport" indicates the part of the tree currently visible in the main window and the user can move to other views by dragging the viewport with the mouse. Copyright © 1994 by Silicon Graphics, Inc., reprinted by permission. </em></p>

<h2>Overview Diagrams</h2>

<p>Since hypertext is so heavily based on navigation, it seems reasonable to use a tourist metaphor and try to provide some of the same assistance to hypertext users as one gives to tourists. One option is the guided tour as mentioned above, but as hypertext users are mostly supposed to find their own way around the information space, we should also give them maps. Since the information space will normally be too large for every node and link to be shown on a single map, many hypertext systems provide overview diagrams to show various levels of detail.</p>

<p>The system described in Chapter 2 uses both a global and a local overview diagram and displays both of them on the screen at the same time. An alternative is to acknowledge that the overview diagram has to be large and then provide a second layer of navigational mechanisms to move within the overview. This "meta-navigation" might be represented as an orthogonal dimension to the main information space through a zoom facility to allow users to see more or less detail. There have also been a few attempts to design three dimensional overview diagrams [Fairchild et al. 1988; Fairchild 1993; Robertson et al. 1991]. Finally, meta-navigation may be accomplished by moving a viewport indicator over a reduced representation of the main diagram as shown in Figure 9.6. Viewports (sometimes called panners) can be moved by direct manipulation and thus allow the user to quickly access other parts of the main diagram at the same time as the reduced view provides an indication of the structure of the data in the main view.</p>

<p>Overview diagrams can be particularly useful for students who can use them not just to navigate the hypertext but also to understand the domain matter. Figure 9.7 shows an example of use of overview diagrams to bring out literary structures in English literature in the Dickens Web developed at Brown University. The "Literary Relations" overview shows authors that influenced Dickens above his name and authors that were influenced by Dickens below his name. Each name is linked to articles about the various authors, so the diagram serves as an overview of the part of the hypertext that talks about various authors. Actually, not only is the "Literary Relations" a local overview of the "author" part of the hypertext, it has been filtered to a specialized local overview of only those authors who are relevant for an understanding of the novel <cite> Great Expectations</cite>.</p>

<p><img alt="Multiple overviews maps showing alternate views of the information space." loading="lazy" src="//media.nngroup.com/media/editor/2012/10/31/multiple_overview_maps.png"/><br/>

<strong>Figure 9.7. </strong> <em> Use of multiple overview diagrams in the Dickens Web [Landow and Kahn 1992]. The "Literary Relations" overview gives students an understanding of the relation between Charles Dickens and other authors and the "Great Expectations" overview shows the various issues relevant for a discussion of that novel. In addition, the figure shows a structural overview of the hypertext generated automatically by the Storyspace system. Copyright © 1992-94 by Paul Kahn, George P. Landow, and Brown University, reprinted by permission. </em></p>

<p>An alternative to multilevel overviews is to use a fisheye view [Furnas 1986] like the one in Figure 9.8 that can show the entire information space in a single overview diagram using varying levels of detail. A fisheye view shows great detail for those parts of the information that are close to the user's current location of interest and gradually diminishing amounts of detail for those parts that are progressively farther away. The use of fisheye views therefore requires two properties of the information space: It should be possible to estimate the distance between a given location and the user's current focus of interest, and it should be possible to display the information at several levels of detail. Both conditions are met for hierarchical structures like that shown in Figure 9.8, but they may be harder to meet for less highly structured hypertexts.</p>

<p>In addition to showing users the layout of the information space, overview diagrams can also help users understand their current location and their own movements. To achieve this understanding, the overview diagram should display the user's "footprints" on the map to indicate both the current location and the previous ones.</p>

<p><img alt="Fisheye view of a hierarchy." height="290" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/31/fisheye_view.png" width="561"/><br/>

<strong>Figure 9.8. </strong> <em> A fisheye view-like browser from Interactive NOVA. Copyright © 1989 by Apple Computer, Inc., WGBH Educational Foundation, and Peace River Films, Inc., reprinted with permission. </em></p>

<p>If the information space in a hypertext has an underlying structure, that structure may be used to make the overview diagram easier to interpret. For example, Figure 9.9 shows parts of the overview diagram for the online proceedings of the 23rd International Congress of Applied Psychology. Along the left part of the diagram is a listing of the different areas of psychology covered by the congress and across the top are the various categories of presentations. The cells in the diagram show the number of objects one would see by going to that combination of topic and format.</p>

<p><img alt="Screenshot of an overview table" height="400" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/31/congress_overview_table.gif" width="625"/><br/>

<strong>Figure 9.9. </strong> <em> Part of the contents overview in the online proceedings of the 23rd International Congress of Applied Psychology (the full overview has several additional entries. <a href="http://www.ucm.es/23ICAP/23icap.html"> http://www.ucm.es/23ICAP/23icap.html</a>). Copyright © 1994 by the 23rd International Congress of Applied Psychology, reprinted by permission. </em></p>

<p>Figure 9.10 shows a review grid from the Interchange online service. The review grid nicely summarizes the content of a large number of reviews and provides hypertext links to the original reviews. Notice how the typed hypertext anchors give a preview of each review: solid anchors are used for links to positive reviews and hollow anchors are used for links to negative reviews, thus allowing the user to dismiss products that have been negatively reviewed without having to navigate to the actual review. This ability of the hypertext overview diagram to summarize the content of the individual reviews highlights the power and responsibility of the hypertext editor since users probably will skip reading about products that are linked to by negative anchors.</p>

<p><img alt="Overview of a set of reviews in the form of a grid with scores." height="488" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/31/review_grid.png" width="648"/><br/>

<strong>Figure 9.10. </strong> <em> Review grid from the Interchange online service. By clicking on one of the review markers, the user can jump to the full review. Copyright © 1994 by Interchange Network Company, reprinted by permission. </em></p>

<p>If the information space can be structured in multiple ways, some research suggests advantages from making several different overview diagrams available to the users. For example, Vora et al. [1994] studied a hypertext about nutrition that could be structured in three different ways: according to vitamins (Vitamin A, Vitamin B, etc.), according to food source (fruit, vegetables, grains, etc.), and according to the diseases and other health problems that can be caused or prevented by eating various food and vitamins. Users performed search tasks 21% faster in a system with overview diagrams for all three structure schemes than in a system where the only overview diagram was one for the vitamins. On the other hand, other studies suggest that multiple organizational schemes may make it more difficult for learners to construct their own mental models of the information space because they do not consistently get reinforcement from a single diagram. In the nutrition hypertext, the three different perspectives on the data were familiar to the users and were probably easy to distinguish, and this may have been the cause of the positive result in Vora et al.'s experiment.</p>

<p>Guided tours and map are both known to help tourists, and to continue the tourist metaphor for hypertext, another facility that often helps users navigate is the use of landmarks in the form of especially prominent nodes. Tourists who visit Paris quickly learn where the Eiffel Tower is and how to use it and a few other landmarks for orientation. Almost all hypertext systems define a specific node in a document as the introductory node and allow fast access to it, but one can also define additional local landmarks for special regions of the information space and make them stand out on the overview diagrams. Landmarks are usually defined by the author of a hypertext system as part of the process of providing a usable structure for the readers. It might be possible for the hypertext system to define landmarks automatically by the use of connectivity measures (see the example in Table 11.1), but it is probably better to have the author choose the landmarks. As an authoring aid, the choice might be made starting from a list of candidate nodes calculated on the basis of connectivity.</p>

<p>Contextual information can also be conveyed by more subtle contextual cues like the use of different background patterns in different parts of the information space. Even though such methods will not eliminate the disorientation problem, they are still needed to solve the <em> homogeneity </em> problem in hypertext. Traditional text is extremely heterogeneous as can be seen by comparing a mystery novel with a corporate annual report. You do not need actually to read the text to distinguish between the two. But the same two texts would have looked exactly the same if they had been presented online on a traditional computer terminal with green letters.</p>

<p>Printed books look different depending on their quality and age. They even automatically change to reflect how often they are used by being more or less worn [Hill et al. 1992]. Modern graphic computer screens allow us to utilize similar principles to provide additional information to the user, but we still have to discover the best ways of doing so.</p>

<p>The main hypertext control structure is the goto statement in the form of a jump. In an analogy with software engineering, it might be possible to use alternative methods that are more similar to structured programming such as the nested hierarchies of Guide.</p>

<p><img alt="Example of link inheritance shown by heavier arrows" height="236" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/31/link_inheritance.png" width="750"/><br/>

<strong>Figure 9.11. </strong> <em> Link inheritance during a clustering operation. </em></p>

<p>Another example of structured hypertext mechanisms is the use of link inheritance [Feiner 1988] to allow simplified views of an information space without having to show all the links. As shown in Figure 9.11, link inheritance replaces the individual links between nodes in an overview diagram with lines connecting clusters of nodes, thus simplifying the diagram considerably.</p>

<p>Figure 9.11 shows a conceptual view of link inheritance but Figures 9.12 and 9.13 show an actual example from a medium-sized hypertext. It is immediately apparent from the pictures that the structure of the hypertext is impossible to understand in the full overview diagram whereas it is much clearer from the diagram where the nodes have been nested according to the hierarchical structure of the information space and where only the connecting links are shown.</p>

<p>Even though the nested view in Figure 9.13 provides a great overview of the structure of the Free Trade Agreement, the individual parts of the diagram are much too small to allow the user to use them to understand specific sections of the Agreement. This is where fisheye views come into play to show the user's current focus of attention at a greater scale. In turn, the other parts of the overview diagram will have to be scaled down given a fixed amount of screen real estate for the diagram. Figure 9.14 shows a fisheye view of the Free Trade Agreement assuming that the user's current interest is in the "definitions" section (possibly because the user is currently viewing a node from that section).</p>

<p><img alt="Reduced view of upper left of visualization of links between sections in a legal document" height="977" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/31/interlinked_nodes_excerpt.png" width="800"/><br/>

<strong>Figure 9.12. </strong> <em> A hypertext version of the Canada-U.S. Free Trade Agreement with all nodes and links visible. Actually, to save space, the figure only shows 17% of the total image, which has 1860 nodes and 3852 links. (Click for <a href="http://media.nngroup.com/media/editor/2013/03/14/full_figure_interlinked_nodes.png"> full image of entire hypertext space</a> at 3400x2986 pixels) Copyright © 1993 by Emanuel G. Noik, reprinted by permission. </em></p>

<p>Fisheye views belong to the class of so-called "distortion-oriented" presentation techniques [Leung and Apperley 1994] because they have to move some of the information around in order to fit everything into a single picture. In calculating the view in Figure 9.14, some of the sections have been moved around from their location in Figure 9.13.</p>

<p><img alt="Nesting and link inheritance visualized by boxes and grayscales" height="886" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/31/nested_hyperspace.png" width="859"/><br/>

<strong>Figure 9.13. </strong> <em> View of the Free Trade Agreement with nesting and link inheritance to clarify the picture. This time, the figure does show the full hypertext. Notice now grayscales are used to indicate the hierarchy of the nesting. Copyright © 1993 by Emanuel G. Noik, reprinted by permission. </em></p>

<p> </p>

<p><img alt="Fisheye view" height="674" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/31/fisheye_view_nondistorted.png" width="960"/><br/>

<strong>Figure 9.14. </strong> <em> Fisheye view of the Free Trade Agreement centered on the definitions. The fisheye view was calculated using Noik's layout-independent algorithm for node placement [Noik 1993], meaning that the placement of each section of the hypertext was determined with an eye to maximize the understandability of the diagram and not just from a rescaling of the original layout. Copyright © 1993 by Emanuel G. Noik, reprinted by permission. </em></p>

<p>Obviously, one wants to minimize the changes in the diagram as the user moves through the information space, but given that the two-dimensional representation of the N-dimensional hyperspace is somewhat artificial anyway, it is more important to preserve the relationships and approximate shapes of the sections than their exact placement.</p>

<p>Most graphical fisheye views use straight geometric distortion to scale a drawing at multiple levels and in doing so balance local detail and global context.</p>

<p><img alt="Distorted fisheye view" height="788" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/31/distorted_fisheye_view.png" width="734"/><br/>

<strong>Figure 9.15. </strong> <em> Fisheye view of the Free Trade Agreement centered on the definitions. This time, the fisheye view was calculated by simple geometric distortion from the base view in Figure 9.13 Note how the structure of the hyperspace is much harder to understand than in the layout-independent fisheye view with the same focus in Figure 9.14 Copyright © 1993 by Emanuel G. Noik, reprinted by permission. </em></p>

<p>Distorted views tend to be difficult to understand (especially of nested graphs) because the technique uses geometric notions of distance (which is not appropriate for hyperspace) and because geometric distortion alters the shapes of nodes too much (which is bad for nested nodes). Figure 9.15 shows what would happen to the Free Trade Agreement if the fisheye view was calculated by a simple geometric distortion that scaled each level at some proportion to its original size in the full nested overview diagram in Figure 9.13. Clearly, the view in Figure 9.15 is much harder to understand and to use as an overview of the hypertext than the more appropriately scaled fisheye view in Figure 9.14.</p>

<p>Link inheritance and nesting both require the hypertext to have a structure. At the same time, the ability to write and generate ideas freely is one of the most attractive aspects of hypertext systems as an intellectual tool. Having to define a structure before one has created the materials feels constaining and also constitutes a barrier to writing. The famous "writer's block" of staring at a blank sheet of paper and not knowing what to write first is a classic indication of the difficulties inherent in any requirements for early structure. It is much easier to start writing and generating ideas as they flow and then later reorganize and link the material as it emerges.</p>

<p>Premature structuring has been found to be a serious problem for hypertext authors [Monty 1986], and much work has therefore been devoted to schemes for structure discovery. The basic goal is to allow authors to develop the hypertext more or less as they please and then to have the system generate suggestions for ways of structuring the material. For example, the VIKI system [Marshall et al. 1994] was explicitly designed to support emerging structure through the use of spatial hypertext where users can associate nodes by placing them near each other on a canvas.</p>

<p>Figure 9.16 shows a screen from Xerox' Aquanet system which is often used to develop argumentation structures [Marshall et al. 1991]. In Aquanet, users get a large canvas on which they can place hypertext nodes spatially as they add information to their knowledge base. Aquanet uses typed nodes and displays different types in different colors. From the screen in Figure 9.16 it is apparent that the hypertext has four major components, each of which seems to be structured very differently with different node types (as indicated by color and shape) in the four corners of the window. It is almost certainly the case that the user has thought of the problem domain as having four parts, even though this may only have become apparent after the fact. Marshall and Shipman [1993] have developed a program to automatically detect such implicit structures by pattern recognition.</p>

<p><img alt="Screenshot of Aquanet sitemap-like spatial visualization of relationships" height="767" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/31/aquanet_sitemap.png" width="1126"/><br/>

<strong>Figure 9.16. </strong> <em> Screen from Aquanet showing a user-constructed spatial layout of hypertext nodes that can be used for discovery of structure by pattern recognition. Copyright © 1994 by Catherine C. Marshall, reprinted by permission. </em></p>

<p>Each of the larger structures in Figure 9.16 has its own internal substructure. For example, the lower left structure is made up of composite nodes, each of which has a two-element box on the top and a list of smaller nodes below that box. The two-element boxes are composite nodes constructed explicitly in the system as a special type. The example in Figure 9.16 is a representation of a writer's notes about machine translation. The full hypertext has 2,000 nodes and took two years to develop as part of a project assessing the state of machine translation [Marshall and Rogers 1992].</p>

<p>The two-element boxes in the lower left corner actually represent links to collections of articles about specific systems. The top element in the box holds the name of the system and the lower element holds the name of its vendor. In addition to this information about the specific systems (and links to backup materials), the user has placed smaller, single-element nodes next to the two-element boxes. These smaller nodes contain further notes about the systems, and it is quite obvious to the human eye what notes go with what system-nodes. The pattern recognition software can also recognize many of these patterns and can build up higher-level composite nodes. In the example, a new type of composite node would be defined with one slot for a two-element system node and a variable number of slots for note-nodes.</p>

<p><img alt="People use different navigation tools depending on their task." height="333" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/31/exploratory_vs_directed_use.png" width="660"/><br/>

<strong>Figure 9.17. </strong> <em> Distribution of the methods used to transfer to new screens in hypertext on the history of York when users were asked to explore the information space and when they performed a directed search to answer specific questions. Data replotted from Hammond and Allinson [1989]. </em></p>

<p>Hammond and Allinson [1989] have studied users of a hypertext history of the city of York. Some subjects used the system for an <em> exploratory task </em> wherein they first read the hypertext on their own and were later given a test to see how much they had learnt. Other subjects were given a <em> directed task </em> wherein they were given a set of questions that they were to answer using the hypertext system. Several different navigational methods were provided in addition to the plain hypertext links between associated parts of the text. One test compared the use of an overview map to the same system without the map and found that users performed slightly better (but insignificantly so) in both the exploratory and directed tasks when they had the use of the map. The same was true for an index mechanism. There were large, significant differences in both task conditions, however, in the ratio of new, different hypertext nodes visited compared to previously visited hypertext nodes being revisited. Both the map and the index led to users seeing a significantly larger proportion of new nodes.</p>

<p>Furthermore, users in the exploratory task also visited more new nodes than users in the directed task. This difference is understandable since the exploratory users could not know what questions they would be asked and therefore would feel encouraged to cover as much of the information base as possible in the time given.</p>

<p>Hammond and Allinson also tested a system wherein users had an overview map, an index, and a guided tour facility available. As shown in Figure 9.17, it turned out that users' use of these facilities varied significantly depending on their task, with the guided tour being used 28% of the time for the exploratory task but only 8% of the time for the directed task, the index being used 6% of the time for the exploratory task compared to 17% for the directed task, and the map being used about the same (12% vs. 16%).</p>

<h2>Navigational Dimensions and Metaphors</h2>

<p>Navigational dimensions and metaphors can help users better understand the structure of the information space and their own movements.</p>

<p>For example, the interactive fiction <cite> </cite> <cite> Inigo Gets Out </cite> mostly uses a navigational metaphor related to Laurel's [1989] definition of <em> personness </em> in interactive systems. Most of the story has a <em> first-person </em> feel wherein the user identifies with the cat and clicks at those points in the environment where the cat wants to go. See the screen in Figure 9.18 where the user would click on the tree if that is where the cat "wants" to go at that point in the interactive fiction.</p>

<p>In a few locations, however, the story changes to a second-person feel where the user orders the cat around by clicking on it rather than on the environment. For example, in Figure 9.19 (one of the last screens of the story), the cat is shown running along the path to the house where it lives.</p>

<p>Because of the general first-person feel of the story, many users click at the end of the path, thus expressing the sentiment "Now let's run in this direction." The system, however, requires the user to click on the cat itself, which leads to a sentiment more like "OK you cat, move along now."</p>

<p>We conducted a field study of children in a Copenhagen kindergarten using <cite> Inigo Gets Out </cite> [Nielsen and Lyngbæk 1990] and mostly found that the children had great fun reading the story and could navigate easily. But from logging user interactions in our field study we know that users in total made 30 clicks on the screen in Figure 9.19 from the (erroneous) first-person perspective and 38 clicks from the second-person perspective. Any first-person click on this screen must have been made before a second-person click, since users would not be moved to the next screen until they realized the need for a second-person click. These data do not prove that first-person stories in general are more intuitive than second-person stories, but they do indicate the need for consistent navigational metaphors in hypertexts.</p>

<p><img alt="Screenshot from children's hypermedia narrative" height="344" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/31/inigo_gets_out.png" width="514"/><br/>

<strong>Figure 9.18. </strong> <em> A central screen from <cite> Inigo Gets Out </cite> . This screen has a first-person perspective: To get the cat to climb the tree, you click the tree. Copyright © 1987 by Amanda Goodenough, reprinted with permission. </em></p>

<p>The hypertext system described in Chapter 2 is based on two navigational dimensions. One dimension is used to move back and forth among the text pages within a given node, and another dimension is used for hypertext jumps. To reinforce users' understanding of these two dimensions, two different animation techniques are used when shifting from one screen to another. (Other studies have confirmed that animated transitions help users understand their movements through an information space [Merwin 1990].)</p>

<p>Movement between pages within a node is seen as a linear left-right dimension, corresponding to the orientation of the scroll bars at the bottom of the screen and to the way printed books are read in Western society. A change to a new page along this dimension is visualized by an animated right or left wipe, using built-in visual effects from HyperCard that look quite like the turning of a page.</p>

<p><img alt="Second-person perspective from children's narrative" height="344" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/31/inigo_second_person_perspective.png" width="514"/><br/>

<strong>Figure 9.19. </strong> <em> Screen from <cite> Inigo Gets Out </cite> . This screen has a second-person perspective: To get the cat to run to the right, you click on the cat itself. The actual image from <cite> Inigo Gets Out </cite> has been overlaid with data from a field study of the use of the system in a Copenhagen kindergarten (the heavy border showing the button on the cat, the small symbols denoting mouse clicks outside the button, and the numbers counting clicks in various regions of the screen). Click markers inside the button rectangle denote cases where the user moved the mouse in between pressing down the mouse button and releasing it. Copyright © 1987 by Amanda Goodenough, reprinted with permission. </em></p>

<p>Hypertext jumps are seen as being orthogonal to the left-right page turning and are visualized as an in-out dimension using an animated iris that opens for anchored jumps and closes for return jumps. The opening iris gives users the impression of diving deeper into the hyperspace when they take a hypertext jump, and the closing iris for return jumps gives the inverse feeling of pulling back again.</p>

<p>Another example of orthogonal navigational dimensions is the "season knob" in the Aspen Movie Map described in <a href="http://www.nngroup.com/articles/hypertext-history/" title="The History of Hypertext"> Chapter 3</a>. It could be operated independently of the navigation through the streets, and navigation in time and geographical navigation were thus done along orthogonal dimensions.</p>

<p><img alt="Metaphors visualized in icons" height="242" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/31/icon_metaphors.png" width="596"/><br/>

<strong>Figure 9.20. </strong> <em> Preliminary (top) and final icons (bottom) from HP's SynerVision. User interface by Jafar Nabkel (Software Engineering Systems Division, Hewlett-Packard Company) and Eviatar Shafrir (User Interaction Design, Hewlett-Packard Company). Copyright © 1993 by Hewlett-Packard Company, reprinted by permission. </em></p>

<p>Even though navigational metaphors are usually beneficial in helping users understand their options and movements, it is not always appropriate to tie a design to a single metaphor that may be too constraining. For example, the top row of icons in Figure 9.20 shows an initial design using a book metaphor for all aspects of navigation. User testing revealed that people had trouble distinguishing the subtle differences in the uses of books, and the designers therefore chose to engage a variety of metaphors for the final design shown in the bottom row in Figure 9.20 [Shafrir and Nabkel 1994].</p>

<p>In the final SynerVision design, pictures of books represented real, physical books (for example, "directions to all information, both online and printed" for the middle icon and "cross-reference to the printed manuals" for the rightmost icon). A geography and travel metaphor was used for the table of content (branching road with road sign in the leftmost icon) and the guided tour (map with highlighted path, second from right), and an office metaphor was used for the index (box of index cards, second from left).</p>

<p>It is possible to provide alternative navigational dimensions that are optimized for specific user needs in cases where the fundamental structure of the information space is unsuited for some user tasks. For example, many online manuals are written from the perspective of the experienced user who needs to know everything about a system. Therefore, they are often structured in ways that make sense for people who want to understand the scope and conceptual nature of the full system.</p>

<p>A user who just wants to accomplish a specific task (e.g., installing a printer or changing the background screen color) without understanding the full system may be better served by an alternative navigation mechanism.</p>

<p>Figure 9.21 shows the Silicon Graphics Topic/Task Navigator which provides an alternative way of navigating the IRIS InSight library of online manuals. The original information base has two underlying navigational dimensions: a hierarchical structure of books, chapters, and sections, and a full text search capability. Novice users may not appreciate the book structure and they also sometimes have difficulty in coming up with appropriate search terms. After all, when you are new to a system you don't always know what things are called. The Topic/Task Navigator alleviates these two problems by providing hierarchical navigation that is structured around tasks users may want to perform, instead of being structured according to the way the computer system is built. By presenting possible tasks and subtasks, the Topic/Task Navigator helps users to understand the way it has structured the information space in much the same way that window-based user interfaces use pull-down or pop-up menus to make their functionality visible to the user. Field feedback shows that the Topic/Task Navigator is also used by many experienced users when desired information exists across a number of books.</p>

<p>Because the Topic/Task Navigator acts as an alternative navigational dimension, there is no one-to-one mapping between its categories and the text units in the underlying information base. Therefore, instead of linking directly from the nodes in its overview diagram to the content nodes, the Topic/Task Navigator uses a fat link in the form of a menu of relevant nodes from which the user can select the final destination.</p>

<p> </p>

<p><img alt="Screenshot of SGI Topic/Task Navigator" height="823" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/31/sgi_task_topic_navigator.png" width="623"/><br/>

<strong>Figure 9.21.</strong> <em> In the Topic/Task Navigator interface to IRIS InSight users can click their way through a topic hierarchy. For each node the system lists a number of links into the online documentation. Copyright © 1994 by Silicon Graphics, Inc., reprinted by permission.</em></p>

<p>In cases where the hypertext does not have an underlying structure or easily comprehensible dimensions it may difficult to present meaningful overviews. One can still give the user an idea of the content of the full system by using a technique called "flying" [Lai and Manber 1991]. Flying through a hypertext is done by flashing each node on the screen for a very brief time (possibly half a second). If the hypertext is fairly small, all nodes can be displayed (unless the user chooses to interrupt the fly-through), but if the hypertext is large the system may only display, say, every tenth node. Flying through a hypertext is analogous to flipping the pages of a book and may also be helpful as a supplemental overview tool in cases where the hypertext does have a structure.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Navigation</span>

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