Flare
=====

## Project Description

A social-media sharing and combination app that allows professionals and businesses to share their profiles, resumes, and portfolios to others with a single QR read.

Using social media APIs. a user will be able to link their profiles to their account. Once another user scans their unique Flare QR Code, they will automatically be added to each other's connections. Once connected, a user can immediately follow any set of profiles associated with another user they're connected to. 

Users may also add files for viewing to their Flare account, such as images or PDFs, to reflect their expereiences and work (such as resumes, work examples, etc.)

User can also add unique website links to their Flare account, allowing easy portfolio sharing alongside allowing users to add any profiles not officially supported by Flare yet.

## Instructions:
Install the libraries required to run the site

    $ make dev_env
Run the site

    $ python main.py
    
On any web browser, navigate to `localhost:5000` to view the site.

To view the test output, navigate to `https://www.travis-ci.org`
+ On the left hand side you should see this repo
+ Clicking on it will show the Travis information 
+ At the bottom of the Travis output summary coverage information will be displayed
    + To view detailed coverage information click the `$ codecov` line below
    + Navigate to the `https://codecov.io/github/suh-fee/teamA34DesignProj/commit/...` link at the bottom of the block
    + Click the files tab, and the file-by-file information will be there
    
`make prod`
`make tests`
`make dev_env`
`make docs`

**TEAM:** Ailyn Tyagi, Maria Mancz, Nassir Ali, Safi Hasani

APIs/File Types that we are aiming to add:
- Milestone 1: Generic URLs
- Milestone 2: Twitter, Facebook
- Milestone 3: LinkedIn, Instagram
- Milestone 4: Generic Files (pdf, doc, jpeg)

Features we intend on including:
- Create/Delete account
- Add/Delete social media accounts/links
- Add/Delete files
- Follow social media account(s) from within Flare

api collection:
https://python-twitter.readthedocs.io/en/latest/twitter.html#module-twitter.api

*Note: Documents from last semester are not present since the idea changed this semester.

