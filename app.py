import requests
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

app.secret_key = 'your_secret_key_here'

API_URL_DM = "http://10.15.5.171/api/method/wtt_module.api_.dm_function"
API_URL_PURCHASE = "http://10.15.5.171/api/method/wtt_module.api_.purchase_function"
API_URL_proposal = "http://10.15.5.171/api/method/wtt_module.api_.proposal_function"
API_URL_PROCESS = "http://10.15.5.171/api/method/wtt_module.api_.Process_function"
API_URL_Design_elec = "http://10.15.5.171/api/method/wtt_module.api_.Design_Electrical_function"
API_URL_Design_mech = "http://10.15.5.171/api/method/wtt_module.api_.Design_Mechanical_function"
API_URL_Accounts = "http://10.15.5.171/api/method/wtt_module.api_.Accounts_function"
API_URL_Marketing = "http://10.15.5.171/api/method/wtt_module.api_.Marketing_function"
API_URL_Store = "http://10.15.5.171/api/method/wtt_module.api_.Store_function"
API_URL_HR = "http://10.15.5.171/api/method/wtt_module.api_.HR_function"
API_URL_ERP = "http://10.15.5.171/api/method/wtt_module.api_.ERP_function"
API_URL_IT = "http://10.15.5.171/api/method/wtt_module.api_.IT_function"
API_URL_Production = "http://10.15.5.171/api/method/wtt_module.api_.Production_function"



def get_active_employees(from_date=None, to_date=None):
    try:
        params = {}
        if from_date:
            params['from_date'] = from_date
        if to_date:
            params['to_date'] = to_date

        response = requests.get(API_URL_DM, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            flash('Failed to retrieve data from the employee API.', 'error')
            return None
    except requests.RequestException as e:
        flash(f'An error occurred: {e}', 'error')
        return None

def get_purchase_data(from_date=None, to_date=None):
    try:
        params = {}
        if from_date:
            params['from_date'] = from_date
        if to_date:
            params['to_date'] = to_date

        response = requests.get(API_URL_PURCHASE, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            flash('Failed to retrieve data from the purchase API.', 'error')
            return None
    except requests.RequestException as e:
        flash(f'An error occurred: {e}', 'error')
        return None

def get_proposal_data(from_date=None, to_date=None):
    try:
        params = {}
        if from_date:
            params['from_date'] = from_date
        if to_date:
            params['to_date'] = to_date

        response = requests.get(API_URL_proposal, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            flash('Failed to retrieve data from the proposal API.', 'error')
            return None
    except requests.RequestException as e:
        flash(f'An error occurred: {e}', 'error')
        return None

# New function for Process data
def get_process_data(from_date=None, to_date=None):
    try:
        params = {}
        if from_date:
            params['from_date'] = from_date
        if to_date:
            params['to_date'] = to_date

        response = requests.get(API_URL_PROCESS, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            flash('Failed to retrieve data from the process API.', 'error')
            return None
    except requests.RequestException as e:
        flash(f'An error occurred: {e}', 'error')
        return None

# New function for Design_elec data

def get_Design_elec_data(from_date=None, to_date=None):
    try:
        params = {}
        if from_date:
            params['from_date'] = from_date
        if to_date:
            params['to_date'] = to_date

        response = requests.get(API_URL_Design_elec, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            flash('Failed to retrieve data from the Design_elec API.', 'error')
            return None
    except requests.RequestException as e:
        flash(f'An error occurred: {e}', 'error')
        return None
 
 # New function for Design_mech data   
    
def get_Design_mech_data(from_date=None, to_date=None):
    try:
        params = {}
        if from_date:
            params['from_date'] = from_date
        if to_date:
            params['to_date'] = to_date

        response = requests.get(API_URL_Design_mech, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            flash('Failed to retrieve data from the Design_mech API.', 'error')
            return None
    except requests.RequestException as e:
        flash(f'An error occurred: {e}', 'error')
        return None

# New function for accounts data 


def get_accounts_data(from_date=None, to_date=None):
    try:
        params = {}
        if from_date:
            params['from_date'] = from_date
        if to_date:
            params['to_date'] = to_date

        response = requests.get(API_URL_Accounts, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            flash('Failed to retrieve data from the accounts_data API.', 'error')
            return None
    except requests.RequestException as e:
        flash(f'An error occurred: {e}', 'error')
        return None     
    
# New function for Marketing data 

def get_Marketing_data(from_date=None, to_date=None):
    try:
        params = {}
        if from_date:
            params['from_date'] = from_date
        if to_date:
            params['to_date'] = to_date

        response = requests.get(API_URL_Marketing, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            flash('Failed to retrieve data from the Marketing_data API.', 'error')
            return None
    except requests.RequestException as e:
        flash(f'An error occurred: {e}', 'error')
        return None
    
    
    
    
# New function for store data 

def fetch_store_data(from_date=None, to_date=None):
    try:
        params = {}
        if from_date:
            params['from_date'] = from_date
        if to_date:
            params['to_date'] = to_date

        response = requests.get(API_URL_Store, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            flash('Failed to retrieve data from the Store_data API.', 'error')
            return None
    except requests.RequestException as e:
        flash(f'An error occurred: {e}', 'error')
        return None
    
    

# New function for HR data 

def fetch_HR_data(from_date=None, to_date=None):
    try:
        params = {}
        if from_date:
            params['from_date'] = from_date
        if to_date:
            params['to_date'] = to_date

        response = requests.get(API_URL_HR, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            flash('Failed to retrieve data from the HR_data API.', 'error')
            return None
    except requests.RequestException as e:
        flash(f'An error occurred: {e}', 'error')
        return None
    
    
    
# New function for erp data
    
    
def get_Erp_data(from_date=None, to_date=None):
    try:
        params = {}
        if from_date:
            params['from_date'] = from_date
        if to_date:
            params['to_date'] = to_date

        response = requests.get(API_URL_ERP, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            flash('Failed to retrieve data from the ERP API.', 'error')
            return None
    except requests.RequestException as e:
        flash(f'An error occurred: {e}', 'error')
        return None
    
    
    
    
    
    
# New function for IT data
    
def get_IT_data(from_date=None, to_date=None):
    try:
        params = {}
        if from_date:
            params['from_date'] = from_date
        if to_date:
            params['to_date'] = to_date

        response = requests.get(API_URL_IT, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            flash('Failed to retrieve data from the IT API.', 'error')
            return None
    except requests.RequestException as e:
        flash(f'An error occurred: {e}', 'error')
        return None
    
    
    

# New function for Production data
    
def get_Production_data(from_date=None, to_date=None):
    try:
        params = {}
        if from_date:
            params['from_date'] = from_date
        if to_date:
            params['to_date'] = to_date

        response = requests.get(API_URL_Production, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            flash('Failed to retrieve data from the Production API.', 'error')
            return None
    except requests.RequestException as e:
        flash(f'An error occurred: {e}', 'error')
        return None
    
    

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if not username or not password:
            flash('Both fields are required!', 'error')
            return redirect(url_for('index'))
        
        if username == 'a' and password == 'a':
            flash('Login successful! Welcome!')
            return redirect(url_for('Department_page'))
        else:
            flash('Invalid credentials, please try again.', 'error')
            return redirect(url_for('index'))
    
    return render_template('login.html')


@app.route('/table', methods=['GET', 'POST'])
def Department_page():
    from_date = request.form.get('from_date')  
    to_date = request.form.get('to_date')     

    # Fetch employee data
    employee_data = get_active_employees(from_date, to_date)

    # Fetch purchase data
    purchase_data = get_purchase_data(from_date, to_date)

    # Fetch proposal data
    proposal_data = get_proposal_data(from_date, to_date)

    if employee_data and 'message' in employee_data and employee_data['message']:
        data = employee_data['message'][0]
    else:
        data = None

    if purchase_data and 'message' in purchase_data and purchase_data['message']:
        purchase_info = purchase_data['message'][0]
    else:
        purchase_info = None

    if proposal_data and 'message' in proposal_data and proposal_data['message']:
        proposal_info = proposal_data['message'][0]
    else:
        proposal_info = None

    return render_template('Department.html', employee_data=data)


@app.route('/purchase_emp_table', methods=['GET', 'POST'])
def purchase_emp_table():
    if request.method == 'POST':
        from_date = request.form.get('from_date')  
        to_date = request.form.get('to_date')     

        # Fetch purchase data
        purchase_data = get_purchase_data(from_date, to_date)

        # Fetch proposal data
        proposal_data = get_proposal_data(from_date, to_date)

        if purchase_data and 'message' in purchase_data and purchase_data['message']:
            data = purchase_data['message'][0]
        else:
            data = None

        if proposal_data and 'message' in proposal_data and proposal_data['message']:
            proposal_info = proposal_data['message'][0]
        else:
            proposal_info = None

        return render_template('purchase_emp_table.html', purchase_data=data, proposal_data=proposal_info)

    # Handle GET request if needed
    from_date = request.args.get('from_date')  
    to_date = request.args.get('to_date')  
    
    purchase_data = get_purchase_data(from_date, to_date)
    proposal_data = get_proposal_data(from_date, to_date)

    if purchase_data and 'message' in purchase_data and purchase_data['message']:
        data = purchase_data['message'][0]
    else:
        data = None

    if proposal_data and 'message' in proposal_data and proposal_data['message']:
        proposal_info = proposal_data['message'][0]
    else:
        proposal_info = None

    return render_template('purchase_emp_table.html', purchase_data=data, proposal_data=proposal_info)


@app.route('/proposal_emp_table', methods=['GET', 'POST'])
def proposal_emp_table():
    if request.method == 'POST':
        from_date = request.form.get('from_date')  
        to_date = request.form.get('to_date')     

        # Fetch proposal data
        proposal_data = get_proposal_data(from_date, to_date)

        if proposal_data and 'message' in proposal_data and proposal_data['message']:
            data = proposal_data['message'][0]
        else:
            data = None

        return render_template('proposal_emp_table.html', proposal_data=data)

    # Handle GET request if needed
    from_date = request.args.get('from_date')  
    to_date = request.args.get('to_date')  
    
    proposal_data = get_proposal_data(from_date, to_date)

    if proposal_data and 'message' in proposal_data and proposal_data['message']:
        data = proposal_data['message'][0]
    else:
        data = None

    return render_template('proposal_emp_table.html', proposal_data=data)


# New route for process data
@app.route('/process_emp_table', methods=['GET', 'POST'])
def process_emp_table():
    if request.method == 'POST':
        from_date = request.form.get('from_date')  
        to_date = request.form.get('to_date')     

        # Fetch process data
        process_data = get_process_data(from_date, to_date)  

        if process_data and 'message' in process_data and process_data['message']:
            data = process_data['message'][0]
        else:
            data = None

        return render_template('process_emp_table.html', process_data=data)

    # Handle GET request if needed
    from_date = request.args.get('from_date')  
    to_date = request.args.get('to_date')  
    
    process_data = get_process_data(from_date, to_date)

    if process_data and 'message' in process_data and process_data['message']:
        data = process_data['message'][0]
    else:
        data = None

    return render_template('process_emp_table.html', process_data=data)



# New route for Design_elec  data
@app.route('/Design_elec_emp_table', methods=['GET', 'POST'])
def Design_elec_emp_table():
    if request.method == 'POST':
        from_date = request.form.get('from_date')  
        to_date = request.form.get('to_date')     

        # Fetch Design_elec data
        Design_elec_data = get_Design_elec_data(from_date, to_date)  

        if Design_elec_data and 'message' in Design_elec_data and Design_elec_data['message']:
            data = Design_elec_data['message'][0]
        else:
            data = None

        return render_template('Design_elec_emp_table.html', Design_elec_data=data)
    
    # Handle GET request - typically show a blank form or initial state
    return render_template('Design_elec_emp_table.html', Design_elec_data=None)




# New route for Design_mech  data    

@app.route('/Design_mech_emp_table', methods=['GET', 'POST'])
def Design_mech_emp_table():
    if request.method == 'POST':
        from_date = request.form.get('from_date')  
        to_date = request.form.get('to_date')     

        # Fetch Design_mech data
        Design_mech_data = get_Design_mech_data(from_date, to_date)  

        if Design_mech_data and 'message' in Design_mech_data and Design_mech_data['message']:
            data = Design_mech_data['message'][0]
        else:
            data = None

        return render_template('Design_mech_emp_table.html', Design_mech_data=data)

    # Handle GET request if needed
    from_date = request.args.get('from_date')  
    to_date = request.args.get('to_date')  
    
    Design_mech_data = get_Design_mech_data(from_date, to_date)

    if Design_mech_data and 'message' in Design_mech_data and Design_mech_data['message']:
        data = Design_mech_data['message'][0]
    else:
        data = None

    return render_template('Design_mech_emp_table.html', Design_mech_data=data)




# New route for Design_elec  data
@app.route('/Accounts_emp_table', methods=['GET', 'POST'])
def Accounts_emp_table():
    if request.method == 'POST':
        from_date = request.form.get('from_date')  
        to_date = request.form.get('to_date')     

        # Fetch Design_elec data
        Accounts_data = get_accounts_data(from_date, to_date)  

        if Accounts_data and 'message' in Accounts_data and Accounts_data['message']:
            data = Accounts_data['message'][0]
        else:
            data = None

        return render_template('Accounts_emp_table.html', Accounts_data=data)
    
    # Handle GET request - typically show a blank form or initial state
    return render_template('Accounts_emp_table.html', Accounts_data=None)


# New route for Marketing  data

@app.route('/Marketing_emp_table', methods=['GET', 'POST'])
def Marketing_emp_table():
    if request.method == 'POST':
        from_date = request.form.get('from_date')  
        to_date = request.form.get('to_date')     

        # Fetch Design_elec data
        Marketing_data = get_Marketing_data(from_date, to_date)  

        if Marketing_data and 'message' in Marketing_data and Marketing_data['message']:
            data = Marketing_data['message'][0]
        else:
            data = None

        return render_template('Marketing_emp_table.html', Marketing_data=data)
    
    # Handle GET request - typically show a blank form or initial state
    return render_template('Marketing_emp_table.html', Marketing_data=None)


# New route for store  data

@app.route('/Store_emp_table', methods=['GET', 'POST'])
def Store_emp_table():
    if request.method == 'POST':
        from_date = request.form.get('from_date')  
        to_date = request.form.get('to_date')     

        # Fetch store data using the fetch_store_data function
        Store_data = fetch_store_data(from_date, to_date)  # Use the correct function to fetch data

        if Store_data and 'message' in Store_data and Store_data['message']:
            data = Store_data['message'][0]  # Process data if present
        else:
            data = None  # If no data is found

        return render_template('Store_emp_table.html', Store_data=data)
    
    # Handle GET request - typically show a blank form or initial state
    return render_template('Store_emp_table.html', Store_data=None)

# New route for HR  data

@app.route('/Hr_emp_table', methods=['GET', 'POST'])
def Hr_emp_table():
    if request.method == 'POST':
        from_date = request.form.get('from_date')  
        to_date = request.form.get('to_date')     

        # Fetch store data using the fetch_HR_data_data function
        HR_data = fetch_HR_data(from_date, to_date)  # Use the correct function to fetch data

        if HR_data and 'message' in HR_data and HR_data['message']:
            data = HR_data['message'][0]  # Process data if present
        else:
            data = None  # If no data is found

        return render_template('Hr_emp_table.html', HR_data=data)
    
    # Handle GET request - typically show a blank form or initial state
    return render_template('Hr_emp_table.html', HR_data=None)



# New route for ERP  data

@app.route('/Erp_emp_table', methods=['GET', 'POST'])
def Erp_emp_table():
    if request.method == 'POST':
        from_date = request.form.get('from_date')  
        to_date = request.form.get('to_date')     

        # Fetch store data using the fetch_HR_data_data function
        Erp_data = get_Erp_data(from_date, to_date)  # Use the correct function to fetch data

        if Erp_data and 'message' in Erp_data and Erp_data['message']:
            data = Erp_data['message'][0]  # Process data if present
        else:
            data = None  # If no data is found

        return render_template('Erp_emp_table.html', Erp_data=data)
    
    # Handle GET request - typically show a blank form or initial state
    return render_template('Erp_emp_table.html', Erp_data=None)


# New route for IT  data

@app.route('/IT_emp_table', methods=['GET', 'POST'])
def IT_emp_table():
    if request.method == 'POST':
        from_date = request.form.get('from_date')  
        to_date = request.form.get('to_date')     

        # Fetch store data using the IT_data_data function
        IT_data = get_IT_data(from_date, to_date)  # Use the correct function to fetch data

        if IT_data and 'message' in IT_data and IT_data['message']:
            data = IT_data['message'][0]  # Process data if present
        else:
            data = None  # If no data is found

        return render_template('IT_emp_table.html', IT_data=data)
    
    # Handle GET request - typically show a blank form or initial state
    return render_template('IT_emp_table.html', IT_data=None)





# New route for IT  data

@app.route('/Production_emp_table', methods=['GET', 'POST'])
def Production_emp_table():
    if request.method == 'POST':
        from_date = request.form.get('from_date')  
        to_date = request.form.get('to_date')     

        # Fetch store data using the Production_emp_table function
        Production_data = get_Production_data(from_date, to_date)  # Use the correct function to fetch data

        if Production_data and 'message' in Production_data and Production_data['message']:
            data = Production_data['message'][0]  # Process data if present
        else:
            data = None  # If no data is found

        return render_template('Production_emp_table.html', Production_data=data)
    
    # Handle GET request - typically show a blank form or initial state
    return render_template('Production_emp_table.html', Production_data=None)




if __name__ == '__main__':
    app.run(debug=True, port=9200)
    
    
    
    
