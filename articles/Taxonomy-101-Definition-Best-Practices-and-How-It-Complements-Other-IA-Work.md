# Taxonomy 101: Definition, Best Practices, and How It Complements Other IA Work

**Author:** Page LaubheimerPage LaubheimerJuly 3, 20222022-07-03

**Topics:** Information Architecture, Navigation

**Source:** https://www.nngroup.com/articles/taxonomy-101/

---

July 3, 20222022-07-03

Share

What is a taxonomy and why does it matter for UX practitioners? In our UX ConferenceInformation Architecturecourse, I often get asked what a taxonomy is, how to build one, and how it fits into the larger landscape ofinformation-architecture (IA) work.

Taxonomies are what information-science professionals callcontrolledvocabularies— planned, prescriptive ways of adding descriptive metadata to content so that it can be retrieved effectively. The idea is that the taxonomy defines a limited set of terms for describing our content in the background; content creators must attach them to any new piece of content, with no ability to expand this vocabulary on an ad hoc basis.

Taxonomy:A closed list of acceptable terms that are arranged hierarchically and are used todescribeand classify content.

Taxonomies are essentially controlled tag systems — while each piece of content will have a set of taxonomy terms attached to it, content creators cannot define their own terms. Each time we tag content using a taxonomy, we must follow some ground rules about which terms to use and how those terms relate to other terms.

It’s important to note that a taxonomy is different from the navigation structure that users interact with and from the underlying IA structure. More on this below.

Admittedly, information architecture can be a confusing discipline — there are many different types of abstract organization models that all seem quite similar but map out different things. The major four organization models are listed below:

(Information architects and taxonomists frequently debate as to whether the IA tree structure constitutes a taxonomy – one could argue that this is a very loose form of taxonomy, but for our purpose we will differentiate this from a formal metadata taxonomy. The meta-classification irony is not lost on me!)

Whereas the IA structure is a map of how our content is organized, a taxonomy is a map of conceptswe use to describe our contentand of how all those concepts relate to one another. A taxonomy is often very different than the IA structure or the navigation and is usually broader than and more technical than the two.

Because the taxonomy itself isn’t shown to users per se (though we may show some of the topics or tags to users as a form of navigation, search suggestions, or refinements), it’s a place where we can be fully immersed in very precise and logical classification work. We are typically concerned with logical precision in a taxonomy, whereas in the visible navigation structure we are concerned with grouping things in a way that adheres tousers’ mental models.

For example, an NN/gArticlehasAuthor(s),which link to those author’s profile pages,Topics(that link to other content with that same topic, and if available, full topic-overview pages), and so on.

Taxonomies aren’t created for the pure love of classifying things (though some UXers like myself absolutely love doing it). Taxonomies allow us to effectively retrieveallthe content that is related to a specific concept. They are typically used in a few ways:

Another common area of confusion regards the difference between a taxonomy, a thesaurus, an Ontology, and a knowledge graph. They are all forms of metadata used for classification. They can all be represented as graphs in which the nodes are concepts and the edges are different kinds of relationships between these concepts.

Taxonomies arethe simplest of these structures. A taxonomy can be either hierarchical or faceted. A faceted taxonomy is made up of several hierarchical , distinct taxonomies that work together to describe different aspects of the same resource. Taxonomies revolve around parent-child relationships between concepts. As you go deeper into a taxonomy, the concepts become more specific (they can also be parts of a larger whole).

A thesaurus(confusingly, not the dictionary type of thesaurus) is a data structure that includes not only parent–child relationships between concepts, but alsoassociativerelationships (“related term” that is not a synonym, but is conceptually related) andequivalencerelationships(synonymous terms, with one being the official preferred term and the rest nonpreferred terms). A thesaurus allows for synonym control and consistency, which is incredibly important for complete information retrieval.

For example, if in your company’s intranet you have tags forRFP,Proposal,StatementofWork, andPitch, but informally they’re all used interchangeably, then each one of these tags will only be associated withsomeof the relevant content, and, therefore, if you search for just one of the terms, you’ll get incomplete results. A thesaurus can link all those concepts together as either related or synonymous (with one chosen as the preferred term). So, in this case, we would probably haveProposalandPitchbe in an equivalence relationship, withProposalbeing the preferred term. Both these concepts would be in an associative relationship toRFPandStatement of Work, because they are not exactly synonymous, but definitely conceptually related. (Note: Most “taxonomies” created for digital products are actually thesauri, since the software for managing taxonomies usually includes thesaurus features such as preferred terms and related terms.)

Ontologiesare the most flexible and complex of these types of metadata structures and are often used for mapping out knowledge in complex technical fields. Ontologies support many different types of meaningful relationships (beyond parent–child, associative, and equivalence relationships) that connect concepts semantically.

For example, in the Linnean biology taxonomy that many of us had to learn in school, a polar bear (Ursus Maritimius) is a specific type of bear (Ursidae), which is a specific type ofCarnivora(and so on). We are limited to only the one type of relationship — parent–child (or class-inclusion relationships). In an ontology, we can map out other types of conceptual connections: not only is aPolar Beara type ofBear, but also itsHabitatisPolar, itsConservation StatusisThreatened, and so on. By building out these relationships of what we can formalize about a field of knowledge, we capture many other aspects into a formal structure that can then be used to build a database.

The flexibility of ontologies to represent many kinds of relationships among concepts allows for detailed multidimensional classification of information.

Ontologies are big, complex projects, typically used to describe a specific knowledge domain. These are not typically the type of project that a single UXer will take on by themselves, as they are often the work of a team of ontologists, taxonomists, software developers, and domain experts. It is, however, important to be aware of them, and how they relate to taxonomies. Especially if you work in scientific fields or on semantic-web projects, ontologies are something you are likely to encounter, so understanding what they are is helpful for a UX practitioner.

Building a taxonomy from scratch is a fairly involved process, and full details on how to do so are out of the scope of this article, but there are some common themes for how to proceed no matter the type of project. It is okay to start small and that a taxonomy need not be a multi-year project — simply having a small set of topics that you assign consistently to your content in the background is a fine start!

Taxonomies are a powerful way to build content relationships in digital products and are the unseen, backstage organization systems that fill in the gaps that user-facing navigation systems may leave. When properly defined and maintained, a taxonomy can support better search suggestions and post-search refinements, faceted navigation, and automatic linking of related content.

Dean Allemang, James Hendler. 2011.Semantic Web for the Working Ontologist (2nd. Ed.).Morgan Kauffman, Waltham, MA.

Heather Hedden. 2016.The Accidental Taxonomist(2nd Ed.). Information Today, Medford, NJ.

International Organization for Standardization. (2011)Information and documentation — Thesauri and interoperability with other vocabularies — Part 1: Thesauri for information retrieval(ISO Standard No. 25964-1:2011) Retrieved fromhttps://www.iso.org/standard/53657.html

Mary Whittaker and Kathryn Breininger. 2008. Taxonomy Development for Knowledge Management. InWorld Library and Information Congress: 74th Ifla General Conference and Council,10-14 August 2008, Québec, Canadahttp://www.ifla.org/IV/ifla74/index.htm

Organize and structure information to improve findability and discoverability

Interaction