

### Step-by-Step Guide: Setting up Apache Airflow Locally with Astro

Here’s a detailed guide on how you can set up Apache Airflow locally using Astro, including Docker installation, and how to troubleshoot potential issues.

---

### **Step 1: Install Docker**

**Docker** is required as Astro uses Docker to create and manage containers for Airflow.

- **Download Docker Desktop:** [Docker Installation for Mac/Windows](https://www.docker.com/products/docker-desktop/)
- Follow the installation instructions on Docker’s website for your operating system.

Make sure Docker is running before proceeding.

---

### **Step 2: Install Astro CLI**

The Astro CLI allows you to manage local and cloud-based Airflow instances.

- **Install Astro CLI:**
  ```bash
  curl -sSL https://install.astronomer.io | sudo bash
  ```

- Verify the installation:
  ```bash
  astro version
  ```

   Official Astro CLI documentation: [Astronomer CLI Installation](https://docs.astronomer.io/astro/cli/install-cli)

---

### **Step 3: Initialize a New Astro Project**

Once Astro CLI is installed, you can set up a new Airflow project.

- **Create a New Project:**
  ```bash
  mkdir Apache_Airflow
  cd Apache_Airflow
  astro dev init
  ```

- **Start the Airflow Environment:**
  ```bash
  astro dev start
  ```

   This will start up Airflow, including the **webserver**, **scheduler**, and a **PostgreSQL database** for Airflow’s metadata. You can access the web interface at `http://localhost:8080`.

---

### **Step 4: Set Up Authentication (Creating an Admin User)**

By default, Astro’s local setup might not have authentication enabled for Airflow.

- **Enable Authentication:**
   In your `Dockerfile` or `docker-compose.yaml`, add the following environment variables:
   ```bash
   ENV AIRFLOW__WEBSERVER__AUTHENTICATE=True
   ENV AIRFLOW__WEBSERVER__AUTH_BACKEND=airflow.auth.backends.password_auth
   ```

- **Create an Admin User:**
   After enabling authentication, create an admin user by running the following command:
   ```bash
   astro dev run airflow users create \
   --username admin \
   --firstname Abhinav \
   --lastname Kumar \
   --role Admin \
   --email admin@example.com
   ```

   Alternatively, use this simplified version if prompted for credentials:
   ```bash
   astro dev run airflow users create --username admin --password admin --role Admin
   ```

---

### **Step 5: Access Airflow UI**

After setting up the admin user, you can log in to the Airflow UI:

- **URL:** `http://localhost:8080`
- **Username:** `admin`
- **Password:** `admin` (or whatever you set)

---

### **Troubleshooting Issues**

1. **Invalid Login:**
   - If the default login (`admin:admin`) doesn’t work, ensure authentication is enabled and create a new admin user using the commands provided above.

2. **Container Not Running:**
   - Error: `Error: airflow is not running. To start a local Airflow environment, run 'astro dev start'`.
     - Solution: Start the Astro environment using `astro dev start`.

3. **Airflow Not Starting Properly:**
   - Run `astro dev ps` to check the status of the containers. If any services (webserver, scheduler) aren’t running, try restarting them using:
     ```bash
     astro dev stop
     astro dev start
     ```

4. **Database Issues:**
   - Ensure that the PostgreSQL database is properly set up and connected to Airflow. You can connect to the database using the details provided by Astro to troubleshoot.

---

### Useful Links:
- **Airflow Documentation:** [Apache Airflow Docs](https://airflow.apache.org/docs/)
- **Astronomer CLI Installation:** [Install Astro CLI](https://docs.astronomer.io/astro/cli/install-cli)
- **Docker Installation:** [Docker for Mac/Windows](https://www.docker.com/products/docker-desktop)

---

By following these steps, you should be able to set up and run Apache Airflow locally using Astro. Let me know if you face any more issues or need further guidance!
