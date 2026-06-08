# AI Design Tools Are Marginally Better: Status Update

**Author:** Megan Brown, Caleb Sponheim, Taylor DykesMegan Brown,Caleb SponheimandTaylor DykesMay 9, 20252025-05-09

**Topics:** Artificial Intelligence, Design Process

**Source:** https://www.nngroup.com/articles/ai-design-tools-update-2/

---

May 9, 20252025-05-09

Share

This is a follow-up to the 2024 articleAI UX-Design Tools Are Not Ready for Primetime: Status Update.

In April 2024,AI-powered design toolswere not useful to designers. As of May 2025, their usefulness has improved, but we’re stillnowhere near the AI-powered design tools we’ve been promised, nor are design professionals yet in danger of being replaced by AI. (This is true even if Figma's new features announced at Config this week turn out to be as good as their demos  — which is never guaranteed with AI tools.)

The greatest improvements in design-specific AI tools is withinnarrow-scopedgenAI. Unlike broad AIs (like ChatGPT), which accept a wide range of inputs and produce an equally wide array of outputs, narrow-scope AIs specialize in one or few specific tasks.

Narrow AI, in general, tends to be more easily adopted and appreciated by users. It’s more likely to meet a specific user need and be understood by those using it. This holds true for AI tools for designers.

Based on interactions with practicing designers, we’ve found thatthe most helpful tools (actually adopted by designers for everyday work) are decidedlynarrow— that is, they are usually focused on completing one specific task. Unlike broader products that generate entire designs or prototypes, these narrow tools take advantage of what current genAI isgood at— automating repetitive tasks with targeted suggestions based on strong pattern recognition.

In our evaluation, the narrow-scope features in three tools stood out: Figma, Khroma Color, and Midjourney.

Since our original article, Figma has released several narrow-scope AI tools that are meaningfully helpful for designers.

This Figma AI tool completely eliminates the tedious task of renaming layers, saving designers time and effort. According to Figma, this tool usesa layer's contents, location, and relationship to other selected layersto recognize patterns, rename layers, and increase the organization of a design.

As many designers know, naming layers is tedious, does not serve an immediate purpose (you’re not creating something; you’re just adding metadata), and even the most detail-oriented designers forget to do it. Even the simple layer naming provided by theRename layerstool makes it easier to quickly search for layers within your Figma.

Designers are not necessarily writers, but they often need to write copy for their design. Figma’sRewrite thisfeature leverages genAI’s talent for text generation. By giving the AI a short prompt, designers can adjust copy or have it generated for them entirely from scratch, thus freeing time to focus on their primary task.

Figma also has similar features that shorten and translate text, creating many opportunities to augment designers’ skills and speed up content production.

The final Figma AI feature we’re highlighting removes the stress of digging through files across multiple projects and teams to find the right asset. By usingFind more like, designers can find their missing or related assets almost instantly. Keywords, descriptive text, a layer selection, or an image can be used as prompts for this functionality. Once you find the design you are looking for, you can open the source file or insert it into your current file. When working for a large company with teams split across features, products, and even time zones, it can be hard to know where to look when you’re trying to find an idea or a model for a design. And even if you are part of a small team or a freelancer, this tool is useful for helping you quickly locate a similar design.

Khroma Color uses AI to assess patterns in designers’ color choices and assemble custom color palettes. Like many of Figma’s AI tools, Khroma Color employs genAI’s pattern recognition and automation to reduce the time spent finding colors that are both aesthetically pleasing and brand-compliant.

Midjourney and other diffusion AI models specialize in generating images; these broader tools offer many of the same benefits as design-specialized AI tools.

Like Figma’sRewrite this, Midjourney provides an excellent resource for creating placeholder content (in this case, images). Once again, this feature allows designers to free up time for the task at hand. It can be a quick workaround for prototype usability testing, when you don’t want to spend time or don’t have the resources to get professional photos (stock or not).

Some teams (especially small companies and startups) use AI-generated images for final designs as well. While we do not recommend you do so, since user trust can plummet if they notice AI use, it does work in a pinch when resources are scarce.

More complicated genAIs like wireframe and prototype design tools, which require a broader skillset and understanding of real-world context, still do not meet expectations.Unlike a human designer who can understand and adjust to a variety of contexts and needs, most genAI tools lack the sophistication to balance all the requirements of a design.

At present, wireframe and prototype tools work best for ideation, possibly as starting points for newer designers or freelancers. While they might provide some good ideas, eliminate some additional overhead, and fill in knowledge gaps, they cannot replace the level of detail brought by an experienced human designer.

Currently, no genAI tool effectively supportsdesign systems; this limitation lowers their utility withindesign teams.Most designers aren’t building things from scratch. A prototype composed of random design elements is not helpful. AI needs to be able to pull from established design systems and create a cohesive look across designs.

Figma and other design tools are working towards AI features that create designs integrated with users’ design systems. After Figma’s ConFig 2025 conference, where no major design-system-related updates were announced, it is unknown when these features will be released.

Another barrier to design-specific genAI success is the strict limit on the number of words in a prompt. With these constraints, it’s impossible for the AI to be aware of all the context that goes into a UX design. Currently, only a human designer can balance the design, business, and user needs that go into a great visual design.

500-character prompts are not enough.AI needs to be able to process complex context information (including business goals, user needs, information about the existing product, etc.) like a human designer. Simply increasing token limits won’t solve the problem, though — it’s hard for designers to create prompts that give sufficient context. To be really useful, these tools need to be able to learn their users’ context over time (like ChatGPT’sMemoryfeature).

We also acknowledge this isn’t a simple fix for most teams. A longer context window might not be available for these tools' AI models. Even if the models could support more context, the additional resources needed to run these long prompts might make it infeasible for many. But while this problem has no easy or quick fix, it needs to be solved for these AI tools to become truly helpful.

While Figma has many great features, it’s not immune to the common pitfall of releasing an AI feature that’s impressive but not practical.

For example, Figma’sFirst draft, an AI-based feature that allows designers to ask for a “first draft” of a design, can use only relatively few design components in a limited number of ways, creating designs that are useful only in very specific circumstances.

For example, when we promptedFirst draftwith specifications for creating an NN/g profile page, the result was generic and had poor information and visual hierarchy, even for a wireframe. Moreover, when we tried to get multiple versions to riff off of, the same prompt generated only minor variations. The quality of the response did not improve regardless of the prompt length or amount of context provided to the AI. These resultsseriously undermine the tool’s value for ideation.

First draftdoes offer a noticeable advantage — it doesn’t have a prompt-length limit. However, the small text box undermines this advantage, allowing users to view only a few sentences at a time. This design choice makes it unlikely that users will be able (or willing to) give the tool enough context to create a functional prototype.

Over the past year, we’ve been monitoring changes in AI design tools and how real practitioners are using them. We’ve conducted both formal and informal interviews to gauge practitioner sentiment. We’ve also incorporated these tools into our workflows while designing real NNGroup products. Finally, we’ve been more generally researching AI and AI features trends and comparing them to our AI design-tool findings.

Figma and competitors are currently working on increasing automation for UX-design work, but it's unknown when these tools will reach viability. For now, design workflows are not substantially improved or altered with AI.

We may be one step closer to that end with the announcement ofFigma Make, a vibe-coding tool powered by Claude 3.7, that is supposed to translate a Figma file into a functional live prototype.

While Figma Make is still a few weeks from public launch, it may change how designers create prototypes and test their designs. It could also improve handoffs from designers to developers. We’ll have to see how well it delivers on its promises compared to other AI coding tools currently on the market.

Design innovative, trusted, and useful AI products and features

Artificial Intelligence

Leverage AI to enhance creativity, efficiency, and impact in everyday design work

Artificial Intelligence

Unearth user pain points to drive breakthrough design concepts

Interaction