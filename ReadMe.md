# Overview Document for the CIT (Comprehensible Input Tracker) App

## Brief Description

This is an application that will allow me to more efficiently learn Dutch. I believe in a mixture of comprehensible input from interesting sources (podcasts, tv shows, movies) and revising sentences sentences that are of use for you personally. I usually get these sentences from the comprehensable input and write them down to revise at a later date. Over and over again I have done this and found massive improvement in my Dutch. I, however, started running into problems with the length of the list of sentences I'm having to revise, spending double the amount of time revising as actually listening to the language.

This led me to come up with a solution involving reading a set amount of sentence that are both random but also trying to consistently cover all the sentences I have. Thus, not having complete randomness. I also have slowly become tired of the paper and the drawbacks it brings like wear and tear, the book becoming thick and uncomfortable to manuever and so on. 

Finally, I came up with the idea to put my software engineering skills to use and make and appllication that hopefully solves all these problems and will finally help me learn Dutch at the desired speed and ease. 

## Tech Stack

- **GUI:** PySide6 (QT)
- **Logic:** Python 3.14 
- **Database:** SQLite 

## User Stories/Scenarios

Within this application there is realistically only one user who for brevity we will just call ... User.

- As a User I must be able to add new sentence pairs (an English sentence and its Dutch translation).
- As a User I must be able to search for and modify a past sentence pair.
- As a User I must be able to read series of random English sentences and then check the Dutch equivalent for each. 
- As a User I must be able to toggle hide/show the Dutch equivilant of the sentence infinitely before moving to the next sentence pair.
- As a User I don't want certain sentence pairs to be shown more often then others because then my coverage of the learning material won't be consistent. 

## Use Cases

These will be the functions that are actually created and how each will work and progress.

- Delete/Modify an Existing Sentence Pair

    - **Definition**: The User will delete a full sentence pair or modify part of said pair.

    - **Scenario**: <br>
                    1. The User chooses to Edit a sentence pair.<br>
                    2. The User chooses a sentence pair.<br>
                    3. The User opts to modify said sentence pair.<br>
                    4. The User updates the sentence pair with different information.<br> 
                    5. The User chooses to save what they have changed.<br>
                    6. The stored sentence pairs are updated to reflect the change.<br>

    - **Extension**: <br>
                    3.1 The User opts to delete the sentence pair.<br>
                    3.2 The User deletes the sentence pair.<br>
                    3.3 The User chooses to save what they have changed.<br>
                    3.4 The stored sentence pairs are updated to reflece the change.<br>

    - **Exceptions**: <br>
                    4.1 The new sentence pair is missing a(both) sentence(s) from the sentence pair.<br>  
                    4.1.2 The User is informed that the sentence pair is not complete.<br>
                
                    4.2 The new information is the same as the old.<br>
                    4.2.2 The User is informed that the sentence pair remains the unchanged.<br>
                    

- Adding a New Sentence Pair
    - **Definition**: 
    - **Scenario**
    - **Extension**
    - **Exceptions**
- Revise Sentence Pairs
    - **Definition**
    - **Scenario**
    - **Extension**
    - **Exceptions**

## Non-Functional Requirements 

## Functional Requirements 

- The system shall use a database to save the sentence pairs. 
- The system shall allow the user to manipulate this data (delete/modify sentence pairs)
- The system shall have a GUI 
- The system won't include any kind of login or auth 
- The system will store how recently each sentence pairs has been presented to the User. 
- The system will present with a new screen for each of the following functionalities: Deleting/Modify an Existing Sentence Pair, Add a New Sentence Pair and Revise Sentence Pairs.

## Class Diagram


## Domain Model

