Generating a random keyword
To get quotes from various backgrounds we will generate a random keyword every time and the program will return a quote from a particular author revolving around the keyword.

To get any random English word we make use of the random_word module. The random_word module can be used to generate either a single random word or a list of random words.

You can install the module using the pip command if importing the same gives you an error. Let’s look at the following lines of code first.


from random_word import RandomWords
r = RandomWords()
w = r.get_random_word()
print(w)
Here we imported a function named RandomWords from the module and created an object of the same which will be helpful to extract words.

Later we applied the get_random_word function on the object created to create a random word and stored the same into a variable.

The code generated a random word from English dictionary.

Get a random quote using the quote module in Python
Now that we have a random keyword with us, the next step is to generate a quote for the keyword using the quote library.

If importing the library gives an error make sure you install quote library using the pip command beforehand.

Let’s look at the following code.

from quote import quote
res = quote('family',limit=1)
print(res)
To generate a random quote we will be using the quote function from the quote module. The quote function requires a keyword to search for the quotes.

We also set the limit value to limit the no of quotes being generated. But on printing the output we get something like this:

[{'author': 'J.R.R. Tolkien', 'book': 'The Fellowship of the Ring', 'quote': "I don't know half of you half as well as I should like; and I like less than half of you half as well as you deserve."}]
The reason behind the same is that the quote function returns a list of dictionaries where each dictionary contains information about a particular quote.

So we will be extracting the quote value from the dictionary. To do the same we will use the following lines of code.


for i in range(len(res)):
    print(res[i]['quote'])
What we are doing here is traversing through the list and for each dictionary value we will print only the value next to the quote key.

Now we get the output as the following:

I don't know half of you half as well as I should like; and I like less than half of you half as well as you deserve.
Getting a random quote using a random word
Now we learned about generating a keyword and quotes using different modules, let’s combine both of them and generate a quote according to a particular keyword.

The code for the same is shown below.

from random_word import RandomWords
from quote import quote
 
r = RandomWords()
w = r.get_random_word()
print("Keyword Generated: ",w)
 
res = quote(w, limit=1)
for i in range(len(res)):
    print("\nQuote Generated: ",res[i]['quote'])
And the result is as follows:

Keyword Generated:  fenman
 
Quote Generated:  The fenman gazed at Wimsey with a slow pity for his bird-witted feebleness of mind.
Conclusion
You can try out by generating multiple quotes on multiple keywords as well! Happy coding!