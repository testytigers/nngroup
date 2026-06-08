# Information Retrieval of Imperfectly Recognized Handwriting - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">11</span>

<div class="article-header">

<h1 class="article-h1">Information Retrieval of Imperfectly Recognized Handwriting</h1>

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

January 1, 1993

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">1993-01-01</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Information Retrieval of Imperfectly Recognized Handwriting&amp;body=https://www.nngroup.com/articles/handwriting-retrieval/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/handwriting-retrieval/&amp;title=Information Retrieval of Imperfectly Recognized Handwriting&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/handwriting-retrieval/&amp;text=Information Retrieval of Imperfectly Recognized Handwriting&amp;via=nngroup" data-share-type="Twitter">

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

</span>A user test of handwritten input on a pen machine achieved a 1.6% recognition error rate at the character level, corresponding to 8.8% errors on the word level. Input speed was 10 words per minute. In spite of the recognition errors, information retrieval of the handwritten notes was almost as good as retrieval of perfect text.

</div>

<div class="article-body">

<p>

<em>by <a href="/people/jakob-nielsen/" title="Author bio"> Jakob Nielsen</a> (Nielsen Norman Group), Victoria L. Phillips (Carnegie Mellon University), and <a href="http://www.research.microsoft.com/~sdumais/" title="Author bio at

Microsoft Research"> Susan T. Dumais</a> (Microsoft Research) </em></p>

<p>

This research was done in 1993 while the authors were with Bellcore (Bell Communications Research).</p>

<h3>

Abstract</h3>

<p>

A user test of handwritten input on a pen machine achieved a 1.6% recognition error rate at the character level, corresponding to 8.8% errors on the word level. Input speed was 10 words per minute. In spite of the recognition errors, information retrieval of the handwritten notes was almost as good as retrieval of perfect text.</p>

<p>

<strong>Keywords: </strong> Handwriting recognition, pen machines, information retrieval, latent semantic indexing, LSI, keyword matching, personal digital assistants, nomadic computing.</p>

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

<a class="ga-article-toc-item" href="#toc-introduction-1">

Introduction</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-speed-and-errors-in-pen-input-2">

Speed and Errors in Pen Input</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-information-retrieval-results-3">

Information Retrieval Results</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-conclusions-4">

Conclusions</a>

</li>

</ul>

</div>

</div><h2 id="toc-introduction-1">

Introduction</h2>

<p>

Handwriting and gesture-based user interfaces [Rhyne and Wolf 1993] are rapidly gaining acceptance as important elements of highly portable personal computers. Unfortunately, computers do not recognize handwriting perfectly, so notes taken on a pen machine will contain several mis-recognized words. Of course, it is possible for the user to correct any incorrectly recognized characters while taking the notes. However, our experience in using pen machines for note-taking at meetings and conferences indicates that paying attention to the accuracy of the recognition destroys the feeling of freely taking notes and distracts the user from participating in the meeting. Therefore, a plausible scenario for nomadic computing would involve the user take notes (at meetings, lectures, etc.) without correcting any erroneously recognized characters. After all, notes taken on a personal digital assistant will to a large extent be used only by the individual who made the notes in the first place, and that person will be able to understand them in spite of some recognition errors.</p>

<p>

An important use of personal digital assistants will probably be the retrieval of previously entered information, allowing the notes to serve as a personal information base for the user. Unfortunately, mis-recognitions in notes may make them hard to find for some types of information retrieval systems, such as those based on simple keyword matching. If the user were searching for one specific keyword that happened to have been recognized erroneously in the note, then the user would never find that note.</p>

<p>

It is likely that pen machines will not be used much for handwritten entry of large amounts of text, since keyboards are still superior for that task. Pen input of text will probably be used more for note-taking than for the writing of long papers or reports. Indeed, many applications of pen machines may not involve handwriting recognition to any great extent, but will rely mostly on graphic sketches and the choosing of pre-specified values from menus in form-filling applications, with very little information entered as free-form text. Even so, significant applications do involve some note-taking, and these applications are likely to be among those where searching and information retrieval are especially important.</p>

<p>

The goal of the study reported here was to investigate whether information retrieval might work in spite of recognition errors. We used the latent semantic indexing method (LSI) [Deerwester et al. 1990] for retrieval. LSI uses statistical techniques to model the way in which words are used in the overall collection of documents. In the resulting semantic space, a query can be similar to a document even if they have no words in common. LSI is thus not dependent on any single word and might handle recognition errors robustly.</p>

<h2 id="toc-speed-and-errors-in-pen-input-2">

Speed and Errors in Pen Input</h2>

<p>

For the experiment described here, we used a commercially available pen machine form NCR running the standard Go PenPoint operating system with its standard recognizer module.</p>

<p>

For the handwriting experiment, a test user input 47 abstracts of papers submitted to a hypertext conference to the pen machine. This text amounted to 58,860 characters, of which about 9,000 were spaces that did not need to be explicitly written. The speed and error data reported in the following has been calculated relative to the total number of characters, including spaces, in order to use the same count for handwriting and keyboard input. For comparison, a smaller number of characters (from five additional abstracts for each input mode) were entered on a personal computer keyboard (without the use of the backspace key or other corrections), as well as by free-form handwriting on paper.</p>

<p>

Pen machine input was performed with discrete characters written in boxes and thus represents the slowest and most accurate mode. Table 1 shows the speed and error results from the three input media. Pen machine input can be seen to be much slower than both typed and free-form handwritten input. Also, pen input has a much higher error rate than keyboard input. Of course, substantial individual variability can be expected for input speeds, especially with respect to keyboard input, so the table should only be seen as a general indication of relative user performance with the three media.</p>

<table align="center" border="1">

<caption valign="BOTTOM">

<strong>Table 1. </strong> Comparing speed and error rates when writing a set of abstracts in three different media. Errors for pen input are recognition errors, and errors for keyboard input are typing errors.</caption>

<tbody>

<tr>

<th>

</th>

<th>

Pen Machine</th>

<th>

Keyboard</th>

<th>

Handwriting on Paper</th>

</tr>

<tr>

<th>

Words per minute</th>

<td>

10</td>

<td>

47</td>

<td>

21</td>

</tr>

<tr>

<th>

Characters per second</th>

<td>

1.1</td>

<td>

5.3</td>

<td>

2.4</td>

</tr>

<tr>

<th>

Errors per minute</th>

<td>

1.1</td>

<td>

1.7</td>

<td>

N/A</td>

</tr>

<tr>

<th>

Error rate per character</th>

<td>

1.6%</td>

<td>

0.5%</td>

<td>

N/A</td>

</tr>

<tr>

<th>

Error rate per word</th>

<td>

8.8%</td>

<td>

3.0%</td>

<td>

N/A</td>

</tr>

</tbody>

</table>

<p>

Table 1 shows that the experienced error rate in terms of errors per minute was actually worse on the keyboard than with the pen machine. Based on our personal observations while using these two input devices it seems, however, that the handwriting recognition errors are much more distracting to the user. One major reason why pen machine errors are more distracting is the delayed feedback implied by the recognition process. With current pen machines, pen input is not recognized immediately, but only after a delay of a few seconds. Even though the user can write ahead and thus does not need to be slowed down while the computer processes the pen input, the fact that the recognized characters appears with a delay means that the user has to scan back over previously entered text to check for recognition errors. Delaying users by more than a second or two is known from the response time literature to interrupt their flow of thought [Miller 1968], and the need to scan previous text is a further distraction. Contrast this interaction technique with the correction of a typing error on a keyboard: The error is usually noticed immediately after hitting the wrong key, and the correction is effected by pressing the backspace key in the context of the error rather than interrupting a later flow of thought.</p>

<p>

The handwriting recognition performance achieved in this experiment (1.6% recognition errors) is somewhat better than that reported in a recent study by Santos et al. [1992] (2.7% recognition errors under our definition). We believe this is because we used a newer recognizer. In general, recognition rates can be expected to go up as better recognition software becomes available, but at the same time, faster and less constrained writing styles (such as connected rather than discrete writing) will prevent perfect recognition from being achieved in the foreseeable future.</p>

<p>

</p>

<center>

<p>

<img alt="Graph of recognition errors over time" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/30/handwriting_errors.gif" style="width: 450px; height: 215px; "/></p>

<p>

<br/>

<strong>Figure 1. </strong> <em> Observed error rates when writing input to the Go pen machine as discrete characters in boxes. </em></p>

</center>

<p>

Figure 1 shows the changes in recognition error rates over time. It can be seen that the error rate was initially very high (more than 5%) and did not reach the 1-2% steady state band until about 5,000 characters had been entered. Apparently, users need to change their handwriting style somewhat to accommodate current recognition software and write in ways that the machine finds easier to understand. This result shows that even handwriting input cannot be considered as requiring zero learning time as an interaction technique. On the other hand, reaching the "expert" level of 1-2% recognition errors only required 65 minutes of practice with the pen machine, indicating that handwriting input is easier to learn than many other input devices, such as using a mouse. Figure 1 also shows that the recognition rates were fairly variable even after the 1.6% recognition error level had been reached for mean performance.</p>

<table align="center" border="1" width="80%">

<caption valign="BOTTOM">

<strong>Figure 2. </strong> Sample abstract as recognized by the pen machine with 2.2% errors. Question marks indicate characters for which the recognizer declined to make a guess.</caption>

<tbody>

<tr>

<td>

HTs/-24 Boy: Indexing hypcrtext documents in context<br/>

To glnlrata intelligent indexing that allows context-sensitive information retrieval, a system must be abld to acavire knowledge directly through interaction with users. In this paper, we present the architecture for LID (Compvter Integrated Documentation,? ? system that enasles integration of various technical documents in a hypertext framework and includes an intelligent browsing system that incorporates indexing in context. LID's knowledge-based indexins mechanism allows ease-based knowledge acquisition by experimentation. It utilizes on-line user information requirements and sussestions either to reinforce current indexing in case of success or to generate new knowledge in case of failure. This allows LID's intelligent interface system to providd helpful responses, even when no a prior; user model is ava:lable. Our system in fact learns how to exploit a user model based on experience cArom user feedback). We describe (ID's current capabilities and provide an overview of our plans for extending the system.<br/>

Keywords: Contextual indexing, information retrieval, tailorable system, context acquisition, hypertext, paradigms for informat:on access (Structuring hypertext documents for reading and retrieval)</td>

</tr>

</tbody>

</table>

<p>

Figure 2 shows a sample abstract as it was recognized by the pen machine. Notice how every occurrence of the important term CID was misrecognized as LID or (ID, so a keyword search for that term would not find this document. Similarly, a search for the full combined term Computer Integrated Documentation would not find the document either, as "Computer" was misrecognized as "Compvter". In many other abstracts, however, important terms were repeated several times with at least one occurrence recognized correctly.</p>

<h2 id="toc-information-retrieval-results-3">

Information Retrieval Results</h2>

<p>

The text used for the experiment was 47 paper abstracts from the Hypertext'91 conference for which we had already conducted extensive information retrieval analyses [Dumais and Nielsen 1992]. 15 members of the program committee judged the relevance of every abstract for their interests, and they had also provided machine-readable representations of their interests. We use both LSI and keyword methods to match each reviewer's interest profile with all the abstracts. Retrieval quality can thus be measured as the mean rated relevance of abstracts that best matched each reviewer's interests.</p>

<p>

Retrieval of 47 handwritten conference paper abstracts is certainly not a typical case of the use of a personal digital assistant. We used this set of documents because of the availability of exhaustive relevance ratings. Also, as mentioned in the introduction, pen machine users will not be expected to handwrite long documents, but will probably only write shorter notes. The abstracts used for this experiment had a mean length of 185 words and might thus be more representative of the length of notes that may be written with a pen machine than, say, the full text of the complete papers would be. Finally, the set of abstracts might be taken to approximate a set of notes taken by a pen machine user attending a hypertext conference in terms of scope and vocabulary use. Thus, even though no user would write in these exact documents in real use of a pen machine, they were still a good test set for our information retrieval experiment.</p>

<p>

Figure 3 shows the mean rated relevance of the top one to ten abstracts retrieved from the handwritten text as recognized by the pen machine as well as from files without any errors. Relevance was rated on a 0-9 scale, with 9 indicating perfect relevance, and 0 indicating complete irrelevance. The measure for retrieval of a single abstract is the mean rated relevance of the top abstract found for each of the fifteen reviewers. In general, the measure for the retrieval of n abstracts is the mean rated relevance for the top n abstracts returned for each of the fifteen reviewers' interest queries. Figure 3 shows relevance curves for both LSI retrieval and keyword retrieval. LSI retrieval was performed using a 50-dimensional semantic space.</p>

<center>

<p>

<img alt="Relevance curves" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/30/handwriting_retrieval.gif" style="width: 450px; height: 334px; "/></p>

<p>

<br/>

<strong>Figure 3. </strong> <em> Mean rated relevance of retrieved abstracts on a 0-9 scale with 9 indicating perfect relevance. Black lines indicate retrieval by latent semantic indexing (LSI), and red lines indicate retrieval by keyword matching. Thin lines indicate retrieval from the original abstracts without any errors, and heavy lines indicate retrieval from the abstracts as recognized by the pen machine from handwritten input. </em></p>

</center>

<p>

It can be seen from Figure 3 that the retrieval quality was basically the same for the original abstracts and the recognized handwriting, in spite of the 8.8% errors on the word level in the recognized test. For the LSI retrieval, the difference in rated relevance between searching the original text and the recognized handwriting was only 0.06% when averaged over the retrieval of one through ten abstracts. For keyword retrieval, the difference was 0.85% between the original text and the recognized handwriting when averaged over the retrieval of one through ten abstracts.</p>

<p>

Latent semantic indexing tended to be slightly better than keyword matching for retrieval of one through five abstracts, with the LSI finding abstracts with a 4% higher relevance rating among the abstracts recognized by the pen machine, and a 1% higher relevance rating among the original abstracts. The two methods were about equivalent when more than five abstracts were asked for.</p>

<p>

One reason that standard keyword search performed well was that both the queries (reviewers' profiles) and abstracts were fairly long (abstracts 185 words, profiles 454 words). Important words tended to be repeated several times in the abstracts, increasing the probability that at least one occurrence would be correctly recognized. Furthermore, since the profiles were fairly long, they contained many words matching words in the abstracts. We therefore repeated the experiment with short interest profiles (three words per reviewer) and got essentially the same results.</p>

<p>

Our good results in finding text with errors is not as surprising as one might have thought, given that experiments with random data corruption has found that information retrieval performance does not degrade significantly until about 30% of the words contain errors [Smith and Stanfill 1990]. Of course, errors in handwriting recognition are not random since the same characters tend to be misrecognized in the same way, but it anything, this consistency in the errors may be an advantage when using LSI, since it will increase the chance that misrecognized words get scaled correctly.</p>

<h2 id="toc-conclusions-4">

Conclusions</h2>

<p>

Input to a pen machine under current constraints on the user's handwriting was very slow and resulted in an 8.8% error rate at the word level. In spite of the high error rate, information retrieval using either latent semantic indexing or keyword matching was able to find documents from the recognized handwriting almost as well as from error-free text, with LSI being slightly better for retrieval of one through five documents.</p>

<p>

Future advances in handwriting recognition may decrease the error rates for any given pen input mode. Users are likely to take advantage of such advances to move to less restrictive and faster pen input modes than the writing in boxes used in this experiment, with free-form handwriting as the ultimate goal. Because of this pressure to move to faster and more error-prone pen input modes, some recognition errors will likely remain in pan-based interfaces for a long time. The finding that information retrieval can robustly handle current levels of recognition errors is thus encouraging for the use of pen machines as personal digital assistants. Pen machine users will be able to find their own notes later, even though the recognized text may not be of sufficient quality to show to others. This result only holds to the extent that the notes are at least as long as the abstracts in our experiment (185 words). Very short notes would be difficult to find without the use of further attributes such as time or context of writing.</p>

<h3>

Acknowledgments</h3>

<p>

This research was done while the authors were at Bellcore in 1993. The authors would like to thank Robert Allen and Scott Stornetta for helpful comments on this manuscript.</p>

<h3>

References</h3>

<ol>

<li>

Deerwester, S., Dumais, S.T., Landauer, T.K., Furnas, G.W., and Harshman, R.A. (1990). Indexing by latent semantic analysis. <cite> Journal of the Society for Information Science </cite> <strong> 41</strong>, 6, 391-407.</li>

<li>

Dumais, S.T., and Nielsen, J. (1992). Automating the assignment of submitted manuscripts to reviewers. <cite> Proc. ACM SIGIR'92 15th International Conference on Research and Development in Information Retrieval </cite> (Copenhagen, Denmark, 21-24 June), 233-244.</li>

<li>

Miller, R.B. (1968). Response time in man-computer conversational transactions. <cite> Proc. Fall Joint Computer Conference 1968 </cite> , AFIPS Conference Proceedings Vol. 33, 267-277.</li>

<li>

Rhyne, J.R., and Wolf, C.G. (1993). Recognition-based user interfaces. In Hartson, H.R., and Hix, D. (Eds.), <cite> Advances in Human-Computer Interaction Vol. 4 </cite> , Ablex, Norwood, NJ, 191-250.</li>

<li>

Santos, P.J., Baltzer, A.J., Badre, A.N., Henneman, R.L., and Miller, M.S. (1992). On handwriting recognition system performance: Some experimental results. <cite> Proc. Human Factors Society 36th Annual Meeting </cite> (Atlanta, GA, 12-16 October 1992), 283-287.</li>

<li>

Smith, S., and Stanfill, C. (1990). An analysis of the effects of data corruption on text retrieval performance. <cite> Technical Report DR90-1 </cite> , Thinking Machines Corporation, Cambridge, MA.</li>

</ol>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Human Computer Interaction</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Human Computer Interaction</span>

<a class="ga-article-related-topic" href="/topic/human-computer-interaction/">Human Computer Interaction</a>

</li>

</ul>

</div>

</div>

</div>

</div>