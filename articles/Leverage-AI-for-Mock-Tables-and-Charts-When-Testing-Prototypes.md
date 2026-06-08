# Leverage AI for Mock Tables and Charts When Testing Prototypes

**Author:** Evan SunwallEvan SunwallSeptember 6, 20242024-09-06

**Topics:** Artificial Intelligence, Prototyping

**Source:** https://www.nngroup.com/articles/ai-data-prototype-testing/

---

September 6, 20242024-09-06

Share

Prototype testing is at the core user-centered design. But crafting realistic data for prototypes that you plan to test is time-consuming. Especially when the design itself is still evolving, you’re pressed for time, or you are aone-person UX team. Don’t let the struggle of crunching numbers discourage you. Generative AI can help.

Research in data sensemaking by Laura Koesten and colleagues found that when participants were given unfamiliar data, they spent more time looking for outliers and inconsistencies than when they worked with familiar data. If you plan to test a prototype (especially if youruser personascritique data frequently),your study participants will scrutinize the prototype’s tables and charts, whether you want them to or not.

This article will discuss practical tactics that any UX professional with access to a general-purpose generative AI tool can use to create higher-quality charts and tables efficiently. To illustrate these tactics, we use a hypothetical example of a sales and marketing-management app targeting ecommerce retailers.

Some of the tactics I recommend involve sharing portions of actual data or examples. In any situation involving generative AI (genAI) and your organization’s data, always be informed and follow your organization’s policies and data-protection regulations.

We recommend that you never share sensitive or identifying data with genAI tools unless your company has verified and approved their use.

Start by gathering the information needed to inform your mock-data generation. Create apromptframeto establish objectives and requirements for content areas. This hybrid form of prompt writing and wireframes will help you facilitate dialog with your collaborators and build prompts to use with an AI.

During this process, remember your testing goals and usability-testing tasks. What would you hope users will accomplish with the prototype during testing? Where are the contentious parts of the design that need clarification?

Consider these 7 tactics when crafting the prompt for generating tables.

Consider the contextual qualities that the AI should mimicand reference from its training data. Your table will be less helpful if your AI is modeling data for a large enterprise when your app targets mall businesses. For example, business size, industry or market, geography, or time periods can all influence the table’s data.

In addition, ask yourself whether the AI should use real or just realistic names for data such as companies or products. Include these details in the prompt.

Determine how much data needs to be generated.You may have room to display only a few dozen rows of a data table in your prototype, but the dataset may be much larger. Describe the size of the larger dataset, if known, so the AI can account for these additional records when calculating values. Mention that you require only a subset to be generated.

For example, a table may typically contain approximately 2,000 transactions totaling 7 million dollars of revenue. You only need 50 transactions to show in your prototype. The AI will account for 2,000 transactions when generating revenue values for those 50.

Ask yourself ifthere is an ideal ordering for the data.There is no need for you to sort your table manually in a spreadsheet; instruct the AI to sort the data by that value.

Add these specifications to your prompt for more authentic-looking data for your table.

If you have a specific chart already designed but need the tests participant to also be able to inspect the table containing that chart’s data,upload the chart along with your prompt. Thanks to the multimodal capabilities of today’s AI tools, they can use this added context when generating table data.

Leverage AI’s abilities to quickly regenerate and revise data to create mock tables tailored to your users.Ask yourself: What do you know about your usability-testing participants? What kinds of data do they use in their domain, and how would that affect the test of your design? For example, a prototype focusing on shoe products could be pivoted into hats with minimal change.

Share your existing mock table with the AI and ask it to revise it with a description of the participant’s background and context. Then, reupload that table back into the prototype.

Alwaysbe cautious when dealing with numbers and generative AI. Large language models’ math skills depend on help from additional tools. Sometimes, the AI will rely on patterns found in its training data, which may fail in more complex calculations. Worse, the AI will confidently hallucinate that it diligently followed your instructions when it did not. Therefore, use these approaches in your prompts to avoid errors:

You may need to display totals in other parts of your prototype, so requesting them in your prompt makes you more efficient and the AI more accurate in its mock-data generation.

Rather than fumbling with numbers for charts,describe the storyinstead. Part of what makes AI powerful is that you can use natural language to convey your intent.

For example, you could include in your prompt that overall revenue has been trending downward over the past year, but there was a spike in December due to seasonal holiday demand. The AI will generate a starting point for your narrative, and you can further refine it.

The AI tool may render charts with gridlines, drop shadows, or legends that aremore clutter thaninsight. By default, most AI tools will include some of these chart elements, so ask it in your prompt not to use them.

In many usability-testing tasks, charts can visualize outliers that require user analysis and attention.In your prompt, call out these outliers.

For example, in a bar chart depicting sales performance across sales representatives, you might specify that one person,Sam H.,has accomplished roughly only 20% of his sales quota, and only his bar should be shaded red. This instruction would be helpful if you were testing to see if the user noticesSam H.’s lagging performance and engages in a sales-coaching workflow.

Include the chart’s dimensionsin your prompt. (You may copy them from your promptframe, if using one.) Setting dimensions will save you significant time readjusting chart elements to fit them into the interface.

Request that generated charts usethe scalable vector graphics (SVG) format. Compared to image formats (JPEG or PNG), SVG preserves the editability of individual chart elements in design tools, which is important if you need to make small adjustments to the chart later.

Even though AI can rapidly construct and modify charts, Claude 3.5 Sonnet and ChatGPT 4o would dutifully create nonsense charts, even when prompted to act as a data-visualization expert. These tools have impressive capabilities, butthey need a discerning human prompter.

You must train oneffective data-visualization techniquesif you frequently design chart content. Relying on AI to catch your mistakes is a mistake.

This is the reverse of the tactic above. Provide the AI with a table and ask to plot it using several chart types. Requesting variants is an efficient way to ideate over charts (but use critical thinking, as mentioned above).

Now that you have sensible content, how do you get it into your design tool?

For charts, this is as easy as copying and pasting or importing the SVG file into the design tool. Tables are more challenging, however. Design tools have historically done a very poor job importing table data, but there are options.

For example, Figma has several community-made plugins that assist with importing data from spreadsheets.Google Sheets SyncandTable Builderare free plugins that import and synchronize spreadsheet data with Figma layers, helping you to populate a table efficiently.

However, there are issues with Figma’s third-party plugin model. These plugins can have usability issues and hidden costs, they may raise data-privacy concerns, or they may become abandoned and unsupported by their author.

More specialized and robust design tools, such as Axure, support importing spreadsheet files directly into prototype components. This feature can be a significant convenience for designers of data-intensive apps testing data-manipulation workflows.

Regardless of your design tool,do not import thousands of rows with these methods and do not attempt to create a complete simulation of a developed design(you’ll probably break your design tool). Import just enough data to enhance the prototype’s content fidelity and support the tested interactions. A fully developed data table may contain thousands of records, but you may need to display only 50 realistic-looking rows in your prototype to support a testing task.

AI tools have differences in their training and available tools; they do not handle tasks in the same way or with the same proficiency.

While exploring mock-data capabilities for this article,Claude 3.5 Sonnet was easier to use and more reliably effective at generating tables and charts than ChatGPT 4o.

Claude 3.5 Sonnet

ChatGPT 4o

Tables

Data Quality

✅ Generated data that more consistently followed requirements, such as enforcing unique values for a column, distributing values, or applying formatting

❌ Would claim that the generated data followed requirements when it did not, despite prompts to verify its output before finishing

Numerical Accuracy

❌ Generated Python code but could not run it to confirm numerical accuracy

✅ Could run Python code to confirm numerical accuracy

File Output

⚠️ Could not generate Excel or CSV files, but the data could be copied and pasted into a spreadsheet

✅ Generated Excel or CSV files containing the data for download

Charts

Generation

✅ Reliably created and modified charts when prompted (using the React-based Recharts library); applied best practices

⚠️ Reliably generated and modified various charts when prompted (using the Python-based matplotlib library); sometimes included unhelpful defaults (e.g., axes’ labels formatted in scientific notation, such as .2e6 for 200,000)

Fonts

✅ Could use web-safe and system font families

❌ Had limited font family options and could not be prompted to use different ones

Ease of Import into Design Tool

✅ Generated charts with text elements that were easy to copy, paste, and edit in a design tool (when prompted to use the SVG file format)

❌ Rendered chart text as vectors and not actual text elements, so the chart’s text could not be edited in the design tool

Also, design tools such as Figma are experimenting with integrating AI-powered commands. These integrations are promising developments, as designers need more efficient workflows that prompt AI tools in their design context. But beware:

AI tools are rapidly evolving, so today’s winner could be tomorrow’s loser as new model versions are released. But if you’re struggling to get desired results from your preferred AI tool, try a different tool instead (if you can). Its results may surprise you.

This article has focused on filling tables with mock data, which is artificially generated and inspired by real data. However, it lacks high statistical fidelity and is used in small quantities. For many UX professionals, mock data is the pragmatic choice for their fast, iterative prototyping.

Yet, synthetic data may be helpful for UX professionals who work in highly regulated industries such as healthcare or finance. Synthetic data is derived from samples of actual data. Specialized AI tools use these samples to artificially generate new data that mimics various properties of the original, such as statistical patterns. Undesirable aspects (originating from those actual data samples) may also be adjusted, like personally identifiable information or human biases. The result is much more realistic data and in much larger quantities.

If a lack of representative data in your prototypes is a recurring problem, build relationships with others in your organization with similar needs. For example, with more authentic data, a presales team could customize more-understandable product demos for prospective customers, and a quality-assurance team could have more realistic testing builds to help them catch more functional defects before release. Forging alliances with other departments with similar pain points can justify the cost and effort of implementing a synthetic-data AI tool.

Data-intensive applications are challenging to design, prototype, and present realistically. Despite the effort required, your prototype’s content fidelity must be high to gain the most valuable insights from usability testing. Clever use of generative AI can help create and refine the data necessary to make these experiences sensible to your meticulous users. Crafting realistic data is a chore, but now we have help.

Laura Koesten, Kathleen Gregory, Paul Groth, and Elena Simperl. 2021. Talking datasets – understanding data sensemaking behaviours.International Journal of Human-Computer Studies146, 102562. DOI:http://dx.doi.org/10.1016/j.ijhcs.2020.102562

Effectively communicate ideas and findings to managers, collaborators, and other stakeholders

Interaction

Create and evaluate applications for advanced decision making, complicated workflows, and complex domains

Interaction

Techniques and tools for implementing an actionable content strategy

Management