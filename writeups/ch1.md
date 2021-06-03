# Chapter 1

## Summary
* Categories are objects and functors, similar to points and functions, respectively.
* Every category has composition, and an identity functor.
* Composition is fundamental to category theory as well as programming. Arguably, all the architecture work we do is an undisciplined version of composition.


## Questions

### 1.4.4

One could picture the WWW as a category where URLs are objects and links are functors. This is similar to the graph interpretation of the web used in the Page Rank Eigenvalue algorithm. This only works if webpages link to themselves, since all objects need to respect the identity morphism.

### 1.4.5

One could argue that Facebook is a category with people as objects and friendships as morphisms, but we would need to add some things. People would necessarily need to be friends with themselves. Moreover, it seems like friendship would have to be transitive. If I am friends with you, and you are friends with Cleopatra, then a friendship must exist which is the composition of those friendships. Perhaps I am misunderstanding whether or not a morphism must exist simply because it is defined.

### 1.4.6

For a directed graph to be a category (where nodes are objects and edges are morphisms), each node must have a self-edge. I don't know if it's true that the following property would have to hold:

If (a,b) is an edge and (b,c) is an edge, then (a,c) is an edge. As in the Facebook example, I'm not sure if (a,c) has to exist, or if it just has to be well-defined.