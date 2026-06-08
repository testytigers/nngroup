# AI-Powered Tools for UX Research in 2023

**Author:** Feifei Liu, Kate MoranFeifei LiuandKate MoranJuly 2, 20232023-07-02

**Topics:** Artificial Intelligence, Design Patterns

**Source:** https://www.nngroup.com/articles/ai-powered-tools-limitations/

---

July 2, 20232023-07-02

Share

Updated guidance is available in a newer article:Accelerating Research with AI.This article captures our early assessment of AI research tools and their marketing claims. Some of these limitations still exist, but many of the tools have improved.

New AI tools of all kinds are entering the marketplace, eager to capitalize on the interest sparked by ChatGPT. The UX field is no exception.

The marketing descriptions of AI-powered tools for UX research make big claims, like:

If these claims sound too good to be true, it’s because they are.It’s likely that, in the future, AI-powered user-research tools will become much better at delivering on these kinds of promises. Right now, however, you should be carefulwhen considering a subscription to one of them.

We evaluated four new AI-powered UX-research tools. In this article, we present the results of our evaluation. Note that we won’t mention any of the tools by name, because we hope that they will learn from their mistakes and improve in the near future.

There are two types of AI-powered tools we currently see on the market:

They both can be used to summarize transcripts of qualitative-research sessions.

AI insight generators summarize user-research sessionsbased solely on the transcripts of those sessions.

These tools don’t accept other types of information from the researcher. This ends up being a big problem because, unlike human researchers,these tools can’t factor in context.You can’t give them background information about the product or about the users. They also cannot take advantage of findings from previous studies.

(Researchers may work around these limitations by uploading background information and their own session notes as separate assets to add to analysis, but these might be treated as different sources instead of session-specific information, whereas human researchers could easily combine the two.)

AI collaborators are like insight generators,except that theycan accept some contextual informationfrom the researcher. Like insight generators, collaborators can absorb your text data and produce insights.

For instance, researchers can show the AI some human-generated codes to “train” it. The tool can then recommend tags for thethematic analysisof the data. In addition to session transcripts, they can also analyze researchers’ notes. As a result, collaborators (unlike basic insight generators) can create themes and insights based on input from multiple sources.

AI collaborators are more sophisticated than AI insight generators but still suffer from similar limitations (discussed below).

We looked at three insight generators and one collaborator. Out of the three insight generators,two were deemed too premature in terms of handling user-research datawhen the article was written. (One generated only a list of top 5 insights for a given project with no capability of modifying the prompt or asking followup questions; the other allowed researchers to upload only text files — a feature that seemed too restricting for most user-research projects, but possibly suitable for analysis of large sets of text, like app-store reviews.)

To evaluate the other two tools,we uploaded recordings from a usability-testing study of NNgroup.com. We compared the tools’ analyses against analysis produced by human researchers. The study aimed to understand how our mobile customers choose from NN/g’s training courses. The data from the study had been already analyzed by NN/g researchers. None of the researchers who originally analyzed the user-testing sessions contributed to this AI evaluation.

Additionally,we supplied the collaborator(which could accept such input)with the tags from the original thematic analysisof the sessions.

The output of the tools included:

None of the AI research tools we tested had the ability to process video or visual input. They were fully text-based, so they could only analyze transcript data. That isn’t a big problem for analyzinguser interviews. However — contrary to the ludicrous claims made by the creators of these tools —no human or AI tool can analyzeusability-testingsessions by the transcript alone.

Usability testing is a method that inherently relies on observing how the user is interacting with the product. Participants oftenthink aloud, describing what they’re doing and thinking. Their words do provide valuable information. However, you should never analyze usability tests based only on what participants say!

Transcript-only analysis misses important context in user tests, because participants:

In the AI-generated high-level summary of a session, one AI tool gave us the recommendation of adding filters to the site we tested. That websitedidhave a filter tool on some pages, and that specific participant did use it during the study without mentioning the feature out loud. However, she expressed the need for filters on a different type of page.

As a result, the AI tool’s recommendation to add filters was confusing: did the site need more filters on the page? Or did it need to include a filter tool on every single page? (This type of recommendation also exemplifies another common problem with AI-generated insights: their vagueness — see the next section below.)

Do not trust AI tools that claim to be able to analyze usability-testing sessions by transcripts alone.Future tools able to process video visuals will be much more useful for this method.

The AI tools often gaveextremely vaguesummaries and recommendations.

For example, one tool made the following recommendations about a description page:

Make sure that all relevant information is easily accessible and clearly presented.

Provide more detailed descriptions[about the page].

This sounds good, but it didn’t explain whatrelevant informationordetailed descriptionsmeant, nor did it say how the existing content should be modified to beclearly presented.

We’ve included two analysis excerpts below — one generated by an AI tool and one written by a human researcher.

AI insight generators severely lack context. They don’t ask for, and can’t accept:

Note that, even though some tools allow people to upload information to a given project, they don’t allow researchers to differentiate between how these resources should be used. For instance, the study goals should be carried over in all sessions, but session-specific participant information should be applied only to certain videos.

That lack of context caused problems in the analysis generated by these tools. For example, the insights were presented without any priority. With no understanding of the study goals,the system can’t know what’s most important or relevant to the researcher.

In fact, some of the themes generated by the tools were extremely uninformative and uninteresting. Here’sa findingprovided by one of the AI insight generators:

The participant was happy that they could share both positive and negative feedback.

This finding appeared at the top of the findings list. Imagine putting such an inane observation in a presentation or a report!

When helpful insights are buried in an ocean of irrelevant ones, identifying and prioritizing them can be time-consuming –- even more so than analyzing the session manually.

When generating quotes and recommendations, some tools don’t reference where they found that information (for example, they fail to attribute a quote to a specific session, timestamp it, or link it to the clip they’re referencing.)

Ironically, this lack of referencing causes lots of problems for the AI collaborators, which can accept content from the researcher. The tool we tested wasnot able to distinguish between the researcher’s notes and the session transcript.That’s a huge ethical issue in reporting research — we always must differentiate between our interpretations or assumptions and what the participants said or did.

Most important, this lack of citationprevents researchers from verifyingwhether the tool’s summary or recommendations came from the research. AI systems have a dangeroustendency to provide incorrect informationthat sounds plausible. Imagine if an AI tool recommended that you add a specific new feature to a product, but that recommendation was not grounded in the user-research data. Such a mistake could be costly in time and resources.

Some of the tools we evaluated hadinformation-accuracy disclaimers. Interestingly, those disclaimers were often nowhere to be seen in their promotional claims.

Unfortunately, none of the tools we tested had solid usability or performance. We encounteredoutages, errors, and unstable performance.We had to reach out to some tools’ customer-support departments several times, just to use the basic features of the tools. These issues have the capacity to slow your analysis down, rather than speed it up.

Anotherquestionable claimmade by some AI-powered research tools is:

Our tool will give you an unbiased perspective of your users, becauseAI systems do not have bias.

Perhaps they may reduce bias in some ways. For example, if youtest your own designs, it’s easy to be subconsciously influenced byconfirmation bias.The AI tool doesn’t care whether your design works as you hoped it would.

However,the claim that AI tools are bias-free is blatantly falseand shows a misunderstanding of how the technology works. According to NIST’s Reva Schwartz and her colleagues, AI systems and applications can involve biases at 3 levels: systematic, statistical and computational, and human biases. AI must be trained on data, which can introduce systematic (such as historical and institutional) and statistical biases (e.g., dataset sampling isn’t representative enough). When people are using AI-powered results in decision making, they can bring in human biases likeanchoring bias.

AI product companies like OpenAI have worked hard to reduce the potential biases as much as possible, which we truly appreciate. Still, users of AI-powered tools should be aware of these biases.

We do believe that user researchers will have good, reliable, useful AI-driven tools in the near future. They will make our work much faster and of higher quality. However, the currently available tools cannot provide those benefits yet.

We hope and expect that future iterations of these types of tools will have:

AI tools definitely have a large role to play in the near future of UX research.But for now, be wary of grandiose claims. Definitely request andtest out a demobefore committing to pay for any AI-powered research tool. Be cautious about the tool’s findings and recommendations, and doublecheck its work. If doublechecking isn’t possible, don’t use it.

Schwartz, R. , Vassilev, A. , Greene, K. , Perine, L. , Burt, A. and Hall, P. (2022), Towards a Standard for Identifying and Managing Bias in Artificial Intelligence, Special Publication (NIST SP), National Institute of Standards and Technology, Gaithersburg, MD, [online], https://doi.org/10.6028/NIST.SP.1270

The AI-assisted user research workflow

Artificial Intelligence