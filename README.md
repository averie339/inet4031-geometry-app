# INET4031 Geometry Calculator Web App

# Program Description

The Geometry Calculator Web App is designed to automate the calculation of volumes for different 3D geometric shapes, such as spheres and cylinders, via a simple web interface. The app allows users to input the dimensions of a shape (e.g., radius, height) and returns the calculated volume, providing a useful tool for students, educators, and anyone working with geometry.

This Flask-based web application simplifies geometry calculations by offering an intuitive interface for users. It includes routes for calculating the volume of a sphere and a cylinder, and can be extended to include other geometric shapes in the future.

By using this app, users can quickly perform complex calculations without needing to manually compute the values using formulas.

# Program User Operation

This section outlines the steps required to operate the Geometry Calculator Web App effectively. Users can calculate volumes for various geometric shapes using the provided web interface.

# Running the Web App

1. Clone the repository:

  git clone https://github.com/averie339/inet4031-geometry-app.git

2. Navigate to the project directory:

  cd inet4031-geometry-app

3. Set up a virtual environment (recommended):

  python -m venv .venv
  
  source .venv/bin/activate  # On Windows use .venv\Scripts\activate

4. Install dependencies:

  pip install -r requirements.txt

5. Run the Flask app:

  python app.py

7. Open your browser and go to http://127.0.0.1:5000 to access the Geometry Calculator.
   
# Using the App

Cylinder: Enter radius and height to calculate the volume.

Sphere: Enter radius to calculate the volume.
