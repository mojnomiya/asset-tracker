```markdown
# Asset Tracker

This is a Django-based web application designed to track corporate assets, such as phones, tablets, laptops, and other devices, that are assigned to employees of multiple companies. The application provides endpoints for managing companies, employees, devices, and asset logs.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/mojnomiya/asset-tracker.git
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply the database migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

## API Endpoints


### Employees

- **List all employees**: `GET /api/`
- **Create a new employee**: `POST /api/add-employees/`

### Asset Logs

- **List all asset logs**: `GET /api/asset-logs/`
- **List asset logs by employee**: `GET /api/asset-logs/<int:employee_id>/`
- **List asset logs by asset**: `GET /api/asset-logs/<int:asset_id>/`
- **Assign an asset to an employee**: `POST /api/assign-asset/<int:employee_id>/`
- **Return an asset by an employee**: `POST /api/return-asset/<int:employee_id>/`

## Usage

1. Create employees, using the respective endpoints.
2. Assign assets to employees using the "Assign Asset" endpoint, specifying the `employee_id`.
3. Return assets using the "Return Asset" endpoint, specifying the `employee_id`.
4. View asset logs to track when devices were checked out and returned using the "Asset Logs" endpoints.

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature-name`.
3. Make your changes and commit them with meaningful messages.
4. Push your branch to your fork: `git push origin feature-name`.
5. Create a pull request on the original repository.
