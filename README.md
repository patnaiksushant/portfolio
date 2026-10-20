# Sushant Kumar Patnaik — portfolio
Responsive, buildless HTML/CSS/JavaScript personal website. No npm installation required.

## Publish through GitHub's website
1. Create a public repository named YOUR_USERNAME.github.io for a root website, or sushant-portfolio for a project website.
2. Unzip this package. Upload the CONTENTS of this folder to the repository root. index.html must be directly in the root, not inside another folder.
3. Include the empty .nojekyll file (create it using Add file → Create new file if your file picker hides it).
4. Commit to main.
5. Open Settings → Pages → Build and deployment. Choose Deploy from a branch, main, / (root), then Save.
6. Wait for deployment; use the URL shown under Settings → Pages.

Root site: https://YOUR_USERNAME.github.io/
Project site: https://YOUR_USERNAME.github.io/sushant-portfolio/

## Configure SEO after you know your URL
With Python 3 installed, run from this folder:

    python3 configure.py https://YOUR_USERNAME.github.io/sushant-portfolio/

For a root site, omit the repository path. Commit the updated index.html, 404.html, robots.txt and generated sitemap.xml. Re-run whenever the URL changes. Sitemap is deliberately generated only after the real URL is supplied. The custom 404 home link also requires this step to work for repository sites and deeply nested missing paths.

## Customize
- Add your verified LinkedIn URL in the marked contact section of index.html.
- Your uploaded resume is included as resume.pdf. Replacing it updates the download without changing the link.
- Edit profile, career history and initiative descriptions in index.html.
- Review contact details, client-related descriptions and commercial metrics before making the repository public.
- Adjust colors and layout in styles.css, behavior in script.js.
- No custom domain/CNAME is preconfigured. Configure a domain in GitHub Pages settings only after owning it, then re-run configure.py using its HTTPS URL.

## Preview locally
    python3 -m http.server 8000
Visit http://localhost:8000. Check mobile navigation, resume download and email link.

## Files
index.html, styles.css, script.js, resume.pdf, favicon.svg, 404.html, robots.txt, configure.py, .nojekyll, .gitignore. configure.py creates sitemap.xml.

## Troubleshooting
- 404 on the site: check repository root, main branch and Pages publishing source.
- Missing styling: preserve relative styles.css and script.js paths and filenames.
- Old content: verify deployment completed and hard-refresh the browser.
- GitHub web uploads: upload extracted files, not the ZIP archive.

Official instructions: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site


## Updated personal-branding version
- US$800K use-case-win references removed
- Introduction and contact copy positioned for executive search
- Six use cases link to their separate public repositories
- Employer outcomes and public prototypes remain distinct

## Use this package
1. Extract this ZIP
2. Open index.html to inspect the portfolio
3. Replace resume.pdf whenever your resume changes
4. Upload the extracted files to the existing repository root
5. Commit to main and wait for GitHub Pages deployment

To add another use case, duplicate a project-card article in
index.html and change its title, description and repository URL.
