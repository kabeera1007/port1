# Port1

This project is a portfolio website showcasing the skills and projects of a Kuldeep Parmar, a data expert. Below is a comprehensive guide to the functionalities, structure, and steps to recreate this website. 

Website is live at (www.kuldeepparmar.com)


## Functions and Why This Website is Amazing for Beginners

- **Project Showcase**: Interactive grid displaying projects.
- **Contact Form**: Integrated Twak and Forspee support.
- **Responsive Design**: Works on all devices.
- **Smooth Animations**: Uses AOS and GSAP effects.
- **Simple Navigation**: Clear sections for easy access.
- **Fast Loading**: Optimized for performance.
- **Minimalistic UI**: Clean and professional look.
- **Easy Deployment**: Hosted via GitHub Pages.
- **Secure Data Handling**: Reliable form submissions.
- **Scalable**: Expand with more projects easily.

## What You Will Learn from This

- **HTML & CSS**: Basic to advanced techniques for structuring and styling web pages.
- **JavaScript**: Implementing animations and interactive features using GSAP and AOS.
- **Form Handling**: Integrating and managing forms with third-party services like Twak and Forspee.
- **Responsive Design**: Techniques for creating responsive layouts that work on various devices.
- **Web Hosting**: Deploying a website using a hosting service like Porkbun.

## How Anyone Can Do This

### Domain and Hosting:
- Purchase a domain from a provider like Porkbun.
- Set up hosting using GitHub Pages or any preferred hosting service.

### Website Structure:
- **HTML**: Create the structure of the web pages (index.html, about.html, projects.html, contact.html).
- **CSS**: Style the web pages using a CSS framework or custom styles (styles.css).
- **JavaScript**: Add interactivity and animations using GSAP and AOS.

### Content:
- **Hero Section**: Add a hero section with a background video or image and a catchy headline.
- **Projects Section**: Create a grid layout to showcase different projects with descriptions and links.
- **Contact Section**: Integrate a contact form using services like Twak and Forspee for handling submissions.

### Installation & Setup:
1. **Install Dependencies:**  
   - Ensure you have Python and Flask installed.  
   - Install required packages:
     ```sh
     pip install flask
     ```

2. **Configure Contact Form:**  
   - Update Twak and Forspee integration in `docs/index.html`:
     ```html
     <script type="text/javascript">
     var Tawk_API=Tawk_API||{}, Tawk_LoadStart=new Date();
     (function(){
     var s1=document.createElement("script"),s0=document.getElementsByTagName("script")[0];
     your credentials
     s0.parentNode.insertBefore(s1,s0);
     })();
     </script>
     ```

3. **Run the Application:**  
   - Start the Flask server:
     ```sh
     python app.py
     ```
   - Access the website at `http://localhost:5000`.

### Deployment:
- Deploy the website to GitHub Pages or any other hosting service.
- Ensure the website is responsive and test it on various devices to confirm it looks good everywhere.

## References
1. [AOS (Animate on Scroll)](https://michalsnik.github.io/aos/)
2. [GSAP (GreenSock Animation Platform)](https://greensock.com/gsap/)
3. [GitHub Pages Deployment Guide](https://pages.github.com/)
