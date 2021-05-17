Flare
=====

## Project Description:

A social-media sharing and combination app that allows professionals and businesses to share their profiles, resumes, and portfolios to others with a single link.

A user will be able to link their social media profiles to their account. Once another user visits their profile, they will be able to add each other as connections with a single click. Using Social Media APIs, a user can immediately follow any set of profiles associated with another user.

In the future, users may also add files for viewing to their Flare account, such as images or PDFs, to reflect their expereiences and work (such as resumes, work examples, etc.)

User can also add unique website links to their Flare account, allowing easy portfolio sharing alongside allowing users to add any profiles not officially supported by Flare yet.

**TEAM:** Ailyn Tyagi, Maria Mancz, Nassir Ali, Safi Hasani

## Instructions:
Navigate to the project folder and install the libraries required to run the site

    $ make dev_env
    
Run the site

    $ python source/main.py
    
On any web browser, navigate to `localhost:5000` to view the site.

To view the test output, navigate to `https://www.travis-ci.org`
+ On the left hand side you should see this repo
+ Clicking on it will show the Travis information 
+ At the bottom of the Travis output summary coverage information will be displayed
    + To view detailed coverage information click the `$ codecov` line below
    + Navigate to the `https://codecov.io/github/suh-fee/teamA34DesignProj/commit/...` link at the bottom of the block
    + Click the files tab, and the file-by-file information will be there

## Make Targets:
`make prod`: Target to push to the GitHub repository after running tests.

`make tests`: Target to run the tests implemented.

`make dev_env`: Target to install all of the requirements needed to set up the development environment.

`make docs`: Target to automatically generate documentation from the docstrings. The html pages generated are saved in the docs/docstrings folder.


## Documentation:
[Sequence Diagram](https://github.com/suh-fee/teamA34DesignProj/blob/main/docs/Sequence%20Diagram%20-%20Flare.png)

*Note: Documents from last semester are not present since the idea changed this semester.

## Timeline:

Features implemented:
- Create/Delete Flare account
- Add/Delete social media accounts/links
- View social media accounts from flare (clicking brings you to the page)
- Follow twitter account(s) from within Flare
- Search for existing Flare users

Future APIs/File Types that we hope to add:
- Facebook, Instagram
- LinkedIn
- Generic Files (pdf, doc, jpeg)

API collection:
https://python-twitter.readthedocs.io/en/latest/twitter.html#module-twitter.api

